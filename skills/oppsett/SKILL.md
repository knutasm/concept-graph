---
name: oppsett
description: Tar i bruk begrepskatalogen i repoet brukeren står i, ved å legge instruksjoner for agenter i CLAUDE.md og avtale hvor sidene skal ligge. Kan også oppdatere instruksjonene fra en nyere versjon av pluginen. Bruk når brukeren vil starte en begrepskatalog, ta i bruk pluginen eller oppdatere oppsettet, f.eks. "sett opp begrepskatalog", "ny katalog", "init", "kom i gang med katalogen", "set up the glossary".
---

# Ta i bruk begrepskatalogen

Du gjør repoet brukeren står i klart for en begrepskatalog. Snakk norsk. Pluginen har malene,
veiledningen og skillene. Repoet til brukeren har sidene, og instruksjonene for agenter i `CLAUDE.md`.
Pluginen bestemmer ikke hvor sidene ligger. Les `${CLAUDE_PLUGIN_ROOT}/kontekst/sider.md` først.

## 1. Se hva som finnes

```sh
grep -rl --include='*.md' -E "^type: (entitet|hendelse|maaltall|dimensjon|klassifisering|prosess|domene|system)$" . | head -20
ls CLAUDE.md 2>/dev/null && grep -n "^#" CLAUDE.md
```

- Finnes det sider fra før, er katalogen i bruk. Se hvor de ligger, og gå til steg 3.
- Er repoet ikke et git-repo, nevn at katalogen bør versjoneres (skillen `gjennomgang` bruker git).

## 2. Hvor skal sidene ligge?

Spør brukeren. Ikke foreslå en struktur før du har spurt hvordan de vil ha det. Aktuelle spørsmål:

- Skal katalogen ha en egen mappe, eller ligge sammen med annen dokumentasjon?
- Skal begrepene sorteres i mapper (for eksempel etter domene), eller ligge samlet?
- Hvor skal prosesser, domener og systemer ligge?
- Skal sidene leses i Obsidian? Da bør alle sidene ligge i én mappe som kan åpnes som vault.

Har brukeren ingen mening, er én mappe med alle sidene det enkleste. Lag ingen mapper før de trengs
for den første siden.

Vil brukeren skrive sider for hånd, kan malene kopieres inn (`${CLAUDE_PLUGIN_ROOT}/maler/`), for
eksempel til en mappe Obsidian-tillegget Templates peker på. Si at kopien ikke oppdateres når pluginen
oppdateres, og at skillene alltid bruker malene i pluginen.

## 3. Instruksjoner for agenter

Les `${CLAUDE_PLUGIN_ROOT}/kontekst/CLAUDE.md`. Den forklarer agenter hvordan katalogen slås opp og brukes.
Fyll inn seksjonen **Plassering** med det brukeren valgte i steg 2, eller det du fant i steg 1.

- Finnes ikke `CLAUDE.md`, lag den med innholdet.
- Finnes `CLAUDE.md` uten en seksjon om begrepskatalogen, legg innholdet til nederst (overskriftene ett nivå ned).
- Finnes seksjonen allerede, vis forskjellene mot pluginens versjon og spør før du erstatter den.
  Behold det brukeren har lagt til selv, særlig **Plassering**.

## 4. Første innhold

Spør hvilke fagområder (domener) og hvilke kildesystemer virksomheten har, og tilby:

- domenene med skillen `domene`
- systemene fra `${CLAUDE_PLUGIN_ROOT}/maler/system.md`, med generiske id-er (`erp`, `crm`, …)
- det første begrepet med skillen `begrep`, eller den første prosessen med skillen `prosess`

Et fullt utfylt eksempel finnes i `example/` i pluginens repo, hvis brukeren vil se hvordan en ferdig
katalog kan se ut. Strukturen der er bare ett valg av mange.
