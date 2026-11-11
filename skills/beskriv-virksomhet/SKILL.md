---
name: beskriv-virksomhet
description: Beskriver virksomheten selv på én side i begrepskatalogen. Hva den gjør, hvordan den tjener penger eller finansieres, marked og kunder, geografi, eierskap og selskapsform. Gir sammenhengen begrepene skal forstås i. Bruk når brukeren vil beskrive eller oppdatere virksomheten, eller etter oppstart av en ny katalog, f.eks. "beskriv virksomheten", "hva driver vi med", "forretningsmodellen vår", "define business", "virksomhetsbeskrivelse".
---

# Beskrive virksomheten

Du hjelper brukeren å beskrive virksomheten på én side (`type: virksomhet`). Siden er sammenhengen alle
begrepene skal forstås i: hva virksomheten gjør, hvordan den tjener penger, hvem den er til for og hva
slags virksomhet den er. Snakk norsk.

Les disse før du begynner, hvis du ikke allerede har gjort det i denne samtalen:

- `${CLAUDE_PLUGIN_ROOT}/maler/virksomhet.md`: malen. Felt og seksjoner er faste.
- `${CLAUDE_PLUGIN_ROOT}/veiledning/forretning-vs-system.md`: siden skal være fri for systemord.
- `${CLAUDE_PLUGIN_ROOT}/kontekst/sider.md`: hvordan du finner sider, og hvor nye sider skal ligge.

Still **ett eller noen få spørsmål om gangen**, med vanlige ord. Foreslå svar når du kan utlede dem fra
det brukeren allerede har sagt, og la brukeren bekrefte. Ikke dikt opp. Det du ikke vet, går i
**Åpne spørsmål**, og da blir `status: utkast`.

## 1. Finnes siden?

```sh
grep -rl --include='*.md' "^type: virksomhet$" .
```

Finnes den, les den og gå til *Oppdatere* under.

## 2. Spør seksjon for seksjon

Følg seksjonene i malen. Kommentarene der gir eksempler på hva du kan spørre om.

1. **Hva virksomheten gjør:** *"Hvordan ville du forklart til en ny kollega hva dere driver med?"*
   Lag `kortdefinisjon` (én setning) av svaret.
2. **Hvordan virksomheten tjener penger:** *"Hva betaler kundene for? Hva er den største
   inntektskilden?"* For offentlige og ideelle virksomheter: *"Hvordan finansieres dere?"*
3. **Marked og kunder:** hvem kundene er, og om virksomheten er lokal, regional, nasjonal eller global.
4. **Eierskap og selskapsform:** privat, børsnotert, statlig eid, offentlig etat, ideell, del av et konsern …
5. **Rammebetingelser** (valgfri): spør bare om det er noe som former hvordan virksomheten drives,
   som regulering eller sesong.

**Hold deg til virksomheten.** Glir svarene over i domener, prosesser, systemer, kanaler eller
måltall, noter dem og si at de hører hjemme på egne sider. Ikke skriv dem på denne siden. Ta dem med
som forslag til neste steg i oppsummeringen.

Systemnavn hører ikke hjemme her. Avdelingsnavn bare når de sier noe om virksomheten, ikke om hvem
som gjør hva.

## 3. Skriv, les over, oppsummer

1. Skriv `virksomhet.md` etter malen, der `sider.md` sier at nye sider skal ligge. Står det ikke noe
   om virksomhetssiden i `CLAUDE.md`, legg den øverst i katalogen. Ta bort alle kommentarer, og
   **Rammebetingelser** og **Åpne spørsmål** hvis de er tomme. `sist_oppdatert` = dagens dato.
   Historikk: én rad "Opprettet".
2. Status: `godkjent` bare hvis brukeren sier at ledelsen eller eier har godkjent beskrivelsen. Ellers
   `til_godkjenning`, eller `utkast` hvis det finnes åpne spørsmål.
3. Les siden over som beskrevet i `sider.md`.
4. Vis en kort oppsummering av siden, og forslagene til neste steg: domener (skillen `beskriv-domene`),
   begreper (`beskriv-begrep`) og prosesser (`beskriv-prosess`) som kom opp underveis.

## Oppdatere

1. Les siden og vis brukeren `kortdefinisjon` og overskriftene med en kort oppsummering.
2. Spør hva som skal endres. Avklar om virksomheten faktisk har **endret seg** (ny eier, nytt marked,
   ny inntektsmodell) eller om bare **formuleringen** blir bedre:
   - Virksomheten har endret seg: oppdater, og legg til en rad i **Historikk** (dato, hva, hvem som besluttet).
   - Bare formulering: ingen ny historikkrad.
3. Oppdater `sist_oppdatert`, les over siden, og oppsummer endringen.

Aldri endre `id`. Det finnes bare én virksomhetsside.
