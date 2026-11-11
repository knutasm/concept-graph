# Finne og lagre sider

Pluginen bestemmer ikke hvor sidene ligger. Brukeren kan ha katalogen i én mappe, spredt i en
dokumentasjonsmappe, eller sortert etter domene, prosess eller noe annet. Sidene kjennes igjen på
frontmatter, ikke på plassering.

## Sidetypene

Hver side har `id` og `type` i frontmatter:

| `type` | Side | Mal |
|---|---|---|
| `entitet`, `hendelse`, `maaltall`, `dimensjon`, `klassifisering` | begrep | `maler/begrep.md` |
| `prosess` | prosess | `maler/prosess.md` |
| `domene` | domene | `maler/domene.md` |
| `system` | system | `maler/system.md` |

`id` er unikt på tvers av alle sider, så `[[id]]` alltid peker på én side. For begreper, prosesser og
systemer er `id` også filnavnet uten `.md`, fordi `[[id]]`-lenker finner sider på filnavnet. Domenesider
lenkes ikke til, så de kan hete hva som helst.
Begreper og prosesser hører til et domene gjennom feltet `domene`, ikke gjennom mappen de ligger i.

## Finne sider

Står det i `CLAUDE.md` hvor katalogen ligger, søk bare der. Ellers søk i hele repoet. Hopp over
kopier av malene (id som begynner på `eksempel`).

```sh
grep -rl --include='*.md' "^id: <id>$" .                                   # siden med en id
grep -rli --include='*.md' -E "^(navn|synonymer|kortdefinisjon):.*<ord>" .   # søk på navn, synonym og definisjon
grep -rl --include='*.md' -E "^type: (entitet|hendelse|maaltall|dimensjon|klassifisering)$" .  # alle begreper
grep -rl --include='*.md' "^type: prosess$" .                               # alle prosesser (domene, system likedan)
grep -rl --include='*.md' "^domene: <domene>$" .                            # alt som hører til et domene
grep -rl --include='*.md' "\[\[<id>\]\]" .                                  # alt som peker på en side
grep -rl --include='*.md' "^type: domene$" . | xargs grep -HE "^(navn|beskrivelse):"   # oversikt over domenene
```

Har repoet en generert indeks eller oversikt, kan du bruke den til å finne fram, men les alltid selve
siden før du stoler på den.

## Lagre nye sider

1. Står det i `CLAUDE.md` hvor nye sider skal ligge, følg det.
2. Ellers: legg siden der brukeren har lagt sider av samme slag. Ligger for eksempel begrepene i
   mapper etter domene, legg det nye begrepet i mappen for sitt domene.
3. Finnes det ingen sider av samme slag, spør brukeren hvor siden skal ligge. Tilby å skrive valget
   inn i `CLAUDE.md`, så du ikke trenger å spørre igjen.

Filnavnet er `<id>.md`, unntatt for domener. Flytt aldri en side uten at brukeren ber om det. Gi aldri en side nytt
filnavn, det bryter `id` og lenkene.

## Lese over før du er ferdig

Pluginen har ingen validering. Les siden over mot malen før du sier at den er ferdig:

- felt og seksjoner som malen krever for typen, i malens rekkefølge, uten malens kommentarer
- frontmatter-lister på én linje
- at hver `[[id]]` peker på en side som finnes (søk som over), og at felt som `granularitet`,
  `tidsdimensjon` og `tidspunkt` peker på en side av riktig type
- at hvert system i `systemer` har en underseksjon under **Systemrepresentasjon**, og at `kilde` står i `systemer`

Har brukeren egen validering (et skript, CI eller pre-commit), og står det i `CLAUDE.md`, kjør den.
