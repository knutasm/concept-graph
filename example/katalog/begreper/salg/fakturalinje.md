---
id: fakturalinje
navn: Fakturalinje
type: entitet
domene: salg
kortdefinisjon: Én vare på en faktura, med fakturert antall, beløp og varekost.
synonymer: [invoice line]
status: godkjent
eier: Økonomiavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-11
systemer: ["[[erp]]"]
kilde: "[[erp]]"
del_av: ["[[faktura]]"]
tilhorer: ["[[vare]]"]
identifiseres_ved: fakturanummer og linjenummer
---
# Fakturalinje

## Definisjon

Én [[vare]] på en [[faktura]], med fakturert antall og beløp. Det laveste nivået [[omsetning]],
[[varekost]] og [[dekningsbidrag]] beregnes på, og det som gjør at de kan brytes ned på vare og
[[varegruppe]].

## Forretningsregler

- Ekskluderer: linjer for frakt, gebyrer og pant. Det er ikke varer.

## Systemrepresentasjon

### erp

- **Representasjon:** Fakturalinjene på fakturaen, med referanse til ordrelinjen.
- **Identifikasjon:** Fakturanummer + linjenummer.
- **Avvik fra forretningsdefinisjon:** Frakt, gebyrer og pant ligger også som fakturalinjer og må filtreres bort.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Økonomisjef |
