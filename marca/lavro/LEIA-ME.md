# marca Lavrō — a pasta

| arquivo | o que é | papel |
|---|---|---|
| `../MARCA-LAVRO.md` | cor, tipografia, abertura, contracapa | **o mestre.** É o que as sessões leem e o deck consome |
| `bloco.html` | o que se cola no esqueleto: as fontes, o `:root` por papel, as constantes da marca (`LOGO_CANTO LOCKUP GRAFISMO QR UNDERSCORE`), abertura e contracapa | a forma executável do mestre |

`01-MARCA-normativo.md`, `02-DESIGN-SYSTEM.md`, `03-styleguide.html`, `manual.html` e `wordmark.svg` são o material de origem; o mestre é o `.md` um nível acima. **Se o `.md` e o HTML divergirem, o `.md` ganha.**

**Marcadores para máquina (03/09/2026):** o `bloco.html` traz `/* TRECHO:fontes */`, `/* TRECHO:root */`, `<!-- TRECHO:constantes -->`, `<!-- TRECHO:abertura -->` e `<!-- TRECHO:contracapa -->`, cada um fechado por `/TRECHO` — é o que `sistemas/montar.py` lê para colar nos `COLAR:x` do esqueleto. Invisíveis na página; não mudam o que se copia à mão.
