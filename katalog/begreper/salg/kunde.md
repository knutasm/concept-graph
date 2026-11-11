---
id: kunde
navn: Kunde
type: entitet
domene: salg
kortdefinisjon: En virksomhet eller person som har kjøpt varer av oss på egen kundekonto.
synonymer: [kundekonto, customer]
status: godkjent
eier: Salgsavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-11
systemer: [erp, crm]
kilde: erp
forveksles_med: ["[[prosjekt]]", "[[aktiv_kunde]]"]
identifiseres_ved: kundenummer
---
# Kunde

## Definisjon

En virksomhet eller person som har minst én bekreftet [[ordre]] hos oss på egen kundekonto. De fleste
kundene er rørleggerbedrifter og entreprenører. Hvilken type kunde det er, beskrives av [[kundesegment]].

## Forretningsregler

- Én virksomhet er én kunde per organisasjonsnummer, også når den kjøper til mange [[prosjekt]]er.
- Ekskluderer: anonymt kontantsalg uten kundekonto.
- Ekskluderer: prospekter som bare har fått tilbud.
- Man forblir kunde selv om det er lenge siden forrige kjøp. Om kunden er i aktivitet, beskrives av [[aktiv_kunde]].

## Eksempler

- En rørleggerbedrift kjøper til fem byggeprosjekter. Er det fem kunder? **Nei**, én kunde med fem prosjekter.
- En privatperson betaler kontant på et utsalgssted. Er hun kunde? **Nei**, hun har ingen kundekonto.

## Avgrensning mot andre begreper

- [[prosjekt]]: et byggeprosjekt kunden kjøper til. Ikke en egen kunde, selv om prosjektet har egne priser.
- [[aktiv_kunde]]: delmengden som har kjøpt nylig.

## Systemrepresentasjon

### erp

- **Representasjon:** Kunderegisteret.
- **Identifikasjon:** Kundenummer.
- **Avvik fra forretningsdefinisjon:** Kontantsalg føres på én samlekunde, som ikke er en kunde og må filtreres bort. Store byggeprosjekter er ofte opprettet som egne kundenumre. De må slås sammen til kunden via organisasjonsnummeret.

### crm

- **Representasjon:** Kontoer av typen kunde.
- **Identifikasjon:** CRM-ets konto-id, med kundenummer fra ERP som eget felt.
- **Avvik fra forretningsdefinisjon:** Kontotypen settes manuelt og er ofte utdatert. Bruk ikke CRM til å telle kunder.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Salgsdirektør |
