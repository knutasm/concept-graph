"""Validerer begrepskatalogen og genererer INDEKS.md.

Bruk:
    uv run scripts/valider.py           # valider og skriv INDEKS.md på nytt
    uv run scripts/valider.py --sjekk   # valider, og feil hvis INDEKS.md er utdatert (for CI / pre-commit)

Avslutter med kode 1 ved feil. Advarsler stopper ikke, men bør leses.
"""
from __future__ import annotations

import datetime as dt
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ROT = Path(__file__).resolve().parent.parent
BEGREPER = ROT / "begreper"
SYSTEMER = ROT / "systemer"
INDEKS = ROT / "INDEKS.md"

# --- Tillatte verdier --------------------------------------------------------

TYPER = ["entitet", "hendelse", "maaltall", "dimensjon", "klassifisering"]
STATUSER = ["utkast", "til_godkjenning", "godkjent", "utfaset"]
# Relasjoner er egne felt på toppnivå i frontmatter (Obsidian støtter ikke nøstede objekter),
# med Obsidian-lenker som verdier: er_en: ["[[kunde]]"]
RELASJONER = ["er_en", "del_av", "tilhorer", "avledet_av", "beskriver",
              "forveksles_med", "se_ogsaa", "erstattet_av"]
# Felt som peker på ett begrep, også som Obsidian-lenke: grain: "[[fakturalinje]]"
REFERANSEFELT = ["grain", "tidsdimensjon", "tidspunkt"]
AGGREGERINGER = ["sum", "antall", "antall_unike", "snitt", "min", "maks", "ratio", "formel"]
ADDITIVITET = ["additiv", "semi_additiv", "ikke_additiv"]
DIMENSJONSTYPER = ["kategori", "tid", "boolsk", "numerisk", "tekst"]

FELLES_PAAKREVD = ["id", "navn", "type", "domene", "kortdefinisjon", "status", "eier", "sist_oppdatert"]
FELLES_VALGFRI = ["synonymer", "systemer", "gyldig_fra"]  # + relasjonstypene i RELASJONER
TYPE_PAAKREVD = {
    "entitet": ["identifiseres_ved"],
    "hendelse": ["tidspunkt"],
    "maaltall": ["aggregering", "enhet", "grain", "tidsdimensjon", "additivitet"],
    "dimensjon": ["dimensjonstype"],
    "klassifisering": [],
}
TYPE_VALGFRI = {
    "entitet": [],
    "hendelse": ["identifiseres_ved"],
    "maaltall": [],
    "dimensjon": [],
    "klassifisering": [],
}

# Seksjoner i fast rekkefølge. (navn, påkrevd for typer, tillatt for typer)
ALLE = set(TYPER)
SEKSJONER = [
    ("Definisjon", ALLE, ALLE),
    ("Forretningsregler", {"klassifisering"}, ALLE),
    ("Beregning", {"maaltall"}, {"maaltall"}),
    ("Gyldige verdier", set(), {"dimensjon"}),
    ("Eksempler", set(), ALLE),
    ("Avgrensning mot andre begreper", set(), ALLE),
    ("Systemrepresentasjon", ALLE, ALLE),
    ("Historikk", ALLE, ALLE),
    ("Åpne spørsmål", set(), ALLE),
]
SEKSJONSNAVN = [s[0] for s in SEKSJONER]
# Seksjoner som skal være systemnøytrale
FORRETNINGSSEKSJONER = ["Definisjon", "Forretningsregler", "Beregning", "Gyldige verdier"]

ID_RE = re.compile(r"^[a-z][a-z0-9_]*$")
LENKE_RE = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
HEL_LENKE_RE = re.compile(r"^\[\[([^\]|#]+)\]\]$")
TEKNISK_RE = re.compile(
    r"(?i:\b\w*(?:tabell|kolonne|statuskode|flagg|primærnøkkel|fremmednøkkel)\w*)"  # også sammensatte ord
    r"|\b[A-Z][A-Z0-9]*_[A-Z0-9_]+\b"          # STORE_BOKSTAVER_MED_UNDERSTREK
    r"|`[^`]*\.[^`]*`",                          # `noe.annet` (tabell.kolonne)
)


