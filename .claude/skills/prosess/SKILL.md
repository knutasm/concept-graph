---
name: prosess
description: Veileder brukeren gjennom å kartlegge eller oppdatere en forretningsprosess (en forretningsevne) i begrepskatalogen. Avgrensning, aktører, steg, beslutninger, resultater, og hvilke entiteter og hendelser som brukes og oppstår. Bruk når brukeren vil beskrive, kartlegge, endre eller rydde i en prosess, en arbeidsflyt eller en evne, f.eks. "kartlegg prosessen", "ny prosess", "prosessflyt", "hvem gjør hva i …", "svømmebaner", "map a business process".
---

# Kartlegge eller oppdatere en prosess

Du hjelper brukeren å beskrive en forretningsprosess som en **evne**: noe virksomheten må kunne
gjøre for å drive. Resultatet er én fil i `prosesser/` der steg, beslutninger og resultater er
strukturerte blokker, slik at et flytskjema med svømmebaner kan lages fra dem senere.
Du skal ikke tegne flytskjemaet. Snakk norsk.

Les disse før du begynner, hvis du ikke allerede har gjort det i denne samtalen:

- `maler/prosess.md`: malen. Felt, seksjoner, blokkformat og rekkefølge er faste.
- `veiledning/prosesser.md`: hvordan steg, beslutninger og resultater skrives.
- `veiledning/begrepstyper.md`: forskjellen på entitet og hendelse.

Still **ett eller noen få spørsmål om gangen**. Foreslå svar når du kan utlede dem (fra
eksisterende begreper og prosesser, fra det brukeren allerede har sagt), og la brukeren bekrefte.
Ikke dikt opp steg, aktører eller regler. Det du ikke vet, går i **Åpne spørsmål**, og da blir
`status: utkast`.

## 1. Søk først

```sh
grep -A20 "^## Prosesser" INDEKS.md
grep -rli "<ord>" prosesser
```

- **Finnes prosessen?** Les filen og gå til *Oppdatere* under.
- **Overlapper den en annen?** Spør om den nye er en delprosess, eller om grensen skal flyttes.
  Delprosesser kobles med `- **Neste:** [[prosess_id]]` og nevnes under **Utenfor**.
- **Ikke funnet?** Gå videre.

## 2. Evne og avgrensning

Spør: *"Hva må virksomheten kunne gjøre her? Hvorfor er det viktig?"*

- Formuler evnen som **verb + objekt** ("Levere bestilte varer til kunden"). Den går i **Formål**,
  sammen med hvorfor virksomheten trenger den. Lag `navn` og `id` (små bokstaver, `_`, æ→ae, ø→o, å→aa).
- **Avgrensning:** spør etter *starter når*, *ferdig når* og *utenfor*. Grensene settes først, så
  prosessen ikke vokser underveis. Det som er utenfor, hører ofte til en nabo-prosess, så lenk til den.
- **Utløser:** hvilken entitet eller hendelse starter prosessen? Den går i `utloser`.
- **Domene og eier:** foreslå domenet som eier evnen, og eieren (en avdeling, ikke en person).

## 3. Hovedløpet

Spør: *"Hva skjer når alt går som det skal, fra start til slutt?"*

- Få 3–10 steg, hvert som verb + objekt. Er brukeren på vei inn i unntak, noter dem og si at dere
  tar dem etterpå. Folk blander gjerne inn unntakene, og hovedløpet først gir en ren ryggrad.
- For hvert steg: *"Hvem gjør dette?"* Svarene blir **Aktører** (rolle eller enhet, ikke person) med
  en kort ansvarsbeskrivelse. Bruk samme navn hver gang.
- Over 10 steg: foreslå å dele opp i delprosesser.

**Pass på system-lekkasje**, som i `begrep`-skillen. "Registrerer i ERP-et", "status settes til 4",
"jobben kjører" beskriver systemet. Si det vennlig, og spør hva som skjer forretningsmessig:
*"Hva betyr det for kunden eller for oss at det skjer?"* → "Kundesenteret bekrefter ordren".
Systemdetaljene hører hjemme under Systemrepresentasjon i begrepene, så tilby å notere dem der.

