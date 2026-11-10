# Begrepskatalog: instruksjoner for agenter

Dette repoet er en norsk begrepskatalog (forretningsordliste/kunnskapsgraf). Hvert begrep er én
Markdown-fil med YAML-frontmatter. Katalogen er laget for å kunne brukes som kontekst når
semantiske modeller og måltall skal genereres.

## Oppbygging

- `INDEKS.md`: **start her.** Alle domener, begreper (id, navn, type, status, synonymer,
  kortdefinisjon) og systemer. Generert, skal ikke redigeres for hånd.
- `begreper/<domene>/<id>.md`: ett begrep per fil. Filnavn = `id`, mappe = `domene`.
- `begreper/<domene>/_domene.md`: hva domenet dekker.
- `systemer/<id>.md`: kildesystemene som begrepene kan finnes i.
- `maler/`: malene. `veiledning/`: skriveveiledning for mennesker.
- `scripts/valider.py`: validering og generering av `INDEKS.md`.

## Slå opp et begrep

1. Søk i `INDEKS.md` (navn, synonymer, kortdefinisjon): `grep -i "<ord>" INDEKS.md`
2. Les filen. Alt **over** `## Systemrepresentasjon` er forretningsdefinisjonen. Alt under er hvordan
   begrepet finnes i hvert system, inkludert **avvik**, som sier hvilke filtre og korreksjoner som
   trengs for at kildedataene skal stemme med definisjonen.
3. Gjett aldri en definisjon. Hvis begrepet ikke finnes, si det.
4. Vær forsiktig med `status: utkast` og sjekk **Åpne spørsmål**.

## Grep-oppskrifter

```sh
grep -rl "^type: maaltall" begreper                     # alle måltall
grep -rl "^type: maaltall" begreper/okonomi             # måltall i ett domene
grep -rl "^status: utkast" begreper                     # alt som ikke er ferdig
grep -rli "^synonymer:.*nettosalg" begreper             # søk på synonym
grep -rl "^systemer:.*\berp\b" begreper                 # begreper som finnes i ERP
grep -rlE "\[\[kunde\]\]|: \[.*\bkunde\b.*\]" begreper  # alt som peker på kunde
grep -rl "^tidsdimensjon: fakturadato" begreper         # måltall plassert i tid av fakturadato
grep -h "^kortdefinisjon:" begreper/*/*.md              # alle kortdefinisjoner
```

Frontmatter-lister står alltid på én linje (`synonymer: [a, b]`), så grep viser hele lista.

## Generere semantiske modeller

Se `veiledning/begrepstyper.md`, avsnittet "Fra katalog til semantisk modell". Kort fortalt:
entitet → entitet med nøkkel (`identifiseres_ved`, `tilhorer`, `del_av`). Dimensjon → attributt
(`beskriver`). Klassifisering → filter/boolsk dimensjon (`er_en`). Måltall → mål (`grain`,
`tidsdimensjon`, `aggregering`, `additivitet`, formel i **Beregning** med `avledet_av`).
Kildedata og filtre hentes fra **Systemrepresentasjon**. Respekter `additivitet`: `semi_additiv`
skal aldri summeres over tid.

## Endre katalogen

- Bruk skillen `begrep` (`.claude/skills/begrep/`) når brukeren vil opprette eller endre et begrep.
- Rediger bare begreper når brukeren ber om det.
- Følg malen nøyaktig: faste felt, faste seksjoner, fast rekkefølge.
- Ingen produkt- eller leverandørnavn i malen, veiledningen eller eksemplene. Systemer omtales med
  generiske id-er (`erp`, `crm` …).
- Kjør alltid `uv run scripts/valider.py` etter endringer. Den regenererer `INDEKS.md`.
  `--sjekk` feiler hvis indeksen er utdatert (for CI).
