---
id: innkjopsordre
navn: Innkjøpsordre
type: entitet
domene: innkjop
kortdefinisjon: En bestilling av varer som vi har sendt til en leverandør.
synonymer: [bestilling til leverandør, purchase order, PO]
status: godkjent
eier: Innkjøpsavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-10
systemer: [erp]
tilhorer: ["[[leverandor]]"]
forveksles_med: ["[[ordre]]"]
identifiseres_ved: innkjøpsordrenummer
---
# Innkjøpsordre

## Definisjon

En bestilling av [[vare]]r som vi har sendt til en [[leverandor]]. Innkjøpsordren har en bekreftet
leveringsdato fra leverandøren og leveres inn gjennom ett eller flere [[varemottak]].

## Forretningsregler

- Inkluderer: bestillinger til eget lager og direkteleveranser fra leverandør til kunde eller byggeplass.
- Ekskluderer: forslag til bestilling som ikke er sendt til leverandøren.
- Bekreftet leveringsdato er datoen leverandøren har bekreftet, ikke datoen vi ønsket.

## Avgrensning mot andre begreper

- [[ordre]]: kundens bestilling til oss. En innkjøpsordre er vår bestilling til leverandøren.

## Systemrepresentasjon

### erp

- **Representasjon:** Innkjøpsordrer med linjer og bekreftet leveringsdato per linje.
- **Identifikasjon:** Innkjøpsordrenummer.
- **Avvik fra forretningsdefinisjon:** Bestillingsforslag ligger i samme register med egen status og må filtreres bort. Mangler bekreftet leveringsdato, er ønsket dato brukt.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Innkjøpssjef |
