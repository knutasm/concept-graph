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
| finne et begrep | [INDEKS.md](INDEKS.md) |
| lage eller endre et begrep | Be Claude om det ("nytt begrep: aktiv kunde"), så blir du guidet gjennom det. Eller bruk [malen](maler/begrep.md) |
| lære å skrive gode begreper | [veiledning/godt-begrep.md](veiledning/godt-begrep.md) |
| forstå skillet forretning/system | [veiledning/forretning-vs-system.md](veiledning/forretning-vs-system.md) |
| velge riktig type | [veiledning/begrepstyper.md](veiledning/begrepstyper.md) |
| knytte begreper sammen | [veiledning/relasjoner.md](veiledning/relasjoner.md) |

## Oppbygging

```
INDEKS.md                      Innholdsfortegnelse (generert)
begreper/<domene>/_domene.md   Hva domenet dekker
begreper/<domene>/<id>.md      Ett begrep per fil
systemer/<id>.md               Kildesystemene
maler/                         Maler for begrep og system
veiledning/                    Skriveveiledning
scripts/valider.py             Validering og generering av INDEKS.md
.claude/skills/begrep/         Veiledet oppretting og oppdatering med Claude
```

### Ett begrep, to deler

Hver oppføring skiller mellom **forretningsbegrepet** (hva det betyr, uavhengig av system) og
**systemrepresentasjonen** (hvordan hvert system lagrer det, og hvor systemet avviker). Det er
den viktigste regelen i katalogen. Les [forretning-vs-system.md](veiledning/forretning-vs-system.md).

### Fem typer

`entitet` (kunde, ordre), `hendelse` (betaling mottatt), `maaltall` (netto omsetning),
`dimensjon` (fakturadato, region) og `klassifisering` (aktiv kunde). Se
[begrepstyper.md](veiledning/begrepstyper.md).

## Konvensjoner

- **id = filnavn**, små bokstaver, `_`, uten æøå (æ→ae, ø→o, å→aa). Visningsnavnet (`navn`) skrives på vanlig norsk.
- **Domene = mappe.** Begrepets `domene` må være lik mappen filen ligger i.
- **Lister på én linje** i frontmatter (`synonymer: [a, b]`), så grep viser hele lista.
- **Lenker** til andre begreper skrives `[[id]]`.
- **Systemer** omtales med generiske id-er fra `systemer/`.

## Søke med grep

```sh
grep -i "omsetning" INDEKS.md                    # finn begreper på navn, synonym eller definisjon
grep -rl "^type: maaltall" begreper              # alle måltall
grep -rl "^status: utkast" begreper              # alt som ikke er ferdig
grep -rlE "\[\[kunde\]\]|: \[.*\bkunde\b.*\]" begreper   # alt som peker på kunde
```

Flere oppskrifter står i [CLAUDE.md](CLAUDE.md).

## Validering

Krever [uv](https://docs.astral.sh/uv/).

```sh
uv run scripts/valider.py          # valider alt og generer INDEKS.md
uv run scripts/valider.py --sjekk  # valider, og feil hvis INDEKS.md er utdatert
```

Valideringen sjekker blant annet påkrevde felt per type, gyldige verdier, at id og domene stemmer
med filplasseringen, at relasjoner, lenker og systemer finnes, seksjonsrekkefølge, og at hvert
system i frontmatter har en underseksjon. Den **advarer** også når forretningsdelen nevner
systemnavn eller ser teknisk ut, og når et synonym brukes av flere begreper.
