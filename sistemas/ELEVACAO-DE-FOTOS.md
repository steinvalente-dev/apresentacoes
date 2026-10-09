# Elevação a partir de fotos — da foto de rua ao DXF

Para levantar uma fachada existente sem medição: prints de Street View ou
fotos do local → elevação frontal → cada esquadria em DXF → fachada montada
em 2D. Serve para estudo, EVTL e base de projeto. **Não é levantamento
métrico**: a escala é provisória até entrar uma medida real.

Ferramentas: `ferramentas/elevacao-de-fotos/` (retificação e gerador de DXF).
Imagem por IA: Magnific, conector no claude.ai.

## As cinco etapas

**1 · Fotos.** Pedir: a fachada inteira (mesmo em ângulo), **um print o mais
frontal possível do trecho central**, e um recorte próximo de cada tipo de
esquadria. O print frontal do centro é o que mais rende — foi ele que salvou
o arco e a loggia no primeiro caso. Perguntar logo: a fachada é simétrica?
Existe alguma medida real (lote, porta, pé-direito)?

**2 · Retificar por geometria, sem IA.** Homografia de 4 pontos por plano
(`retificar.py`). Fiel ao plano escolhido; o lado em ângulo rasante não se
recupera (aparece o "lado" de batente e pilar). Fachada simétrica: retificar o
lado bom e espelhar pelo eixo. Montagem: cada trecho da melhor fonte, com a
origem marcada (medido · espelhado). Saída: elevação com perspectiva leve.

**3 · Elevação completa na IA.** Magnific, edição precisa (`ideogram`,
`preciseEdit`), a elevação retificada como referência, **3 variações**. Prompt
curto: "orthographic frontal elevation, every vertical vertical…, keep the
exact architecture…, remove razor wire and cables". Resultado bom para ver a
fachada inteira reta; **não** é fonte de medida (regulariza e às vezes
inventa). Escolher a que mantém a volumetria (blocos salientes, degraus de
cornija) e a simetria.

**4 · Detalhe de cada esquadria.** Recorte do print, ampliado 3–4×, mesma
edição precisa, 3 variações. No prompt, **descrever a composição contando os
vidros** (ex.: "bandeira 4×3, duas folhas de 2 colunas"). Elemento que já está
frontal no print retificado (ex.: loggia vista de frente) **pula a IA** e vai
direto ao desenho.

**5 · DXF.** Desenhado por parâmetro (`caixilho_dxf.py`): blocos por tipo de
janela, camadas e hachuras padrão, arcos verdadeiros. Posição de cada elemento
medida na elevação da etapa 3 e calibrada por **uma** janela de largura
adotada; quando chega a medida real, escala uniforme do arquivo inteiro.

## Regras que valem para toda fachada

- **O print manda na contagem; a IA serve para ortogonalidade e proporção.**
  No primeiro caso, a maioria das variações errou o número de vidros.
- Validar uma etapa antes da próxima, e um elemento por vez. Primeiro DXF de
  um elemento só, para aprovar o formato (camadas, hachura, detalhe); depois
  replicar.
- Arquivos numerados em sequência (`00_comparativo…`, `01…`, `02…`) e
  comparativo lado a lado a cada rodada — o quadro do Magnific não garante a
  ordem das variações.
- Medida derivada de foto é leitura, não fato: marcar no DXF (`NOTA`) o que é
  escala provisória, o que foi espelhado e o que estava oculto.

## Armadilhas já encontradas

- **Profundidade engana a medida.** Bloco saliente, recesso, batente fundo:
  a retificação de um plano não acerta o outro, e o tamanho deduzido sai
  errado. Retificar plano por plano e conferir proporção entre elementos.
- **O que está no alto parece menor** no print tirado de baixo. A janela de
  cima saiu 25% estreita no desenho tirado direto do recorte; a elevação
  corrigida pela IA acertou.
- **Espelhar sem conferir o eixo** deforma o centro (o arco virou ogiva).
  Medir o eixo por pares simétricos do plano principal, não pelo ornamento,
  que está em outro plano.
- **Elemento visto de dentro de um recesso** (arco profundo): só a borda da
  frente é confiável.
- **Topos sob abóbada** seguem um só arco; desenhar um por abertura sai torto.
- **Concertina e fios** escondem a parte de baixo das esquadrias — contagem
  ali é palpite; dizer isso.
- **Google Drive pelo conector não recebe imagem grande** (só texto e binário
  pequeno). Entregar pelo chat e pelo projeto do Magnific; binário de trabalho
  vai para `michel-stein-sistemas/entregas/<projeto>/`.

## O que não vem para cá

Foto do local, print de Street View, endereço, nome do projeto e as medidas de
um caso: o repositório é público. O caso fica no Drive do projeto.
