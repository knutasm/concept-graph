---
id: rabatt
navn: Rabatt
type: maaltall
domene: salg
kortdefinisjon: Hvor mye lavere enn listepris kunden ble fakturert, i kroner eksklusiv mva.
synonymer: [kunderabatt, avslag, discount]
status: utkast
eier: Salgsavdelingen
sist_oppdatert: 2026-11-10
systemer: ["[[erp]]"]
avledet_av: ["[[fakturalinje]]", "[[listepris]]"]
aggregering: sum
enhet: NOK
granularitet: "[[fakturalinje]]"
tidsdimensjon: "[[fakturadato]]"
additivitet: additiv
---
# Rabatt

## Definisjon

Summen av forskjellen mellom [[listepris]] og fakturert pris for [[vare]]r solgt til en [[kunde]],
eksklusiv merverdiavgift. Viser hvor mye vi har gitt kundene i avslag. [[omsetning]] er allerede
regnet etter rabatt.

## Forretningsregler

- Måles i perioden fakturaen eller kreditnotaen er utstedt, som [[omsetning]].
- Inkluderer: avtalepriser og rabatter per kunde, [[prosjekt]] eller [[varegruppe]], kampanjerabatter
  og mengderabatter.
- Ekskluderer: kontantrabatt for rask betaling, bonus og etterskuddsrabatt, innkjøpsrabatter fra
  [[leverandor]]er, og linjer for frakt, gebyrer og pant.
- Kreditnotaer trekker rabatten tilbake, med negativt fortegn.

## Beregning

Per [[fakturalinje]]: `(listepris - fakturert pris) × fakturert antall`, summert over alle
fakturalinjer og fordelt på [[fakturadato]]. Kan summeres over tid, kunder, varer og lagre.

Rabatt i prosent er rabatt delt på (omsetning + rabatt). Den er ikke-additiv og skal regnes ut
fra summene, ikke som snitt av prosenter.

## Eksempler

- Listepris 200 kr, kunden fakturert 150 kr, 10 stk: rabatt = 500 kr.
- Kunden fakturert til listepris: rabatt = 0.
- Årsbonus utbetalt til en entreprenør i januar: ikke rabatt.
- Kreditnota for 2 av de 10 stk over: rabatt = −100 kr.

## Avgrensning mot andre begreper

- [[omsetning]]: fakturert beløp etter rabatt. Omsetning + rabatt = salg til listepris.
- Bonus/etterskuddsrabatt: avtalt tilbakebetaling i ettertid, ofte per år. Ikke rabatt (eget begrep, ikke opprettet).
- Innkjøpsrabatt: rabatter vi får fra leverandører. Påvirker [[varekost]], ikke rabatt (eget begrep, ikke opprettet).

## Systemrepresentasjon

### erp

- **Representasjon:** Finnes på fakturalinjene. Ikke kartlagt i detalj.
- **Avvik fra forretningsdefinisjon:** Frakt, gebyrer og pant ligger også som fakturalinjer og må filtreres bort (se [[fakturalinje]]). Ellers ikke kartlagt.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2026-11-10 | Opprettet | Salgsavdelingen |

## Åpne spørsmål

- Gjelder listeprisen på fakturadatoen eller på ordredatoen? Listeprisen kan endres mellom de to.
- Hvordan ligger listepris og rabatt i ERP-et (felt, rabattlinjer, kampanjer), og er det kjente avvik?
- Bekreft synonymene.
