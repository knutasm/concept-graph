---
name: domene
description: Veileder brukeren gjennom å opprette, avgrense eller se over et domene (et fagområde med eget språk) i begrepskatalogen. Domenetype, eier, avgrensning mot nabodomener, og om begrepene ligger i riktig domene. Bruk når brukeren vil lage et nytt domene, flytte grenser, rydde i domenene eller vurdere koblingen mellom dem, f.eks. "nytt domene", "hvor hører dette hjemme", "se over domenegrensene", "domenekartet", "bounded context".
---

# Opprette, avgrense eller se over et domene

Du hjelper brukeren å beskrive et domene: et område av virksomheten med sitt eget språk, der
begrepene henger tett sammen og én avdeling har ansvaret. Resultatet er
`katalog/begreper/<id>/_domene.md`. Snakk norsk.

Les disse før du begynner, hvis du ikke allerede har gjort det i denne samtalen:

- `katalog/maler/domene.md`: malen. Felt og seksjoner er faste.
- `katalog/veiledning/domener.md`: domenetyper, delte begreper og kobling mellom domener.

Still **ett eller noen få spørsmål om gangen**. Foreslå svar når du kan utlede dem, og la
brukeren bekrefte. Ikke dikt opp grenser eller eiere. Det du ikke vet, går i **Åpne spørsmål**.

## 1. Søk først

```sh
grep -A10 "^## Domener" katalog/INDEKS.md
cat katalog/begreper/*/_domene.md
```

- **Dekkes området av et domene som finnes?** Da trengs det ikke et nytt. Kanskje avgrensningen
  bare må utvides. Gå til *Se over* under.
- **Nytt område?** Gå videre.

## 2. Problemområde og evner

Spør: *"Hva må virksomheten kunne gjøre her? Hvilke prosesser hører til?"*

- Et domene er et **problemområde**, ikke en avdeling eller et system. Test: *"Ville området
  fortsatt finnes hvis vi omorganiserte, eller byttet systemer?"*
- Se hvilke prosesser som finnes (`grep -h "^domene:" katalog/prosesser/*.md`), og hvilke som hører hit.
- Lag `navn` og `id` (små bokstaver, `_`, æ→ae, ø→o, å→aa). `beskrivelse` er én setning.

## 3. Domenetype

Spør: *"Er dette det som gjør oss unike, noe vi må gjøre for å drive, eller noe alle gjør likt?"*
Foreslå én av `kjerne`, `stottende`, `generisk`, og forklar konsekvensen
(se tabellen i `katalog/veiledning/domener.md`): kjernedomener trenger de grundigste
definisjonene, generiske bør vise til ekstern standard i stedet for å finne opp egne.

Det finnes ikke noe felles domene for delte begreper. Brukes et begrep av mange domener, eies det
likevel av ett: domenet der det oppstår.

## 4. Avgrensning

Spør: *"Hva hører hjemme her, og hva hører til nabodomenene?"*

- Skriv **Hører hjemme her** og **Hører ikke hjemme her**, med henvisning til nabodomenet.
- Oppdater nabodomenets `_domene.md` hvis grensen mot det nye domenet bør nevnes der også.
- **Samme ord, ulik betydning:** spør om nøkkelordene i domenet brukes i andre domener med en annen
  betydning. Da trengs to begreper med `forveksles_med` (se `katalog/veiledning/godt-begrep.md`).

## 5. Eier

En avdeling eller rolle, ikke en person. Eieren godkjenner begrepene i domenet.

## 6. Se over et domene som finnes

Når brukeren vil vurdere grensene, eller etter at et nytt domene er laget:

1. Les **Domenekart** og avsnittet for domenet i `katalog/OVERSIKT.md` ("Bruker fra andre domener").
2. For de sterkeste koblingene: finn begrepene som skaper dem, og les relasjonene deres:
   ```sh
   grep -l "\[\[<id>\]\]" katalog/begreper/<domene>/*.md
   ```
3. Kjør `uv run scripts/valider.py` og se etter advarsler om eierskap ("oppstår i … men ligger i …").
4. Spør for hvert funn: *"Ligger begrepet i riktig domene, eller er grensen trukket feil?"*
   Mange koblinger begge veier mellom to domener er det sterkeste signalet.
5. Flytte et begrep: flytt filen til ny mappe og endre `domene`. Aldri endre `id`. Legg en rad i
   **Historikk**. Spør hvem som besluttet det.

## 7. Skriv, valider, oppsummer

1. Skriv `katalog/begreper/<id>/_domene.md` etter malen. Ta bort alle kommentarer.
2. Kjør `uv run scripts/valider.py`. Rett alle **FEIL**. Gå gjennom **ADVARSLER** med brukeren.
3. Vis en kort oppsummering: navn, domenetype med begrunnelse, eier, avgrensning, prosessene som
   hører til, funn fra gjennomgangen, åpne spørsmål.

Aldri endre `id` på et domene, og aldri slett et domene som har begreper.
