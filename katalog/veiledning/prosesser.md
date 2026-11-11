# Prosesser

En forretningsprosess beskriver en **evne**: noe virksomheten må kunne gjøre for å drive. Den sier
hvem som gjør hva, i hvilken rekkefølge, hvilke valg som tas, hvordan prosessen kan ende, og hvilke
entiteter og hendelser som brukes og oppstår underveis. Mal: [maler/prosess.md](../maler/prosess.md).

## Godt å vite

- **Navngi evnen med verb + objekt:** "Levere bestilte varer til kunden", ikke "Leveranseprosessen"
  eller "Lagersystemet". Det samme gjelder stegene: "Bekrefte ordre", "Kontrollere varer".
- **Sett grensene først:** hva starter prosessen, når er den ferdig, og hva hører til nabo-prosessene?
- **Uavhengig av organisering:** evnen skal finnes selv om virksomheten omorganiseres eller setter
  arbeidet ut. Ikke bruk avdelingsnavn i navn og formål ("Kundesenterets ordrebehandling" →
  "Bekrefte ordre"). Avdelinger og roller står under Aktører, ikke i selve evnen.
- **Se verdikjeden:** hvilken prosess leverer utløseren, og hvilken tar over når denne er ferdig?
  Lenk med `Neste: [[prosess_id]]` og under **Utenfor**. [OVERSIKT.md](../OVERSIKT.md) tegner
  prosesskartet ut fra dette.
- **Hovedløpet først, unntakene etterpå:** beskriv det som skjer når alt går som det skal, i 3–10 steg.
  Legg så til beslutningene og de alternative veiene.
- **Alle veier skal ende et sted:** i et resultat (også uønskede, som "ordre avvist") eller i en annen prosess.
- **Forretningsord, ikke systemord:** "Kundesenteret bekrefter ordren", ikke "ordren registreres i ERP".
  Hvordan det ser ut i systemene, står under Systemrepresentasjon i begrepene.
- **Over 10 steg?** Del opp i delprosesser som peker på hverandre med `[[prosess_id]]`.

## Steg, beslutninger og resultater

Hvert steg, hver beslutning og hvert resultat er en `###`-blokk med faste felt. Det gjør teksten
lesbar for mennesker og samtidig strukturert nok til at et flytskjema med svømmebaner kan lages fra den.

| Blokk | Id | Under | Felt |
|---|---|---|---|
| Steg | `s1`, `s2`, `s2a` … | `## Steg` | **Aktør**, **Bruker**, **Gir**, **Neste** (nøyaktig én) |
| Beslutning | `b1`, `b2` … | `## Steg` | **Aktør**, **Regel**, **Bruker**, **Neste** (minst to, med etikett) |
| Resultat | `r1`, `r2` … | `## Resultater` | **Hendelse** (valgfri) |

- **Aktør:** en rolle eller enhet fra tabellen under `## Aktører`. Hver aktør blir en svømmebane.
- **Bruker:** entiteter og hendelser steget trenger. **Gir:** det som oppstår eller endres.
  Bare `[[entitet]]` og `[[hendelse]]`, og alle skal også stå i `begreper` i frontmatter.
- **Neste:** en id i samme fil, eller `[[annen_prosess]]` når flyten fortsetter der.
  For beslutninger: `ja → s4; nei → r2`.
- **Regel:** hva som avgjør valget. Er regelen egentlig en klassifisering (f.eks. [[restordre]]),
  bør den være et begrep.
- Rekkefølgen i filen er leserekkefølgen, og flyten starter i første blokk under `## Steg`.
  Id-ene er faste: sett inn `s2a` i stedet for å nummerere om.
- Et steg har én vei videre. Trengs det et valg, legg inn en beslutning.

**Overleveringer** skrives ikke eksplisitt. De er overgangene der **Aktør** skifter fra én blokk til neste.

## Fra prosess til måltall

- **Gjennomløpstid:** tiden fra `tidspunkt` på `utloser` til `tidspunkt` på hendelsen i et resultat,
  f.eks. fra [[ordredato]] til [[fakturadato]].
- **Andel per resultat:** hvor mange gjennomføringer som ender i hvert resultat (f.eks. andel avviste ordre).
- **Ventetid ved overlevering:** tiden mellom hendelsene på hver side av et aktørskifte.

Derfor bør resultater ha en **Hendelse**, og hendelser bør ha et `tidspunkt`.

## Eierskap følger prosessen

En entitet eller hendelse eies normalt av domenet til prosessen der den oppstår (**Gir** eller
**Hendelse**). Valideringen advarer når et begrep oppstår bare i prosesser fra andre domener. Da
ligger begrepet i feil domene, eller prosessgrensen er satt feil.
