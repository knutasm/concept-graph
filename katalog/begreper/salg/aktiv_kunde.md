---
id: aktiv_kunde
navn: Aktiv kunde
type: klassifisering
domene: salg
kortdefinisjon: En kunde med minst én bekreftet ordre de siste 12 månedene.
synonymer: [active customer]
status: godkjent
eier: Salgsavdelingen
gyldig_fra: 2024-03-01
sist_oppdatert: 2026-11-10
systemer: ["[[datavarehus]]"]
er_en: ["[[kunde]]"]
avledet_av: ["[[ordre]]"]
forveksles_med: ["[[kunde]]"]
---
# Aktiv kunde

## Definisjon

En [[kunde]] som har minst én bekreftet [[ordre]] med [[ordredato]] innenfor de siste 12 månedene,
regnet bakover fra og med måledatoen.

## Forretningsregler

- Tidsvindu: 12 måneder bakover fra måledatoen, inkludert måledatoen.
- Bare bekreftede ordre teller. Kansellerte ordre teller ikke.
- Status beregnes per dag. En kunde kan være aktiv i januar og ikke aktiv i februar.

## Eksempler

- Entreprenør med siste ordre for 14 måneder siden, mens de venter på neste prosjekt. **Ikke aktiv.**

## Avgrensning mot andre begreper

- [[kunde]]: alle som noen gang har hatt en bekreftet ordre.

## Systemrepresentasjon

### datavarehus

- **Representasjon:** Beregnes per kunde og dag. Finnes ikke i noe kildesystem.
- **Avvik fra forretningsdefinisjon:** Ingen kjente.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet med tidsvindu på 6 måneder | Salgsdirektør |
| 2024-03-01 | Tidsvindu utvidet til 12 måneder, fordi entreprenører ofte kjøper i lange sykluser | Salgsdirektør |
