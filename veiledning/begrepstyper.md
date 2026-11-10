# Begrepstyper

Alle begreper har én `type`. Typen bestemmer hvilke felt og seksjoner som er påkrevd, og hvilken
rolle begrepet får i en semantisk modell.

| Type | Spørsmål den svarer på | Eksempler | Rolle i semantisk modell |
|---|---|---|---|
| `entitet` | *Hva* holder vi rede på? | kunde, ordre, faktura, produkt | Entitet med nøkkel. Andre begreper kobles til den |
| `hendelse` | *Hva skjer* på et tidspunkt? | betaling mottatt, abonnement sagt opp | Faktagrunnlag med eget tidspunkt |
| `maaltall` | *Hvor mye / hvor mange?* | netto omsetning, MRR, antall ordre | Mål / metrikk |
| `dimensjon` | *Hvordan* grupperer og filtrerer vi? | fakturadato, kundesegment, region | Dimensjon (kategori- eller tidsdimensjon) |
| `klassifisering` | *Hvilke* forekomster hører til en gruppe? | aktiv kunde, tapt kunde, ny kunde | Filter, segment eller boolsk dimensjon |

## Velge riktig type

- **Kan du telle det, og har det en identitet?** → `entitet`. "Hvilken kunde?" gir mening.
- **Skjedde det på et bestemt tidspunkt, og er det tidspunktet poenget?** → `hendelse`.
  En ordre er både en ting og en hendelse. Velg `entitet` når den har livsløp og egenskaper,
  og `hendelse` når den bare er en registrering av at noe skjedde.
- **Er svaret et tall som summeres, telles eller beregnes?** → `maaltall`.
- **Brukes det til å dele opp eller filtrere et tall?** → `dimensjon`.
- **Er det en regel som avgjør om en forekomst er "inne" eller "ute"?** → `klassifisering`.
  Ofte et adjektiv foran en entitet: *aktiv* kunde, *forfalt* faktura.

## Typespesifikke felt

### entitet

| Felt | Betydning |
|---|---|
| `identifiseres_ved` | Det virksomheten bruker for å skille forekomstene, med forretningsord: "kundenummer", "ordrenummer og linjenummer". |

### hendelse

| Felt | Betydning |
|---|---|
| `tidspunkt` | id til en `dimensjon` med `dimensjonstype: tid` som sier når hendelsen skjedde. |
| `identifiseres_ved` | Valgfri. |

### maaltall

| Felt | Verdier | Betydning |
|---|---|---|
| `aggregering` | `sum`, `antall`, `antall_unike`, `snitt`, `min`, `maks`, `ratio`, `formel` | Hvordan grunnverdiene slås sammen. `ratio` og `formel` betyr at måltallet beregnes fra andre måltall. Skriv formelen i **Beregning**. |
| `enhet` | `NOK`, `antall`, `prosent`, `dager` … | Hva tallet måles i. |
| `grain` | id til en `entitet` eller `hendelse` | Det laveste nivået måltallet gir mening på. Én grunnverdi per forekomst. |
| `tidsdimensjon` | id til en `dimensjon` med `dimensjonstype: tid` | Hvilken dato som plasserer verdien i tid. Avgjørende: omsetning per ordredato og per fakturadato er ulike tall. |
| `additivitet` | `additiv`, `semi_additiv`, `ikke_additiv` | Om tallet kan summeres. Se under. |

**Additivitet** er det enkeltpunktet som oftest gir feil tall i rapporter:

- `additiv`: kan summeres over alle dimensjoner, også tid. *Omsetning for et kvartal = summen av tre måneder.*
- `semi_additiv`: kan summeres over alle dimensjoner **unntatt tid**. Beholdninger og
  øyeblikksbilder. *MRR for et kvartal er MRR ved kvartalets slutt, ikke summen av tre måneder.*
  Skriv i **Beregning** hvilken verdi som gjelder over tid (siste, første, snitt).
- `ikke_additiv`: kan ikke summeres i det hele tatt. Andeler, snitt, antall unike.
  *Snittlig ordreverdi for to regioner er ikke summen av regionenes snitt.*

### dimensjon

| Felt | Verdier | Betydning |
|---|---|---|
| `dimensjonstype` | `kategori`, `tid`, `boolsk`, `numerisk`, `tekst` | Tidsdimensjoner kan brukes som `tidsdimensjon` og `tidspunkt`. |

Bruk relasjonen `beskriver` for å si hvilken entitet eller hendelse dimensjonen tilhører.
For `kategori`, list verdiene i seksjonen **Gyldige verdier**.

### klassifisering

Ingen egne felt, men relasjonen `er_en` er påkrevd (hvilket begrep som deles inn), og regelen
skal stå i **Forretningsregler**.

## Fra katalog til semantisk modell

En generator kan bygge en semantisk modell slik:

1. **Entiteter** blir tabeller/objekter med nøkkel fra `identifiseres_ved` og koblinger fra `tilhorer` og `del_av`.
2. **Dimensjoner** med `beskriver` blir attributter på entiteten de beskriver.
3. **Klassifiseringer** blir boolske dimensjoner eller navngitte filtre på entiteten i `er_en`.
4. **Måltall** blir mål på `grain`-entiteten, plassert i tid av `tidsdimensjon`, aggregert med
   `aggregering`. Måltall med `formel`/`ratio` bygges av måltallene i `avledet_av`.
5. **Systemrepresentasjon** og avvikene der sier hvilke kildedata som skal brukes og hvilke filtre
   som trengs for at tallene skal stemme med forretningsdefinisjonen.

Derfor er det viktig at `grain`, `tidsdimensjon`, `additivitet` og formelen er riktige. De styrer
direkte hvordan tallene beregnes.
