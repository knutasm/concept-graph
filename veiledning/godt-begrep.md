# Slik skriver du et godt begrep

En god oppføring lar en ny kollega, eller en maskin, forstå begrepet riktig uten å spørre noen.
Bruk [malen](../maler/begrep.md), eller enda enklere: be Claude om å "lage et nytt begrep", så
blir du guidet gjennom det (skillen `begrep`).

## Sjekkliste

- [ ] **Søkt først.** Finnes begrepet allerede, kanskje under et annet navn? Sjekk [INDEKS.md](../INDEKS.md) og synonymer.
- [ ] **Ett begrep per fil.** Har begrepet to betydninger, er det to begreper.
- [ ] **Definisjonen er systemnøytral.** Se [forretning-vs-system.md](forretning-vs-system.md).
- [ ] **Definisjonen starter med overbegrepet.** "En [[kunde]] som …", "Summen av …".
- [ ] **Grensetilfellene er avklart.** Hva er med, hva er ikke med?
- [ ] **Riktig type, og typefeltene er fylt ut.** Se [begrepstyper.md](begrepstyper.md).
- [ ] **For måltall: grain, tidsdimensjon og additivitet er gjennomtenkt.**
- [ ] **Relasjoner til begreper som allerede finnes.** Se [relasjoner.md](relasjoner.md).
- [ ] **Hvert system har en avvikslinje**, også når den er "Ingen kjente".
- [ ] **Eieren er en rolle eller avdeling**, ikke en person.
- [ ] **Historikken er oppdatert** når definisjonen endres.
- [ ] **Valideringen er kjørt:** `uv run scripts/valider.py`.

## Definisjonen

Definisjonen er det viktigste. Den skal være:

| Egenskap | ❌ Dårlig | ✅ Bra |
|---|---|---|
| **Presis**. Én tolkning | "Kunder som handler jevnlig." | "En kunde med minst én bekreftet ordre de siste 12 månedene." |
| **Ikke sirkulær** | "Netto omsetning er omsetningen netto." | "Brutto omsetning fratrukket returer og rabatter." |
| **Systemnøytral** | "Debitorer i ERP-et." | "En person eller virksomhet med minst én bekreftet ordre." |
| **Kort** | Et avsnitt med unntak og historikk | 1–3 setninger. Unntak i Forretningsregler, endringer i Historikk |
| **Positiv** | "Alt som ikke er en kreditnota." | Si hva det *er*. Bruk Forretningsregler for hva det ikke er |
| **Forståelig** | Fagsjargong og forkortelser uten forklaring | Skriv for en ny kollega. Forklar forkortelser første gang |

`kortdefinisjon` i frontmatter er én setning som oppsummerer definisjonen. Den vises i indeksen og
i søkeresultater, så den må kunne stå alene.

## Navn, id og synonymer

- **`navn`** er det virksomheten faktisk kaller begrepet, i entall: "Ordre", ikke "Ordrer".
- **`id`** er navnet med små bokstaver og `_`, uten æøå (æ→ae, ø→o, å→aa): `maaned`, `okonomi`.
  Ikke endre id-en senere. Andre begreper peker på den.
- **`synonymer`** er alle andre navn folk bruker, også engelske og forkortelser. Det er dem folk
  søker etter. Hvis et synonym egentlig er et annet begrep, lag begrepet og bruk `forveksles_med`.

## Forretningsregler

Punktliste med presise regler. Gode regler svarer på:

- **Hva er med, og hva er ikke med?** ("Inkluderer: …", "Ekskluderer: …")
- **Hvilket tidsvindu og hvilke terskler gjelder?** ("siste 12 måneder", "over 0 kr")
- **Når teller noe?** ("i perioden kreditnotaen er utstedt")
- **Hvordan håndteres grensetilfeller?** (kansellering, interne kjøp, prøveperioder)

## Måltall

For måltall avgjør disse feltene om tallene blir riktige:

1. **Grain:** Hva beregnes én grunnverdi for? Faktura, ordrelinje, abonnement?
2. **Tidsdimensjon:** Hvilken dato plasserer tallet i tid? Ordredato og fakturadato gir ulike månedstall.
3. **Additivitet:** Kan tallet summeres over tid? Beholdninger og MRR kan ikke det.
4. **Beregning:** Avledede måltall skrives som formel med begreps-id-er: `brutto_omsetning - returer - rabatt`.
   Aldri tabeller eller kolonner.

## Endre et begrep

- **Endres betydningen?** Oppdater Definisjon/Forretningsregler, sett ny `gyldig_fra`, og legg til
  en rad i **Historikk** med hva som endret seg og hvem som besluttet det. Historiske tall er
  beregnet etter den gamle definisjonen, og historikken er det som forklarer bruddet.
- **Bare bedre formulering?** Oppdater teksten og `sist_oppdatert`. Ingen ny historikkrad.
- **Begrepet brukes ikke lenger?** Sett `status: utfaset` og `erstattet_av`. Ikke slett filen.

## Status

| Status | Betyr |
|---|---|
| `utkast` | Under arbeid eller ikke bekreftet av eier. Kan brukes, men med forsiktighet |
| `til_godkjenning` | Ferdig skrevet, venter på eier |
| `godkjent` | Bekreftet av eier. Gjeldende definisjon |
| `utfaset` | Brukes ikke lenger. Se `erstattet_av` |
