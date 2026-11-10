---
id: kunde
navn: Kunde
type: entitet
domene: kunde
kortdefinisjon: En person eller virksomhet som har minst én bekreftet ordre hos oss.
synonymer: [klient, customer]
status: godkjent
eier: Salgsavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-10
systemer: [erp, crm]
relasjoner:
  forveksles_med: [aktiv_kunde]
identifiseres_ved: kundenummer
---
# Kunde

## Definisjon

En person eller virksomhet som har minst én bekreftet [[ordre]] hos oss. Man forblir kunde selv om
det er lenge siden forrige kjøp. Om kunden er i aktivitet, beskrives av [[aktiv_kunde]].

## Forretningsregler

- Inkluderer: privatpersoner og virksomheter, også de som bare har kjøpt én gang.
- Ekskluderer: prospekter og leads som har fått tilbud, men aldri bekreftet en ordre.
- Ekskluderer: interne kjøp mellom egne selskaper.
- En virksomhet med flere avdelinger er én kunde hvis den har ett organisasjonsnummer.

## Eksempler

- En bedrift fikk tilbud i fjor, men takket nei. Er den en kunde? **Nei**, den har ingen bekreftet ordre.
- En privatperson kjøpte én gang for fem år siden. Er hun en kunde? **Ja**, men ikke en [[aktiv_kunde]].

## Avgrensning mot andre begreper

- [[aktiv_kunde]]: en delmengde av kundene. "Antall kunder" og "antall aktive kunder" er ulike tall.

## Systemrepresentasjon

### erp

- **Representasjon:** Kunderegisteret (debitorer). En kunde er en debitor med minst én ordre med status bekreftet eller senere.
- **Identifikasjon:** Kundenummer.
- **Avvik fra forretningsdefinisjon:** ERP oppretter en debitor allerede når et tilbud sendes. Kunderegisteret inneholder derfor prospekter som ikke er kunder. Filtrer på at det finnes en bekreftet ordre.

### crm

- **Representasjon:** Kontoer med kontotype "Kunde".
- **Identifikasjon:** CRM-ets konto-id. Kundenummer fra ERP ligger som et eget felt på kontoen.
- **Avvik fra forretningsdefinisjon:** Kontotypen settes manuelt av selger og er ofte utdatert. Bruk ikke CRM til å telle kunder.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Salgsledelsen |
