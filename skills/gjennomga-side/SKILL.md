---
name: gjennomga-side
description: Gjennomgår et begrep eller en prosess som en fagekspert har skrevet for hånd, finner mangler og stiller oppklaringsspørsmål før siden rettes. Bruk når brukeren vil se over, gjennomgå, kvalitetssikre eller reviewe en side i katalogen, f.eks. "se over begrepet X skrev", "gjennomgå ordreinngang", "review denne siden", "sjekk de nye sidene", "manuelt skrevet begrep".
---

# Gjennomgå en manuelt skrevet side

En fagekspert har skrevet et begrep eller en prosess selv. Du finner det som mangler eller er uklart,
stiller oppklaringsspørsmål og retter siden. Snakk norsk.

Denne skillen bestemmer **hvordan gjennomgangen gjøres**. **Hva som skal spørres om og hvordan siden
skal se ut**, står i skillen for typen. Les den før du begynner, hvis du ikke allerede har gjort det i
denne samtalen:

- Begrep: `${CLAUDE_PLUGIN_ROOT}/skills/beskriv-begrep/SKILL.md`, med lesestoffet den lister opp (mal og veiledning).
- Prosess: `${CLAUDE_PLUGIN_ROOT}/skills/beskriv-prosess/SKILL.md`, med lesestoffet den lister opp.
- Begge: sjekklisten i `${CLAUDE_PLUGIN_ROOT}/veiledning/godt-begrep.md`, og
  `${CLAUDE_PLUGIN_ROOT}/kontekst/sider.md` for hvordan du finner sider.

Domener dekkes ikke her. Bruk skillen `beskriv-domene`.

## 1. Finn siden

Bruk stien brukeren oppgir. Er det ikke oppgitt noen, vis nye og endrede sider og la brukeren velge:

```sh
git status --porcelain -- '*.md'
git diff --name-only main -- '*.md'
```

Ta bare med sidene som er begreper eller prosesser (se `type` i frontmatter).

Gjennomgå én side om gangen. Har brukeren valgt flere, ta dem etter hverandre.

## 2. Sjekk mot malen

Les siden over som beskrevet i `sider.md`, og noter det som avviker fra malen.

## 3. Faglig sjekk

Gå gjennom siden etter stegene i skillen for typen, som om du skulle skrevet den selv, og noter avvik.
For et begrep betyr det:

- **Søk (steg 1):** Finnes begrepet fra før under et annet navn, eller som synonym? Brukes ordet i et
  annet domene med en annen betydning?
- **Navn, type og domene (steg 2):** Er typen riktig? Ligger en entitet eller hendelse i domenet der den
  oppstår?
- **Definisjonen (steg 3):**
  - Er forretningsdelen fri for systemord (se `${CLAUDE_PLUGIN_ROOT}/veiledning/forretning-vs-system.md`)?
  - Starter den med overbegrepet, er den presis, og unngår den å være sirkulær?
  - Er grensetilfellene dekket?
- **Typefelt (steg 4):** For måltall: alle fem feltene, og stemmer **Beregning** med dem?
- **Relasjoner (steg 5):** Mangler det relasjoner til begreper som finnes? Peker relasjonene på
  begreper som ikke finnes?
- **Systemrepresentasjon (steg 6):** Har hvert system en avvikslinje? Er `kilde` satt der den trengs?
- **Status:** Stemmer statusen med **Åpne spørsmål**?

For en prosess bruker du stegene i prosess-skillen på samme måte.

## 4. Vis funnene

Vis en kort liste i tre grupper, med én linje per funn:

- **Må rettes:** brudd på malen, og lenker til sider som ikke finnes.
- **Må avklares:** det som krever svar fra fagsiden (definisjon, regler, typevalg, avvik).
- **Forslag:** det som kan gjøres bedre, men ikke er feil.

Er siden god, si det kort, og hopp til steg 7.

## 5. Rett det mekaniske

Rett det som ikke endrer innholdet, med en gang. Det gjelder rekkefølgen på felt og seksjoner,
lenkeformatet (`[[id]]`), lister som er brutt over flere linjer, og kommentarer fra malen som er blitt
stående. Si kort hva du rettet.

## 6. Still spørsmål

Gå gjennom **Må avklares** og **Forslag**. Still **ett eller noen få spørsmål om gangen**, formulert som i
steg 3–6 i skillen for typen. Foreslå svar når du kan utlede dem. Rett siden etter hvert svar.

- **Behold forfatterens formuleringer** når de holder mål. Siden er deres.
- **Systemtekst over `## Systemrepresentasjon`** slettes ikke. Flytt den til riktig system, og spør hva
  regelen betyr uavhengig av systemet.
- **Ikke dikt opp.** Kan ikke brukeren svare, går spørsmålet i **Åpne spørsmål**.

Status og historikk:

- Løft aldri siden til `godkjent`, med mindre brukeren er eier eller sier at eier har godkjent.
- Står det noe under **Åpne spørsmål**, er statusen `utkast`. Ellers beholdes statusen, eller den settes
  til `til_godkjenning`.
- Mangler historikken raden «Opprettet», legg den til.
- Gjennomgangen gir ingen ny historikkrad. Unntaket er når **betydningen** endres, og da gjelder reglene
  for oppdatering i skillen for typen.

## 7. Les over og oppsummer

1. Les over siden igjen som i steg 2, og rett det som gjenstår.
2. Oppsummer kort:
   - hva som ble rettet
   - hva som ble avklart
   - hva som står åpent, og hvilken status siden har
3. Kunne ikke brukeren svare på noe, gi en kort liste med **spørsmål til forfatteren**, klar til å sende.
