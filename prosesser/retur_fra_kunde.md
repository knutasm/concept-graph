---
id: retur_fra_kunde
navn: Retur fra kunde
domene: salg
kortdefinisjon: Fra kunden ber om å returnere varer til varen er kontrollert og kunden er kreditert, eller returen er avvist.
synonymer: [returhåndtering, kunderetur, customer return]
status: utkast
eier: Salgsavdelingen
sist_oppdatert: 2026-11-10
utloser: "[[returforesporsel]]"
begreper: ["[[returforesporsel]]", "[[retur]]", "[[kunde]]", "[[ordre]]", "[[vare]]", "[[faktura]]", "[[leveranse]]", "[[lager]]", "[[returmottak]]"]
---
# Retur fra kunde

## Formål

Virksomheten må kunne ta imot og gjøre opp varer kunden sender tilbake, slik at kunden får oppgjør,
og varene kommer tilbake i salg eller blir tatt hånd om på en kontrollert måte.

## Avgrensning

- **Starter når:** En [[kunde]] ber om å få returnere [[vare]]r.
- **Ferdig når:** Varen er kontrollert og kunden har fått kreditnota, eller kunden har fått beskjed om at returen er avvist.
- **Utenfor:** [[reklamasjon]] (feil eller mangel ved varen, feil vare levert eller skade før levering). Salget og faktureringen av
  varene (se [[ordre_til_faktura]]).

## Aktører

| Aktør | Ansvar i prosessen |
|---|---|
| Kunde | Ber om retur og sender varen tilbake |
| Kundesenter | Vurderer og godkjenner eller avviser returen |
| Lager | Tar imot, kontrollerer og setter varen tilbake på lager |
| Økonomi | Krediterer kunden |

## Steg

### s1 Be om retur
Kunden ber om å returnere varer og viser til fakturaen varene ble kjøpt på.
- **Aktør:** Kunde
- **Bruker:** [[kunde]], [[ordre]], [[vare]], [[faktura]]
- **Gir:** [[returforesporsel]]
- **Neste:** s2

### s2 Vurdere returforespørselen
- **Aktør:** Kundesenter
- **Bruker:** [[returforesporsel]], [[faktura]], [[leveranse]]
- **Neste:** b1

### b1 Godkjennes returforespørselen?
- **Aktør:** Kundesenter
- **Regel:** Forespørselen må vise til fakturaen varene ble kjøpt på, slik at den kan knyttes til en ordre. Øvrige vilkår er ikke avklart (se Åpne spørsmål).
- **Neste:** ja → s2a; nei → r2

### s2a Godkjenne returen
Den godkjente forespørselen blir en retur med eget returnummer.
- **Aktør:** Kundesenter
- **Bruker:** [[returforesporsel]]
- **Gir:** [[retur]]
- **Neste:** s3

### s3 Sende varen tilbake
- **Aktør:** Kunde
- **Bruker:** [[retur]]
- **Neste:** s4

### s4 Ta imot og kontrollere varen
- **Aktør:** Lager
- **Bruker:** [[retur]], [[lager]]
- **Gir:** [[returmottak]]
- **Neste:** s5

### s5 Sette varen tilbake på lager
- **Aktør:** Lager
- **Bruker:** [[vare]], [[lager]]
- **Neste:** s6

### s6 Kreditere kunden
Kunden får en kreditnota for de returnerte varene.
- **Aktør:** Økonomi
- **Bruker:** [[returmottak]], [[faktura]]
- **Gir:** [[faktura]]
- **Neste:** r1

## Resultater

### r1 Retur kreditert
Varen er kontrollert og satt tilbake på lager, og kunden har fått kreditnota.
- **Hendelse:** [[faktura]]

### r2 Retur avvist
Kunden har fått beskjed om at returforespørselen ikke godkjennes.

## Åpne spørsmål

- Utkast. Steg, aktører og begreper må bekreftes av eier.
- Hva avgjør om en retur godkjennes, utover at den viser til en faktura? For eksempel en frist etter
  levering, at varen er ubrukt og i originalemballasje, eller varer som ikke kan returneres (skaffevarer, kappet vare).
- Hva skjer hvis varen ikke er i salgbar stand ved kontrollen (s4)? Kasseres den, krediteres kunden
  med trekk, eller sendes varen tilbake? Det kan gi en ny beslutning og nye resultater.
- Hva skjer hvis kunden får godkjent retur, men aldri sender varen? Avsluttes returen etter en frist?
- [[returmottak]], [[returmottaksdato]] og [[reklamasjon]] er stubber og må defineres.
