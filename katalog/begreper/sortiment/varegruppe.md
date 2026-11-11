---
id: varegruppe
navn: Varegruppe
type: dimensjon
domene: sortiment
kortdefinisjon: Hovedinndelingen av sortimentet som brukes i innkjøp, lager og salg.
synonymer: [produktgruppe, kategori, product group]
status: godkjent
eier: Kategoriavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-11
systemer: ["[[erp]]"]
beskriver: ["[[vare]]"]
dimensjonstype: kategori
---
# Varegruppe

## Definisjon

Hovedinndelingen av sortimentet. Hver [[vare]] tilhører nøyaktig én varegruppe.
Inndelingen er den samme i innkjøp, lager og salg.

## Gyldige verdier

- `ror_og_deler`: rør, rørdeler, koblinger og festemateriell
- `sanitar`: servanter, toaletter, dusjer og blandebatterier
- `varme`: varmepumper, varmtvannsberedere, radiatorer og gulvvarme
- `vann_og_avlop`: utvendige vann- og avløpsprodukter, kummer og pumper
- `verktoy`: verktøy og forbruksmateriell

## Systemrepresentasjon

### erp

- **Representasjon:** Øverste nivå i varetreet, som har tre nivåer.
- **Avvik fra forretningsdefinisjon:** Ingen kjente. De to nederste nivåene er ikke en del av dette begrepet.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Kategoriledelsen |
| 2026-11-11 | Flyttet fra domenet kjerne til innkjop. Definisjonen er uendret | … |
| 2026-11-11 | Flyttet fra domenet innkjop til sortiment. Definisjonen er uendret | … |
