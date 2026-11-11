# Begrepskatalog

En felles, norsk forretningsordliste. Den beskriver hva begrepene våre **betyr**, hvordan de
henger sammen, og hvordan de finnes i systemene våre.

Katalogen har to formål:

1. **Felles språk.** Når to avdelinger sier "kunde" eller "omsetning", skal de mene det samme, og
   når de ikke gjør det, skal det stå hvorfor.
2. **Grunnlag for analyse.** Godt utfylt kan katalogen brukes som kontekst for å bygge semantiske
   modeller og måltall automatisk. Definisjonene sier *hva* som skal beregnes, og
   systemrepresentasjonene sier *hvor* dataene finnes.

## Kom i gang

| Jeg vil … | Gå til |
|---|---|
| finne et begrep | [INDEKS.md](katalog/INDEKS.md) |
| se sammenhenger, måltall og systemavvik | [OVERSIKT.md](katalog/OVERSIKT.md) |
| lage eller endre et begrep | Be Claude om det ("nytt begrep: returandel"), så blir du guidet gjennom det. Eller bruk [malen](katalog/maler/begrep.md) |
| lære å skrive gode begreper | [veiledning/godt-begrep.md](katalog/veiledning/godt-begrep.md) |
| forstå skillet forretning/system | [veiledning/forretning-vs-system.md](katalog/veiledning/forretning-vs-system.md) |
| velge riktig type | [veiledning/begrepstyper.md](katalog/veiledning/begrepstyper.md) |
| knytte begreper sammen | [veiledning/relasjoner.md](katalog/veiledning/relasjoner.md) |
| lage et domene eller se over grensene | Be Claude om det ("se over domenegrensene"). Eller les [veiledning/domener.md](katalog/veiledning/domener.md) |

## Oppbygging

Åpne mappen `katalog/` som vault i Obsidian. Verktøy og instruksjoner for Claude ligger utenfor.

```
katalog/                               Obsidian-vaulten: alt som skal leses
  INDEKS.md                            Innholdsfortegnelse (generert)
  OVERSIKT.md                          Domene- og prosesskart, prosessdiagrammer, måltall, kilder, systemavvik og uferdige begreper (generert)
  begreper/<domene>/_domene.md         Hva domenet dekker
  begreper/<domene>/<id>.md            Ett begrep per fil
  systemer/<id>.md                     Kildesystemene
  prosesser/<id>.md                    Forretningsprosessene: aktører, steg, beslutninger, resultater
  maler/                               Maler for begrep, prosess, domene og system
  veiledning/                          Skriveveiledning
scripts/valider.py                     Validering og generering av INDEKS.md og OVERSIKT.md
.claude/skills/                        Veiledet arbeid med Claude: begrep, prosess og domene
```

### Ett begrep, to deler

Hver oppføring skiller mellom **forretningsbegrepet** (hva det betyr, uavhengig av system) og
**systemrepresentasjonen** (hvordan hvert system lagrer det, og hvor systemet avviker). Det er
den viktigste regelen i katalogen. Les [forretning-vs-system.md](katalog/veiledning/forretning-vs-system.md).

### Fem typer

`entitet` (vare, kunde, ordre), `hendelse` (varemottak, leveranse), `maaltall` (omsetning,
lagerbeholdning), `dimensjon` (fakturadato, varegruppe) og `klassifisering` (aktiv kunde, restordre). Se
[begrepstyper.md](katalog/veiledning/begrepstyper.md).

### Prosesser

En forretningsprosess (`katalog/prosesser/<id>.md`, mal i [maler/prosess.md](katalog/maler/prosess.md)) beskriver en
evne virksomheten må ha: hvor den starter og slutter, hvem som deltar, stegene, beslutningene og
resultatene, og hvilke entiteter og hendelser som brukes og oppstår i hvert steg. Stegene er
strukturerte blokker, så et flytskjema med svømmebaner kan lages fra dem. Se
[prosesser.md](katalog/veiledning/prosesser.md). [OVERSIKT.md](katalog/OVERSIKT.md) har ett diagram per prosess
som viser relasjonene mellom begrepene.

## Konvensjoner

- **id = filnavn**, små bokstaver, `_`, uten æøå (æ→ae, ø→o, å→aa). Visningsnavnet (`navn`) skrives på vanlig norsk.
- **Tittel = `navn`.** Første overskrift (`# `) i filen er lik `navn`. Obsidian viser `navn` som tittel med tillegget Front Matter Title. Gi aldri filen nytt navn i Obsidian, det bryter `id`.
- **Domene = mappe.** Begrepets `domene` må være lik mappen filen ligger i.
- **Standard Markdown.** Filene skal være lesbare uten Obsidian. Obsidian-oppsettet (tittel fra `navn`, strenge linjeskift i lesemodus) ligger i `katalog/.obsidian/`, ikke i filene.
- **Lister på én linje** i frontmatter (`synonymer: [a, b]`), så grep viser hele lista.
- **Lenker** til andre begreper skrives `[[id]]`.
- **Systemer** omtales med generiske id-er fra `katalog/systemer/`.
- **Kilde:** `kilde` sier hvilket system en entitet eller hendelse oppstår og endres i. De andre systemene er kopier.

## Søke med grep

```sh
grep -i "omsetning" katalog/INDEKS.md                    # finn begreper på navn, synonym eller definisjon
grep -rl "^type: maaltall" katalog/begreper              # alle måltall
grep -rl "^status: utkast" katalog/begreper              # alt som ikke er ferdig
grep -rl "\[\[kunde\]\]" katalog/begreper           # alt som peker på kunde
grep -rl "\[\[kunde\]\]" katalog/prosesser          # prosesser kunde inngår i
```

Flere oppskrifter står i [CLAUDE.md](CLAUDE.md).

## Validering

Krever [uv](https://docs.astral.sh/uv/).

```sh
uv run scripts/valider.py          # valider alt og generer katalog/INDEKS.md og katalog/OVERSIKT.md
uv run scripts/valider.py --sjekk  # valider, og feil hvis katalog/INDEKS.md eller katalog/OVERSIKT.md er utdatert
```

Valideringen sjekker blant annet påkrevde felt per type, gyldige verdier, at id og domene stemmer
med filplasseringen, at relasjoner, lenker og systemer finnes, seksjonsrekkefølge, og at hvert
system i frontmatter har en underseksjon. Den **advarer** også når forretningsdelen nevner
systemnavn eller ser teknisk ut, og når et synonym brukes av flere begreper.
