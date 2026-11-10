---
id: ordre
navn: Ordre
type: entitet
domene: salg
kortdefinisjon: En bekreftet bestilling av varer fra en kunde.
synonymer: [salgsordre, kundeordre, bestilling, order]
status: godkjent
eier: Salgsavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-10
systemer: [erp, nettbutikk]
tilhorer: ["[[kunde]]", "[[prosjekt]]"]
forveksles_med: ["[[faktura]]", "[[innkjopsordre]]"]
identifiseres_ved: ordrenummer
---
# Ordre

## Definisjon

En bestilling av [[vare]]r fra en [[kunde]] som vi har bekreftet. Ordren kan gjelde et [[prosjekt]],
består av én eller flere [[ordrelinje]]r og har en [[ordredato]].

## Forretningsregler

- Inkluderer: ordre fra alle kanaler, dvs. utsalgssted, telefon, e-post og netthandel.
- Inkluderer: ordre som senere er kansellert. Kansellering endrer ikke at ordren fantes.
- Ekskluderer: tilbud som kunden ikke har bekreftet.

## Avgrensning mot andre begreper

- [[faktura]]: kravet om betaling. En ordre kan faktureres i flere omganger ved delleveranser.
- [[innkjopsordre]]: vår bestilling til en leverandør.

## Systemrepresentasjon

### erp

- **Representasjon:** Ordreregisteret. Tilbud og ordre ligger sammen og skilles med status.
- **Identifikasjon:** Ordrenummer.
- **Avvik fra forretningsdefinisjon:** Tilbud må filtreres bort.

### nettbutikk

- **Representasjon:** Innsendte handlekurver. Overføres til ERP og får ordrenummer der.
- **Identifikasjon:** Nettbutikkens eget bestillingsnummer, med ordrenummeret fra ERP som eget felt.
- **Avvik fra forretningsdefinisjon:** Handlekurver som avvises ved overføring til ERP, f.eks. på grunn av kredittsperre, finnes bare her og er ikke ordre.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Salgsdirektør |