# --- Datastrukturer ----------------------------------------------------------

@dataclass
class Dokument:
    sti: Path
    fm: dict
    seksjoner: dict[str, str]           # ## overskrift -> innhold
    rekkefolge: list[str]
    underseksjoner: dict[str, list[str]]  # ## overskrift -> [### overskrifter]

    @property
    def rel(self) -> str:
        return self.sti.relative_to(ROT).as_posix()


@dataclass
class Resultat:
    feil: list[str] = field(default_factory=list)
    advarsler: list[str] = field(default_factory=list)

    def f(self, dok: Dokument | Path | str, melding: str) -> None:
        self.feil.append(f"{_navn(dok)}: {melding}")

    def a(self, dok: Dokument | Path | str, melding: str) -> None:
        self.advarsler.append(f"{_navn(dok)}: {melding}")


def _navn(dok) -> str:
    if isinstance(dok, Dokument):
        return dok.rel
    if isinstance(dok, Path):
        return dok.relative_to(ROT).as_posix()
    return str(dok)


# --- Parsing -------------------------------------------------------------------

def les(sti: Path, res: Resultat) -> Dokument | None:
    tekst = sti.read_text(encoding="utf-8")
    if not tekst.startswith("---\n"):
        res.f(sti, "mangler frontmatter (filen må starte med '---')")
        return None
    slutt = tekst.find("\n---\n", 4)
    if slutt == -1:
        res.f(sti, "frontmatter er ikke avsluttet med '---'")
        return None
    try:
        fm = yaml.safe_load(tekst[4:slutt]) or {}
    except yaml.YAMLError as e:
        res.f(sti, f"ugyldig YAML i frontmatter: {e}")
        return None
    if not isinstance(fm, dict):
        res.f(sti, "frontmatter må være et YAML-objekt")
        return None

    seksjoner: dict[str, list[str]] = {}
    rekkefolge: list[str] = []
    under: dict[str, list[str]] = {}
    gjeldende = None
    i_kodeblokk = False
    for linje in tekst[slutt + 5:].splitlines():
        if linje.startswith("```"):
            i_kodeblokk = not i_kodeblokk
        if not i_kodeblokk and linje.startswith("## "):
            gjeldende = linje[3:].strip()
            rekkefolge.append(gjeldende)
            seksjoner[gjeldende] = []
            under[gjeldende] = []
            continue
        if not i_kodeblokk and linje.startswith("### ") and gjeldende:
            under[gjeldende].append(linje[4:].strip())
        if gjeldende:
            seksjoner[gjeldende].append(linje)
    return Dokument(sti, fm, {k: "\n".join(v) for k, v in seksjoner.items()}, rekkefolge, under)


def som_liste(verdi) -> list:
    if verdi is None:
        return []
    return verdi if isinstance(verdi, list) else [verdi]


# --- Validering ----------------------------------------------------------------

def valider_enkel_fm(dok: Dokument, paakrevd: list[str], res: Resultat) -> None:
    for felt in paakrevd:
        if dok.fm.get(felt) in (None, "", []):
            res.f(dok, f"mangler påkrevd felt '{felt}'")
    if dok.fm.get("id") != dok.sti.stem.lstrip("_") and dok.sti.name != "_domene.md":
        res.f(dok, f"id '{dok.fm.get('id')}' må være lik filnavnet '{dok.sti.stem}'")


def last_systemer(res: Resultat) -> dict[str, Dokument]:
    systemer: dict[str, Dokument] = {}
    for sti in sorted(SYSTEMER.glob("*.md")):
        dok = les(sti, res)
        if not dok:
            continue
        valider_enkel_fm(dok, ["id", "navn", "kategori", "eier", "beskrivelse"], res)
        sid = dok.fm.get("id")
        if sid:
            if not ID_RE.match(str(sid)):
                res.f(dok, f"ugyldig id '{sid}' (bruk små bokstaver a-z, 0-9 og _)")
            systemer[sid] = dok
    return systemer


