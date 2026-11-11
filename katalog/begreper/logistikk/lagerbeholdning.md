---
id: lagerbeholdning
navn: Lagerbeholdning
type: maaltall
domene: logistikk
kortdefinisjon: Verdien av varene vi har på lager ved slutten av en dag, til gjennomsnittlig innkjøpskost.
synonymer: [lagerverdi, varelager, beholdning, inventory]
status: godkjent
eier: Logistikkavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-10
systemer: ["[[lagerstyringssystem]]", "[[erp]]"]
avledet_av: ["[[vare]]", "[[lager]]"]
aggregering: sum
enhet: NOK
granularitet: "[[vare]]"
tidsdimensjon: "[[beholdningsdato]]"
additivitet: semi_additiv
---
# Lagerbeholdning

## Definisjon

Verdien av [[vare]]ne vi har på [[lager]] ved slutten av en [[beholdningsdato]]. Beregnes som antall i
lagerenhet ganger vektet gjennomsnittlig innkjøpskost. Måles per vare og lager.

## Forretningsregler

- Inkluderer: varer som er reservert for en kunde, men ikke levert.
- Ekskluderer: varer i transitt, i karantene og ukontrollerte returer (se [[lager]]).
- Antall kan bare summeres for én og samme vare, fordi varene har ulik [[maaleenhet]]. Verdien kan summeres på tvers av varer.

## Beregning

Sum av antall i lagerenhet ganger gjennomsnittlig innkjøpskost, per vare og lager, ved dagens slutt.

**Semi-additiv:** kan summeres på tvers av varer, varegrupper og lagre, men **ikke over tid**.
Lagerbeholdningen for en måned er beholdningen ved siste dag i måneden. Gjennomsnittlig beholdning
er et eget måltall.

## Eksempler

- Beholdning 30. september 12 mill. og 31. oktober 13 mill. Lagerbeholdning for september og
  oktober samlet er 13 mill. (siste dag), ikke 25 mill.

## Systemrepresentasjon

### lagerstyringssystem

- **Representasjon:** Antall per vare og lagerplass. Kilden for antall.
- **Avvik fra forretningsdefinisjon:** Har ikke verdi. Virtuelle lagre må filtreres bort.

### erp

- **Representasjon:** Gjennomsnittlig innkjøpskost per vare. Kilden for verdien.
- **Avvik fra forretningsdefinisjon:** ERP har også sin egen beholdning, som kan avvike fra lagerstyringssystemet frem til nattlig avstemming. Bruk antall fra lagerstyringssystemet.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Logistikksjef |
