---
id: varekost
navn: Varekost
type: maaltall
domene: okonomi
kortdefinisjon: Hva de solgte varene kostet oss, til gjennomsnittlig innkjøpskost på salgstidspunktet.
synonymer: [vareforbruk, kost solgte varer, COGS]
status: godkjent
eier: Økonomiavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-11
systemer: [erp]
avledet_av: ["[[fakturalinje]]"]
aggregering: sum
enhet: NOK
grain: "[[fakturalinje]]"
tidsdimensjon: "[[fakturadato]]"
additivitet: additiv
---
# Varekost

## Definisjon

Hva de solgte [[vare]]ne kostet oss. Beregnes som fakturert antall ganger vektet gjennomsnittlig
innkjøpskost på fakturatidspunktet, inkludert inngående frakt.

## Forretningsregler

- Måles i samme periode som [[omsetning]], altså på [[fakturadato]].
- Ved direktelevering fra leverandør er varekosten den faktiske innkjøpsprisen for leveransen.
- Kreditnotaer for returnerte varer gir negativ varekost.

## Beregning

Sum over [[fakturalinje]]r av fakturert antall i lagerenhet ganger gjennomsnittlig innkjøpskost.

## Systemrepresentasjon

### erp

- **Representasjon:** Kostbeløpet på fakturalinjen, satt ved fakturering.
- **Avvik fra forretningsdefinisjon:** Ved direktelevering kommer leverandørfakturaen ofte etter at vi har fakturert kunden. Da står foreløpig innkjøpspris på linjen, og den rettes ikke i ettertid.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Økonomisjef |
| 2026-11-11 | Flyttet fra domenet salg til okonomi. Definisjonen er uendret | … |
