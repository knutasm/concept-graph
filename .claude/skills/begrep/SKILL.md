---
name: begrep
description: Veileder brukeren gjennom å opprette eller oppdatere et begrep (forretningsbegrep, måltall, dimensjon, entitet, klassifisering) i begrepskatalogen. Bruk når brukeren vil legge til, definere, endre, rydde i eller dokumentere et begrep, et måltall eller et system i katalogen, f.eks. "nytt begrep", "definer aktiv kunde", "oppdater dekningsgrad", "add a glossary term".
---

# Opprette eller oppdatere et begrep

Du hjelper brukeren å skrive en god, konsistent oppføring i begrepskatalogen. Snakk norsk.
Les disse før du begynner, hvis du ikke allerede har gjort det i denne samtalen:

- `katalog/maler/begrep.md`: malen. Felt, seksjoner og rekkefølge er faste.
- `katalog/veiledning/forretning-vs-system.md`: det viktigste du skal passe på.
- `katalog/veiledning/begrepstyper.md` og `katalog/veiledning/relasjoner.md`: gyldige typer og relasjoner.

Still **ett eller noen få spørsmål om gangen**. Foreslå svar når du kan utlede dem (fra
eksisterende begreper, fra det brukeren allerede har sagt), og la brukeren bekrefte. Ikke dikt opp
forretningsregler. Det du ikke vet, går i **Åpne spørsmål**, og da blir `status: utkast`.

## 1. Søk først

Finn ut om begrepet finnes, også under andre navn:

```sh
grep -i "<ord>" katalog/INDEKS.md
grep -rli "synonymer:.*<ord>" katalog/begreper
grep -rli "^navn:.*<ord>" katalog/begreper
```

- **Finnes det?** Les filen og gå til *Oppdatere* under.
- **Finnes noe lignende?** Spør om det er samme begrep (da legger du til synonym) eller et annet
  (da lager du nytt og knytter dem med `forveksles_med`).
- **Finnes ordet i et annet domene?** Spør om det betyr det samme der. Hvert domene har sitt eget
  språk, og samme ord kan bety ulike ting i salg og logistikk. Ulik betydning gir to begreper med
  hver sin id (gjerne et presiserende navn), ordet som synonym på begge, `forveksles_med`, og en
  forklaring under **Avgrensning mot andre begreper** av hvilket domene som mener hva. Lag aldri
  én vag definisjon som skal passe alle. Se `katalog/veiledning/godt-begrep.md`.
- **Ikke funnet?** Gå videre.

## 2. Navn, type og domene

- **Navn:** det virksomheten faktisk kaller det, entall. Lag `id` (små bokstaver, `_`, æ→ae, ø→o, å→aa).
- **Type:** foreslå en type ut fra `katalog/veiledning/begrepstyper.md` og forklar kort hvorfor.
- **Domene:** foreslå blant mappene i `katalog/begreper/` (se `_domene.md` i hver). For entiteter og
  hendelser: velg domenet til prosessen der begrepet **oppstår** (`grep -rl "Gir:\*\*.*\[\[<id>\]\]" katalog/prosesser`).
  Eierskapet følger oppstedet. Nytt domene bare hvis ingen passer, og da bruker du skillen `domene`
  før du fortsetter.
  Hvert begrep har ett domene som eier, også når mange domener bruker det. Det finnes ikke noe
  felles domene for delte begreper: varen eies av sortiment, kalenderen av økonomi, og de andre
  domenene lenker til dem.

## 3. Forretningsdefinisjonen (systemnøytral)

Spør: *"Hva betyr dette for virksomheten? Hvordan ville du forklart det til en ny kollega?"*
Spør også: *"Bruker andre avdelinger ordet? Betyr det det samme for dem?"* (se steg 1).

**Pass på system-lekkasje.** Hvis svaret handler om et system (systemnavn, tabeller, felt,
statuskoder, flagg, "det som ligger i …", "en rad i …"):

1. Si det tydelig, vennlig: *"Dette beskriver hvordan det ser ut i ERP-et. Det tar jeg med under
   Systemrepresentasjon."*
2. Noter det til steg 6.
3. Spør igjen: *"Men hva betyr det uavhengig av system? Hvis vi byttet ut systemet i morgen, hva
   ville fortsatt vært sant?"* Det hjelper ofte å spørre *hvorfor* systemet har den regelen.

Skriv så:

- `kortdefinisjon`: én setning, under 200 tegn.
- **Definisjon**: 1–3 setninger som starter med overbegrepet. Lenk andre begreper med `[[id]]`.
- **Forretningsregler**: spør konkret etter hva som er med og ikke med, tidsvinduer, terskler og
  grensetilfeller. Lag gjerne 2–3 tenkte eksempler og spør "Er dette en X?". Svarene går i **Eksempler**.
- **Synonymer**: spør hvilke andre navn folk bruker, også engelske og forkortelser.

## 4. Typespesifikke spørsmål

- **entitet:** Hva identifiserer en forekomst (med forretningsord)? Hva tilhører den (`tilhorer`)?
  Er den del av noe (`del_av`)?
