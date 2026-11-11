# Begrepskatalog: instruksjoner for agenter

Dette repoet er en norsk begrepskatalog (forretningsordliste/kunnskapsgraf). Hvert begrep er én
Markdown-fil med YAML-frontmatter. Katalogen er laget for å kunne brukes som kontekst når
semantiske modeller og måltall skal genereres.

## Oppbygging

Alt innhold ligger i `katalog/`, som også er Obsidian-vaulten. Skills, skript og instruksjoner
ligger utenfor. Lenker inne i katalogen er relative til `katalog/`.

- `katalog/INDEKS.md`: **start her.** Alle domener, begreper (id, navn, type, status, synonymer,
  kortdefinisjon) og systemer. Generert, skal ikke redigeres for hånd.
- `katalog/OVERSIKT.md`: Mermaid-diagram per forretningsprosess, måltallsmatrise (grain, tidsdimensjon, additivitet),
  kjente systemavvik og uferdige begreper. Generert. Godt utgangspunkt for semantiske modeller.
- `katalog/begreper/<domene>/<id>.md`: ett begrep per fil. Filnavn = `id`, mappe = `domene`.
  Første overskrift `# ` er lik `navn` (tittelen i Obsidian).
- `katalog/begreper/<domene>/_domene.md`: hva domenet dekker.
- `katalog/systemer/<id>.md`: kildesystemene som begrepene kan finnes i.
- `katalog/prosesser/<id>.md`: forretningsprosessene (evner). Steg (`### s1`), beslutninger (`### b1`) og
  resultater (`### r1`) er blokker med faste felt: **Aktør**, **Bruker**, **Gir**, **Neste**, **Regel**,
  **Hendelse**. `utloser` og `begreper` lister entitetene og hendelsene som inngår (bare disse typene).
  Mal: `katalog/maler/prosess.md`. Veiledning: `katalog/veiledning/prosesser.md`.
- `katalog/begreper/<domene>/_domene.md` har valgfri `domenetype` (`kjerne | stottende | generisk`).
  Mal: `katalog/maler/domene.md`. Veiledning: `katalog/veiledning/domener.md`.
- `katalog/maler/`: malene. `katalog/veiledning/`: skriveveiledning for mennesker.
- `scripts/valider.py`: validering og generering av `katalog/INDEKS.md` og `katalog/OVERSIKT.md`.

## Slå opp et begrep

1. Søk i `katalog/INDEKS.md` (navn, synonymer, kortdefinisjon): `grep -i "<ord>" katalog/INDEKS.md`
2. Les filen. Alt **over** `## Systemrepresentasjon` er forretningsdefinisjonen. Alt under er hvordan
   begrepet finnes i hvert system, inkludert **avvik**, som sier hvilke filtre og korreksjoner som
   trengs for at kildedataene skal stemme med definisjonen. `kilde` sier hvilket system begrepet
   oppstår og endres i. De andre systemene er kopier.
3. Gjett aldri en definisjon. Hvis begrepet ikke finnes, si det.
4. Vær forsiktig med `status: utkast` og sjekk **Åpne spørsmål**.

## Grep-oppskrifter

```sh
grep -rl "^type: maaltall" katalog/begreper                     # alle måltall
grep -rl "^type: maaltall" katalog/begreper/salg                # måltall i ett domene
grep -rl "^status: utkast" katalog/begreper                     # alt som ikke er ferdig
grep -rli "^synonymer:.*bruttomargin" katalog/begreper          # søk på synonym
grep -rl "^systemer:.*\berp\b" katalog/begreper                 # begreper som finnes i ERP
grep -rl "^kilde: erp" katalog/begreper                         # begreper der ERP er kilden
grep -h "^domenetype:" katalog/begreper/*/_domene.md             # domenetypene
grep -rl "\[\[kunde\]\]" katalog/begreper                     # alt som peker på kunde
grep -rl "\[\[kunde\]\]" katalog/prosesser                    # prosesser kunde inngår i
grep -h "^kortdefinisjon:" katalog/prosesser/*.md               # alle prosesser
grep -rh "^- \*\*Aktør:\*\*" katalog/prosesser | sort -u        # alle aktører
grep -rl "Gir:\*\*.*\[\[faktura\]\]" katalog/prosesser          # prosesser der en faktura oppstår
grep -rl "Neste:\*\*.*\[\[plukk_og_levering\]\]" katalog/prosesser # prosesser som fortsetter i en annen
grep -rl "^tidsdimensjon:.*\[\[fakturadato\]\]" katalog/begreper # måltall plassert i tid av fakturadato
grep -h "^kortdefinisjon:" katalog/begreper/*/*.md              # alle kortdefinisjoner
```

Frontmatter-lister står alltid på én linje (`synonymer: [a, b]`), så grep viser hele lista.
Referanser til andre begreper (relasjoner, `grain`, `tidsdimensjon`, `tidspunkt` og lenker i teksten)
skrives alltid `[[id]]`, så `grep "\[\[id\]\]"` finner alle.

## Generere semantiske modeller

Se `katalog/veiledning/begrepstyper.md`, avsnittet "Fra katalog til semantisk modell". Kort fortalt:
entitet → entitet med nøkkel (`identifiseres_ved`, `tilhorer`, `del_av`). Dimensjon → attributt
(`beskriver`). Klassifisering → filter/boolsk dimensjon (`er_en`). Måltall → mål (`grain`,
`tidsdimensjon`, `aggregering`, `additivitet`, formel i **Beregning** med `avledet_av`).
Kildedata og filtre hentes fra **Systemrepresentasjon**. Les fra systemet i `kilde`, og bruk kopier
bare med avvikene deres. Respekter `additivitet`: `semi_additiv`
skal aldri summeres over tid.

## Endre katalogen

- Bruk skillen `begrep` (`.claude/skills/begrep/`) når brukeren vil opprette eller endre et begrep.
- Bruk skillen `prosess` (`.claude/skills/prosess/`) når brukeren vil kartlegge eller endre en prosess.
- Bruk skillen `domene` (`.claude/skills/domene/`) når brukeren vil lage et domene eller se over domenegrensene.
- Rediger bare begreper når brukeren ber om det.
- Følg malen nøyaktig: faste felt, faste seksjoner, fast rekkefølge.
- Ingen produkt- eller leverandørnavn i malen, veiledningen eller eksemplene. Systemer omtales med
  generiske id-er (`erp`, `crm` …).
- Kjør alltid `uv run scripts/valider.py` etter endringer. Den regenererer `katalog/INDEKS.md` og `katalog/OVERSIKT.md`.
  `--sjekk` feiler hvis en av dem er utdatert (for CI).
