---
id: brutto_omsetning
navn: Brutto omsetning
type: maaltall
domene: okonomi
kortdefinisjon: Fakturert salg eksklusiv mva, før returer og rabatter.
synonymer: [bruttosalg, gross revenue]
status: godkjent
eier: Økonomiavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-10
systemer: [erp]
relasjoner:
  se_ogsaa: [netto_omsetning]
aggregering: sum
enhet: NOK
grain: faktura
tidsdimensjon: fakturadato
additivitet: additiv
---
# Brutto omsetning

## Definisjon

Summen av fakturert beløp eksklusiv merverdiavgift, før [[returer]] og [[rabatt]] er trukket fra.

## Forretningsregler

- Inkluderer: alle utsendte fakturaer med positivt beløp.
- Ekskluderer: merverdiavgift, kreditnotaer (se [[returer]]).

## Beregning

Sum av fakturabeløp eksklusiv mva over alle [[faktura]]er med positivt beløp, fordelt på [[fakturadato]].
Kan summeres fritt over tid, kunder og produkter.

## Systemrepresentasjon

### erp

- **Representasjon:** Linjebeløp eksklusiv mva på fakturalinjene, summert per faktura.
- **Avvik fra forretningsdefinisjon:** Ingen kjente.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Økonomisjef |
