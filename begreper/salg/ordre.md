---
id: ordre
navn: Ordre
type: entitet
domene: salg
kortdefinisjon: En bekreftet bestilling fra en kunde om levering av varer eller tjenester.
synonymer: [salgsordre, bestilling, order]
status: godkjent
eier: Salgsavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-10
systemer: [erp]
relasjoner:
  tilhorer: [kunde]
  forveksles_med: [faktura]
identifiseres_ved: ordrenummer
---
# Ordre

## Definisjon

En bestilling fra en [[kunde]] som vi har bekreftet at vi skal levere. Ordren består av én eller
flere [[ordrelinje]]r og har en [[ordredato]].

## Forretningsregler

- Inkluderer: bekreftede, leverte og senere kansellerte ordrer. Kansellering endrer ikke at ordren fantes.
- Ekskluderer: tilbud og utkast som kunden ikke har bekreftet.

## Avgrensning mot andre begreper

- [[faktura]]: kravet om betaling. Én ordre kan gi flere fakturaer (delleveranser), og omsetning måles på faktura, ikke ordre.

## Systemrepresentasjon

### erp

- **Representasjon:** Ordrehodet. Tilbud, utkast og ordre ligger i samme register og skilles med et statusfelt.
- **Identifikasjon:** Ordrenummer.
- **Avvik fra forretningsdefinisjon:** Tilbud og utkast ligger i samme register og må filtreres bort. Status "bekreftet" og senere (levert, kansellert) er ordre.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Salgsledelsen |
