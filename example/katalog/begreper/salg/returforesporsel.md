---
id: returforesporsel
navn: Returforespørsel
type: entitet
domene: salg
kortdefinisjon: En kundes forespørsel om å levere tilbake feilfrie varer fra en ordre, som vi godkjenner eller avviser.
synonymer: [forespørsel om retur, return request]
status: utkast
eier: Salgsavdelingen
gyldig_fra: 2026-11-10
sist_oppdatert: 2026-11-10
systemer: []
tilhorer: ["[[ordre]]"]
forveksles_med: ["[[retur]]"]
identifiseres_ved: returforespørselsnummer
---
# Returforespørsel

## Definisjon

En [[kunde]]s forespørsel om å levere tilbake feilfrie [[vare]]r fra en [[ordre]], fordi kunden av egne
grunner ikke vil ha dem likevel. Vi godkjenner eller avviser forespørselen. En godkjent
returforespørsel blir en [[retur]].

## Forretningsregler

- Inkluderer: både godkjente og avviste forespørsler. Forespørselen finnes fra kunden ber om retur.
- Ekskluderer: krav om varer med feil eller mangel, feil vare levert, eller skade før levering. Det er [[reklamasjon]].
- En returforespørsel må vise til [[faktura]]en varene ble kjøpt på, slik at den kan knyttes til en ordre.
- Kan gjelde deler av en ordre: én av flere varer, eller deler av antallet på en vare.
- Får et eget returforespørselsnummer når den kommer inn, før den er vurdert.

## Avgrensning mot andre begreper

- [[retur]]: bare godkjente forespørsler blir en retur, med eget returnummer. Antall returforespørsler
  minus antall returer er antall avviste.

## Systemrepresentasjon

Ikke kartlagt.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2026-11-10 | Opprettet | Kundeansvarlig |

## Åpne spørsmål

- Kan én returforespørsel gi mer enn én retur, f.eks. hvis den bare godkjennes delvis?
- Hvilket system ligger returforespørslene i? Systemrepresentasjon er ikke kartlagt.
