"""caixilho_dxf.py — desenho paramétrico de caixilhos e fachadas em DXF (ezdxf).

Geometria pura: só polilinhas fechadas (retas e arcos por bulge), blocos e
hachuras. Nada é contornado a partir de pixel — a imagem serve para medir
proporção e contar vidros; o desenho é refeito por parâmetro.

Padrão de camadas (mantém igual entre fachadas):
  JAN-MARCO  JAN-FOLHA  JAN-VIDRO  HACH-CAIXILHO (sólido)  HACH-VIDRO (AR-RROOF)
  COLUNA  PEITORIL  FACH-CONTORNO  FACH-CORNIJA  FACH-ALMOFADADO  FACH-ORNAMENTO
  FACH-ARCO  COTA  NOTA
Unidade: cm. Escala provisória até haver uma medida real; depois, escalar tudo junto.
"""
import math, ezdxf

CAMADAS = {'JAN-MARCO': 7, 'JAN-FOLHA': 4, 'JAN-VIDRO': 5, 'HACH-CAIXILHO': 33, 'HACH-VIDRO': 151,
           'COLUNA': 8, 'PEITORIL': 8, 'FACH-CONTORNO': 7, 'FACH-CORNIJA': 7, 'FACH-ALMOFADADO': 8,
           'FACH-ORNAMENTO': 8, 'FACH-ARCO': 7, 'COTA': 1, 'NOTA': 3}
COTA = {'dimlfac': 1, 'dimtxt': 5, 'dimasz': 3, 'dimdec': 0}   # sem dimlfac=1 a cota sai x100

def novo_doc():
    doc = ezdxf.new('R2010', setup=True); doc.units = ezdxf.units.CM
    for n, c in CAMADAS.items(): doc.layers.add(n, color=c)
    return doc

def rect(x0, y0, x1, y1): return [(x0, y0, 0), (x1, y0, 0), (x1, y1, 0), (x0, y1, 0)]
def arco_pleno(x0, y0, x1, ys):
    """retângulo até ys com semicírculo em cima (bulge 1)."""
    return [(x0, y0, 0), (x1, y0, 0), (x1, ys, 1), (x0, ys, 0)]
def poly(L, pts, camada): L.add_lwpolyline(pts, format='xyb', close=True, dxfattribs={'layer': camada})

def grade(L, x0, y0, x1, y1, cols, linhas, baguete=2):
    """vidros iguais numa grade; devolve os contornos (para a hachura)."""
    w = (x1 - x0 - (cols - 1) * baguete) / cols; h = (y1 - y0 - (linhas - 1) * baguete) / linhas; out = []
    for i in range(cols):
        for j in range(linhas):
            a = x0 + i * (w + baguete); b = y0 + j * (h + baguete); p = rect(a, b, a + w, b + h)
            poly(L, p, 'JAN-VIDRO'); out.append(p)
    return out

def hachuras(L, contorno, vidros, escala_vidro=0.4):
    """caixilho = contorno menos vidros (sólido); vidro = padrão. Duas camadas, troca de cor por camada."""
    hc = L.add_hatch(color=33, dxfattribs={'layer': 'HACH-CAIXILHO'}); hc.set_solid_fill(color=33)
    hc.paths.add_polyline_path(contorno, is_closed=True, flags=ezdxf.const.BOUNDARY_PATH_EXTERNAL)
    for v in vidros: hc.paths.add_polyline_path(v, is_closed=True, flags=ezdxf.const.BOUNDARY_PATH_OUTERMOST)
    hv = L.add_hatch(color=151, dxfattribs={'layer': 'HACH-VIDRO'})
    hv.set_pattern_fill('AR-RROOF', color=151, angle=45, scale=escala_vidro)
    for v in vidros: hv.paths.add_polyline_path(v, is_closed=True)

