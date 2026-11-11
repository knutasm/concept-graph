---
id: ordre_til_faktura
navn: Ordre til faktura
domene: salg
kortdefinisjon: Fra kunden bestiller varer til leveransen er fakturert.
synonymer: [order to cash, ordre til kontant]
status: utkast
eier: Salgsavdelingen
sist_oppdatert: 2026-11-10
utloser: "[[ordre]]"
begreper: ["[[kunde]]", "[[prosjekt]]", "[[ordre]]", "[[ordrelinje]]", "[[vare]]", "[[leveranse]]", "[[faktura]]", "[[fakturalinje]]"]
---
# Ordre til faktura

## Formål

Virksomheten må kunne selge varer til kunder og få betalt for det de har fått levert. En [[ordre]] kan
leveres og faktureres i flere omganger, og én [[faktura]] kan dekke flere ordre.

## Avgrensning

- **Starter når:** En [[kunde]] bestiller [[vare]]r, eventuelt til et [[prosjekt]].
- **Ferdig når:** Alle leverte varer på ordren er fakturert.
- **Utenfor:** Selve plukkingen og utleveringen (se [[plukk_og_levering]]), returer (se [[retur_fra_kunde]]), og innbetaling av fakturaen.

## Aktører

| Aktør | Ansvar i prosessen |
|---|---|
| Kunde | Bestiller varene |
| Kundesenter | Bekrefter ordren |
| Lager | Leverer varene |
| Økonomi | Fakturerer |

## Steg

### s1 Bestille varer
Kunden bestiller varer, eventuelt til et prosjekt.
- **Aktør:** Kunde
- **Bruker:** [[vare]], [[prosjekt]]
- **Neste:** s2

### s2 Bekrefte ordre
Vi bekrefter bestillingen som en ordre med én ordrelinje per vare.
- **Aktør:** Kundesenter
- **Bruker:** [[kunde]], [[vare]]
- **Gir:** [[ordre]], [[ordrelinje]]
- **Neste:** s3

### s3 Levere varer
Varene overleveres til kunden i én eller flere leveranser. Detaljene står i [[plukk_og_levering]].
- **Aktør:** Lager
- **Bruker:** [[ordre]], [[ordrelinje]]
- **Gir:** [[leveranse]]
- **Neste:** s4

### s4 Fakturere leverte varer
Leverte varer faktureres. Hver faktura består av fakturalinjer.
- **Aktør:** Økonomi
- **Bruker:** [[leveranse]]
- **Gir:** [[faktura]], [[fakturalinje]]
- **Neste:** b1

### b1 Er hele ordren levert og fakturert?
- **Aktør:** Økonomi
- **Regel:** Ordren er ferdig når alle ordrelinjene er levert og fakturert.
- **Neste:** ja → b2; nei → s3

### b2 Vil kunden returnere varer?
- **Aktør:** Kundesenter
- **Regel:** Returer håndteres og krediteres i en egen prosess.
- **Neste:** nei → r1; ja → [[retur_fra_kunde]]

## Resultater

### r1 Ordre fakturert
Alle leverte varer på ordren er fakturert.
- **Hendelse:** [[faktura]]

## Åpne spørsmål

- Utkast. Steg, aktører og begreper må bekreftes av eier. Aktørene er foreslått ut fra beskrivelsen.
- Skal tilbud, før kunden har bekreftet, være en del av prosessen?
- Kan en ordre kanselleres eller avvises? I så fall trengs et eget resultat.
- Hvor hører reklamasjon (feil eller skade) hjemme? Retur er flyttet til [[retur_fra_kunde]].
