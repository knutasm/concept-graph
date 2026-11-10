# Indeks

<!-- GENERERT av scripts/valider.py. Ikke rediger for hånd. -->

33 begreper i 4 domener, 5 systemer. Les [README.md](README.md) for hvordan katalogen er bygd opp.

## Domener

| Domene | Navn | Eier | Antall | Beskrivelse |
|---|---|---|---|---|
| [innkjop](#innkjop) | Innkjøp | Innkjøpsavdelingen | 5 | Innkjøp av varer fra leverandører, og oppfølging av leverandørene. |
| [kjerne](#kjerne) | Kjerne | Dataplattformteamet | 5 | Begreper som brukes av flere domener og ikke har én naturlig faglig eier, f.eks. vare og kalender. |
| [logistikk](#logistikk) | Logistikk | Logistikkavdelingen | 7 | Lagring og levering av varer: lagre, beholdning, utleveringer og leveringsevne. |
| [salg](#salg) | Salg | Salgsavdelingen | 16 | Salg til håndverkere og byggeprosjekter: kunder, ordre, fakturering og lønnsomhet. |

## innkjop

**Innkjøp**: Innkjøp av varer fra leverandører, og oppfølging av leverandørene. ([domenebeskrivelse](begreper/innkjop/_domene.md))

| id | navn | type | status | synonymer | kortdefinisjon |
|---|---|---|---|---|---|
| [innkjopsordre](begreper/innkjop/innkjopsordre.md) | Innkjøpsordre | entitet | godkjent | bestilling til leverandør, purchase order, PO | En bestilling av varer som vi har sendt til en leverandør. |
| [leverandor](begreper/innkjop/leverandor.md) | Leverandør | entitet | godkjent | vareleverandør, supplier | En produsent eller grossist som vi kjøper varer fra for videresalg. |
| [leveringspresisjon_leverandor](begreper/innkjop/leveringspresisjon_leverandor.md) | Leveringspresisjon leverandør | maaltall | godkjent | leverandørpresisjon, OTD leverandør, supplier on-time delivery | Andelen varemottak som kom senest på leverandørens bekreftede leveringsdato. |
| [mottaksdato](begreper/innkjop/mottaksdato.md) | Mottaksdato | dimensjon | godkjent | mottatt dato, receipt date | Datoen varene i et varemottak ble mottatt og kontrollert. |
| [varemottak](begreper/innkjop/varemottak.md) | Varemottak | hendelse | godkjent | mottak, inngående levering, goods receipt | At varer fra en innkjøpsordre er mottatt og kontrollert på et av våre lagre eller hos kunden. |

## kjerne

**Kjerne**: Begreper som brukes av flere domener og ikke har én naturlig faglig eier, f.eks. vare og kalender. ([domenebeskrivelse](begreper/kjerne/_domene.md))

| id | navn | type | status | synonymer | kortdefinisjon |
|---|---|---|---|---|---|
| [kalenderdag](begreper/kjerne/kalenderdag.md) | Kalenderdag | dimensjon | godkjent | dato, kalender, date | En dag i den felles kalenderen, med uke, måned og regnskapsår. |
| [maaleenhet](begreper/kjerne/maaleenhet.md) | Måleenhet | dimensjon | godkjent | enhet, unit of measure | Enheten en mengde av en vare uttrykkes i, f.eks. stykk, meter eller pakke. |
| [vare](begreper/kjerne/vare.md) | Vare | entitet | godkjent | artikkel, produkt, item | En fysisk artikkel i sortimentet vårt som vi kjøper inn, lagerfører eller selger. |
| [varegruppe](begreper/kjerne/varegruppe.md) | Varegruppe | dimensjon | godkjent | produktgruppe, kategori, product group | Hovedinndelingen av sortimentet som brukes i innkjøp, lager og salg. |
| [virkedag](begreper/kjerne/virkedag.md) | Virkedag | klassifisering | godkjent | arbeidsdag, business day | En kalenderdag fra mandag til fredag som ikke er en offentlig helligdag. |

## logistikk

**Logistikk**: Lagring og levering av varer: lagre, beholdning, utleveringer og leveringsevne. ([domenebeskrivelse](begreper/logistikk/_domene.md))

| id | navn | type | status | synonymer | kortdefinisjon |
|---|---|---|---|---|---|
| [beholdningsdato](begreper/logistikk/beholdningsdato.md) | Beholdningsdato | dimensjon | godkjent | lagerdato, snapshot date | Dagen en lagerbeholdning gjelder for, målt ved dagens slutt. |
| [lager](begreper/logistikk/lager.md) | Lager | entitet | godkjent | lagersted, utsalgssted, filial, warehouse | Et fysisk sted der vi oppbevarer varer for salg, dvs. sentrallageret eller et utsalgssted. |
| [lagerbeholdning](begreper/logistikk/lagerbeholdning.md) | Lagerbeholdning | maaltall | godkjent | lagerverdi, varelager, beholdning, inventory | Verdien av varene vi har på lager ved slutten av en dag, til gjennomsnittlig innkjøpskost. |
| [leveranse](begreper/logistikk/leveranse.md) | Leveranse | hendelse | godkjent | utlevering, forsendelse, delivery | At varer fra en ordre er overlevert til kunden, enten hentet på utsalgssted eller levert til byggeplass. |
| [leveringsdato](begreper/logistikk/leveringsdato.md) | Leveringsdato | dimensjon | godkjent | utleveringsdato, delivery date | Datoen kunden mottok og kvitterte for en leveranse. |
| [leveringsgrad](begreper/logistikk/leveringsgrad.md) | Leveringsgrad | maaltall | godkjent | leveringsevne, servicegrad, fill rate | Andelen ordrelinjer som ble levert komplett på avtalt dato. |
| [restordre](begreper/logistikk/restordre.md) | Restordre | klassifisering | godkjent | rest, restnotert, backorder | En ordrelinje som ikke kunne leveres som avtalt fordi varen ikke var på lager. |

## salg

**Salg**: Salg til håndverkere og byggeprosjekter: kunder, ordre, fakturering og lønnsomhet. ([domenebeskrivelse](begreper/salg/_domene.md))

| id | navn | type | status | synonymer | kortdefinisjon |
|---|---|---|---|---|---|
| [aktiv_kunde](begreper/salg/aktiv_kunde.md) | Aktiv kunde | klassifisering | godkjent | active customer | En kunde med minst én bekreftet ordre de siste 12 månedene. |
| [dekningsbidrag](begreper/salg/dekningsbidrag.md) | Dekningsbidrag | maaltall | godkjent | DB, bruttofortjeneste, gross margin | Omsetning minus varekost. Hva salget bidrar med til å dekke kostnader og gi overskudd. |
| [dekningsgrad](begreper/salg/dekningsgrad.md) | Dekningsgrad | maaltall | godkjent | DG, bruttomargin, margin, gross margin percent | Dekningsbidrag i prosent av omsetningen. |
| [faktura](begreper/salg/faktura.md) | Faktura | entitet | godkjent | invoice, kreditnota | Et krav om betaling sendt til en kunde for leverte varer, inkludert kreditnotaer. |
| [fakturadato](begreper/salg/fakturadato.md) | Fakturadato | dimensjon | godkjent | invoice date | Datoen fakturaen er utstedt. Avgjør hvilken periode omsetningen hører til. |
| [fakturalinje](begreper/salg/fakturalinje.md) | Fakturalinje | entitet | godkjent | invoice line | Én vare på en faktura, med fakturert antall, beløp og varekost. |
| [kunde](begreper/salg/kunde.md) | Kunde | entitet | godkjent | kundekonto, customer | En virksomhet eller person som har kjøpt varer av oss på egen kundekonto. |
| [kundesegment](begreper/salg/kundesegment.md) | Kundesegment | dimensjon | godkjent | segment, kundetype, customer segment | Hva slags virksomhet kunden er, f.eks. rørleggerbedrift eller entreprenør. |
| [listepris](begreper/salg/listepris.md) | Listepris | dimensjon | utkast | veiledende pris, bruttopris, list price | Den veiledende salgsprisen for en vare før kunde- eller prosjektrabatter, eksklusiv mva. |
| [omsetning](begreper/salg/omsetning.md) | Omsetning | maaltall | godkjent | netto omsetning, salg, salgsinntekt, revenue | Fakturert salg av varer eksklusiv mva, fratrukket kreditnotaer. |
| [ordre](begreper/salg/ordre.md) | Ordre | entitet | godkjent | salgsordre, kundeordre, bestilling, order | En bekreftet bestilling av varer fra en kunde. |
| [ordredato](begreper/salg/ordredato.md) | Ordredato | dimensjon | godkjent | bestillingsdato, order date | Datoen ordren ble bekreftet. |
| [ordrelinje](begreper/salg/ordrelinje.md) | Ordrelinje | entitet | godkjent | linje, order line | Én vare på en ordre, med bestilt antall og avtalt pris. |
| [prosjekt](begreper/salg/prosjekt.md) | Prosjekt | entitet | til_godkjenning | byggeprosjekt, kundeprosjekt, project | Et byggeprosjekt som en kunde kjøper varer til, ofte med egne priser og egen leveringsadresse. |
| [rabatt](begreper/salg/rabatt.md) | Rabatt | maaltall | utkast | kunderabatt, avslag, discount | Hvor mye lavere enn listepris kunden ble fakturert, i kroner eksklusiv mva. |
| [varekost](begreper/salg/varekost.md) | Varekost | maaltall | godkjent | vareforbruk, kost solgte varer, COGS | Hva de solgte varene kostet oss, til gjennomsnittlig innkjøpskost på salgstidspunktet. |

## Systemer

| id | navn | kategori | antall begreper | beskrivelse |
|---|---|---|---|---|
| [crm](systemer/crm.md) | CRM-systemet | CRM | 3 | Brukes av selgerne til å følge opp kunder, kontaktpersoner og prosjektmuligheter. |
| [datavarehus](systemer/datavarehus.md) | Datavarehuset | datavarehus | 9 | Samler data fra kildesystemene og beregner analytiske modeller og måltall. |
| [erp](systemer/erp.md) | ERP-systemet | ERP | 24 | Kjernesystem for varer, kunder, leverandører, ordre, innkjøp, fakturering og regnskap. |
| [lagerstyringssystem](systemer/lagerstyringssystem.md) | Lagerstyringssystemet | lager | 7 | Styrer varemottak, lagerplasser, plukk og utlevering på sentrallageret og utsalgsstedene. |
| [nettbutikk](systemer/nettbutikk.md) | Nettbutikken | netthandel | 4 | Netthandel for innloggede bedriftskunder, med kundens egne avtalepriser. |
