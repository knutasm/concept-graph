---
# ── Felles for alle typer ──────────────────────────────────────────────
id: eksempel_begrep            # = filnavn uten .md. Små bokstaver, a-z 0-9 _, ingen æøå (ae, oe, aa)
navn: Eksempel begrep          # Visningsnavn på vanlig norsk, entall. Overskriften (# ) under skal være lik
type: entitet                  # entitet | hendelse | maaltall | dimensjon | klassifisering
domene: salg                   # id-en til domenet som eier begrepet (siden med type: domene)
kortdefinisjon: Én setning, systemnøytral, under 200 tegn.
synonymer: [annet navn, engelsk navn]   # Hold lista på ÉN linje, så grep viser hele lista
status: utkast                 # utkast | til_godkjenning | godkjent | utfaset
eier: Fagavdeling som eier definisjonen   # En rolle eller avdeling, ikke en person
gyldig_fra: 2026-01-01         # Når gjeldende definisjon trådte i kraft (valgfri)
sist_oppdatert: 2026-01-01
systemer: ["[[erp]]"]          # lenker til system-sider. Hvert system får en ### under Systemrepresentasjon
kilde: "[[erp]]"               # Kun entitet, hendelse og dimensjon (valgfri). Systemet der begrepet oppstår og endres.
                               # Må stå i systemer. De andre systemene er kopier. Påkrevd i praksis når det er flere systemer
# ── Relasjoner ─────────────────────────────────────────────────────────
# Ett felt per relasjonstype, bare de du trenger. Verdiene er lister med Obsidian-lenker
# i anførselstegn, så de blir klikkbare og vises i grafen: ["[[a]]", "[[b]]"]
er_en: ["[[kunde]]"]           # spesialisering: aktiv_kunde er_en kunde
del_av: []                     # helhet/del: ordrelinje del_av ordre
tilhorer: []                   # mange-til-én: ordre tilhorer kunde
avledet_av: []                 # beregnes fra: dekningsbidrag avledet_av omsetning
beskriver: []                  # dimensjon → det den beskriver: ordredato beskriver ordre
forveksles_med: []             # ulike begreper som ofte blandes sammen
se_ogsaa: []
erstattet_av: []               # kun ved status: utfaset

# ── Kun entitet ─────────────────────────────────────────────────────────
identifiseres_ved: kundenummer # Hva virksomheten bruker for å skille én forekomst fra en annen

# ── Kun hendelse ────────────────────────────────────────────────────────
# tidspunkt: "[[ordredato]]"    # lenke til en dimensjon med dimensjonstype: tid
# identifiseres_ved: ...        # valgfri

# ── Kun maaltall ────────────────────────────────────────────────────────
# aggregering: sum              # sum | antall | antall_unike | snitt | min | maks | ratio | formel
# enhet: NOK                    # NOK, antall, prosent, dager …
# granularitet: "[[ordrelinje]]"       # lenke til entitet/hendelse: én verdi beregnes per forekomst av denne
# tidsdimensjon: "[[fakturadato]]"  # lenke til dimensjon med dimensjonstype: tid
# additivitet: additiv          # additiv | semi_additiv (ikke over tid) | ikke_additiv

# ── Kun dimensjon ───────────────────────────────────────────────────────
# dimensjonstype: kategori      # kategori | tid | boolsk | numerisk | tekst
---
# Eksempel begrep

<!--
Slett alle kommentarer og felt/seksjoner som ikke gjelder typen før du lagrer.
Alt OVER "## Systemrepresentasjon" skal være systemnøytralt: ingen systemnavn,
tabeller, felt, statuskoder eller skjermbilder. Testen: ville teksten fortsatt
vært sann om alle systemene ble byttet ut i morgen?
Lenk til andre begreper med [[id]].
-->

## Definisjon

<!-- 1–3 setninger. Hva ER dette for virksomheten? Start med overbegrepet:
"En [[kunde]] som …", "Summen av …". Ikke sirkulær, ikke "se systemet". -->

## Forretningsregler

<!-- Påkrevd for klassifisering, ellers valgfri. Punktliste med presise regler:
hva er med, hva er ikke med, terskler, tidsvinduer, grensetilfeller. -->
- Inkluderer: …
- Ekskluderer: …

## Beregning

<!-- KUN maaltall. Formel uttrykt med begreps-id-er, aldri med tabeller/kolonner.
Ta med filter og hvordan verdien oppfører seg over tid. -->
`omsetning - varekost`

## Gyldige verdier

<!-- KUN dimensjon (typisk kategori). Én linje per verdi: `kode`: betydning. -->
- `verdi_a`: …

## Eksempler

<!-- Konkrete eksempler og grensetilfeller. Gjerne "Er X en Y? Ja/nei, fordi …" -->

## Avgrensning mot andre begreper

<!-- Hvordan skiller dette seg fra begreper det ofte forveksles med? -->
- [[annet_begrep]]: …

## Systemrepresentasjon

<!-- Én ### per system i frontmatter 'systemer', med system-id-en som overskrift.
Her hører alle tekniske detaljer hjemme. -->

### erp

- **Representasjon:** Hvor og hvordan begrepet finnes i systemet (objekt, felt, statusverdier, filtre).
- **Identifikasjon:** Hvilken nøkkel identifiserer en forekomst.
- **Avvik fra forretningsdefinisjon:** Hva systemet tar med/utelater som ikke stemmer med definisjonen over. Skriv "Ingen kjente" om det ikke finnes avvik.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2026-01-01 | Opprettet | … |

## Åpne spørsmål

<!-- Uavklarte punkter. Fjern seksjonen når alt er avklart. -->
