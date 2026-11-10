---
id: rabatt
navn: Rabatt
type: maaltall
domene: okonomi
kortdefinisjon: Alle prisavslag gitt til kunden, både på fakturaen og som kreditering i etterkant.
synonymer: [prisavslag, bonus, discount]
status: godkjent
eier: Økonomiavdelingen
gyldig_fra: 2024-07-01
sist_oppdatert: 2026-11-10
systemer: [erp]
relasjoner:
  forveksles_med: [returer]
aggregering: sum
enhet: NOK
grain: faktura
tidsdimensjon: fakturadato
additivitet: additiv
---
# Rabatt

## Definisjon

Alle prisavslag gitt til [[kunde]]n, målt som differansen mellom listepris og fakturert pris, pluss
krediteringer i etterkant som volumbonus. Eksklusiv merverdiavgift.

## Forretningsregler

- Inkluderer: linjerabatter på fakturaen og etterskuddsvis volumbonus.
- Ekskluderer: [[returer]].

## Beregning

Sum av (listepris − fakturert pris) × antall, pluss krediteringer med årsak bonus eller prisavslag.
Fordeles på [[fakturadato]].

## Systemrepresentasjon

### erp

- **Representasjon:** Rabattbeløp på fakturalinjene, pluss kreditnotaer med årsak bonus eller prisavslag.
- **Avvik fra forretningsdefinisjon:** Ingen kjente.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet. Kun linjerabatter | Økonomisjef |
| 2024-07-01 | Etterskuddsvis volumbonus tatt med | Økonomisjef |
