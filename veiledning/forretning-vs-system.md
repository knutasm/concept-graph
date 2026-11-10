# Forretningsbegrep eller systembegrep?

Den vanligste feilen i en begrepskatalog er å beskrive hvordan et begrep **ser ut i et system**
i stedet for hva det **betyr for virksomheten**. Mange av oss jobber i ett system hver dag, og da
blir systemets ord og regler fort "sannheten". Men systemer byttes ut, og flere systemer har ofte
hver sin versjon av samme begrep.

Hver oppføring har derfor to tydelig adskilte deler:

| Del | Seksjoner | Innhold |
|---|---|---|
| **Forretningsbegrepet** | `kortdefinisjon`, Definisjon, Forretningsregler, Beregning, Gyldige verdier | Hva begrepet betyr, uavhengig av system |
| **Systemrepresentasjonen** | Systemrepresentasjon (én `###` per system) | Hvor og hvordan begrepet finnes i hvert system, og hvordan systemet avviker |

## Testen

> **Ville teksten fortsatt vært sann om alle systemene ble byttet ut i morgen?**

Hvis nei, hører teksten hjemme under Systemrepresentasjon.

## Faresignaler

Hvis du skriver noe av dette over Systemrepresentasjon, beskriver du sannsynligvis systemet:

- Navn på systemer, moduler, skjermbilder eller rapporter
- Tabeller, felt, kolonner, statuskoder, flagg, tekniske id-er (`KUNDE_STATUS = 3`)
- "En rad i …", "alt som ligger i …", "det som vises i …"
- "Det systemet kaller …"
- Regler som bare finnes fordi systemet fungerer slik ("unntatt de med kode 99")

Valideringen advarer når den finner systemnavn eller teknisk utseende ord i forretningsdelen.

## Eksempler

### Kunde

| ❌ Systemformulert | ✅ Forretningsformulert |
|---|---|
| "En kunde er en debitor i ERP-et." | "En person eller virksomhet som har minst én bekreftet ordre hos oss." |

ERP-et oppretter debitorer allerede ved tilbud, så "alle debitorer" gir et annet (og feil) tall.
Dette er nyttig kunnskap, men den hører hjemme under `### erp` som et **avvik**:

```markdown
### erp
- **Representasjon:** Kunderegisteret (debitorer) …
- **Avvik fra forretningsdefinisjon:** Debitor opprettes ved tilbud. Registeret inneholder
  derfor prospekter. Filtrer på at det finnes en bekreftet ordre.
```

### Aktiv kunde

| ❌ Systemformulert | ✅ Forretningsformulert |
|---|---|
| "Kunder der aktiv-flagget er satt." | "En kunde med minst én bekreftet ordre de siste 12 månedene." |

Hvem setter flagget, og etter hvilken regel? Det er regelen som er begrepet. Flagget er bare én
implementasjon av den, og kanskje en utdatert en.

### Ordre

| ❌ Systemformulert | ✅ Forretningsformulert |
|---|---|
| "Ordrehoder med status 20–50." | "En bestilling fra en kunde som vi har bekreftet at vi skal levere." |

Statuskodene er nyttige for den som skal hente dataene, så skriv dem under `### erp`.

## Når systemet ER definisjonen

Noen ganger har virksomheten ingen definisjon utover det systemet gjør. Da:

1. Formuler det systemet gjør som en forretningsregel, med forretningsord.
2. Sett `status: utkast` og skriv i **Åpne spørsmål** at definisjonen må bekreftes av eier.
3. Beskriv den tekniske implementasjonen under Systemrepresentasjon som vanlig.

## Når systemer er uenige

Hvis to systemer har ulik oppfatning av samme begrep, er det **ett** forretningsbegrep med
**to** systemrepresentasjoner, og minst én av dem har avvik. Lag ikke to begreper ("ERP-kunde"
og "CRM-kunde"). Unntaket er når virksomheten faktisk trenger begge begrepene, med hver sin
forretningsdefinisjon. Da lager du to begreper og knytter dem med `forveksles_med`.

## Hvorfor dette er viktig for analyse

Katalogen brukes som grunnlag for å bygge semantiske modeller og måltall automatisk.
Forretningsdelen sier **hva** som skal beregnes. Systemrepresentasjonen, og særlig avvikene, sier
**hvordan** man kommer dit fra kildedataene. Blandes de, arver måltallene systemfeilene, og
definisjonen må skrives om når systemet byttes.
