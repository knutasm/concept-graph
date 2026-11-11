---
id: innkjop_til_mottak
navn: Innkjøp til mottak
domene: innkjop
kortdefinisjon: Fra vi bestiller varer hos en leverandør til varene er mottatt og kontrollert.
synonymer:
  - purchase to receipt
  - procure to pay
status: utkast
eier: Innkjøpsavdelingen
sist_oppdatert: 2026-11-10
utloser: "[[innkjopsordre]]"
begreper:
  - "[[leverandor]]"
  - "[[innkjopsordre]]"
  - "[[varemottak]]"
  - "[[vare]]"
  - "[[lager]]"
---
# Innkjøp til mottak

## Formål

Virksomheten må kunne skaffe varer fra leverandører, slik at vi har det kundene trenger på lager eller
kan få det levert direkte til kunden.

## Avgrensning

- **Starter når:** Vi sender en [[innkjopsordre]] på [[vare]]r til en [[leverandor]].
- **Ferdig når:** Alle varene er mottatt og kontrollert i ett eller flere [[varemottak]], på et av våre
  [[lager]] eller hos kunden ved direktelevering.
- **Utenfor:** Vurderingen av hva som skal bestilles (se [[lagerstyring]]).

## Aktører

| Aktør | Ansvar i prosessen |
|---|---|
| Innkjøp | Bestiller og følger opp |
| Leverandør | Bekrefter og leverer |
| Lager | Tar imot og kontrollerer varene |
| Kunde | Tar imot varer ved direktelevering |

## Steg

### s1 Sende innkjøpsordre
- **Aktør:** Innkjøp
- **Bruker:** [[leverandor]], [[vare]]
- **Gir:** [[innkjopsordre]]
- **Neste:** s2

### s2 Bekrefte leveringsdato
- **Aktør:** Leverandør
- **Bruker:** [[innkjopsordre]]
- **Neste:** b1

### b1 Skal varene til vårt lager?
- **Aktør:** Innkjøp
- **Regel:** Varene går til et av våre lagre, med mindre innkjøpsordren gjelder direktelevering til kunden.
- **Neste:** ja → s3; nei, direktelevering → s4

### s3 Motta og kontrollere varer på lager
- **Aktør:** Lager
- **Bruker:** [[innkjopsordre]], [[lager]]
- **Gir:** [[varemottak]]
- **Neste:** b2

### s4 Motta varer hos kunden
- **Aktør:** Kunde
- **Bruker:** [[innkjopsordre]]
- **Gir:** [[varemottak]]
- **Neste:** b2

### b2 Er alle varene mottatt?
- **Aktør:** Innkjøp
- **Regel:** Innkjøpsordren er ferdig når alle linjene er mottatt og kontrollert.
- **Neste:** ja → r1; nei → b1

## Resultater

### r1 Varer mottatt
Alle varene på innkjøpsordren er mottatt og kontrollert.
- **Hendelse:** [[varemottak]]

## Åpne spørsmål

- Utkast. Steg, aktører og begreper må bekreftes av eier. Aktørene er foreslått ut fra beskrivelsen.
- Varemottak har ingen relasjon til lager i katalogen ennå. Skal det legges til?
- Hører betaling av leverandørfakturaen med i prosessen?
- Hvem kontrollerer og registrerer mottaket ved direktelevering: kunden, eller vi?
- Hva skjer med avvik i mottaket (feil vare, skade, mangler)? Trengs et eget resultat?
