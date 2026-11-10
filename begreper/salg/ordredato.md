---
id: ordredato
navn: Ordredato
type: dimensjon
domene: salg
kortdefinisjon: Datoen kunden bekreftet ordren.
synonymer: [bestillingsdato, order date]
status: godkjent
eier: Salgsavdelingen
sist_oppdatert: 2026-11-10
systemer: [erp]
relasjoner:
  beskriver: [ordre]
  forveksles_med: [fakturadato]
dimensjonstype: tid
---
# Ordredato

## Definisjon

Datoen [[kunde]]n bekreftet [[ordre]]n. Ikke datoen tilbudet ble sendt, og ikke leveringsdatoen.

## Avgrensning mot andre begreper

- [[fakturadato]]: når vi krevde betaling. Kan ligge uker etter ordredatoen.

## Systemrepresentasjon

### erp

- **Representasjon:** Bekreftelsesdatoen på ordrehodet.
- **Avvik fra forretningsdefinisjon:** Ordrer importert før 2023 har opprettelsesdato i stedet for bekreftelsesdato.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Salgsledelsen |
