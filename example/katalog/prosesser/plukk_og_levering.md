---
id: plukk_og_levering
type: prosess
navn: Plukk og levering
domene: logistikk
kortdefinisjon: Fra en ordre er klar til utlevering til kunden har kvittert for varene.
synonymer: [utlevering, fulfillment]
status: utkast
eier: Logistikkavdelingen
sist_oppdatert: 2026-11-10
utloser: "[[ordre]]"
begreper: ["[[ordre]]", "[[ordrelinje]]", "[[vare]]", "[[lager]]", "[[leveranse]]", "[[kunde]]"]
---
# Plukk og levering

## Formål

Virksomheten må kunne få bestilte varer fra lager og ut til kunden, enten kunden henter selv på et
utsalgssted eller vi kjører til byggeplass eller kundens adresse.

## Avgrensning

- **Starter når:** En [[ordre]] skal leveres.
- **Ferdig når:** [[kunde]]n har kvittert for varene.
- **Utenfor:** Bestilling og fakturering (se [[ordre_til_faktura]]), og påfylling av lageret (se [[lagerstyring]]).

## Aktører

| Aktør | Ansvar i prosessen |
|---|---|
| Lager | Plukker, pakker og gjør klar for henting |
| Transport | Kjører varene ut |
| Kunde | Henter eller tar imot, og kvitterer |

## Steg

### s1 Plukke ordrelinjer
Ordrelinjene plukkes fra lageret. Det som ikke er på lager, blir [[restordre]] og leveres senere.
- **Aktør:** Lager
- **Bruker:** [[ordre]], [[ordrelinje]], [[vare]], [[lager]]
- **Neste:** b1

### b1 Hvordan skal varene leveres?
- **Aktør:** Lager
- **Regel:** Kunden velger henting eller utkjøring når ordren bekreftes.
- **Neste:** utkjøring → s2; henting → s3

### s2 Pakke og kjøre ut varer
- **Aktør:** Transport
- **Bruker:** [[ordre]]
- **Neste:** s4

### s3 Gjøre klar for henting
- **Aktør:** Lager
- **Bruker:** [[ordre]]
- **Neste:** s4

### s4 Kvittere for varene
Kunden kvitterer, og leveransen er gjennomført.
- **Aktør:** Kunde
- **Gir:** [[leveranse]]
- **Neste:** r1

## Resultater

### r1 Varer levert
Kunden har kvittert for varene.
- **Hendelse:** [[leveranse]]

## Åpne spørsmål

- Utkast. Steg, aktører og begreper må bekreftes av eier. Aktørene er foreslått ut fra beskrivelsen.
- Leveranse har ingen relasjon til lager i katalogen ennå. Skal det legges til?
- Er transport en egen enhet hos oss, eller en ekstern fraktfører?
- Hva skjer hvis kunden ikke henter, eller ikke tar imot? Trengs et eget resultat?
- Stemmer regelen for leveringsmåte (valgt når ordren bekreftes)?
