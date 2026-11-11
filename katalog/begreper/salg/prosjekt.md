---
id: prosjekt
navn: Prosjekt
type: entitet
domene: salg
kortdefinisjon: Et byggeprosjekt som en kunde kjøper varer til, ofte med egne priser og egen leveringsadresse.
synonymer: [byggeprosjekt, kundeprosjekt, project]
status: til_godkjenning
eier: Salgsavdelingen
gyldig_fra: 2025-01-01
sist_oppdatert: 2026-11-10
systemer: ["[[erp]]", "[[crm]]"]
tilhorer: ["[[kunde]]"]
forveksles_med: ["[[kunde]]"]
identifiseres_ved: prosjektnummer
---
# Prosjekt

## Definisjon

Et byggeprosjekt som en [[kunde]] kjøper varer til, for eksempel et boligfelt, et sykehus eller en
skole. Et prosjekt har ofte egne avtalepriser, en egen leveringsadresse (byggeplassen) og en
avgrenset varighet. Hvert prosjekt tilhører én kunde.

## Forretningsregler

- Et prosjekt finnes fra første bekreftede [[ordre]] til prosjektet er avsluttet.
- Samme byggeplass med to kunder (f.eks. to underentreprenører) er to prosjekter.
- Ekskluderer: salgsmuligheter som ikke har gitt ordre.

## Avgrensning mot andre begreper

- [[kunde]]: virksomheten som kjøper. Prosjektet er hva den kjøper til.

## Systemrepresentasjon

### erp

- **Representasjon:** Finnes ikke som eget objekt. Prosjektet står som en referanse i fritekst på ordren, eller er opprettet som et eget kundenummer.
- **Identifikasjon:** Ingen sikker nøkkel. Prosjektnummeret må utledes fra referansen eller fra kundenummeret.
- **Avvik fra forretningsdefinisjon:** Stort. Fritekstreferansene er ikke konsekvente, og prosjekter med eget kundenummer ser ut som egne kunder.

### crm

- **Representasjon:** Salgsmuligheter av typen byggeprosjekt.
- **Identifikasjon:** CRM-ets id på salgsmuligheten.
- **Avvik fra forretningsdefinisjon:** Inneholder også prosjekter som aldri ga ordre.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2025-01-01 | Opprettet | Salgsdirektør |

## Åpne spørsmål

- Hvem tildeler prosjektnummer, og hvor skal det registreres?
- Når regnes et prosjekt som avsluttet?
