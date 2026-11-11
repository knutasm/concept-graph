---
id: leveringsgrad
navn: Leveringsgrad
type: maaltall
domene: logistikk
kortdefinisjon: Andelen ordrelinjer som ble levert komplett på avtalt dato.
synonymer: [leveringsevne, servicegrad, fill rate]
status: godkjent
eier: Logistikkavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-10
systemer: ["[[datavarehus]]"]
avledet_av: ["[[ordrelinje]]", "[[leveranse]]", "[[restordre]]"]
forveksles_med: ["[[leveringspresisjon_leverandor]]"]
aggregering: ratio
enhet: prosent
granularitet: "[[ordrelinje]]"
tidsdimensjon: "[[ordredato]]"
additivitet: ikke_additiv
---
# Leveringsgrad

## Definisjon

Andelen [[ordrelinje]]r som ble levert komplett senest på avtalt leveringsdato. Måler hvor godt vi
leverer til [[kunde]]ne.

## Forretningsregler

- En linje er levert komplett hvis hele mengden er levert senest på avtalt dato, i én eller flere [[leveranse]]r.
- Linjer som har blitt [[restordre]], er ikke levert komplett.
- Linjer der kunden har bedt om senere levering, regnes mot den nye datoen.
- Kansellerte linjer er ikke med.

## Beregning

Antall ordrelinjer levert komplett i tide delt på antall ordrelinjer, i prosent, fordelt på [[ordredato]].

**Ikke-additiv:** beregnes fra antallene for hele utvalget, ikke som snittet av leveringsgraden per lager eller måned.

## Avgrensning mot andre begreper

- [[leveringspresisjon_leverandor]]: hvor godt leverandørene leverer til oss.

## Systemrepresentasjon

### datavarehus

- **Representasjon:** Beregnes per ordrelinje fra leveranser og avtalt leveringsdato.
- **Avvik fra forretningsdefinisjon:** Arver avviket i [[restordre]]: utsatte prosjektleveranser telles som ikke levert i tide.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Logistikksjef |
