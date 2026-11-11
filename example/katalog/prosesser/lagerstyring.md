---
id: lagerstyring
type: prosess
navn: Lagerstyring
domene: logistikk
kortdefinisjon: Å holde riktig beholdning av varer på hvert lager, fra varene mottas til de leveres ut.
synonymer: [beholdningsstyring, inventory management]
status: utkast
eier: Logistikkavdelingen
sist_oppdatert: 2026-11-10
begreper: ["[[lager]]", "[[vare]]", "[[varemottak]]", "[[leveranse]]"]
---
# Lagerstyring

## Formål

Virksomheten må kunne holde nok av hver [[vare]] på hvert [[lager]] til å levere uten restordre, uten
å binde mer kapital enn nødvendig.

## Avgrensning

- **Starter når:** Løpende. Beholdningen øker ved [[varemottak]] og minker ved [[leveranse]]r.
- **Ferdig når:** Beholdningen er vurdert, nødvendig påfylling er bestilt, og beholdningen er avstemt.
- **Utenfor:** Selve bestillingen og mottaket (se [[innkjop_til_mottak]]) og utleveringen (se [[plukk_og_levering]]).

## Aktører

| Aktør | Ansvar i prosessen |
|---|---|
| Lager | Følger opp, teller og avstemmer beholdningen |
| Innkjøp | Avgjør påfylling |

## Steg

### s1 Følge opp beholdningen
Beholdningen øker når varer mottas og minker når varer plukkes til en leveranse.
- **Aktør:** Lager
- **Bruker:** [[lager]], [[vare]], [[varemottak]], [[leveranse]]
- **Neste:** b1

### b1 Trengs påfylling?
- **Aktør:** Innkjøp
- **Regel:** Ikke avklart. Se Åpne spørsmål.
- **Neste:** ja → [[innkjop_til_mottak]]; nei → s2

### s2 Telle og avstemme beholdningen
- **Aktør:** Lager
- **Bruker:** [[lager]], [[vare]]
- **Neste:** r1

## Resultater

### r1 Beholdning avstemt
Den telte beholdningen stemmer med den registrerte.

## Åpne spørsmål

- Utkast. Steg, aktører og begreper må bekreftes av eier. Aktørene er foreslått ut fra beskrivelsen.
- Prosessen er løpende. Hva starter én gjennomgang (fast intervall, en terskel, en hendelse), og er
  "beholdning avstemt" riktig resultat?
- Hva er regelen for påfylling (bestillingspunkt, minimumsbeholdning)?
- Ingen av begrepene har relasjoner til hverandre i katalogen ennå. Trengs det en entitet for
  lagerplassering (vare på lager)?
- Hører vareflytting mellom lagre med her?
