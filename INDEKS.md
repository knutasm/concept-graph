# Indeks

<!-- GENERERT av scripts/valider.py. Ikke rediger for hånd. -->

14 begreper i 5 domener, 4 systemer. Les [README.md](README.md) for hvordan katalogen er bygd opp.

## Domener

| Domene | Navn | Eier | Antall | Beskrivelse |
|---|---|---|---|---|
| [abonnement](#abonnement) | Abonnement | Kundeservice | 2 | Løpende avtaler som faktureres periodisk, og måltall for gjentakende inntekt. |
| [felles](#felles) | Felles | Dataplattformteamet | 1 | Tverrgående begreper som brukes av flere domener, f.eks. kalenderbegreper. |
| [kunde](#kunde) | Kunde | Salgsavdelingen | 2 | Hvem virksomheten har et kundeforhold til, og hvordan kundeforholdet klassifiseres. |
| [okonomi](#okonomi) | Økonomi | Økonomiavdelingen | 6 | Fakturering, inntekter og fradrag slik de rapporteres økonomisk. |
| [salg](#salg) | Salg | Salgsavdelingen | 3 | Bestillinger fra kunder og innholdet i dem. |

## abonnement

**Abonnement**: Løpende avtaler som faktureres periodisk, og måltall for gjentakende inntekt. ([domenebeskrivelse](begreper/abonnement/_domene.md))

| id | navn | type | status | synonymer | kortdefinisjon |
|---|---|---|---|---|---|
| [abonnement](begreper/abonnement/abonnement.md) | Abonnement | entitet | godkjent | løpende avtale, subscription | En løpende avtale med en kunde om levering mot en fast pris per periode, til den sies opp. |
| [mrr](begreper/abonnement/mrr.md) | Månedlig gjentakende inntekt (MRR) | maaltall | godkjent | MRR, monthly recurring revenue, månedlig abonnementsinntekt | Samlet abonnementspris for alle aktive abonnementer, omregnet til én måned. |

## felles

**Felles**: Tverrgående begreper som brukes av flere domener, f.eks. kalenderbegreper. ([domenebeskrivelse](begreper/felles/_domene.md))

| id | navn | type | status | synonymer | kortdefinisjon |
|---|---|---|---|---|---|
| [maaned](begreper/felles/maaned.md) | Måned | dimensjon | godkjent | kalendermåned, month | Kalendermåned, fra den første til den siste dagen i måneden. |

## kunde

**Kunde**: Hvem virksomheten har et kundeforhold til, og hvordan kundeforholdet klassifiseres. ([domenebeskrivelse](begreper/kunde/_domene.md))

| id | navn | type | status | synonymer | kortdefinisjon |
|---|---|---|---|---|---|
| [aktiv_kunde](begreper/kunde/aktiv_kunde.md) | Aktiv kunde | klassifisering | godkjent | active customer, nåværende kunde | En kunde med minst én bekreftet ordre de siste 12 månedene. |
| [kunde](begreper/kunde/kunde.md) | Kunde | entitet | godkjent | klient, customer | En person eller virksomhet som har minst én bekreftet ordre hos oss. |

## okonomi

**Økonomi**: Fakturering, inntekter og fradrag slik de rapporteres økonomisk. ([domenebeskrivelse](begreper/okonomi/_domene.md))

| id | navn | type | status | synonymer | kortdefinisjon |
|---|---|---|---|---|---|
| [brutto_omsetning](begreper/okonomi/brutto_omsetning.md) | Brutto omsetning | maaltall | godkjent | bruttosalg, gross revenue | Fakturert salg eksklusiv mva, før returer og rabatter. |
| [faktura](begreper/okonomi/faktura.md) | Faktura | entitet | godkjent | invoice, kreditnota | Et krav om betaling sendt til en kunde for leverte varer eller tjenester, inkludert kreditnotaer. |
| [fakturadato](begreper/okonomi/fakturadato.md) | Fakturadato | dimensjon | godkjent | invoice date | Datoen fakturaen er utstedt. Avgjør hvilken periode omsetningen hører til. |
| [netto_omsetning](begreper/okonomi/netto_omsetning.md) | Netto omsetning | maaltall | godkjent | nettosalg, omsetning, net revenue | Brutto omsetning fratrukket returer og rabatter, eksklusiv mva. |
| [rabatt](begreper/okonomi/rabatt.md) | Rabatt | maaltall | godkjent | prisavslag, bonus, discount | Alle prisavslag gitt til kunden, både på fakturaen og som kreditering i etterkant. |
| [returer](begreper/okonomi/returer.md) | Returer | maaltall | godkjent | kreditert beløp, returns | Verdien av varer kunden har sendt tilbake og fått kreditert, eksklusiv mva. |

## salg

**Salg**: Bestillinger fra kunder og innholdet i dem. ([domenebeskrivelse](begreper/salg/_domene.md))

| id | navn | type | status | synonymer | kortdefinisjon |
|---|---|---|---|---|---|
| [ordre](begreper/salg/ordre.md) | Ordre | entitet | godkjent | salgsordre, bestilling, order | En bekreftet bestilling fra en kunde om levering av varer eller tjenester. |
| [ordredato](begreper/salg/ordredato.md) | Ordredato | dimensjon | godkjent | bestillingsdato, order date | Datoen kunden bekreftet ordren. |
| [ordrelinje](begreper/salg/ordrelinje.md) | Ordrelinje | entitet | godkjent | linje, order line | Én vare eller tjeneste på en ordre, med antall og avtalt pris. |

## Systemer

| id | navn | kategori | antall begreper | beskrivelse |
|---|---|---|---|---|
| [abonnementssystem](systemer/abonnementssystem.md) | Abonnementssystemet | abonnement | 1 | Håndterer abonnementer, fornyelser, oppsigelser og periodisk fakturagrunnlag. |
| [crm](systemer/crm.md) | CRM-systemet | crm | 1 | Brukes av salg til å følge opp leads, prospekter og kundekontoer. |
| [datavarehus](systemer/datavarehus.md) | Datavarehuset | datavarehus | 3 | Samler data fra kildesystemene og beregner analytiske modeller og måltall. |
| [erp](systemer/erp.md) | ERP-systemet | erp | 10 | Kjernesystem for ordre, fakturering, regnskap og lager. |
