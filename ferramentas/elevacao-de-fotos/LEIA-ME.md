# elevacao-de-fotos · retificar foto e desenhar caixilho em DXF

Ferramentas das etapas 2 e 5 do método `sistemas/ELEVACAO-DE-FOTOS.md`.
**Rodam no container do Claude (Cowork), não na máquina do Michel** — lá não
há Python. Dependências: `opencv-python-headless`, `pillow`, `numpy`, `ezdxf`
(`pip install ... --break-system-packages`), `matplotlib` para o preview.

## O que tem aqui

| arquivo | faz |
|---|---|
| `retificar.py` | homografia de 4 pontos (corrige perspectiva de um plano), `--espelhar` pelo eixo de simetria, `--grade` para escolher os pontos |
| `caixilho_dxf.py` | biblioteca: camadas padrão, grade de vidros, arco pleno, vidro cortado por arco abatido, caixilho recortado atrás de coluna, hachuras, cotas, auditoria e preview |
| `exemplo.py` | fachada sintética que usa tudo — rodar depois de mexer na biblioteca; auditoria tem de dar 0 |

## Decisões já tomadas (não reabrir sem motivo)

- **Geometria pura.** Nada é contornado a partir de pixel. A imagem dá proporção
  e contagem; o desenho é refeito por parâmetro. Só polilinhas fechadas; arco
  é arco (bulge), nunca segmentos.
- **Janela repetida é bloco.** Muda o bloco, mudam todas as cópias.
- **Duas hachuras, duas camadas:** `HACH-CAIXILHO` (sólido, contorno menos os
  vidros) e `HACH-VIDRO` (AR-RROOF a 45°). Hachura vai para trás das linhas
  (`salvar()` faz a ordem de desenho).
- **Unidade cm, escala provisória** até haver uma medida real; depois escala
  uniforme do arquivo inteiro. A nota da escala vai na camada `NOTA`.
- **Cota com `dimlfac=1`.** O estilo EZDXF vem com 100 e a cota sai ×100.
- **Coluna na frente de caixilho:** o caixilho é cortado em faixas
  (`subtrair_faixas`), não desenhado inteiro por baixo.
- **Topo que segue abóbada:** um círculo único para todas as aberturas
  (`circulo_por_3` + `limite_por_circulo`), não um arco por abertura.

## O que ainda não faz

- Ornamento (capitel, cartucho, almofada) sai como contorno simples.
- Não lê medida de nenhum lugar: a escala é sempre um parâmetro.
- Retificação de dois planos ao mesmo tempo (bloco saliente + recuado) não
  existe — é um plano por vez, e o resíduo fica.