def last_domener(res: Resultat) -> dict[str, Dokument]:
    domener: dict[str, Dokument] = {}
    for mappe in sorted(p for p in BEGREPER.iterdir() if p.is_dir() and not p.name.startswith(".")):
        sti = mappe / "_domene.md"
        if not sti.exists():
            res.f(mappe, "domenemappen mangler _domene.md")
            continue
        dok = les(sti, res)
        if not dok:
            continue
        valider_enkel_fm(dok, ["id", "navn", "eier", "beskrivelse"], res)
        if dok.fm.get("id") != mappe.name:
            res.f(dok, f"id '{dok.fm.get('id')}' må være lik mappenavnet '{mappe.name}'")
        domener[mappe.name] = dok
    return domener


def last_begreper(res: Resultat) -> dict[str, Dokument]:
    begreper: dict[str, Dokument] = {}
    for sti in sorted(BEGREPER.rglob("*.md")):
        if sti.name.startswith("_") or any(d.startswith(".") for d in sti.relative_to(BEGREPER).parts):
            continue
        if sti.parent.parent != BEGREPER:
            res.f(sti, "begrepsfiler skal ligge direkte i begreper/<domene>/")
            continue
        dok = les(sti, res)
        if not dok:
            continue
        bid = dok.fm.get("id")
        if bid in begreper:
            res.f(dok, f"id '{bid}' er allerede brukt i {begreper[bid].rel}")
            continue
        if bid:
            begreper[bid] = dok
    return begreper


