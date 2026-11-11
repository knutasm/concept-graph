---
id: faktura
navn: Faktura
type: entitet
domene: salg
kortdefinisjon: Et krav om betaling sendt til en kunde for leverte varer, inkludert kreditnotaer.
synonymer: [invoice, kreditnota]
status: godkjent
eier: Økonomiavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-10
systemer: [erp]
tilhorer: ["[[kunde]]"]
forveksles_med: ["[[ordre]]"]
identifiseres_ved: fakturanummer
---
# Faktura

## Definisjon

Et krav om betaling sendt til en [[kunde]] for leverte [[vare]]r. En kreditnota er en faktura med
negativt beløp. Fakturaen består av én eller flere [[fakturalinje]]r og har en [[fakturadato]].

## Forretningsregler

- Inkluderer: fakturaer og kreditnotaer, også for kontantsalg.
- Ekskluderer: proformafakturaer og utkast som ikke er sendt.
- En faktura kan dekke flere ordre (samlefaktura), og en ordre kan gi flere fakturaer.

## Avgrensning mot andre begreper

- [[ordre]]: bestillingen. Fakturaen kommer når varene er levert.

## Systemrepresentasjon

### erp

- **Representasjon:** Fakturaregisteret. Kreditnotaer har egen dokumenttype.
- **Identifikasjon:** Fakturanummer.
- **Avvik fra forretningsdefinisjon:** Proformafakturaer ligger i samme register og må filtreres bort.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Økonomisjef |
