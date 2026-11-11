---
id: kalenderdag
navn: Kalenderdag
type: dimensjon
domene: kjerne
kortdefinisjon: En dag i den felles kalenderen, med uke, måned og regnskapsår.
synonymer: [dato, kalender, date]
status: godkjent
eier: Dataplattformteamet
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-10
systemer: [datavarehus]
se_ogsaa: ["[[virkedag]]"]
dimensjonstype: tid
---
# Kalenderdag

## Definisjon

En dag i den felles kalenderen. Alle datoer i katalogen, som [[ordredato]], [[fakturadato]] og
[[leveringsdato]], følger konvensjonene her når de grupperes til uke, måned eller år.

## Forretningsregler

- Uker følger ISO-standarden: uken starter mandag, og uke 1 er uken med årets første torsdag.
- Regnskapsåret følger kalenderåret.
- Måned og kvartal følger kalendermåned og kalenderkvartal.

## Systemrepresentasjon

### datavarehus

- **Representasjon:** Felles kalendertabell med én rad per dag.
- **Avvik fra forretningsdefinisjon:** Ingen kjente.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Dataplattformteamet |
