---
id: leveringsdato
navn: Leveringsdato
type: dimensjon
domene: logistikk
kortdefinisjon: Datoen kunden mottok og kvitterte for en leveranse.
synonymer: [utleveringsdato, delivery date]
status: godkjent
eier: Logistikkavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-10
systemer: [lagerstyringssystem, erp]
beskriver: ["[[leveranse]]"]
forveksles_med: ["[[ordredato]]"]
dimensjonstype: tid
---
# Leveringsdato

## Definisjon

Datoen [[kunde]]n mottok og kvitterte for en [[leveranse]]. Ikke datoen kunden ønsket levering, og ikke datoen varene ble sendt.

## Systemrepresentasjon

### lagerstyringssystem

- **Representasjon:** Forsendelsesdato.
- **Avvik fra forretningsdefinisjon:** Er datoen varene ble sendt. For kjøring til byggeplass er det vanligvis samme dag, men ikke alltid.

### erp

- **Representasjon:** Kvitteringsdato for direkteleveranser.
- **Avvik fra forretningsdefinisjon:** Registreringsdato, ofte flere dager for sent.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Logistikksjef |
