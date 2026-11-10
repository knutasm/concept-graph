---
id: restordre
navn: Restordre
type: klassifisering
domene: logistikk
kortdefinisjon: En ordrelinje som ikke kunne leveres som avtalt fordi varen ikke var på lager.
synonymer: [rest, restnotert, backorder]
status: godkjent
eier: Logistikkavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-10
systemer: [erp]
er_en: ["[[ordrelinje]]"]
avledet_av: ["[[leveranse]]", "[[lagerbeholdning]]"]
---
# Restordre

## Definisjon

En [[ordrelinje]] som ikke kunne leveres helt på avtalt dato fordi [[vare]]n ikke var på [[lager]].
Den resterende mengden leveres senere.

## Forretningsregler

- En linje er restordre fra avtalt leveringsdato og til resten er levert.
- Ekskluderer: linjer der kunden selv har bedt om senere eller trinnvis levering, f.eks. et byggeprosjekt som vil ha varer i takt med fremdriften.
- Ekskluderer: skaffevarer før leverandørens bekreftede dato er passert.

## Eksempler

- Kunden bestiller 100 meter rør og vi har 60. **Restordre** for 40 meter.
- Entreprenør ber om at varmepumpene leveres om tre måneder. **Ikke restordre.**

## Systemrepresentasjon

### erp

- **Representasjon:** Ordrelinjer med status "delvis levert" eller "ikke levert" etter avtalt leveringsdato.
- **Avvik fra forretningsdefinisjon:** Statusen skiller ikke mellom manglende varer og levering utsatt etter kundens ønske. Utsatte leveranser for prosjekter blir derfor feilaktig talt som restordre.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Logistikksjef |

## Åpne spørsmål

- Hvordan skal kundens ønske om senere levering registreres, slik at det kan skilles fra mangel på varer?
