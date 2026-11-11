---
id: ordredato
navn: Ordredato
type: dimensjon
domene: salg
kortdefinisjon: Datoen ordren ble bekreftet.
synonymer: [bestillingsdato, order date]
status: godkjent
eier: Salgsavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-10
systemer: ["[[erp]]"]
beskriver: ["[[ordre]]"]
forveksles_med: ["[[fakturadato]]", "[[leveringsdato]]"]
dimensjonstype: tid
---
# Ordredato

## Definisjon

Datoen [[ordre]]n ble bekreftet. Ikke datoen tilbudet ble gitt, og ikke datoen kunden ønsker levering.

## Avgrensning mot andre begreper

- [[leveringsdato]]: når varene ble levert. For byggeprosjekter kan det gå måneder fra ordre til levering.
- [[fakturadato]]: når vi krevde betaling. Omsetning følger fakturadato.

## Systemrepresentasjon

### erp

- **Representasjon:** Bekreftelsesdatoen på ordren.
- **Avvik fra forretningsdefinisjon:** Ingen kjente.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Salgsdirektør |
