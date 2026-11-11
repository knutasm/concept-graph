---
id: eksempel_prosess           # = filnavn. Små bokstaver, _, uten æøå. Må ikke være lik et begreps id
navn: Eksempelprosess          # Visningsnavn: evnen som verb + objekt, eller "Fra … til …"
domene: salg                   # Domenet som eier prosessen (mappe i begreper/)
kortdefinisjon: Én setning om hva virksomheten må kunne gjøre, og hvor prosessen starter og slutter.
synonymer: []
status: utkast                 # utkast | til_godkjenning | godkjent | utfaset
eier: Avdeling som eier prosessen
gyldig_fra: 2026-01-01         # valgfri
sist_oppdatert: 2026-01-01
utloser: "[[ordre]]"           # valgfri. Entiteten eller hendelsen som starter prosessen
# Alle entiteter og hendelser som inngår, også fra andre domener (alt i Bruker, Gir og Hendelse under).
# Bare type entitet eller hendelse. Relasjonene mellom dem hentes fra begrepene selv.
begreper: ["[[ordre]]", "[[kunde]]"]
---
# Eksempelprosess

<!--
Slett alle kommentarer før du lagrer.
Beskriv prosessen med forretningsord, uten systemnavn eller skjermbilder.
Lenk til begreper med [[id]] og til andre prosesser med [[prosess_id]].
Steg, beslutninger og resultater skrives som ###-blokker med faste felt, slik at et flytskjema
med svømmebaner kan lages fra dem. Se veiledning/prosesser.md.
-->

## Formål

<!-- Evnen virksomheten må ha, som verb + objekt ("Levere bestilte varer til kunden"),
og hvorfor virksomheten trenger den. 1–3 setninger. -->

## Avgrensning

- **Starter når:** …
- **Ferdig når:** …
- **Utenfor:** … <!-- Det som hører til nabo-prosesser, gjerne med [[prosess_id]] -->

## Aktører

<!-- Rollene eller enhetene som utfører steg. Navnene brukes i feltet Aktør under, og blir svømmebaner. -->
| Aktør | Ansvar i prosessen |
|---|---|
| Kunde | Bestiller varene |
| Kundesenter | Bekrefter ordren |

## Steg

<!--
Steg (s…) og beslutninger (b…) i flytrekkefølge. Første blokk er der flyten starter.
Id-ene er faste: ikke nummerer om når du setter inn et steg, bruk f.eks. s2a.
Felt for steg:        Aktør, Bruker, Gir, Neste (nøyaktig én)
Felt for beslutning:  Aktør, Regel, Bruker, Neste (minst to, med etikett: "ja → s2; nei → r2")
Bruker = begreper som leses. Gir = begreper som oppstår eller endres. Bare [[entitet]] og [[hendelse]].
Neste = en id i denne filen eller [[annen_prosess]] (flyten fortsetter der).
-->

### s1 Bekrefte ordre
Kunden bestiller varer, og vi bekrefter bestillingen.
- **Aktør:** Kundesenter
- **Bruker:** [[kunde]]
- **Gir:** [[ordre]]
- **Neste:** b1

### b1 Kan ordren leveres?
- **Aktør:** Kundesenter
- **Regel:** …
- **Neste:** ja → r1; nei → r2

## Resultater

<!-- Alle måter prosessen kan ende på, også de uønskede. Hendelse er valgfri. -->

### r1 Ordre bekreftet
…
- **Hendelse:** [[ordre]]

### r2 Ordre avvist
…

## Åpne spørsmål

<!-- Valgfri. Det som ikke er avklart ennå. -->
