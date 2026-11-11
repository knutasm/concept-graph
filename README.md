# Begrepskatalog

En felles, norsk forretningsordliste. Den beskriver hva begrepene våre **betyr**, hvordan de
henger sammen, og hvordan de finnes i systemene våre.

Katalogen har to formål:

1. **Felles språk.** Når to avdelinger sier "kunde" eller "omsetning", skal de mene det samme, og
   når de ikke gjør det, skal det stå hvorfor.
2. **Grunnlag for analyse.** Godt utfylt kan katalogen brukes som kontekst for å bygge semantiske
   modeller og måltall automatisk. Definisjonene sier *hva* som skal beregnes, og
   systemrepresentasjonene sier *hvor* dataene finnes. Se [skills/semantisk-modell](skills/semantisk-modell/SKILL.md).

## Installere

Repoet er en Claude Code-plugin, med en markedsplass som bare har denne pluginen:

```
/plugin marketplace add knutasm/concept-graph
/plugin install begrepskatalog@begrepskatalog
```

Gå så til repoet der katalogen skal ligge, og be Claude om å sette den opp ("sett opp begrepskatalog").
Claude spør hvor sidene skal ligge, og legger instruksjoner for agenter i `CLAUDE.md`.

Pluginen bestemmer ikke mappestrukturen, og den validerer ikke. Sidene kjennes igjen på `type` og
`id` i frontmatter, uansett hvor de ligger. Hvor de ligger, står i `CLAUDE.md`.

Vil du se hvordan en ferdig katalog kan se ut, se [example/](example/): en utfylt katalog for en
varehandel, med domener, begreper, prosesser og systemer. Åpne `example/katalog/` som vault i Obsidian.
Eksempelet har også et eget valideringsskript, som et eksempel på hva et team kan lage selv.

## Kom i gang

| Jeg vil … | Gå til |
|---|---|
| sette opp en katalog | Be Claude om det ("sett opp begrepskatalog") |
| lage eller endre et begrep | Be Claude om det ("nytt begrep: returandel"), så blir du guidet gjennom det. Eller bruk [malen](maler/begrep.md) |
| kartlegge en prosess | Be Claude om det ("kartlegg prosessen ordre til faktura"). Eller bruk [malen](maler/prosess.md) |
| få gjennomgått en side jeg har skrevet selv | Be Claude om det ("se over ordreinngang"), så får du spørsmål til det som er uklart |
| intervjue en fagekspert | Be Claude om en intervjuguide ("lag en intervjuguide om returandel"). Lim inn notater eller transkript etterpå, så blir sidene fylt ut |
| lage en semantisk modell fra katalogen | Be Claude om det ("lag semantisk modell for salg"). Se [skillen](skills/semantisk-modell/SKILL.md) |
| lære å skrive gode begreper | [veiledning/godt-begrep.md](veiledning/godt-begrep.md) |
| forstå skillet forretning/system | [veiledning/forretning-vs-system.md](veiledning/forretning-vs-system.md) |
| velge riktig type | [veiledning/begrepstyper.md](veiledning/begrepstyper.md) |
| knytte begreper sammen | [veiledning/relasjoner.md](veiledning/relasjoner.md) |
| lage et domene eller se over grensene | Be Claude om det ("se over domenegrensene"). Eller les [veiledning/domener.md](veiledning/domener.md) |

## Oppbygging

```
.claude-plugin/                        Plugin og markedsplass
skills/                                oppsett, begrep, prosess, domene, gjennomgang, intervju og semantisk-modell
maler/                                 Maler for begrep, prosess, domene og system
veiledning/                            Skriveveiledning
kontekst/CLAUDE.md                     Instruksjoner for agenter, som legges i repoet med katalogen
kontekst/sider.md                      Hvordan skillene finner sider og lagrer nye
example/                               Ferdig utfylt eksempelkatalog, med egen validering
```

I ditt eget repo er det fire slags sider, hver med `type` i frontmatter:

| Side | `type` | Mal |
|---|---|---|
| Begrep | `entitet`, `hendelse`, `maaltall`, `dimensjon`, `klassifisering` | [maler/begrep.md](maler/begrep.md) |
| Prosess | `prosess` | [maler/prosess.md](maler/prosess.md) |
| Domene | `domene` | [maler/domene.md](maler/domene.md) |
| System | `system` | [maler/system.md](maler/system.md) |

### Ett begrep, to deler

Hver oppføring skiller mellom **forretningsbegrepet** (hva det betyr, uavhengig av system) og
**systemrepresentasjonen** (hvordan hvert system lagrer det, og hvor systemet avviker). Det er
den viktigste regelen i katalogen. Les [forretning-vs-system.md](veiledning/forretning-vs-system.md).

### Fem typer

`entitet` (vare, kunde, ordre), `hendelse` (varemottak, leveranse), `maaltall` (omsetning,
lagerbeholdning), `dimensjon` (fakturadato, varegruppe) og `klassifisering` (aktiv kunde, restordre). Se
[begrepstyper.md](veiledning/begrepstyper.md).

### Prosesser

En forretningsprosess (mal i [maler/prosess.md](maler/prosess.md)) beskriver en
evne virksomheten må ha: hvor den starter og slutter, hvem som deltar, stegene, beslutningene og
resultatene, og hvilke entiteter og hendelser som brukes og oppstår i hvert steg. Stegene er
strukturerte blokker, så et flytskjema med svømmebaner kan lages fra dem. Se
[prosesser.md](veiledning/prosesser.md), og [OVERSIKT.md](example/katalog/OVERSIKT.md) i eksempelet for diagrammer laget fra prosessene.

## Konvensjoner

- **id = filnavn** (unntatt domenesider), unik på tvers av alle sider, små bokstaver, `_`, uten æøå (æ→ae, ø→o, å→aa). Visningsnavnet (`navn`) skrives på vanlig norsk.
- **Tittel = `navn`.** Første overskrift (`# `) i filen er lik `navn`. Obsidian viser `navn` som tittel med tillegget Front Matter Title. Gi aldri filen nytt navn i Obsidian, det bryter `id`.
- **Domene = felt.** Begreper og prosesser hører til et domene gjennom feltet `domene`, ikke gjennom mappen de ligger i.
- **Standard Markdown.** Filene skal være lesbare uten Obsidian. Obsidian-oppsett hører hjemme i vaultens `.obsidian/`, ikke i filene.
- **Lister på én linje** i frontmatter (`synonymer: [a, b]`), så grep viser hele lista.
- **Lenker** til andre begreper skrives `[[id]]`.
- **Systemer** omtales med generiske id-er (`erp`, `crm` …), og har hver sin side. I `systemer` og `kilde` skrives de som lenker: `systemer: ["[[erp]]"]`.
- **Kilde:** `kilde` sier hvilket system en entitet eller hendelse oppstår og endres i. De andre systemene er kopier.

## Søke med grep

```sh
grep -rli --include='*.md' -E "^(navn|synonymer|kortdefinisjon):.*omsetning" .  # finn begreper på navn, synonym eller definisjon
grep -rl --include='*.md' "^type: maaltall$" .           # alle måltall
grep -rl --include='*.md' "^status: utkast$" .           # alt som ikke er ferdig
grep -rl --include='*.md' "\[\[kunde\]\]" .              # alt som peker på kunde
```

Flere oppskrifter står i [kontekst/CLAUDE.md](kontekst/CLAUDE.md).
