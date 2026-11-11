---
id: maaleenhet
navn: Måleenhet
type: dimensjon
domene: kjerne
kortdefinisjon: Enheten en mengde av en vare uttrykkes i, f.eks. stykk, meter eller pakke.
synonymer: [enhet, unit of measure]
status: godkjent
eier: Kategoriavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-10
systemer: [erp, nettbutikk]
beskriver: ["[[vare]]"]
dimensjonstype: kategori
---
# Måleenhet

## Definisjon

Enheten en mengde av en [[vare]] uttrykkes i. Hver vare har én **lagerenhet** som beholdningen føres i.
I tillegg kan den ha en **kjøpsenhet** (slik [[leverandor]]en selger den) og en **salgsenhet** (slik
[[kunde]]n kjøper den), med faste omregningsfaktorer til lagerenheten.

## Forretningsregler

- Alle mengder i måltall og rapporter regnes om til lagerenheten.
- Mengder i ulike enheter kan ikke summeres. 10 meter rør og 10 stykk rørdeler er ikke 20 av noe.

## Gyldige verdier

- `stk`: stykk
- `m`: meter
- `kg`: kilo
- `l`: liter
- `pk`: pakke med fast antall stykk
- `bunt`: bunt med fast antall lengder

## Eksempler

- Kobberrør kjøpes i bunter på 10 lengder, lagerføres i meter og selges i lengder på 5 meter.
  Kjøpsenhet `bunt` = 50 `m`. Salgsenhet lengde = 5 `m`.

## Systemrepresentasjon

### erp

- **Representasjon:** Lagerenhet og omregningsfaktorer på varen.
- **Avvik fra forretningsdefinisjon:** Ingen kjente.

### nettbutikk

- **Representasjon:** Viser pris og antall i salgsenhet.
- **Avvik fra forretningsdefinisjon:** Antall i nettbutikkens rapporter er i salgsenhet, ikke lagerenhet.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Kategoriledelsen |
