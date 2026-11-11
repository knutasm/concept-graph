# Begrepstyper

Alle begreper har én `type`. Typen bestemmer hvilke felt og seksjoner som er påkrevd.

| Type | Spørsmål den svarer på | Eksempler |
|---|---|---|
| `entitet` | *Hva* holder vi rede på? | vare, kunde, ordre, lager |
| `hendelse` | *Hva skjer* på et tidspunkt? | varemottak, leveranse |
| `maaltall` | *Hvor mye / hvor mange?* | omsetning, dekningsgrad, lagerbeholdning |
| `dimensjon` | *Hvordan* grupperer og filtrerer vi? | fakturadato, varegruppe, kundesegment |
| `klassifisering` | *Hvilke* forekomster hører til en gruppe? | aktiv kunde, restordre, virkedag |

## Velge riktig type

- **Kan du telle det, og har det en identitet?** → `entitet`. "Hvilken kunde?" gir mening.
- **Skjedde det på et bestemt tidspunkt, og er det tidspunktet poenget?** → `hendelse`.
  En ordre er både en ting og en hendelse. Velg `entitet` når den har livsløp og egenskaper,
  og `hendelse` når den bare er en registrering av at noe skjedde.
- **Er svaret et tall som summeres, telles eller beregnes?** → `maaltall`.
- **Brukes det til å dele opp eller filtrere et tall?** → `dimensjon`.
- **Er det en regel som avgjør om en forekomst er "inne" eller "ute"?** → `klassifisering`.
  Ofte et adjektiv foran en entitet: *aktiv* kunde, *restnotert* ordrelinje.

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

| Felt | Verdier | Spørsmål |
|---|---|---|
| `aggregering` | `sum`, `antall`, `antall_unike`, `snitt`, `min`, `maks`, `ratio`, `formel` | Legges tallene sammen, telles de, eller regnes tallet ut fra andre måltall? Ved `ratio` og `formel` står regnestykket i **Beregning**. |
| `enhet` | `NOK`, `antall`, `prosent`, `dager` … | Hva måles tallet i? |
| `granularitet` | id til en `entitet` eller `hendelse` | Hva er én forekomst? *Omsetning: én verdi per fakturalinje.* |
| `tidsdimensjon` | id til en `dimensjon` med `dimensjonstype: tid` | Hvilken dato teller? *Omsetning per ordredato og per fakturadato er ulike tall.* |
| `additivitet` | `additiv`, `semi_additiv`, `ikke_additiv` | Kan tallene legges sammen? Se under. |

**Additivitet** svarer på om tallet for et kvartal er summen av tre måneder:

- `additiv`: ja. *Omsetningen for et kvartal er summen av tre måneder.*
- `semi_additiv`: ikke over tid. Beholdninger. *Lagerbeholdningen for et kvartal er beholdningen
  ved kvartalets slutt.* Skriv i **Beregning** hvilken verdi som gjelder (siste, første, snitt).
- `ikke_additiv`: nei. Andeler, snitt, antall unike. *Dekningsgraden for to varegrupper er ikke
  snittet av de to dekningsgradene.* Pek på delene tallet regnes ut fra med `avledet_av`.

Svar ut fra hva tallet betyr, ikke ut fra hvordan et system lagrer det. Lagrer et system tallet
slik at det ikke kan legges sammen på samme måte, er det et avvik under **Systemrepresentasjon**.

### dimensjon

| Felt | Verdier | Betydning |
|---|---|---|
| `dimensjonstype` | `kategori`, `tid`, `boolsk`, `numerisk`, `tekst` | Tidsdimensjoner kan brukes som `tidsdimensjon` og `tidspunkt`. |

Bruk relasjonen `beskriver` for å si hvilken entitet eller hendelse dimensjonen tilhører.
For `kategori`, list verdiene i seksjonen **Gyldige verdier**.

### klassifisering

Ingen egne felt, men relasjonen `er_en` er påkrevd (hvilket begrep som deles inn), og regelen
skal stå i **Forretningsregler**.
