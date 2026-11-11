---
name: beskriv-domene
description: Veileder brukeren gjennom å opprette, avgrense eller se over et domene (et fagområde med eget språk) i begrepskatalogen. Domenetype, eier, avgrensning mot nabodomener, og om begrepene ligger i riktig domene. Bruk når brukeren vil lage et nytt domene, flytte grenser, rydde i domenene eller vurdere koblingen mellom dem, f.eks. "nytt domene", "hvor hører dette hjemme", "se over domenegrensene", "domenekartet", "bounded context".
---

# Opprette, avgrense eller se over et domene

Du hjelper brukeren å beskrive et domene: et område av virksomheten med sitt eget språk, der
begrepene henger tett sammen og én avdeling har ansvaret. Resultatet er én side med
`type: domene`. Begreper og prosesser hører til domenet gjennom feltet `domene`. Snakk norsk.

Les disse før du begynner, hvis du ikke allerede har gjort det i denne samtalen:

- `${CLAUDE_PLUGIN_ROOT}/maler/domene.md`: malen. Felt og seksjoner er faste.
- `${CLAUDE_PLUGIN_ROOT}/veiledning/domener.md`: domenetyper, delte begreper og kobling mellom domener.
- `${CLAUDE_PLUGIN_ROOT}/kontekst/sider.md`: hvordan du finner sider, og hvor nye sider skal ligge.
- Virksomhetssiden (`type: virksomhet`), hvis den finnes, for sammenhengen begrepene skal forstås i.

Still **ett eller noen få spørsmål om gangen**. Foreslå svar når du kan utlede dem, og la
brukeren bekrefte. Ikke dikt opp grenser eller eiere. Det du ikke vet, går i **Åpne spørsmål**.

## 1. Søk først

```sh
grep -rl --include='*.md' "^type: domene$" . | xargs cat
```

- **Dekkes området av et domene som finnes?** Da trengs det ikke et nytt. Kanskje avgrensningen
  bare må utvides. Gå til *Se over* under.
- **Nytt område?** Gå videre.

## 2. Problemområde og evner

Spør: *"Hva må virksomheten kunne gjøre her? Hvilke prosesser hører til?"*

- Et domene er et **problemområde**, ikke en avdeling eller et system. Test: *"Ville området
  fortsatt finnes hvis vi omorganiserte, eller byttet systemer?"*
- Se hvilke prosesser som finnes, og hvilke som hører hit:
  `grep -rl --include='*.md' "^type: prosess$" . | xargs grep -HE "^(navn|domene):"`
- Lag `navn` og `id` (små bokstaver, `_`, æ→ae, ø→o, å→aa). `beskrivelse` er én setning.

## 3. Domenetype

Spør: *"Er dette det som gjør oss unike, noe vi må gjøre for å drive, eller noe alle gjør likt?"*
Foreslå én av `kjerne`, `stottende`, `generisk`, og forklar konsekvensen
(se tabellen i `${CLAUDE_PLUGIN_ROOT}/veiledning/domener.md`): kjernedomener trenger de grundigste
definisjonene, generiske bør vise til ekstern standard i stedet for å finne opp egne.

Det finnes ikke noe felles domene for delte begreper. Brukes et begrep av mange domener, eies det
likevel av ett: domenet der det oppstår.

## 4. Avgrensning

Spør: *"Hva hører hjemme her, og hva hører til nabodomenene?"*

- Skriv **Hører hjemme her** og **Hører ikke hjemme her**, med henvisning til nabodomenet.
- Oppdater siden til nabodomenet hvis grensen mot det nye domenet bør nevnes der også.
- **Samme ord, ulik betydning:** spør om nøkkelordene i domenet brukes i andre domener med en annen
  betydning. Da trengs to begreper med `forveksles_med` (se `${CLAUDE_PLUGIN_ROOT}/veiledning/godt-begrep.md`).

## 5. Eier

En avdeling eller rolle, ikke en person. Eieren godkjenner begrepene i domenet.

## 6. Se over et domene som finnes

Når brukeren vil vurdere grensene, eller etter at et nytt domene er laget:

1. Finn begrepene i domenet, og hvilke begreper i andre domener de lenker til (relasjoner og lenker i teksten):
   ```sh
   grep -rl --include='*.md' "^domene: <domene>$" .
   ```
   Tell koblingene per nabodomene, begge veier. Mange koblinger til ett nabodomene er verdt å se på.
2. For de sterkeste koblingene: les begrepene som skaper dem, og relasjonene deres.
3. **Eierskap:** for hver entitet og hendelse i domenet, finn prosessene der den oppstår
   (`grep -rl --include='*.md' "Gir:\*\*.*\[\[<id>\]\]" .`). Hører prosessen til et annet domene,
   er det et funn.
4. Spør for hvert funn: *"Ligger begrepet i riktig domene, eller er grensen trukket feil?"*
   Mange koblinger begge veier mellom to domener er det sterkeste signalet.
5. Flytte et begrep: endre `domene`. Ligger sidene i mapper etter domene, spør om filen skal flyttes også.
   Aldri endre `id`. Legg en rad i
   **Historikk**. Spør hvem som besluttet det.

## 7. Skriv, les over, oppsummer

1. Skriv siden etter malen, der `sider.md` sier at nye sider skal ligge. Ta bort alle kommentarer.
2. Les siden over som beskrevet i `sider.md`.
3. Vis en kort oppsummering: navn, domenetype med begrunnelse, eier, avgrensning, prosessene som
   hører til, funn fra gjennomgangen, åpne spørsmål.

Aldri endre `id` på et domene, og aldri slett et domene som har begreper.
