---
id: gjennomsnittlig_lagerbeholdning
navn: Gjennomsnittlig lagerbeholdning
type: maaltall
domene: logistikk
kortdefinisjon: Snittet av de daglige lagerbeholdningene i en periode.
synonymer: [snittbeholdning, gjennomsnittlig varelager, average inventory]
status: utkast
eier: Logistikkavdelingen
sist_oppdatert: 2026-11-11
systemer: []
avledet_av: ["[[lagerbeholdning]]"]
aggregering: snitt
enhet: NOK
granularitet: "[[vare]]"
tidsdimensjon: "[[beholdningsdato]]"
additivitet: semi_additiv
---
# Gjennomsnittlig lagerbeholdning

## Definisjon

Snittet av [[lagerbeholdning]]en ved slutten av hver dag i en periode.

## Forretningsregler

- Alle kalenderdager i perioden teller, også helger og helligdager.

## Beregning

`sum av daglig lagerbeholdning / antall dager i perioden`

**Semi-additiv:** kan summeres på tvers av varer, varegrupper og lagre for samme periode, men **ikke over
tid**. Snittet for et kvartal regnes på nytt fra de daglige beholdningene. Det er ikke summen av
månedssnittene.

## Systemrepresentasjon

Ikke kartlagt.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2026-11-11 | Opprettet som stubb | Logistikkavdelingen |

## Åpne spørsmål

- Stubb. Synonymer, eksempler og systemrepresentasjon må fylles ut.
