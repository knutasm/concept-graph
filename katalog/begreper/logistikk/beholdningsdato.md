---
id: beholdningsdato
navn: Beholdningsdato
type: dimensjon
domene: logistikk
kortdefinisjon: Dagen en lagerbeholdning gjelder for, målt ved dagens slutt.
synonymer: [lagerdato, snapshot date]
status: godkjent
eier: Logistikkavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-10
systemer: [datavarehus]
se_ogsaa: ["[[kalenderdag]]"]
dimensjonstype: tid
---
# Beholdningsdato

## Definisjon

Dagen en [[lagerbeholdning]] gjelder for, målt ved dagens slutt etter alle mottak og leveranser.

## Systemrepresentasjon

### datavarehus

- **Representasjon:** Datoen beholdningen ble lest inn med den nattlige lastingen.
- **Avvik fra forretningsdefinisjon:** Ingen kjente. Mangler en natt, finnes ikke beholdningen for den dagen.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Logistikksjef |
