---
id: fakturadato
navn: Fakturadato
type: dimensjon
domene: okonomi
kortdefinisjon: Datoen fakturaen er utstedt. Avgjør hvilken periode omsetningen hører til.
synonymer: [invoice date]
status: godkjent
eier: Økonomiavdelingen
sist_oppdatert: 2026-11-10
systemer: [erp]
relasjoner:
  beskriver: [faktura]
  forveksles_med: [ordredato]
dimensjonstype: tid
---
# Fakturadato

## Definisjon

Datoen [[faktura]]en er utstedt. Avgjør hvilken regnskapsperiode omsetningen hører til.

## Avgrensning mot andre begreper

- [[ordredato]]: når kunden bestilte. Salgsrapporter per ordredato og omsetning per fakturadato vil ikke stemme for samme måned.

## Systemrepresentasjon

### erp

- **Representasjon:** Fakturadato på fakturahodet.
- **Avvik fra forretningsdefinisjon:** Ingen kjente.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Økonomisjef |
