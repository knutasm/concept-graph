---
name: sett-opp-katalog
description: Setter opp en ny begrepskatalog i repoet brukeren står i. Velger mappestruktur, oppretter mappene, legger instruksjoner for agenter i CLAUDE.md, og beskriver virksomheten. Bruk når brukeren vil starte eller initialisere en begrepskatalog eller ta i bruk pluginen, eller når repoet har få eller ingen sider i katalogen, f.eks. "sett opp begrepskatalog", "ny katalog", "init", "kom i gang", "start forretningsordliste", "set up the glossary".
---

# Starte en begrepskatalog

Du setter opp **strukturen** for en begrepskatalog i repoet brukeren står i. Snakk norsk. Pluginen har
malene, veiledningen og skillene. Repoet til brukeren har sidene, og instruksjonene for agenter i `CLAUDE.md`.

Denne skillen lager ikke innhold. Ikke spør etter, og ikke foreslå, domener, prosesser, begreper eller
systemer. Det gjøres etterpå med skillene for dem. Det eneste innholdet som lages her, er
virksomhetssiden (steg 5).

Les `${CLAUDE_PLUGIN_ROOT}/kontekst/sider.md` først.

## 1. Se hva som finnes

```sh
grep -rl --include='*.md' -E "^type: (entitet|hendelse|maaltall|dimensjon|klassifisering|prosess|domene|system|virksomhet)$" . | head -30
ls CLAUDE.md 2>/dev/null && grep -n "^#" CLAUDE.md
```

- **Finnes det sider fra før,** beskriv strukturen de følger (mapper, tags), og foreslå å beholde den.
  Gå så til steg 4.
- **Er repoet ikke et git-repo,** nevn at katalogen bør versjoneres (skillen `gjennomga-side` bruker git).

## 2. Velg struktur

Vis alternativene med et lite eksempeltre hver, og la brukeren velge. `type` og `domene` står alltid i
frontmatter, uansett hva som velges. Mappene er bare et tillegg som gjør det lettere å bla.

**Type → domene → side**

```
begreper/salg/kunde.md
begreper/salg/_domene.md
prosesser/salg/ordre_til_faktura.md
systemer/erp.md
```

**Domene → type → side**

```
salg/_domene.md
salg/begreper/kunde.md
salg/prosesser/ordre_til_faktura.md
systemer/erp.md
```

**Bare type** (domenet står bare i `domene`)

```
begreper/kunde.md
domener/salg.md
prosesser/ordre_til_faktura.md
systemer/erp.md
```

**Bare domene** (typen står bare i `type`)

```
salg/_domene.md
salg/kunde.md
salg/ordre_til_faktura.md
systemer/erp.md
```

Spør også:

- **Tags:** skal sidene i tillegg ha `tags` (for eksempel `tags: [salg, begrep]`)? Nyttig i Obsidian og
  for å bla i domener eller typer som ikke har egen mappe.
- **Rotmappe:** skal katalogen ligge i en egen mappe (for eksempel `katalog/`, som kan åpnes som
  Obsidian-vault), eller i roten av repoet?
- **Systemer** gjelder ofte flere domener. Foreslå egen mappe for dem, også når resten sorteres etter domene.
- **Domenesider og virksomhetssiden:** forslag er domenesiden i domenemappen (`_domene.md`, eller
  `domener/<id>.md` når det ikke finnes domenemapper), og `virksomhet.md` øverst i katalogen.

Har brukeren ingen mening, foreslå **type → domene → side** i en egen `katalog/`-mappe, uten tags.

## 3. Lag mappene

Lag toppnivåmappene som ikke avhenger av et domenenavn, for eksempel:

```sh
mkdir -p katalog/begreper katalog/prosesser katalog/systemer
```

Domenemapper lages først når det første domenet eller den første siden i domenet skrives. Git tar ikke
med tomme mapper. Det er greit, fordi strukturen står i `CLAUDE.md`.

Vil brukeren skrive sider for hånd, kan malene kopieres inn (`${CLAUDE_PLUGIN_ROOT}/maler/`), for
eksempel til en mappe Obsidian-tillegget Templates peker på. Si at kopien ikke oppdateres når pluginen
oppdateres, og at skillene alltid bruker malene i pluginen.

## 4. Instruksjoner for agenter

Les `${CLAUDE_PLUGIN_ROOT}/kontekst/CLAUDE.md`. Den forklarer agenter hvordan katalogen slås opp og brukes.
Fyll inn seksjonen **Plassering** med strukturen som stimaler, én linje per sidetype, og om tags skal brukes:

```
- Begreper: `katalog/begreper/<domene>/<id>.md`
- Domener: `katalog/begreper/<domene>/_domene.md`
- Prosesser: `katalog/prosesser/<domene>/<id>.md`
- Systemer: `katalog/systemer/<id>.md`
- Virksomheten: `katalog/virksomhet.md`
- Tags: nei
```

- Finnes ikke `CLAUDE.md`, lag den med innholdet.
- Finnes `CLAUDE.md` uten en seksjon om begrepskatalogen, legg innholdet til nederst (overskriftene ett nivå ned).
- Finnes seksjonen allerede, vis forskjellene mot pluginens versjon og spør før du erstatter den.
  Behold det brukeren har lagt til selv, særlig **Plassering**.

## 5. Beskriv virksomheten

Finnes det ikke en side med `type: virksomhet`, fortsett med skillen `beskriv-virksomhet`
(`${CLAUDE_PLUGIN_ROOT}/skills/beskriv-virksomhet/SKILL.md`). Brukeren kan hoppe over dette og gjøre det senere.

## 6. Neste steg

Oppsummer strukturen som ble valgt, og foreslå neste steg:

- domenene med skillen `beskriv-domene`
- det første begrepet med `beskriv-begrep`, eller den første prosessen med `beskriv-prosess`
- et intervju med en fagekspert med `intervju-fagekspert`

Et fullt utfylt eksempel finnes i `example/` i pluginens repo. Strukturen der er type → domene → side.
