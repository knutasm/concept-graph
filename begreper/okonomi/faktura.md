---
id: faktura
navn: Faktura
type: entitet
domene: okonomi
kortdefinisjon: Et krav om betaling sendt til en kunde for leverte varer eller tjenester, inkludert kreditnotaer.
synonymer: [invoice, kreditnota]
status: godkjent
eier: Økonomiavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-10
systemer: [erp]
relasjoner:
  tilhorer: [kunde]
  forveksles_med: [ordre]
identifiseres_ved: fakturanummer
---
# Faktura

## Definisjon

Et krav om betaling som er sendt til en [[kunde]] for leverte varer eller tjenester. En kreditnota
regnes som en faktura med negativt beløp, og viser til fakturaen den krediterer.

## Forretningsregler

- Inkluderer: utsendte fakturaer og kreditnotaer.
- Ekskluderer: proformafakturaer og fakturautkast som ikke er sendt.

## Avgrensning mot andre begreper

- [[ordre]]: bestillingen. Fakturaen er kravet som følger av leveransen.

## Systemrepresentasjon

### erp

- **Representasjon:** Fakturaregisteret. Kreditnotaer har egen dokumenttype.
- **Identifikasjon:** Fakturanummer. Kreditnotaer har egen nummerserie.
- **Avvik fra forretningsdefinisjon:** Proformafakturaer ligger i samme register og må filtreres bort.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Økonomisjef |