def valider_begrep(dok: Dokument, begreper: dict, systemer: dict, res: Resultat) -> None:
    fm = dok.fm
    typ = fm.get("type")

    # Felt
    for felt in FELLES_PAAKREVD:
        if fm.get(felt) in (None, "", []):
            res.f(dok, f"mangler påkrevd felt '{felt}'")
    if typ not in TYPER:
        res.f(dok, f"type '{typ}' er ugyldig. Tillatt: {', '.join(TYPER)}")
        return
    for felt in TYPE_PAAKREVD[typ]:
        if fm.get(felt) in (None, "", []):
            res.f(dok, f"mangler felt '{felt}' (påkrevd for type {typ})")
    tillatt = set(FELLES_PAAKREVD + FELLES_VALGFRI + RELASJONER + TYPE_PAAKREVD[typ] + TYPE_VALGFRI[typ])
    if "relasjoner" in fm:
        res.f(dok, "'relasjoner' er erstattet av egne felt per relasjonstype, f.eks. er_en: [\"[[kunde]]\"]")
    for felt in fm:
        if felt not in tillatt and felt != "relasjoner":
            res.f(dok, f"feltet '{felt}' er ikke tillatt for type {typ}")

    bid = str(fm.get("id", ""))
    if not ID_RE.match(bid):
        res.f(dok, f"ugyldig id '{bid}' (bruk små bokstaver a-z, 0-9 og _)")
    if bid != dok.sti.stem:
        res.f(dok, f"id '{bid}' må være lik filnavnet '{dok.sti.stem}'")
    if fm.get("domene") != dok.sti.parent.name:
        res.f(dok, f"domene '{fm.get('domene')}' må være lik mappen '{dok.sti.parent.name}'")
    if fm.get("status") not in STATUSER:
        res.f(dok, f"status '{fm.get('status')}' er ugyldig. Tillatt: {', '.join(STATUSER)}")
    for felt in ("sist_oppdatert", "gyldig_fra"):
        if felt in fm and not isinstance(fm[felt], dt.date):
            res.f(dok, f"'{felt}' må være en dato på formen ÅÅÅÅ-MM-DD")
    kort = str(fm.get("kortdefinisjon", ""))
    if "\n" in kort.strip() or len(kort) > 200:
        res.a(dok, "kortdefinisjon bør være én setning på under 200 tegn")
    for felt in ("synonymer", "systemer"):
        if felt in fm and not isinstance(fm[felt], list):
            res.f(dok, f"'{felt}' må være en liste, f.eks. [a, b]")

    # Referanser
    def finnes(ref: str, felt: str, typer: set[str] | None = None) -> None:
        if ref not in begreper:
            res.f(dok, f"{felt} peker på ukjent begrep '{ref}'")
        elif typer and begreper[ref].fm.get("type") not in typer:
            res.f(dok, f"{felt} '{ref}' må være av type {' eller '.join(sorted(typer))}")

    def lenke(verdi, felt: str) -> str | None:
        m = HEL_LENKE_RE.match(str(verdi).strip())
        if not m:
            res.f(dok, f"{felt}: '{verdi}' må være en Obsidian-lenke i anførselstegn, f.eks. \"[[kunde]]\"")
            return None
        return m.group(1).strip()

    rel: dict[str, list[str]] = {}
    for rtype in RELASJONER:
        if rtype not in fm:
            continue
        if not isinstance(fm[rtype], list):
            res.f(dok, f"relasjonen {rtype} må være en liste, f.eks. {rtype}: [\"[[kunde]]\"]")
            continue
        rel[rtype] = [m for m in (lenke(v, f"relasjonen {rtype}") for v in fm[rtype]) if m]
        for m in rel[rtype]:
            if m == bid:
                res.f(dok, f"relasjonen {rtype} peker på seg selv")
            finnes(m, f"relasjonen {rtype}")
    ref = {felt: lenke(fm[felt], felt) for felt in REFERANSEFELT if fm.get(felt)}
    for s in som_liste(fm.get("systemer")):
        if s not in systemer:
            res.f(dok, f"systemet '{s}' finnes ikke i systemer/")

    if typ == "maaltall":
        if fm.get("aggregering") not in AGGREGERINGER:
            res.f(dok, f"aggregering må være en av: {', '.join(AGGREGERINGER)}")
        if fm.get("additivitet") not in ADDITIVITET:
            res.f(dok, f"additivitet må være en av: {', '.join(ADDITIVITET)}")
        if ref.get("grain"):
            finnes(ref["grain"], "grain", {"entitet", "hendelse"})
        if ref.get("tidsdimensjon"):
            finnes(ref["tidsdimensjon"], "tidsdimensjon", {"dimensjon"})
            td = begreper.get(ref["tidsdimensjon"])
            if td and td.fm.get("dimensjonstype") != "tid":
                res.f(dok, f"tidsdimensjon '{ref['tidsdimensjon']}' må ha dimensjonstype: tid")
    if typ == "hendelse" and ref.get("tidspunkt"):
        finnes(ref["tidspunkt"], "tidspunkt", {"dimensjon"})
    if typ == "dimensjon":
        if fm.get("dimensjonstype") not in DIMENSJONSTYPER:
            res.f(dok, f"dimensjonstype må være en av: {', '.join(DIMENSJONSTYPER)}")
        if not rel.get("beskriver") and fm.get("dimensjonstype") != "tid":
            res.a(dok, "dimensjon bør ha relasjonen 'beskriver' (hvilken entitet/hendelse den beskriver)")
    if typ == "klassifisering" and not rel.get("er_en"):
        res.f(dok, "klassifisering må ha relasjonen 'er_en' (hvilket begrep den deler inn)")

    # Seksjoner
    for navn in dok.rekkefolge:
        if navn not in SEKSJONSNAVN:
            res.f(dok, f"ukjent seksjon '## {navn}'. Tillatt: {', '.join(SEKSJONSNAVN)}")
    for navn, paakrevd, tillatt_for in SEKSJONER:
        if typ in paakrevd and navn not in dok.seksjoner:
            res.f(dok, f"mangler seksjonen '## {navn}'")
        if navn in dok.seksjoner and typ not in tillatt_for:
            res.f(dok, f"seksjonen '## {navn}' brukes ikke for type {typ}")
    kjente = [n for n in dok.rekkefolge if n in SEKSJONSNAVN]
    if kjente != sorted(kjente, key=SEKSJONSNAVN.index):
        res.f(dok, f"seksjonene står i feil rekkefølge. Riktig: {', '.join(SEKSJONSNAVN)}")
    if "Definisjon" in dok.seksjoner and not dok.seksjoner["Definisjon"].strip():
        res.f(dok, "seksjonen '## Definisjon' er tom")

    # Systemrepresentasjon: én ### per system i frontmatter, og omvendt
    if "Systemrepresentasjon" in dok.underseksjoner:
        under = dok.underseksjoner["Systemrepresentasjon"]
        fm_sys = som_liste(fm.get("systemer"))
        for s in fm_sys:
            if s not in under:
                res.f(dok, f"systemet '{s}' står i frontmatter, men mangler '### {s}' under Systemrepresentasjon")
        for s in under:
            if s not in fm_sys:
                res.f(dok, f"'### {s}' under Systemrepresentasjon må også stå i frontmatter 'systemer'")
            elif "avvik fra forretningsdefinisjon" not in _underseksjon(dok.seksjoner["Systemrepresentasjon"], s).lower():
                res.a(dok, f"'### {s}' mangler linjen 'Avvik fra forretningsdefinisjon' (skriv 'Ingen kjente' om det ikke finnes)")

    # Lenker i brødtekst
    for navn, innhold in dok.seksjoner.items():
        for lenke in LENKE_RE.findall(innhold):
            if lenke not in begreper:
                res.f(dok, f"lenken [[{lenke}]] i '## {navn}' peker på ukjent begrep")

    # Forretning vs. system: systemnavn og tekniske uttrykk i forretningsseksjonene
    systemord = {}
    for sid, sdok in systemer.items():
        for ord_ in [sid, sdok.fm.get("navn"), *som_liste(sdok.fm.get("synonymer"))]:
            if ord_:
                systemord[str(ord_).lower()] = sid
    forretningstekst = {navn: dok.seksjoner.get(navn, "") for navn in FORRETNINGSSEKSJONER}
    forretningstekst["kortdefinisjon"] = str(fm.get("kortdefinisjon", ""))
    for navn, innhold in forretningstekst.items():
        ren = LENKE_RE.sub("", innhold)
        for ord_, sid in systemord.items():
            if re.search(rf"(?<![\w-]){re.escape(ord_)}(?![\w-])", ren, re.IGNORECASE):
                res.a(dok, f"'{navn}' nevner systemet '{sid}'. Flytt systemdetaljer til '## Systemrepresentasjon'")
        for treff in {m.group(0) for m in TEKNISK_RE.finditer(ren)}:
            res.a(dok, f"'{navn}' inneholder det som ser teknisk ut ('{treff}'). Beskriv begrepet uavhengig av system")
    if typ == "maaltall":
        for kode in re.findall(r"`([^`]+)`", dok.seksjoner.get("Beregning", "")):
            for tok in re.findall(r"[a-z][a-z0-9_]*", kode):
                if tok not in begreper and "_" in tok:
                    res.a(dok, f"'{tok}' i Beregning er ikke en begreps-id. Uttrykk formelen med begreps-id-er")


