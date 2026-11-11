# Fra katalog til semantisk modell

Hvordan begrepskatalogen brukes til å bygge semantiske modeller og måltall. Dokumentet er for den
som bygger modellen (menneske eller agent). Katalogen selv beskriver virksomheten, og forklarer
ikke modellering. Se `katalog/veiledning/` for hvordan begrepene skrives.

## Typene

| Type | Rolle i semantisk modell |
|---|---|
| `entitet` | Entitet med nøkkel. Andre begreper kobles til den |
| `hendelse` | Faktagrunnlag med eget tidspunkt |
| `maaltall` | Mål / metrikk |
| `dimensjon` | Attributt, kategori- eller tidsdimensjon |
| `klassifisering` | Filter, segment eller boolsk dimensjon |

## Fremgangsmåte

1. **Entiteter** blir tabeller/objekter med nøkkel fra `identifiseres_ved` og koblinger fra
   `tilhorer` og `del_av`.
2. **Hendelser** blir fakta, plassert i tid av `tidspunkt`.
3. **Dimensjoner** med `beskriver` blir attributter på entiteten de beskriver.
4. **Klassifiseringer** blir boolske dimensjoner eller navngitte filtre på entiteten i `er_en`.
   Regelen står i **Forretningsregler**.
5. **Måltall** blir mål på `grain`-entiteten, plassert i tid av `tidsdimensjon`, aggregert med
   `aggregering`. Måltall med `formel`/`ratio` bygges av måltallene i `avledet_av`, med formelen i
   **Beregning**.
6. **Systemrepresentasjon** sier hvilke kildedata som skal brukes. Les fra systemet i `kilde`. Bruk
   en kopi bare når kilden mangler noe, og ta da med avvikene for kopien.
7. **Avvik** sier hvilke filtre og korreksjoner som trengs for at tallene skal stemme med
   forretningsdefinisjonen. Alle avvik skal med i modellen.

`katalog/OVERSIKT.md` har måltallsmatrisen (grain, tidsdimensjon, additivitet), kildene og alle
kjente avvik samlet.

## Additivitet

`additivitet` sier hvordan måltallet kan summeres på sitt eget `grain`, ut fra hva tallet betyr.
En andel er ikke-additiv, og en beholdning er semi-additiv, uansett hvordan dataene er lagret.

- `additiv`: summeres over alle dimensjoner.
- `semi_additiv`: summeres aldri over tid. **Beregning** sier hvilken verdi som gjelder over tid
  (siste, første, snitt).
- `ikke_additiv`: summeres ikke. Beregnes på nytt på hvert nivå.

Hvordan en tabell er bygget, kan likevel gjøre at kolonnen ikke kan summeres slik måltallet sier.
Slike forhold skal stå som avvik under **Systemrepresentasjon**. Se etter dem også når de mangler:

- **Annet grain.** Et beløp fra fakturahodet gjentas på hver fakturalinje. Summen blir for høy.
  Ta beløpet én gang per faktura.
- **Øyeblikksbilder eller bevegelser.** En beholdning kan lagres som daglige øyeblikksbilder, eller
  bare som bevegelser inn og ut. Måltallet er semi-additivt i begge tilfeller, men med bevegelser
  må beholdningen regnes ut som en løpende sum.
- **Forhåndsaggregert.** Én rad per måned eller per varegruppe kan ikke brytes ned under det
  nivået, selv om måltallet kan det.
- **Ferdig utregnet andel.** En lagret dekningsgrad kan ikke summeres eller snittes. Regn den ut
  på nytt fra delene.

## Andeler

Et ikke-additivt måltall med `aggregering: ratio` eller `formel` peker på delene med `avledet_av`,
f.eks. dekningsgrad = dekningsbidrag / omsetning. Summer delene på ønsket nivå først, og del
etterpå. Snitt aldri ferdige andeler.
