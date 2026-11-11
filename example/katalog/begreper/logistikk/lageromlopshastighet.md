---
id: lageromlopshastighet
navn: Lageromløpshastighet
type: maaltall
domene: logistikk
kortdefinisjon: Hvor mange ganger per år vi selger ut og fyller opp et gjennomsnittlig varelager. Varekost delt på gjennomsnittlig lagerbeholdning.
synonymer: [lageromløp, omløpshastighet, inventory turnover]
status: utkast
eier: Logistikkavdelingen
sist_oppdatert: 2026-11-11
systemer: ["[[datavarehus]]"]
avledet_av: ["[[varekost]]", "[[gjennomsnittlig_lagerbeholdning]]"]
aggregering: ratio
enhet: ganger per år
granularitet: "[[vare]]"
tidsdimensjon: "[[kalenderdag]]"
additivitet: ikke_additiv
---
# Lageromløpshastighet

## Definisjon

Forholdet mellom [[varekost]] og [[gjennomsnittlig_lagerbeholdning]] i en periode, regnet om til
omløp per år. Sier hvor mange ganger i året vi selger ut og fyller opp et gjennomsnittlig varelager.

## Forretningsregler

- Teller og nevner er begge verdsatt til gjennomsnittlig innkjøpskost, så de er sammenlignbare. Derfor
  brukes varekost og ikke [[omsetning]] i telleren.
- Ekskluderer: varekost for direkteleveranser fra leverandør til kunde, fordi de varene aldri har ligget
  på [[lager]].
- Gjennomsnittlig lagerbeholdning er snittet av de daglige beholdningene i perioden (se
  [[gjennomsnittlig_lagerbeholdning]]).
- Tallet annualiseres alltid, slik at perioder av ulik lengde kan sammenlignes.

## Beregning

`(varekost uten direkteleveranser / gjennomsnittlig_lagerbeholdning) × 365 / antall dager i perioden`

Varekost plasseres i tid etter [[fakturadato]] og lagerbeholdningen etter [[beholdningsdato]]. Begge
avgrenses til samme periode i [[kalenderdag]].

**Ikke-additiv:** teller og nevner beregnes først for hele utvalget og perioden, og så deles de.
Omløpet for et år er **ikke** snittet av omløpet for de tolv månedene, og omløpet for to varegrupper er
**ikke** snittet av de to.

## Eksempler

- Varekost for et år er 120 mill., og et gjennomsnittlig varelager er verdt 20 mill. Omløpet blir 6 ganger
  per år, altså omtrent 61 dager på lager.
- Varekost for oktober (31 dager) er 10 mill., og gjennomsnittlig beholdning i oktober er 20 mill.
  Omløpet blir 10 / 20 × 365 / 31 ≈ 5,9 ganger per år.
- En vare som leveres direkte fra leverandør til byggeplass og aldri har vært på lager, er ikke med i
  telleren.

## Avgrensning mot andre begreper

- Lagerdager (365 / lageromløpshastighet): sier hvor mange dagers salg som ligger på lager. Det er samme
  sak sett fra motsatt side, men et annet tall. Høyt omløp gir få lagerdager. Finnes ikke som eget begrep
  ennå.
- [[lagerbeholdning]]: et øyeblikksbilde ved slutten av en dag. Omløpet bruker gjennomsnittet over
  perioden, ikke beholdningen den siste dagen.

## Systemrepresentasjon

### datavarehus

- **Representasjon:** Beregnes i datavarehuset. Ikke kartlagt i detalj.
- **Avvik fra forretningsdefinisjon:** Ikke kartlagt. Se Åpne spørsmål.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2026-11-11 | Opprettet | Logistikkavdelingen |

## Åpne spørsmål

- Skal omløpet kunne brytes ned per [[lager]]? Varekost er knyttet til [[fakturalinje]], og den sier
  ikke hvilket lager varen ble levert fra. Hvordan et salg knyttes til et lager, må avklares.
- Trekker datavarehuset fra direkteleveranser, og annualiserer det tallet, slik definisjonen sier?
