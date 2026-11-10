---
id: kundesegment
navn: Kundesegment
type: dimensjon
domene: salg
kortdefinisjon: Hva slags virksomhet kunden er, f.eks. rørleggerbedrift eller entreprenør.
synonymer: [segment, kundetype, customer segment]
status: godkjent
eier: Salgsavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-10
systemer: [crm, erp]
beskriver: ["[[kunde]]"]
dimensjonstype: kategori
---
# Kundesegment

## Definisjon

Hva slags virksomhet [[kunde]]n er. Hver kunde har ett segment, ut fra kundens hovedvirksomhet.

## Gyldige verdier

- `haandverker`: rørleggerbedrifter og andre håndverkere som kjøper til egne oppdrag
- `entreprenor`: total- og hovedentreprenører som kjøper til større byggeprosjekter
- `offentlig`: kommuner, fylker og offentlige byggherrer
- `privat`: privatpersoner med kundekonto

## Avgrensning mot andre begreper

- Prisgruppe: hvilke priser kunden har. Ikke det samme som segment, selv om de ofte henger sammen.

## Systemrepresentasjon

### crm

- **Representasjon:** Segmentfeltet på kundekontoen. Dette er kilden.
- **Avvik fra forretningsdefinisjon:** Settes manuelt av selger, og mangler for rundt 10 % av kundene.

### erp

- **Representasjon:** Har ikke segment, bare prisgruppe.
- **Avvik fra forretningsdefinisjon:** Prisgruppe brukes ofte som erstatning for segment, men det er et annet begrep.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Salgsdirektør |