def limite_por_circulo(cx, cy, r):
    """devolve f(a,b,c,d) -> contorno do retângulo [a,c]x[b,d] cortado por cima pelo círculo.
    Serve para vidro sob arco abatido e para aberturas cujo topo segue uma abóbada.
    O arco sai como bulge (arco verdadeiro), não como segmentos."""
    yc = lambda x: cy + math.sqrt(max(r * r - (x - cx) ** 2, 0))
    bul = lambda p, q: math.tan((math.atan2(q[1] - cy, q[0] - cx) - math.atan2(p[1] - cy, p[0] - cx)) / 4)
    def f(a, b, c, d):
        if b >= cy + r: return None
        xb = math.sqrt(max(r * r - (b - cy) ** 2, 0)); xa, xc = max(a, cx - xb), min(c, cx + xb)
        if xc - xa < 1: return None
        topo = lambda x: min(d, yc(x))
        dx = math.sqrt(max(r * r - (d - cy) ** 2, 0)) if d < cy + r else -1
        xs = [xc] + sorted([x for x in (cx + dx, cx - dx) if dx >= 0 and xa < x < xc], reverse=True) + [xa]
        p = [(xa, b, 0), (xc, b, 0)]
        for k in range(len(xs) - 1):
            x1, x2 = xs[k], xs[k + 1]; p1 = (x1, topo(x1)); p2 = (x2, topo(x2))
            p.append((p1[0], p1[1], bul(p1, p2) if yc((x1 + x2) / 2) < d - 1e-6 else 0))
        p.append((xa, topo(xa), 0)); o = []
        for q in p:
            if o and abs(o[-1][0] - q[0]) < 1e-6 and abs(o[-1][1] - q[1]) < 1e-6:
                o[-1] = (o[-1][0], o[-1][1], q[2] or o[-1][2]); continue
            o.append(q)
        if abs(o[0][0] - o[-1][0]) < 1e-6 and abs(o[0][1] - o[-1][1]) < 1e-6: o.pop()
        return o
    return f

def circulo_por_3(p1, p2, p3):
    (x1, y1), (x2, y2), (x3, y3) = p1, p2, p3
    d = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    ux = ((x1*x1+y1*y1)*(y2-y3)+(x2*x2+y2*y2)*(y3-y1)+(x3*x3+y3*y3)*(y1-y2)) / d
    uy = ((x1*x1+y1*y1)*(x3-x2)+(x2*x2+y2*y2)*(x1-x3)+(x3*x3+y3*y3)*(x2-x1)) / d
    return ux, uy, math.hypot(x1 - ux, y1 - uy)

def subtrair_faixas(a, c, ocultas):
    """intervalo [a,c] menos as faixas ocultas (colunas na frente do caixilho)."""
    seg = [(a, c)]
    for (o0, o1) in ocultas:
        nx = []
        for (p, q) in seg:
            if o1 <= p or o0 >= q: nx.append((p, q)); continue
            if p < o0: nx.append((p, o0))
            if o1 < q: nx.append((o1, q))
        seg = nx
    return [(p, q) for (p, q) in seg if q - p > 0.5]

def cotas(msp, lista):
    for base, p1, p2, ang in lista:
        msp.add_linear_dim(base=base, p1=p1, p2=p2, angle=ang, dimstyle='EZDXF', override=COTA,
                           dxfattribs={'layer': 'COTA'}).render()

def salvar(doc, caminho_sem_ext, preview=True):
    """hachuras atrás das linhas, audita, grava .dxf e um .png de conferência."""
    msp = doc.modelspace()
    hs = [(h.dxf.handle, '1') for h in msp.query('HATCH')]
    outros = [(e.dxf.handle, '%X' % (i + 16)) for i, e in enumerate(msp) if e.dxftype() != 'HATCH']
    msp.set_redraw_order(hs + outros)
    doc.saveas(caminho_sem_ext + '.dxf')
    erros = len(ezdxf.readfile(caminho_sem_ext + '.dxf').audit().errors)
    if preview:
        import matplotlib; matplotlib.use('Agg')
        from ezdxf.addons.drawing import matplotlib as dm
        dm.qsave(msp, caminho_sem_ext + '_preview.png', bg='#FFFFFF', dpi=200)
    return erros
