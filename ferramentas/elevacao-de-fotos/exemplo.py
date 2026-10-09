"""exemplo.py — fachada sintética que exercita todas as peças da biblioteca.
python3 exemplo.py  ->  exemplo.dxf + exemplo_preview.png  (auditoria tem de dar 0)"""
import math
from caixilho_dxf import *

doc = novo_doc(); msp = doc.modelspace()

# 1 · bloco de janela: bandeira 4x3 + duas folhas 2x6
B = doc.blocks.new('JAN_DUAS_FOLHAS'); W, H, M, S = 120, 330, 5, 8; T0, T1 = 185, 201; vid = []
poly(B, rect(0, 0, W, H), 'JAN-MARCO'); poly(B, rect(M, M, W - M, H - M), 'JAN-MARCO'); poly(B, rect(M, T0, W - M, T1), 'JAN-MARCO')
poly(B, rect(M, T1, W - M, H - M), 'JAN-FOLHA'); vid += grade(B, M + S, T1 + S, W - M - S, H - M - S, 4, 3)
for a, c in ((M, W / 2), (W / 2, W - M)):
    poly(B, rect(a, M, c, T0), 'JAN-FOLHA'); vid += grade(B, a + S, M + 10, c - S, T0 - S, 2, 6)
hachuras(B, rect(0, 0, W, H), vid)

# 2 · bloco de janela em arco pleno, com painel inferior envidraçado em arco abatido 5x3
A = doc.blocks.new('JAN_ARCO'); W2, H2 = 110, 185; R = W2 / 2; ys = H2 - R; vid = []
poly(A, arco_pleno(0, 0, W2, ys), 'JAN-MARCO'); poly(A, arco_pleno(M, M, W2 - M, ys), 'JAN-MARCO')
YR = M + 0.42 * (ys - M)
cima = arco_pleno(M + 6, YR + 3, W2 - M - 6, ys); poly(A, cima, 'JAN-VIDRO'); vid.append(cima)
gx0, gx1, gy0, gtop = M + 6, W2 - M - 6, M + 6, YR - 9; cols, lin = 5, 3
ph = (gtop - gy0 - (lin - 1) * 2) / lin; nasc = gy0 + (lin - 1) * (ph + 2)
cx, cy, r = circulo_por_3((gx0, nasc), ((gx0 + gx1) / 2, gtop), (gx1, nasc))
corta = limite_por_circulo(cx, cy, r); pw = (gx1 - gx0 - (cols - 1) * 2) / cols
for i in range(cols):
    for j in range(lin):
        a = gx0 + i * (pw + 2); b = gy0 + j * (ph + 2); p = corta(a, b, a + pw, b + ph)
        if p: poly(A, p, 'JAN-VIDRO'); vid.append(p)
hachuras(A, arco_pleno(0, 0, W2, ys), vid)

# 3 · fachada: contorno, cornija, janelas inseridas como bloco, colunata na frente de caixilho contínuo
poly(msp, rect(-500, 0, 500, 600), 'FACH-CONTORNO'); msp.add_line((-500, 540), (500, 540), dxfattribs={'layer': 'FACH-CORNIJA'})
for x in (-430, -290): msp.add_blockref('JAN_DUAS_FOLHAS', (x, 60))
for x in (170, 310): msp.add_blockref('JAN_DUAS_FOLHAS', (x, 60))
msp.add_blockref('JAN_ARCO', (-55, 330))
eixos = [-120, -40, 40, 120]; ocultas = [(e - 10, e + 10) for e in eixos]; vid = []
for (p, q) in subtrair_faixas(-140, 140, ocultas):
    c = rect(p, 80, q, 260); poly(msp, c, 'JAN-MARCO'); v = []
    for (u, w) in subtrair_faixas(p + 4, q - 4, ocultas):
        v += [rect(u, 84 + k * 44, w, 84 + k * 44 + 40) for k in range(4)]
    for vv in v: poly(msp, vv, 'JAN-VIDRO')
    hachuras(msp, c, v)
for e in eixos: poly(msp, rect(e - 10, 60, e + 10, 300), 'COLUNA')
cotas(msp, [((-500, 640), (-500, 600), (500, 600), 0), ((-560, 0), (-500, 0), (-500, 600), 90)])
msp.add_text('EXEMPLO SINTETICO - escala provisoria, cm', height=10, dxfattribs={'layer': 'NOTA'}).set_placement((-500, -40))
print('auditoria:', salvar(doc, 'exemplo'))
