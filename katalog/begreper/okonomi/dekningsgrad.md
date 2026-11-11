---
id: dekningsgrad
navn: Dekningsgrad
type: maaltall
domene: okonomi
kortdefinisjon: Dekningsbidrag i prosent av omsetningen.
synonymer: [DG, bruttomargin, margin, gross margin percent]
status: godkjent
eier: Økonomiavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-11
systemer: ["[[datavarehus]]"]
avledet_av: ["[[dekningsbidrag]]", "[[omsetning]]"]
forveksles_med: ["[[dekningsbidrag]]"]
aggregering: ratio
enhet: prosent
granularitet: "[[fakturalinje]]"
tidsdimensjon: "[[fakturadato]]"
additivitet: ikke_additiv
---
# Dekningsgrad

## Definisjon

[[dekningsbidrag]] i prosent av [[omsetning]].

## Beregning

`dekningsbidrag / omsetning`

**Ikke-additiv:** teller og nevner summeres først for utvalget, og så deles de. Dekningsgraden for to
varegrupper er **ikke** snittet av de to dekningsgradene.

## Eksempler

- Rør: omsetning 900 000, DB 180 000 (20 %). Verktøy: omsetning 100 000, DB 40 000 (40 %).
  Samlet dekningsgrad = 220 000 / 1 000 000 = **22 %**, ikke 30 %.

## Avgrensning mot andre begreper

- [[dekningsbidrag]]: beløpet i kroner.

## Systemrepresentasjon

### datavarehus

- **Representasjon:** Beregnes i rapporteringen etter at omsetning og dekningsbidrag er summert.
- **Avvik fra forretningsdefinisjon:** Ingen kjente.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Økonomisjef |
| 2026-11-11 | Flyttet fra domenet salg til okonomi. Definisjonen er uendret | … |
