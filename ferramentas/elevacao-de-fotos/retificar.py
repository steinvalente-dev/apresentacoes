#!/usr/bin/env python3
"""retificar.py — corrige a perspectiva de um plano de fachada por homografia.

Não usa IA: reprojeta a foto. Proporções do plano escolhido ficam fiéis; o que
está fora dele (volumes salientes, recessos, profundidade de batente) não.

Uso:
  python3 retificar.py foto.png saida.png "x1,y1 x2,y2 x3,y3 x4,y4" "X1,Y1 X2,Y2 X3,Y3 X4,Y4" [LARGURA ALTURA]
    pontos de origem (na foto) e de destino (na saída), na ordem
    sup-esq, sup-dir, inf-dir, inf-esq.
  python3 retificar.py --espelhar entrada.png saida.png EIXO_X
    completa uma fachada simétrica: espelha a metade esquerda pelo eixo x=EIXO_X.

Dica para escolher os pontos: grade de coordenadas sobre a foto
(python3 retificar.py --grade foto.png grade.png), recortes ampliados nos cantos.
"""
import sys
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageOps

def pts(s): return np.float32([[float(v) for v in p.split(',')] for p in s.split()])

def retificar(src, dst, origem, destino, W=None, H=None, folga=40):
    im = cv2.imread(src)
    o, d = pts(origem), pts(destino)
    M = cv2.getPerspectiveTransform(o, d)
    T = np.array([[1, 0, folga], [0, 1, folga], [0, 0, 1]], float) @ M
    W = int(W or d[:, 0].max() + 2 * folga); H = int(H or d[:, 1].max() + 2 * folga)
    cv2.imwrite(dst, cv2.warpPerspective(im, T, (W, H), flags=cv2.INTER_CUBIC))

def espelhar(src, dst, eixo, x0=0):
    im = Image.open(src).convert('RGB'); eixo = int(eixo)
    L = im.crop((x0, 0, eixo, im.height)); out = Image.new('RGB', (L.width * 2, L.height))
    out.paste(L, (0, 0)); out.paste(ImageOps.mirror(L), (L.width, 0)); out.save(dst)

def grade(src, dst, passo=50):
    im = Image.open(src).convert('RGB'); d = ImageDraw.Draw(im)
    for x in range(0, im.width, passo):
        d.line([(x, 0), (x, im.height)], fill=(255, 0, 0) if x % (2 * passo) == 0 else (255, 170, 170))
        if x % (2 * passo) == 0: d.text((x + 2, 2), str(x), fill='red')
    for y in range(0, im.height, passo):
        d.line([(0, y), (im.width, y)], fill=(0, 0, 255) if y % (2 * passo) == 0 else (170, 170, 255))
        if y % (2 * passo) == 0: d.text((2, y + 2), str(y), fill='blue')
    im.save(dst)

if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == '--espelhar': espelhar(a[1], a[2], a[3])
    elif a and a[0] == '--grade': grade(a[1], a[2])
    elif len(a) >= 4: retificar(a[0], a[1], a[2], a[3], *(a[4:6] if len(a) >= 6 else []))
    else: print(__doc__)
