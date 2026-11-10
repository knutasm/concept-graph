---
id: mrr
navn: Månedlig gjentakende inntekt (MRR)
type: maaltall
domene: abonnement
kortdefinisjon: Samlet abonnementspris for alle aktive abonnementer, omregnet til én måned.
synonymer: [MRR, monthly recurring revenue, månedlig abonnementsinntekt]
status: godkjent
eier: Økonomiavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-10
systemer: [datavarehus]
relasjoner:
  avledet_av: [abonnement]
  forveksles_med: [netto_omsetning]
aggregering: sum
enhet: NOK
grain: abonnement
tidsdimensjon: maaned
additivitet: semi_additiv
---
# Månedlig gjentakende inntekt (MRR)

## Definisjon

Summen av prisen på alle aktive [[abonnement]] ved utgangen av en [[maaned]], omregnet til
månedsbeløp. Eksklusiv merverdiavgift og engangsbeløp.

## Forretningsregler

- Måles ved siste dag i måneden. Bare abonnementer som er aktive den dagen er med.
- Årspris deles på 12, kvartalspris på 3.
- Engangsbeløp som etableringsgebyr er ikke med.

## Beregning

Sum av månedspris over aktive [[abonnement]] per siste dag i [[maaned]].

**Semi-additiv:** kan summeres på tvers av kunder og produkter, men **ikke over tid**.
MRR for et kvartal er MRR i siste måned i kvartalet, ikke summen av tre måneder.

## Avgrensning mot andre begreper

- [[netto_omsetning]]: hva som faktisk er fakturert i perioden. Årsabonnementer gir høy omsetning én måned, men jevn MRR.

## Systemrepresentasjon

### datavarehus

- **Representasjon:** Beregnes månedlig fra abonnementsdata.
- **Avvik fra forretningsdefinisjon:** Ingen kjente.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Økonomisjef |
