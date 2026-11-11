---
id: retur
navn: Retur
type: entitet
domene: salg
kortdefinisjon: En godkjent returforespørsel, altså en avtale om at kunden kan levere tilbake bestemte feilfrie varer fra en ordre.
synonymer: [godkjent retur, return]
status: utkast
eier: Salgsavdelingen
gyldig_fra: 2026-11-10
sist_oppdatert: 2026-11-10
systemer: []
tilhorer: ["[[returforesporsel]]", "[[ordre]]"]
forveksles_med: ["[[reklamasjon]]"]
identifiseres_ved: returnummer
---
# Retur

## Definisjon

En godkjent [[returforesporsel]]: en avtale om at [[kunde]]n kan levere tilbake bestemte feilfrie
[[vare]]r fra en [[ordre]], fordi kunden av egne grunner ikke vil ha dem likevel. Inngår i prosessen
Retur fra kunde.

## Forretningsregler

- Inkluderer: bare forespørsler vi har godkjent. Avviste forespørsler er ikke returer.
- Inkluderer: feilfrie varer kunden har bestilt for mye av, har bestilt feil, eller ikke trenger.
- Ekskluderer: varer med feil eller mangel, feil vare levert av oss, og varer skadet under
  transport. Det er [[reklamasjon]].
- Avgjørende er hvem som har skylden for at varen kommer tilbake: kunden selv (retur) eller vi
  eller produsenten (reklamasjon).
- Kan gjelde deler av en ordre: én av flere varer, eller deler av antallet på en vare.
- Får returnummer når forespørselen godkjennes. Hver retur hører til nøyaktig én [[returforesporsel]].

## Eksempler

- Rørleggeren bestilte 20 bend, brukte 14 og vil levere tilbake 6 ubrukte. **Retur**, når forespørselen er godkjent.
- Kunden bestilte to varer på samme ordre og vil returnere den ene. **Retur** for den ene varen.
- Kunden bestilte feil dimensjon selv, og varen er ubrukt. **Retur.**
- Kunden ba om retur, men forespørselen ble avvist. **Ikke retur**, bare en [[returforesporsel]].
- Vi plukket og leverte feil vare. **Ikke retur**, men reklamasjon: feilen er vår.
- Varen ble skadet under transport til byggeplassen. **Ikke retur**, men reklamasjon.
- Et blandebatteri lekker etter tre måneder i bruk. **Ikke retur**, men reklamasjon.

## Avgrensning mot andre begreper

- [[returforesporsel]]: kundens forespørsel, godkjent eller avvist. Retur er bare de godkjente.
- [[reklamasjon]]: kunden leverer tilbake eller klager på en vare med feil eller mangel, eller en vare
  vi har levert feil eller skadet. Ved retur er varen feilfri, og grunnen ligger hos kunden.

## Systemrepresentasjon

Ikke kartlagt.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2026-11-10 | Opprettet som stubb | Salgsavdelingen |
| 2026-11-10 | Definisjon, avgrensning mot reklamasjon, og skilt fra returforespørsel | Kundeansvarlig |

## Åpne spørsmål

- Kan én retur gjelde flere varer? I så fall trengs returlinje (del av retur, knyttet til en ordrelinje).
- Hvilket system ligger returene i, og hvordan er koblingen til returforespørselen lagret der?
  Systemrepresentasjon er ikke kartlagt.
