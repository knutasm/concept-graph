# Begrepskatalog: instruksjoner for agenter

Dette repoet har en norsk begrepskatalog (forretningsordliste/kunnskapsgraf). Hvert begrep, hver
prosess, hvert domene og hvert system er én Markdown-side med YAML-frontmatter. Katalogen er laget for
å kunne brukes som kontekst når semantiske modeller og måltall skal genereres.

Malene, skriveveiledningen og skillene kommer fra pluginen `begrepskatalog`.

## Plassering

<!-- Fyll inn hvor sidene ligger, og hvor nye sider skal lagres. For eksempel:
- Alle sidene ligger i `katalog/`, som også er Obsidian-vaulten.
- Begreper: `katalog/begreper/<domene>/<id>.md`. Prosesser: `katalog/prosesser/`. Systemer: `katalog/systemer/`.
- Domenesider: `katalog/begreper/<domene>/_domene.md`.
- Validering: `uv run scripts/valider.py` (hvis teamet har egen validering).
-->

## Sidene

Sidene kjennes igjen på `type` i frontmatter, ikke på hvor de ligger:

- **Begreper** (`entitet`, `hendelse`, `maaltall`, `dimensjon`, `klassifisering`): alt **over**
  `## Systemrepresentasjon` er forretningsdefinisjonen. Alt under er hvordan begrepet finnes i hvert
  system, inkludert **avvik**, som sier hvilke filtre og korreksjoner som trengs for at kildedataene
  skal stemme med definisjonen. `kilde` sier hvilket system begrepet oppstår og endres i. De andre
  systemene er kopier.
- **Prosesser** (`prosess`): forretningsprosessene (evner). Steg (`### s1`), beslutninger (`### b1`) og
  resultater (`### r1`) er blokker med faste felt: **Aktør**, **Bruker**, **Gir**, **Neste**, **Regel**,
  **Hendelse**. `utloser` og `begreper` lister entitetene og hendelsene som inngår.
- **Domener** (`domene`): hva domenet dekker. Begreper og prosesser hører til et domene gjennom feltet `domene`.
- **Systemer** (`system`): kildesystemene som begrepene kan finnes i.

`id` er unik på tvers av alle sider. For begreper, prosesser og systemer er den også filnavnet.

## Slå opp et begrep

1. Søk på navn, synonymer og kortdefinisjon:
   `grep -rli --include='*.md' -E "^(navn|synonymer|kortdefinisjon):.*<ord>" .`
2. Les siden.
3. Gjett aldri en definisjon. Hvis begrepet ikke finnes, si det.
4. Vær forsiktig med `status: utkast` og sjekk **Åpne spørsmål**.

## Grep-oppskrifter

Begrens søket til mappen under **Plassering** hvis det står en der.

```sh
grep -rl --include='*.md' "^type: maaltall$" .                       # alle måltall
grep -rl --include='*.md' "^domene: salg$" .                         # alt i ett domene
grep -rl --include='*.md' "^status: utkast$" .                       # alt som ikke er ferdig
grep -rli --include='*.md' "^synonymer:.*bruttomargin" .             # søk på synonym
grep -rl --include='*.md' "^systemer:.*\[\[erp\]\]" .                # begreper som finnes i ERP
grep -rl --include='*.md' "^kilde:.*\[\[erp\]\]" .                   # begreper der ERP er kilden
grep -rl --include='*.md' "\[\[kunde\]\]" .                          # alt som peker på kunde
grep -rl --include='*.md' "^type: prosess$" .                        # alle prosesser
grep -rh --include='*.md' "^- \*\*Aktør:\*\*" . | sort -u            # alle aktører
grep -rl --include='*.md' "Gir:\*\*.*\[\[faktura\]\]" .              # prosesser der en faktura oppstår
grep -rl --include='*.md' "^tidsdimensjon:.*\[\[fakturadato\]\]" .   # måltall plassert i tid av fakturadato
```

Frontmatter-lister står alltid på én linje (`synonymer: [a, b]`), så grep viser hele lista.
Referanser til andre sider (relasjoner, `granularitet`, `tidsdimensjon`, `tidspunkt`, `systemer`,
`kilde` og lenker i teksten) skrives alltid `[[id]]`, så `grep "\[\[id\]\]"` finner alle.

## Generere semantiske modeller

Bruk skillen `semantisk-modell`. Kort fortalt: entitet → entitet med nøkkel (`identifiseres_ved`,
`tilhorer`, `del_av`). Dimensjon → attributt (`beskriver`). Klassifisering → filter/boolsk dimensjon
(`er_en`). Måltall → mål (`granularitet`, `tidsdimensjon`, `aggregering`, `additivitet`, formel i
**Beregning** med `avledet_av`). Kildedata og filtre hentes fra **Systemrepresentasjon**. Les fra
systemet i `kilde`, og bruk kopier bare med avvikene deres. `semi_additiv` skal aldri summeres over tid.

## Endre katalogen

- Bruk skillene fra pluginen: `begrep` (opprette/endre begrep), `prosess` (kartlegge prosess),
  `domene` (domener og domenegrenser), `gjennomgang` (se over en side en fagekspert har skrevet),
  `intervju` (forberede intervju, eller gjøre notater/transkript om til sider).
- Rediger bare sider når brukeren ber om det.
- Følg malen nøyaktig: faste felt, faste seksjoner, fast rekkefølge.
- Lagre nye sider etter **Plassering**.
- Skriv standard Markdown som er lesbar uten Obsidian. Ikke tilpass sidene til Obsidian utover `[[id]]`-lenkene.
- Systemer omtales med generiske id-er (`erp`, `crm` …), ikke produkt- eller leverandørnavn.