def _underseksjon(innhold: str, overskrift: str) -> str:
    del_ = innhold.split(f"### {overskrift}", 1)
    return del_[1].split("\n### ", 1)[0] if len(del_) > 1 else ""


def sjekk_synonymer(begreper: dict, res: Resultat) -> None:
    sett: dict[str, str] = {}
    for bid, dok in begreper.items():
        for ord_ in {bid, str(dok.fm.get("navn", "")).lower(), *[str(s).lower() for s in som_liste(dok.fm.get("synonymer"))]}:
            if ord_ in sett and sett[ord_] != bid:
                res.a(dok, f"'{ord_}' brukes også av '{sett[ord_]}'. Mulig duplikat. Bruk 'forveksles_med' hvis begrepene er ulike")
            sett.setdefault(ord_, bid)


# --- Indeks --------------------------------------------------------------------

def celle(verdi) -> str:
    return str(verdi or "").replace("|", "\\|").replace("\n", " ").strip()


def lag_indeks(begreper: dict, domener: dict, systemer: dict) -> str:
    linjer = [
        "# Indeks",
        "",
        "<!-- GENERERT av scripts/valider.py. Ikke rediger for hånd. -->",
        "",
        f"{len(begreper)} begreper i {len(domener)} domener, {len(systemer)} systemer. "
        "Les [README.md](README.md) for hvordan katalogen er bygd opp.",
        "",
        "## Domener",
        "",
        "| Domene | Navn | Eier | Antall | Beskrivelse |",
        "|---|---|---|---|---|",
    ]
    per_domene: dict[str, list[Dokument]] = {d: [] for d in domener}
    for dok in begreper.values():
        per_domene.setdefault(dok.fm.get("domene"), []).append(dok)
    for d, ddok in domener.items():
        linjer.append(f"| [{d}](#{d}) | {celle(ddok.fm.get('navn'))} | {celle(ddok.fm.get('eier'))} "
                      f"| {len(per_domene[d])} | {celle(ddok.fm.get('beskrivelse'))} |")
    for d, ddok in domener.items():
        linjer += ["", f"## {d}", "", f"**{celle(ddok.fm.get('navn'))}**: {celle(ddok.fm.get('beskrivelse'))} "
                   f"([domenebeskrivelse]({ddok.rel}))", ""]
        if not per_domene[d]:
            linjer.append("_Ingen begreper ennå._")
            continue
        linjer += ["| id | navn | type | status | synonymer | kortdefinisjon |", "|---|---|---|---|---|---|"]
        for dok in sorted(per_domene[d], key=lambda x: x.fm["id"]):
            fm = dok.fm
            linjer.append(f"| [{fm['id']}]({dok.rel}) | {celle(fm.get('navn'))} | {celle(fm.get('type'))} "
                          f"| {celle(fm.get('status'))} | {celle(', '.join(map(str, som_liste(fm.get('synonymer')))))} "
                          f"| {celle(fm.get('kortdefinisjon'))} |")
    linjer += ["", "## Systemer", "", "| id | navn | kategori | antall begreper | beskrivelse |", "|---|---|---|---|---|"]
    for sid, sdok in systemer.items():
        antall = sum(1 for b in begreper.values() if sid in som_liste(b.fm.get("systemer")))
        linjer.append(f"| [{sid}]({sdok.rel}) | {celle(sdok.fm.get('navn'))} | {celle(sdok.fm.get('kategori'))} "
                      f"| {antall} | {celle(sdok.fm.get('beskrivelse'))} |")
    return "\n".join(linjer) + "\n"


