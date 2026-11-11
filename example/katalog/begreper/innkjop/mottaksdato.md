---
id: mottaksdato
navn: Mottaksdato
type: dimensjon
domene: innkjop
kortdefinisjon: Datoen varene i et varemottak ble mottatt og kontrollert.
synonymer: [mottatt dato, receipt date]
status: godkjent
eier: Innkjøpsavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-10
systemer: ["[[lagerstyringssystem]]", "[[erp]]"]
beskriver: ["[[varemottak]]"]
dimensjonstype: tid
---
# Mottaksdato

## Definisjon

Datoen varene i et [[varemottak]] ble mottatt og kontrollert.

## Systemrepresentasjon

### lagerstyringssystem

- **Representasjon:** Kontrolldatoen på mottaket.
- **Avvik fra forretningsdefinisjon:** Ingen kjente.

### erp

- **Representasjon:** Registreringsdato for direkteleveranser.
- **Avvik fra forretningsdefinisjon:** Er datoen kvitteringen ble registrert, ikke datoen varen ble levert. Kan være flere dager for sent.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Innkjøpssjef |
