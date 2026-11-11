---
id: fakturadato
navn: Fakturadato
type: dimensjon
domene: salg
kortdefinisjon: Datoen fakturaen er utstedt. Avgjør hvilken periode omsetningen hører til.
synonymer: [invoice date]
status: godkjent
eier: Økonomiavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-10
systemer: ["[[erp]]"]
beskriver: ["[[faktura]]"]
forveksles_med: ["[[ordredato]]"]
dimensjonstype: tid
---
# Fakturadato

## Definisjon

Datoen [[faktura]]en er utstedt. Avgjør hvilken periode [[omsetning]] og [[dekningsbidrag]] hører til.

## Avgrensning mot andre begreper

- [[ordredato]]: når kunden bestilte. Salg per ordredato og omsetning per fakturadato stemmer ikke for samme måned.

## Systemrepresentasjon

### erp

- **Representasjon:** Fakturadatoen på fakturaen.
- **Avvik fra forretningsdefinisjon:** Ingen kjente.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Økonomisjef |
