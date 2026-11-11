---
id: omsetning
navn: Omsetning
type: maaltall
domene: okonomi
kortdefinisjon: Fakturert salg av varer eksklusiv mva, fratrukket kreditnotaer.
synonymer: [netto omsetning, salg, salgsinntekt, revenue]
status: godkjent
eier: Økonomiavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-11
systemer: [erp, nettbutikk, datavarehus]
avledet_av: ["[[fakturalinje]]"]
aggregering: sum
enhet: NOK
grain: "[[fakturalinje]]"
tidsdimensjon: "[[fakturadato]]"
additivitet: additiv
---
# Omsetning

## Definisjon

Summen av fakturert beløp for [[vare]]r, eksklusiv merverdiavgift og etter rabatter, fratrukket
kreditnotaer. Dette er omsetningstallet som brukes i all rapportering når ikke annet er sagt.

## Forretningsregler

- Måles i perioden fakturaen eller kreditnotaen er utstedt.
- Inkluderer: kontantsalg og direkteleveranser fra leverandør til kunde.
- Ekskluderer: merverdiavgift, frakt, gebyrer og pant.

## Beregning

Sum av fakturert beløp eksklusiv mva over alle [[fakturalinje]]r, fordelt på [[fakturadato]].
Kreditnotaer gir negative beløp. Kan summeres over tid, kunder, varer og lagre.

## Avgrensning mot andre begreper

- Ordreinngang: verdien av bekreftede [[ordre]] per [[ordredato]]. Ikke det samme som omsetning.

## Systemrepresentasjon

### erp

- **Representasjon:** Fakturerte beløp på fakturalinjene.
- **Avvik fra forretningsdefinisjon:** Frakt og gebyrer må filtreres bort.

### nettbutikk

- **Representasjon:** Rapportene viser "salg", men det er ordreverdi på bestillingstidspunktet.
- **Avvik fra forretningsdefinisjon:** Stort. Ordreverdi, ikke fakturert beløp. Kanselleringer og kreditnotaer er ikke trukket fra. Bruk ikke nettbutikkens tall som omsetning.

### datavarehus

- **Representasjon:** Beregnes fra fakturalinjer etter definisjonen over.
- **Avvik fra forretningsdefinisjon:** Ingen kjente.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Økonomisjef |
| 2026-11-11 | Flyttet fra domenet salg til okonomi. Definisjonen er uendret | … |
