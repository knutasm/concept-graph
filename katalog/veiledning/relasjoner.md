# Relasjoner

Relasjoner gjør katalogen til en graf. Hver relasjonstype er et eget felt i frontmatter, med en
liste av Obsidian-lenker i anførselstegn som verdi, og alltid fra dette begrepet **til** det andre:

```yaml
er_en: ["[[kunde]]"]
avledet_av: ["[[ordre]]"]
```

Lenkene gjør relasjonene klikkbare i Obsidian og synlige i graf- og backlink-visningen.
Feltene `granularitet`, `tidsdimensjon` og `tidspunkt` peker også på begreper, og skrives som én lenke:
`granularitet: "[[fakturalinje]]"`.

Skriv relasjonen bare i én retning. Den motsatte retningen finner du med grep (se under).

| Relasjon | Les som | Brukes når | Eksempel |
|---|---|---|---|
| `er_en` | A er en (spesiell) B | A er en delmengde eller spesialisering av B | `aktiv_kunde er_en kunde` |
| `del_av` | A er en del av B | A finnes ikke uten B | `ordrelinje del_av ordre` |
| `tilhorer` | Hver A tilhører én B | Mange-til-én-kobling mellom selvstendige entiteter | `ordre tilhorer kunde` |
| `avledet_av` | A beregnes fra B | Måltall og klassifiseringer som bygger på andre begreper | `dekningsbidrag avledet_av omsetning` |
| `beskriver` | A beskriver B | Dimensjon som er en egenskap ved en entitet eller hendelse | `fakturadato beskriver faktura` |
| `forveksles_med` | A er ikke B | Ulike begreper som ofte blandes sammen. Forklar forskjellen i **Avgrensning mot andre begreper** | `ordredato forveksles_med fakturadato` |
| `se_ogsaa` | A er relevant for B | Nyttig kobling som ikke passer i noen annen type. Bruk sparsomt | |
| `erstattet_av` | A er erstattet av B | Bare når `status: utfaset` | |

## Tips

- **`tilhorer` og `del_av` er det som lar en generator koble tabeller.** Sørg for at alle
  entiteter har dem der det er relevant.
- **Velg den mest presise relasjonen.** `se_ogsaa` sier nesten ingenting.
- **Relasjoner peker bare på begreper som finnes.** Mangler begrepet, lag det med `status: utkast`
  og bare de påkrevde feltene, så det kan fylles ut senere.
- **Lenker i teksten** skrives `[[id]]`. De valideres på samme måte som relasjoner.

## Finne relasjoner med grep

```sh
# Alt som peker på kunde (i frontmatter eller tekst)
grep -rl "\[\[kunde\]\]" begreper

# Alle spesialiseringer av kunde
grep -rl "^er_en:.*\[\[kunde\]\]" begreper

# Hva er dekningsbidrag avledet av?
grep -h "avledet_av" begreper/salg/dekningsbidrag.md
```
