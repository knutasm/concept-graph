---
id: virkedag
navn: Virkedag
type: klassifisering
domene: logistikk
kortdefinisjon: En kalenderdag fra mandag til fredag som ikke er en offentlig helligdag.
synonymer: [arbeidsdag, business day]
status: godkjent
eier: Logistikkavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-11
systemer: [datavarehus]
er_en: ["[[kalenderdag]]"]
---
# Virkedag

## Definisjon

En [[kalenderdag]] fra mandag til fredag som ikke er en offentlig helligdag i Norge. Brukes når
leveringstid og forsinkelse måles.

## Forretningsregler

- Lørdag og søndag er ikke virkedager.
- Offentlige helligdager og 1. og 17. mai er ikke virkedager.
- Julaften og nyttårsaften er ikke virkedager.
- Fellesferien teller som virkedager, fordi lageret holder åpent.

## Eksempler

- Bestilt fredag, levert mandag: **1 virkedag**.
- Onsdag før skjærtorsdag til tirsdag etter påske: **1 virkedag**.

## Systemrepresentasjon

### datavarehus

- **Representasjon:** Egenskap på kalendertabellen.
- **Avvik fra forretningsdefinisjon:** Ingen kjente.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Logistikkledelsen |
| 2026-11-11 | Flyttet fra domenet kjerne til logistikk. Definisjonen er uendret | … |
