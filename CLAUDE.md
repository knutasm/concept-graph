# Begrepskatalog-pluginen: instruksjoner for agenter

Dette repoet er en Claude Code-plugin for norske begrepskataloger (forretningsordliste/kunnskapsgraf).
Pluginen har det som trengs for å bygge en katalog: skills, maler, skriveveiledning og kontekst for
agenter. Selve katalogen ligger i repoet til den som bruker pluginen.
`example/` er en ferdig utfylt eksempelkatalog, brukt til å vise og teste pluginen.

To prinsipper:

- **Pluginen validerer ikke.** Skillene leser sidene over mot malen, men det finnes ikke noe
  valideringsskript i pluginen. Validering er noe hvert team kan lage selv (se `example/scripts/`).
- **Pluginen bestemmer ikke mappestrukturen.** Sidene kjennes igjen på `type` og `id` i frontmatter,
  ikke på plassering. Brukerens `CLAUDE.md` (seksjonen **Plassering**) sier hvor de ligger.

## Oppbygging

- `.claude-plugin/plugin.json` og `.claude-plugin/marketplace.json`: pluginen, og en markedsplass med
  bare denne pluginen, så repoet kan installeres direkte.
- `skills/<navn>/SKILL.md`: `oppsett`, `begrep`, `prosess`, `domene`, `gjennomgang`, `intervju` og
  `semantisk-modell`. Skillene viser til filer i pluginen med `${CLAUDE_PLUGIN_ROOT}/…`. Til brukerens
  sider viser de aldri med en fast sti, men søker på frontmatter.
- `maler/`: malene for begrep, prosess, domene og system.
- `veiledning/`: skriveveiledning for mennesker, som skillene også leser.
- `kontekst/CLAUDE.md`: instruksjonene for agenter som `oppsett` legger i brukerens repo
  (sidene, oppslag, grep-oppskrifter, og en **Plassering** brukeren fyller inn).
- `kontekst/sider.md`: hvordan skillene finner sider, hvor nye sider lagres, og hva de leser over før de er ferdige.
- `example/`: eksempelkatalogen. `example/CLAUDE.md` er `kontekst/CLAUDE.md` med eksempelets **Plassering**.
  `example/scripts/valider.py` validerer eksempelet og genererer `example/katalog/INDEKS.md` og `OVERSIKT.md`.
  Skriptet hører til eksempelet og forutsetter eksempelets mappestruktur.

## Endre pluginen

- Malene, veiledningen, skillene og `kontekst/` henger sammen. Endres et felt, en seksjon eller en regel
  ett sted, oppdater de andre, eksempelkatalogen og `example/scripts/valider.py`.
- Hold `example/CLAUDE.md` lik `kontekst/CLAUDE.md`, bortsett fra **Plassering**.
- Ingen faste stier til brukerens sider i skillene, malene eller veiledningen.
- Ingen produkt- eller leverandørnavn i malene, veiledningen, skillene eller eksemplene. Systemer omtales med
  generiske id-er (`erp`, `crm` …).
- Skriv standard Markdown som er lesbar uten Obsidian. Ikke tilpass filene til Obsidian utover `[[id]]`-lenkene.
- Kjør `uv run scripts/valider.py` fra `example/` etter endringer, så eksempelet holder seg gyldig.
- Test pluginen lokalt med `claude --plugin-dir .` (f.eks. fra `example/`: `claude --plugin-dir ..`).
- Øk `version` i `.claude-plugin/plugin.json` når en endring skal ut til brukerne.

## Endre eksempelkatalogen

Eksempelkatalogen følger reglene i `example/CLAUDE.md`. Rediger bare begreper når brukeren ber om det.
