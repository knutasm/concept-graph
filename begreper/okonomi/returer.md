---
id: returer
navn: Returer
type: maaltall
domene: okonomi
kortdefinisjon: Verdien av varer kunden har sendt tilbake og fått kreditert, eksklusiv mva.
synonymer: [kreditert beløp, returns]
status: godkjent
eier: Økonomiavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-10
systemer: [erp]
relasjoner:
  forveksles_med: [rabatt]
aggregering: sum
enhet: NOK
grain: faktura
tidsdimensjon: fakturadato
additivitet: additiv
---
# Returer

## Definisjon

Verdien av varer som [[kunde]]n har sendt tilbake og fått kreditert, eksklusiv merverdiavgift.
Rapporteres som et positivt tall og trekkes fra i [[netto_omsetning]].

## Forretningsregler

- Inkluderer: kreditnotaer som krediterer en tidligere faktura fordi varen er returnert.
- Ekskluderer: kreditnotaer for prisavslag i etterkant. De er [[rabatt]].
- Returen regnes i perioden kreditnotaen er utstedt, ikke i perioden den opprinnelige fakturaen ble utstedt.

## Beregning

Sum av beløpet eksklusiv mva på kreditnotaer med årsak retur, med motsatt fortegn, fordelt på [[fakturadato]].

## Avgrensning mot andre begreper

- [[rabatt]]: også en kreditering, men uten at varen leveres tilbake.

## Systemrepresentasjon

### erp

- **Representasjon:** Kreditnotaer med årsakskode for retur.
- **Avvik fra forretningsdefinisjon:** Før 2024 ble årsakskode ikke alltid fylt ut. Kreditnotaer uten årsakskode er regnet som retur.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Økonomisjef |
