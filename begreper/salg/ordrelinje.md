---
id: ordrelinje
navn: Ordrelinje
type: entitet
domene: salg
kortdefinisjon: Én vare eller tjeneste på en ordre, med antall og avtalt pris.
synonymer: [linje, order line]
status: godkjent
eier: Salgsavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-10
systemer: [erp]
relasjoner:
  del_av: [ordre]
identifiseres_ved: ordrenummer og linjenummer
---
# Ordrelinje

## Definisjon

Én vare eller tjeneste på en [[ordre]], med antall, listepris og avtalt pris.

## Systemrepresentasjon

### erp

- **Representasjon:** Ordrelinjene som hører til ordrehodet.
- **Identifikasjon:** Ordrenummer + linjenummer.
- **Avvik fra forretningsdefinisjon:** Fraktgebyr og tekstlinjer ligger også som ordrelinjer. Tekstlinjer har ingen pris og er ikke ordrelinjer i forretningsforstand.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Salgsledelsen |
