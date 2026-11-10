---
id: aktiv_kunde
navn: Aktiv kunde
type: klassifisering
domene: kunde
kortdefinisjon: En kunde med minst én bekreftet ordre de siste 12 månedene.
synonymer: [active customer, nåværende kunde]
status: godkjent
eier: Salgsavdelingen
gyldig_fra: 2024-03-01
sist_oppdatert: 2026-11-10
systemer: [datavarehus]
relasjoner:
  er_en: [kunde]
  avledet_av: [ordre]
  forveksles_med: [kunde]
---
# Aktiv kunde

## Definisjon

En [[kunde]] som har minst én bekreftet [[ordre]] med [[ordredato]] innenfor de siste 12 månedene,
regnet bakover fra og med måledatoen.

## Forretningsregler

- Tidsvindu: 12 måneder bakover fra måledatoen, inkludert måledatoen.
- Bare bekreftede ordrer teller. Kansellerte ordrer teller ikke, selv om de var bekreftet først.
- Status beregnes per dag. En kunde kan være aktiv i januar og ikke aktiv i februar.

## Eksempler

- Siste ordre var 13 måneder siden. **Ikke aktiv.**
- Eneste ordre i perioden ble kansellert. **Ikke aktiv.**

## Avgrensning mot andre begreper

- [[kunde]]: alle som noen gang har hatt en bekreftet ordre, uavhengig av når.

## Systemrepresentasjon

### datavarehus

- **Representasjon:** Beregnes i datavarehuset per kunde og dag. Finnes ikke i noe kildesystem.
- **Avvik fra forretningsdefinisjon:** Ingen kjente.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet med tidsvindu på 6 måneder | Salgsledelsen |
| 2024-03-01 | Tidsvindu utvidet fra 6 til 12 måneder | Salgsledelsen |
