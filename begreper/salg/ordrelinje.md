---
id: ordrelinje
navn: Ordrelinje
type: entitet
domene: salg
kortdefinisjon: Én vare på en ordre, med bestilt antall og avtalt pris.
synonymer: [linje, order line]
status: godkjent
eier: Salgsavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-10
systemer: [erp]
del_av: ["[[ordre]]"]
tilhorer: ["[[vare]]"]
identifiseres_ved: ordrenummer og linjenummer
---
# Ordrelinje

## Definisjon

Én [[vare]] på en [[ordre]], med bestilt antall i salgsenhet og avtalt pris.

## Forretningsregler

- Ekskluderer: linjer for frakt, gebyrer og pant. Det er ikke varer (se [[vare]]).
- Antall regnes om til lagerenhet (se [[maaleenhet]]) når det skal sammenlignes med beholdning og leveranser.

## Systemrepresentasjon

### erp

- **Representasjon:** Ordrelinjene på ordren.
- **Identifikasjon:** Ordrenummer + linjenummer.
- **Avvik fra forretningsdefinisjon:** Frakt, gebyrer og rene tekstlinjer ligger også som ordrelinjer og må filtreres bort.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Salgsdirektør |
