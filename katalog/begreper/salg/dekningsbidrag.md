---
id: dekningsbidrag
navn: Dekningsbidrag
type: maaltall
domene: salg
kortdefinisjon: Omsetning minus varekost. Hva salget bidrar med til å dekke kostnader og gi overskudd.
synonymer: [DB, bruttofortjeneste, gross margin]
status: godkjent
eier: Økonomiavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-10
systemer: [datavarehus]
avledet_av: ["[[omsetning]]", "[[varekost]]"]
forveksles_med: ["[[dekningsgrad]]"]
aggregering: formel
enhet: NOK
grain: "[[fakturalinje]]"
tidsdimensjon: "[[fakturadato]]"
additivitet: additiv
---
# Dekningsbidrag

## Definisjon

[[omsetning]] minus [[varekost]]. Viser hva salget bidrar med til å dekke andre kostnader og gi overskudd.

## Beregning

`omsetning - varekost`

Begge har samme grain og tidsdimensjon, så formelen gjelder på alle nivåer og kan summeres fritt.

## Eksempler

- Omsetning 100 000, varekost 72 000: dekningsbidrag = 28 000.

## Avgrensning mot andre begreper

- [[dekningsgrad]]: dekningsbidraget i prosent av omsetningen.

## Systemrepresentasjon

### datavarehus

- **Representasjon:** Beregnes fra omsetning og varekost.
- **Avvik fra forretningsdefinisjon:** Arver avviket i [[varekost]] for direkteleveranser.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Økonomisjef |