## 4. Beslutninger og alternative veier

Gå gjennom stegene ett for ett: *"Kan dette gå annerledes? Hva avgjør det?"*

- Hvert valg blir en beslutning `b…` med spørsmålet som tittel, **Regel** (hva som avgjør) og
  **Neste** med etiketter: `ja → s4; nei → r2`.
- Et steg har bare én vei videre. Trengs det et valg, legg inn en beslutning etter steget.
- Er regelen egentlig en klassifisering ("restordre", "aktiv kunde"), sjekk om begrepet finnes,
  og tilby å lage det med `begrep`-skillen.

## 5. Resultater

Spør: *"På hvilke måter kan prosessen ende?"* Ta med de uønskede også (avvist, kansellert, avbrutt).

- Hvert resultat blir `r…` under `## Resultater`, med en **Hendelse** når det finnes en.
- Sjekk at alle veier ender i et resultat eller i en annen prosess. Spør om det som henger.

## 6. Entiteter og hendelser per steg

For hvert steg:

- *"Hva trenger dere for å gjøre dette?"* → **Bruker**
- *"Hva finnes, eller har endret seg, når steget er ferdig?"* → **Gir**

Bare `entitet` og `hendelse` hører hjemme her. Slå opp hvert begrep:

```sh
grep -i "<ord>" INDEKS.md
grep -rli "^synonymer:.*<ord>" begreper
```

For hvert begrep som **ikke finnes**, gi brukeren tre valg:

1. **Lag det nå** med `begrep`-skillen. Fortsett prosessen etterpå.
2. **Lag en stubb** og vent med resten: `status: utkast`, bare påkrevde felt, kort definisjon,
   "Ikke kartlagt." under Systemrepresentasjon, og et punkt under **Åpne spørsmål**. En stubb for en
   `hendelse` trenger også en tidsdimensjon (`dimensjon` med `dimensjonstype: tid` og `beskriver`),
   fordi `tidspunkt` er påkrevd. Finn en eksisterende først, eller lag en stubb for den også.
3. **Ikke et begrep:** nevn det i teksten uten lenke, og skriv det under **Åpne spørsmål**.

Er det et måltall, en dimensjon eller en klassifisering, hører det ikke i blokkene. Nevn det i
teksten med `[[id]]` hvis det finnes.

Alle begreper fra **Bruker**, **Gir**, **Hendelse** og `utloser` skal stå i `begreper` i frontmatter, på én linje.

## 7. Skriv, valider, oppsummer

1. Skriv `prosesser/<id>.md` etter malen. Ta bort alle kommentarer og eksempelblokker.
   `sist_oppdatert` = dagens dato. Id-ene på blokkene: `s1`, `b1`, `r1` …, i flytrekkefølge.
2. Status: `godkjent` bare hvis brukeren er eier eller sier at eier har godkjent. Ellers
   `til_godkjenning`, eller `utkast` hvis det finnes åpne spørsmål.
3. Kjør `uv run scripts/valider.py`. Rett alle **FEIL**. Gå gjennom **ADVARSLER** med brukeren
   (et steg som ikke kan nås eller aldri ender, er nesten alltid et hull i kartleggingen).
4. Vis en kort oppsummering:
   - evnen og avgrensningen
   - aktørene
   - stegene i rekkefølge, med **overleveringene** markert (der aktøren skifter: "s2 Kundesenter → s3 Lager")
   - beslutningene med regel
   - resultatene
   - nye begreper og stubber
   - åpne spørsmål

## Oppdatere en eksisterende prosess

1. Les filen og vis brukeren stegene og resultatene kort.
2. Spør hva som skal endres. Gjør endringen i blokkene, og pass på at **Neste** fortsatt henger
   sammen. Ikke nummerer om id-er, bruk `s2a` for nye steg mellom `s2` og `s3`.
3. Oppdater `begreper` og `utloser` hvis begrepene endres, og `sist_oppdatert`.
4. Se om andre prosesser peker hit: `grep -rl "\[\[<id>\]\]" prosesser`. Nevn dem for brukeren.
5. Kjør valideringen og oppsummer endringen.

Aldri endre `id` på en prosess.
