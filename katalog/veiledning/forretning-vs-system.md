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
| "En kunde er et kundenummer i ERP-et." | "En virksomhet eller person som har kjøpt varer av oss på egen kundekonto." |

I ERP-et er kontantsalg ført på én samlekunde, og store byggeprosjekter er ofte opprettet som egne
kundenumre. "Antall kundenumre" gir derfor et annet (og feil) tall. Dette er nyttig kunnskap, men den
hører hjemme under `### erp` som et **avvik**:

```markdown
### erp
- **Representasjon:** Kunderegisteret …
- **Avvik fra forretningsdefinisjon:** Kontantsalg føres på én samlekunde, som må filtreres bort.
  Store byggeprosjekter er ofte egne kundenumre og må slås sammen til kunden via organisasjonsnummeret.
```

Legg merke til at prosjektet er et **eget begrep** ([prosjekt](../begreper/salg/prosjekt.md)), selv om
systemet ikke har det.

### Restordre

| ❌ Systemformulert | ✅ Forretningsformulert |
|---|---|
| "Ordrelinjer med status «delvis levert»." | "En ordrelinje som ikke kunne leveres som avtalt fordi varen ikke var på lager." |

Statusen omfatter også linjer der en entreprenør selv har bedt om senere levering. Bruker man
statusen som definisjon, ser leveringsevnen dårligere ut enn den er. Regelen er begrepet, og
statusen er en ufullkommen implementasjon av den.

### Omsetning

| ❌ Systemformulert | ✅ Forretningsformulert |
|---|---|
| "Salg slik det vises i nettbutikken." | "Fakturert salg av varer eksklusiv mva, fratrukket kreditnotaer." |

Nettbutikken viser ordreverdi på bestillingstidspunktet. Det er et annet tall, selv om det heter
"salg" i rapporten.

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
