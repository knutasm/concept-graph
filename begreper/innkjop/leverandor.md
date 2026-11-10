---
id: leverandor
navn: Leverandør
type: entitet
domene: innkjop
kortdefinisjon: En produsent eller grossist som vi kjøper varer fra for videresalg.
synonymer: [vareleverandør, supplier]
status: godkjent
eier: Innkjøpsavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-10
systemer: [erp]
identifiseres_ved: leverandørnummer
---
# Leverandør

## Definisjon

En produsent, importør eller annen grossist som vi kjøper [[vare]]r fra for å selge dem videre.

## Forretningsregler

- Inkluderer: alle vi har sendt minst én [[innkjopsordre]] til.
- Ekskluderer: leverandører av driftsmidler og tjenester, som husleie, strøm, transport og IT.
- Et konsern med flere selskaper vi kjøper fra, er én leverandør per selskap.

## Systemrepresentasjon

### erp

- **Representasjon:** Leverandørregisteret (kreditorer).
- **Identifikasjon:** Leverandørnummer.
- **Avvik fra forretningsdefinisjon:** Registeret inneholder alle kreditorer, også de som leverer tjenester og driftsmidler. Bare kreditorer med kreditortype "vareleverandør" er leverandører.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Innkjøpssjef |