# --- Hovedprogram --------------------------------------------------------------

def main() -> int:
    sjekk = "--sjekk" in sys.argv[1:]
    res = Resultat()
    systemer = last_systemer(res)
    domener = last_domener(res)
    begreper = last_begreper(res)
    for dok in begreper.values():
        valider_begrep(dok, begreper, systemer, res)
    sjekk_synonymer(begreper, res)

    for a in res.advarsler:
        print(f"ADVARSEL  {a}")
    for f in res.feil:
        print(f"FEIL      {f}")
    if res.feil:
        print(f"\n{len(res.feil)} feil, {len(res.advarsler)} advarsler. INDEKS.md er ikke oppdatert.")
        return 1

    ny = lag_indeks(begreper, domener, systemer)
    gammel = INDEKS.read_text(encoding="utf-8") if INDEKS.exists() else ""
    if sjekk:
        if ny != gammel:
            print("FEIL      INDEKS.md er utdatert. Kjør: uv run scripts/valider.py")
            return 1
        print(f"OK: {len(begreper)} begreper, {len(res.advarsler)} advarsler. INDEKS.md er oppdatert.")
        return 0
    if ny != gammel:
        INDEKS.write_text(ny, encoding="utf-8")
    print(f"OK: {len(begreper)} begreper, {len(res.advarsler)} advarsler. INDEKS.md "
          f"{'skrevet' if ny != gammel else 'uendret'}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
