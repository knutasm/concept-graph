---
id: netto_omsetning
navn: Netto omsetning
type: maaltall
domene: okonomi
kortdefinisjon: Brutto omsetning fratrukket returer og rabatter, eksklusiv mva.
synonymer: [nettosalg, omsetning, net revenue]
status: godkjent
eier: Økonomiavdelingen
gyldig_fra: 2024-07-01
sist_oppdatert: 2026-11-10
systemer: [erp, datavarehus]
relasjoner:
  avledet_av: [brutto_omsetning, returer, rabatt]
  forveksles_med: [mrr]
aggregering: formel
enhet: NOK
grain: faktura
tidsdimensjon: fakturadato
additivitet: additiv
---
# Netto omsetning

## Definisjon

[[brutto_omsetning]] fratrukket [[returer]] og [[rabatt]]. Eksklusiv merverdiavgift.
Dette er omsetningstallet som brukes i ledelsesrapportering når ikke annet er sagt.

## Forretningsregler

- Måles i perioden fakturaen eller kreditnotaen er utstedt.
- Engangsbeløp og gjentakende inntekter er begge med.

## Beregning

`brutto_omsetning - returer - rabatt`

Alle tre måltallene har samme grain og tidsdimensjon, så formelen kan brukes på alle nivåer.

## Eksempler

- Faktura 10 000, rabatt 1 000, senere retur for 2 000: netto omsetning = 10 000 − 1 000 − 2 000 = 7 000.

## Avgrensning mot andre begreper

- [[mrr]]: gjentakende inntekt omregnet til én måned, uavhengig av når det faktureres. Ikke det samme som netto omsetning per måned.

## Systemrepresentasjon

### erp

- **Representasjon:** Omsetningskontoene i hovedboken.
- **Avvik fra forretningsdefinisjon:** Hovedboken trekker volumbonus fra i perioden den bokføres, ikke perioden kreditnotaen er utstedt. Det gir små periodeavvik.

### datavarehus

- **Representasjon:** Beregnes fra fakturaer og kreditnotaer etter formelen over.
- **Avvik fra forretningsdefinisjon:** Ingen kjente.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet som brutto omsetning minus returer | Økonomisjef |
| 2024-07-01 | Rabatt trukket fra i tillegg | Økonomisjef |
