---
id: leveringspresisjon_leverandor
navn: Leveringspresisjon leverandør
type: maaltall
domene: innkjop
kortdefinisjon: Andelen varemottak som kom senest på leverandørens bekreftede leveringsdato.
synonymer: [leverandørpresisjon, OTD leverandør, supplier on-time delivery]
status: godkjent
eier: Innkjøpsavdelingen
gyldig_fra: 2024-01-01
sist_oppdatert: 2026-11-10
systemer: ["[[datavarehus]]"]
avledet_av: ["[[varemottak]]", "[[innkjopsordre]]"]
forveksles_med: ["[[leveringsgrad]]"]
aggregering: ratio
enhet: prosent
granularitet: "[[varemottak]]"
tidsdimensjon: "[[mottaksdato]]"
additivitet: ikke_additiv
---
# Leveringspresisjon leverandør

## Definisjon

Andelen [[varemottak]] som kom senest på den bekreftede leveringsdatoen på [[innkjopsordre]]n.
Måler hvor godt [[leverandor]]ene holder det de har lovet.

## Forretningsregler

- Et mottak er i tide hvis [[mottaksdato]] er på eller før bekreftet leveringsdato.
- Forsinkelse måles i [[virkedag]]er.
- Mottak av varer som ikke var bestilt, er ikke med.

## Beregning

Antall varemottak i tide delt på antall varemottak, i prosent.

**Ikke-additiv:** presisjonen for et kvartal eller for alle leverandører beregnes fra antallene, ikke
som summen eller snittet av presisjonen per måned eller per leverandør.

## Avgrensning mot andre begreper

- [[leveringsgrad]]: hvor godt **vi** leverer til kundene. Leveringspresisjon gjelder leverandørene til oss.

## Systemrepresentasjon

### datavarehus

- **Representasjon:** Beregnes per varemottak ved å sammenligne mottaksdato med bekreftet leveringsdato.
- **Avvik fra forretningsdefinisjon:** Direkteleveranser får for sen mottaksdato (se [[mottaksdato]]), så presisjonen blir noe for lav.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2024-01-01 | Opprettet | Innkjøpssjef |