- **hendelse:** Hvilken dato markerer hendelsen (`tidspunkt`)?
- **maaltall:** gå gjennom alle fem, og forklar hvorfor de betyr noe:
  - `aggregering`: summeres, telles, telles unikt, snitt, eller formel av andre måltall?
  - `grain`: én grunnverdi per hva?
  - `tidsdimensjon`: hvilken dato plasserer tallet i tid? Nevn alternativene (f.eks. ordredato
    eller fakturadato) og at de gir ulike tall.
  - `additivitet`: kan tallet for et kvartal regnes ut som summen av tre måneder? Hvis ikke, er det
    `semi_additiv` (beholdninger, øyeblikksbilder) eller `ikke_additiv` (andeler, snitt, unike).
  - `enhet`, og **Beregning**: formelen med begreps-id-er, aldri tabeller eller kolonner.
- **dimensjon:** `dimensjonstype`. Hva beskriver den (`beskriver`)? For kategorier: hvilke verdier
  finnes (**Gyldige verdier**)?
- **klassifisering:** Hva deles inn (`er_en`)? Regelen går i **Forretningsregler**.

`grain`, `tidsdimensjon` og `tidspunkt` må peke på begreper som finnes, av riktig type.

## 5. Relasjoner

Foreslå relasjoner ut fra det som er sagt, og bruk bare typene i `katalog/veiledning/relasjoner.md`.
Hver relasjonstype er et eget felt med lenker: `er_en: ["[[kunde]]"]`. Det samme gjelder `grain`,
`tidsdimensjon` og `tidspunkt`: `grain: "[[fakturalinje]]"`.
Alle mål må finnes. Mangler et begrep, tilby å lage det som stubb: `status: utkast`, bare påkrevde
felt, kort definisjon, og "Ikke kartlagt." under Systemrepresentasjon. Spør om noe ofte forveksles
med dette begrepet (`forveksles_med` + seksjonen **Avgrensning mot andre begreper**).

For `entitet` og `hendelse`: spør hvilke forretningsprosesser begrepet inngår i (se `katalog/prosesser/` og
tabellen Prosesser i `katalog/INDEKS.md`). Legg `"[[<id>]]"` til i prosessens `begreper`, og oppdater
prosessens `sist_oppdatert`. Spør også hvilke steg begrepet brukes i (**Bruker**) eller oppstår i
(**Gir**). Finnes ikke prosessen, tilby å kartlegge den med skillen `prosess` når begrepet er ferdig.

## 6. Systemrepresentasjon

Spør hvilke systemer begrepet finnes i. Systemene må finnes i `katalog/systemer/` (se `katalog/INDEKS.md`). Er et
system nytt, lag det fra `katalog/maler/system.md` med et generisk id (`erp`, `crm`, …).

For hvert system, én `### <system-id>` med:

- **Representasjon:** hvor og hvordan det ligger (her er tabeller, felt og statuskoder velkomne).
- **Identifikasjon:** for entiteter.
- **Avvik fra forretningsdefinisjon:** spør aktivt: *"Er det noe systemet tar med som egentlig ikke
  hører med, eller omvendt?"* Skriv "Ingen kjente" hvis det ikke er noe.

Ta med det du noterte i steg 3. Alle system-id-er må også stå i `systemer:` i frontmatter.
Har brukeren ingen systeminformasjon, skriv "Ikke kartlagt." og la `systemer: []` stå tom.

**Kilde** (entitet, hendelse, dimensjon): spør *"I hvilket system oppstår og endres dette? Hvor
retter dere det hvis det er feil?"* Svaret går i `kilde`. De andre systemene er kopier. Forklar
hvorfor: en semantisk modell leser fra kilden, og bruker kopier bare med avvikene deres. Et
datavarehus er nesten aldri kilden for en entitet. Måltall og klassifiseringer har ingen kilde,
fordi filtre, koblinger og summeringer ikke skaper nye fakta. Sjekk at `Formål` i systemfilen
stemmer. Er det uklart, la `kilde` stå tom og legg spørsmålet i **Åpne spørsmål**.

## 7. Skriv, valider, oppsummer

1. Skriv `katalog/begreper/<domene>/<id>.md` etter malen. Ta bort alle kommentarer, felt og seksjoner som
   ikke gjelder typen. Behold seksjonsrekkefølgen. `sist_oppdatert` = dagens dato.
   Historikk: én rad "Opprettet".
2. Status: `godkjent` bare hvis brukeren er eier eller sier at eier har godkjent. Ellers
   `til_godkjenning`, eller `utkast` hvis det finnes åpne spørsmål.
3. Kjør `uv run scripts/valider.py`. Rett alle **FEIL**. Gå gjennom **ADVARSLER** med brukeren.
   Advarsler om systemnavn eller tekniske ord i forretningsdelen skal nesten alltid rettes.
4. Vis en kort oppsummering: definisjon, type og typefelt, relasjoner, kilde og systemer med avvik,
   åpne spørsmål.

## Oppdatere et eksisterende begrep

1. Les filen og vis brukeren gjeldende definisjon.
2. Spør hva som skal endres, og avklar om **betydningen** endres eller bare **formuleringen**:
   - Betydningen endres: oppdater, sett ny `gyldig_fra`, og legg til en rad i **Historikk**
     (dato, hva som endret seg, hvem som besluttet det). Spør hvem som besluttet.
   - Bare formulering: ingen ny historikkrad.
3. Se om andre begreper påvirkes: `grep -rl "\[\[<id>\]\]\|\b<id>\b" katalog/begreper`. Nevn dem for brukeren.
4. Oppdater `sist_oppdatert`, kjør valideringen, og oppsummer endringen.

Aldri endre `id`, og aldri slett et begrep. Bruk `status: utfaset` + `erstattet_av`.
