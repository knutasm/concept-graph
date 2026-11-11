---
id: vare
navn: Vare
type: entitet
domene: sortiment
kortdefinisjon: En fysisk artikkel i sortimentet vårt som vi kjøper inn, lagerfører eller selger.
synonymer: [artikkel, produkt, item]
status: godkjent
eier: Kategoriavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-11
systemer: ["[[erp]]", "[[lagerstyringssystem]]", "[[nettbutikk]]"]
kilde: "[[erp]]"
identifiseres_ved: varenummer
---
# Vare

## Definisjon

En fysisk artikkel i sortimentet vårt, som rør, rørdeler, servanter, blandebatterier og verktøy, som vi
kjøper inn fra en [[leverandor]] og selger til en [[kunde]]. Hver vare tilhører én [[varegruppe]]
og har en [[maaleenhet]] som beholdningen føres i.

## Forretningsregler

- Inkluderer: både lagerførte varer og skaffevarer som bare bestilles inn når en kunde trenger dem.
- Ekskluderer: tjenester og kostnader som frakt, gebyrer og pant på returemballasje.
- Samme artikkel fra to leverandører er én vare hvis den er helt lik for kunden.

## Eksempler

- Et 15 mm kobberrør i 5-meterslengder. **Vare.**
- Fraktgebyr for levering til byggeplass. **Ikke vare**, det er en kostnad.
- En spesialbestilt pumpe som aldri ligger på lager. **Vare** (skaffevare).

## Systemrepresentasjon

### erp

- **Representasjon:** Vareregisteret.
- **Identifikasjon:** Varenummer. Bransjens felles varenummer er lagret som et eget felt.
- **Avvik fra forretningsdefinisjon:** Frakt, gebyrer og pant er registrert som varer med egen varetype. De må filtreres bort.

### lagerstyringssystem

- **Representasjon:** Artikler med lagerplass. Bare lagerførte varer finnes her.
- **Identifikasjon:** Varenummer fra ERP.
- **Avvik fra forretningsdefinisjon:** Skaffevarer mangler.

### nettbutikk

- **Representasjon:** Produktkatalogen.
- **Identifikasjon:** Varenummer fra ERP.
- **Avvik fra forretningsdefinisjon:** Varer som ikke selges på nett, er skjult og mangler i katalogen.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Kategoriledelsen |
| 2026-11-11 | Flyttet fra domenet kjerne til innkjop. Definisjonen er uendret | … |
| 2026-11-11 | Flyttet fra domenet innkjop til sortiment. Definisjonen er uendret | … |
