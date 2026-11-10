"""Validerer begrepskatalogen og genererer INDEKS.md og OVERSIKT.md.

Bruk:
    uv run scripts/valider.py           # valider og skriv INDEKS.md og OVERSIKT.md på nytt
    uv run scripts/valider.py --sjekk   # valider, og feil hvis INDEKS.md eller OVERSIKT.md er utdatert (for CI / pre-commit)

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
PROSESSER = ROT / "prosesser"
INDEKS = ROT / "INDEKS.md"
OVERSIKT = ROT / "OVERSIKT.md"

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

# Forretningsprosesser: prosesser/<id>.md
PROSESS_PAAKREVD = ["id", "navn", "domene", "kortdefinisjon", "status", "eier", "sist_oppdatert", "begreper"]
PROSESS_VALGFRI = ["synonymer", "gyldig_fra", "utloser"]
PROSESS_SEKSJONER = [("Formål", True), ("Avgrensning", True), ("Aktører", True), ("Steg", True),
                     ("Resultater", True), ("Åpne spørsmål", False)]
PROSESS_BEGREPSTYPER = {"entitet", "hendelse"}  # begrepene som inngår i en prosess
# Flyten: ### <id> <tittel> under Steg (s = steg, b = beslutning) og Resultater (r = resultat)
FLYT_ART = {"s": "steg", "b": "beslutning", "r": "resultat"}
FLYT_SEKSJON = {"s": "Steg", "b": "Steg", "r": "Resultater"}
FLYT_FELT = {
    "steg": {"Aktør", "Bruker", "Gir", "Neste"},
    "beslutning": {"Aktør", "Regel", "Bruker", "Neste"},
    "resultat": {"Hendelse"},
}
FLYT_BEGREPSFELT = ("Bruker", "Gir", "Hendelse")
FLYT_ID_RE = re.compile(r"^[sbr][0-9][a-z0-9]*$")
FLYT_OVERSKRIFT_RE = re.compile(r"^###\s+(\S+)\s*(.*)$")
FLYT_FELT_RE = re.compile(r"^\s*[-*]\s+\*\*([^*:]+):\*\*\s*(.*)$")

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


@dataclass
class Flytnode:
    """Ett steg, én beslutning eller ett resultat i en prosess. Grunnlag for å tegne flytskjema."""
    id: str
    tittel: str
    art: str                                  # steg | beslutning | resultat
    seksjon: str                              # ## overskriften noden står under
    felt: dict[str, str]                      # feltnavn -> rå verdi
    neste: list[tuple[str | None, str]]       # (etikett, mål). Mål: lokal id eller "[[prosess_id]]"
    tekst: str = ""                           # fritekst mellom overskrift og felt

    @property
    def aktor(self) -> str | None:
        return self.felt.get("Aktør") or None

    def begreper(self, felt: str) -> list[str]:
        return [_lenkemaal(d) or d for d in _deler(self.felt.get(felt, ""), ",")]


def _deler(verdi: str, skille: str) -> list[str]:
    return [d.strip() for d in verdi.split(skille) if d.strip()]


def _lenkemaal(verdi: str) -> str | None:
    m = HEL_LENKE_RE.match(verdi.strip())
    return m.group(1).strip() if m else None


def _les_neste(verdi: str) -> list[tuple[str | None, str]]:
    neste = []
    for del_ in _deler(verdi, ";"):
        etikett, pil, maal = del_.replace("->", "→").rpartition("→")
        neste.append(((etikett.strip() or None) if pil else None, maal.strip()))
    return neste


def les_flyt(dok: Dokument) -> list[Flytnode]:
    """Leser ###-blokkene under Steg og Resultater, i leserekkefølge."""
    noder: list[Flytnode] = []
    for seksjon in ("Steg", "Resultater"):
        node = None
        for linje in dok.seksjoner.get(seksjon, "").splitlines():
            m = FLYT_OVERSKRIFT_RE.match(linje)
            if m:
                node = Flytnode(m.group(1), m.group(2).strip(), FLYT_ART.get(m.group(1)[:1], "ukjent"),
                                seksjon, {}, [])
                noder.append(node)
                continue
            if node is None:
                continue
            f = FLYT_FELT_RE.match(linje)
            if f:
                node.felt[f.group(1).strip()] = f.group(2).strip()
            elif linje.strip() and not linje.strip().startswith("<!--") and not node.felt:
                node.tekst = f"{node.tekst} {linje.strip()}".strip()
        for n in noder:
            if n.seksjon == seksjon:
                n.neste = _les_neste(n.felt.get("Neste", ""))
    return noder


def _aktorer_i_tabell(innhold: str) -> list[str]:
    rader = [l for l in innhold.splitlines() if l.strip().startswith("|")]
    return [r.strip().strip("|").split("|")[0].strip() for r in rader[2:]]  # hopp over overskrift og skillelinje


def valider_flyt(dok: Dokument, begreper: dict, res: Resultat) -> None:
    pid = dok.fm.get("id")
    noder = les_flyt(dok)
    ider: dict[str, Flytnode] = {}
    for n in noder:
        if not FLYT_ID_RE.match(n.id):
            res.f(dok, f"'### {n.id} {n.tittel}': id må være s<nr> (steg), b<nr> (beslutning) eller r<nr> (resultat)")
            continue
        if FLYT_SEKSJON[n.id[0]] != n.seksjon:
            res.f(dok, f"'{n.id}' står under '## {n.seksjon}', men {n.art} hører under '## {FLYT_SEKSJON[n.id[0]]}'")
        if n.id in ider:
            res.f(dok, f"id '{n.id}' er brukt flere ganger")
        ider[n.id] = n
        if not n.tittel:
            res.f(dok, f"'{n.id}' mangler tittel (### {n.id} Verb objekt)")
        for felt in n.felt:
            if felt not in FLYT_FELT[n.art]:
                res.f(dok, f"'{n.id}': feltet '{felt}' er ikke tillatt for {n.art}. "
                           f"Tillatt: {', '.join(sorted(FLYT_FELT[n.art]))}")
        if n.art != "resultat":
            for felt in ("Aktør", "Neste"):
                if not n.felt.get(felt):
                    res.f(dok, f"'{n.id}' mangler feltet '{felt}'")
        if n.art == "beslutning":
            if len(n.neste) < 2 or any(e is None for e, _ in n.neste):
                res.f(dok, f"'{n.id}': en beslutning trenger minst to alternativer med etikett: 'ja → s2; nei → r2'")
            if not n.felt.get("Regel"):
                res.a(dok, f"'{n.id}': beslutningen mangler 'Regel' (hva avgjør valget?)")
        if n.art == "steg" and len(n.neste) > 1:
            res.f(dok, f"'{n.id}': et steg har bare én 'Neste'. Bruk en beslutning (b…) for valg")
        for felt in FLYT_BEGREPSFELT:
            for verdi in _deler(n.felt.get(felt, ""), ","):
                bid = _lenkemaal(verdi)
                if not bid:
                    res.f(dok, f"'{n.id}': '{felt}' skal bare ha begrepslenker, f.eks. [[ordre]], ikke '{verdi}'")
                elif bid not in begreper:
                    res.f(dok, f"'{n.id}': '{felt}' peker på ukjent begrep '{bid}'")
                elif begreper[bid].fm.get("type") not in PROSESS_BEGREPSTYPER:
                    res.f(dok, f"'{n.id}': '{felt}' peker på '{bid}' av type {begreper[bid].fm.get('type')}. "
                               "Bare entiteter og hendelser")
                elif f"[[{bid}]]" not in [str(v).strip() for v in som_liste(dok.fm.get("begreper"))]:
                    res.a(dok, f"'{n.id}': '{bid}' mangler i 'begreper' i frontmatter")
    steg = [n for n in ider.values() if n.art != "resultat"]
    if not steg:
        res.f(dok, "'## Steg' må ha minst ett steg som '### s1 Verb objekt'")
    if not any(n.art == "resultat" for n in ider.values()):
        res.f(dok, "'## Resultater' må ha minst ett resultat som '### r1 Navn'")
    aktorer = _aktorer_i_tabell(dok.seksjoner.get("Aktører", ""))
    if not aktorer:
        res.f(dok, "'## Aktører' må være en tabell: | Aktør | Ansvar i prosessen |")
    for n in steg:
        if n.aktor and n.aktor not in aktorer:
            res.f(dok, f"'{n.id}': aktøren '{n.aktor}' står ikke i tabellen under '## Aktører'")
        for _, maal in n.neste:
            prosess = _lenkemaal(maal)
            if prosess:
                if prosess == pid or not (PROSESSER / f"{prosess}.md").exists():
                    res.f(dok, f"'{n.id}': 'Neste' peker på ukjent prosess '{prosess}'")
            elif maal not in ider:
                res.f(dok, f"'{n.id}': 'Neste' peker på '{maal}', som ikke finnes. Bruk en id eller [[prosess]]")
    if not steg:
        return
    # Nåbarhet: alt skal kunne nås fra første steg, og alt skal kunne føre til et resultat eller en annen prosess
    kanter = {n.id: [m for _, m in n.neste if m in ider] for n in ider.values()}
    naadd, kø = set(), [steg[0].id]
    while kø:
        nid = kø.pop()
        if nid not in naadd:
            naadd.add(nid)
            kø += kanter.get(nid, [])
    for nid in ider:
        if nid not in naadd:
            res.a(dok, f"'{nid}' kan ikke nås fra første steg '{steg[0].id}'")
    ferdig = {n.id for n in ider.values() if n.art == "resultat" or any(_lenkemaal(m) for _, m in n.neste)}
    endret = True
    while endret:
        endret = False
        for nid, mål in kanter.items():
            if nid not in ferdig and any(m in ferdig for m in mål):
                ferdig.add(nid)
                endret = True
    for n in steg:
        if n.id not in ferdig:
            res.a(dok, f"'{n.id}' fører aldri til et resultat eller en annen prosess")


def last_prosesser(res: Resultat, begreper: dict, domener: dict) -> dict[str, Dokument]:
    prosesser: dict[str, Dokument] = {}
    if not PROSESSER.exists():
        return prosesser
    for sti in sorted(PROSESSER.glob("*.md")):
        dok = les(sti, res)
        if not dok:
            continue
        fm = dok.fm
        for felt in PROSESS_PAAKREVD:
            if fm.get(felt) in (None, "", []):
                res.f(dok, f"mangler påkrevd felt '{felt}'")
        for felt in fm:
            if felt not in PROSESS_PAAKREVD + PROSESS_VALGFRI:
                res.f(dok, f"feltet '{felt}' er ikke tillatt for en prosess")
        pid = str(fm.get("id", ""))
        if not ID_RE.match(pid):
            res.f(dok, f"ugyldig id '{pid}' (bruk små bokstaver a-z, 0-9 og _)")
        if pid != sti.stem:
            res.f(dok, f"id '{pid}' må være lik filnavnet '{sti.stem}'")
        if pid in begreper:
            res.f(dok, f"id '{pid}' er allerede brukt av begrepet i {begreper[pid].rel}")
        if fm.get("domene") not in domener:
            res.f(dok, f"domenet '{fm.get('domene')}' finnes ikke i begreper/")
        if fm.get("status") not in STATUSER:
            res.f(dok, f"status '{fm.get('status')}' er ugyldig. Tillatt: {', '.join(STATUSER)}")
        for felt in ("sist_oppdatert", "gyldig_fra"):
            if felt in fm and not isinstance(fm[felt], dt.date):
                res.f(dok, f"'{felt}' må være en dato på formen ÅÅÅÅ-MM-DD")
        if "begreper" in fm and not isinstance(fm["begreper"], list):
            res.f(dok, "'begreper' må være en liste, f.eks. [\"[[ordre]]\", \"[[kunde]]\"]")
        for v in som_liste(fm.get("begreper")) if isinstance(fm.get("begreper"), list) else []:
            m = HEL_LENKE_RE.match(str(v).strip())
            if not m:
                res.f(dok, f"begreper: '{v}' må være en Obsidian-lenke i anførselstegn, f.eks. \"[[ordre]]\"")
            elif m.group(1) not in begreper:
                res.f(dok, f"begreper peker på ukjent begrep '{m.group(1)}'")
            elif begreper[m.group(1)].fm.get("type") not in PROSESS_BEGREPSTYPER:
                res.f(dok, f"begreper: '{m.group(1)}' er av type {begreper[m.group(1)].fm.get('type')}. "
                           "En prosess lister bare entiteter og hendelser")
        if "utloser" in fm:
            uid = _lenkemaal(str(fm["utloser"]))
            if not uid:
                res.f(dok, f"utloser: '{fm['utloser']}' må være én lenke i anførselstegn, f.eks. \"[[ordre]]\"")
            elif uid not in begreper:
                res.f(dok, f"utloser peker på ukjent begrep '{uid}'")
            elif begreper[uid].fm.get("type") not in PROSESS_BEGREPSTYPER:
                res.f(dok, f"utloser: '{uid}' er av type {begreper[uid].fm.get('type')}. Bare entiteter og hendelser")
            elif f"[[{uid}]]" not in [str(v).strip() for v in som_liste(fm.get("begreper"))]:
                res.a(dok, f"utloser '{uid}' mangler i 'begreper'")
        valider_flyt(dok, begreper, res)
        navn = [n for n, _ in PROSESS_SEKSJONER]
        for seksjon in dok.rekkefolge:
            if seksjon not in navn:
                res.f(dok, f"ukjent seksjon '## {seksjon}'. Tillatt: {', '.join(navn)}")
        for seksjon, paakrevd in PROSESS_SEKSJONER:
            if paakrevd and not dok.seksjoner.get(seksjon, "").strip():
                res.f(dok, f"mangler eller har tom seksjon '## {seksjon}'")
        kjente = [n for n in dok.rekkefolge if n in navn]
        if kjente != sorted(kjente, key=navn.index):
            res.f(dok, f"seksjonene står i feil rekkefølge. Riktig: {', '.join(navn)}")
        for seksjon, innhold in dok.seksjoner.items():
            for lenke in LENKE_RE.findall(innhold):
                if lenke not in begreper and lenke != pid and not (PROSESSER / f"{lenke}.md").exists():
                    res.f(dok, f"lenken [[{lenke}]] i '## {seksjon}' peker på ukjent begrep eller prosess")
        if pid:
            prosesser[pid] = dok
    return prosesser


# --- Indeks --------------------------------------------------------------------

def celle(verdi) -> str:
    return str(verdi or "").replace("|", "\\|").replace("\n", " ").strip()


def lag_indeks(begreper: dict, domener: dict, systemer: dict, prosesser: dict) -> str:
    linjer = [
        "# Indeks",
        "",
        "<!-- GENERERT av scripts/valider.py. Ikke rediger for hånd. -->",
        "",
        f"{len(begreper)} begreper i {len(domener)} domener, {len(prosesser)} prosesser, {len(systemer)} systemer. "
        "Les [README.md](README.md) for hvordan katalogen er bygd opp. "
        "Diagrammer, måltall og systemavvik står i [OVERSIKT.md](OVERSIKT.md).",
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
    linjer += ["", "## Prosesser", "", "Forretningsprosessene: hva som starter dem, hvem som deltar, og hvor mange entiteter og hendelser som inngår.", ""]
    if prosesser:
        linjer += ["| id | navn | domene | status | utløser | aktører | begreper | kortdefinisjon |",
                   "|---|---|---|---|---|---|---|---|"]
        for pdok in sorted(prosesser.values(), key=lambda x: (x.fm.get("domene"), x.fm["id"])):
            fm = pdok.fm
            aktorer = list(dict.fromkeys(n.aktor for n in les_flyt(pdok) if n.aktor))
            linjer.append(f"| [{fm['id']}]({pdok.rel}) | {celle(fm.get('navn'))} | {celle(fm.get('domene'))} "
                          f"| {celle(fm.get('status'))} | {celle(_lenkemaal(str(fm.get('utloser', ''))))} "
                          f"| {celle(', '.join(aktorer))} | {len(som_liste(fm.get('begreper')))} "
                          f"| {celle(fm.get('kortdefinisjon'))} |")
    else:
        linjer.append("_Ingen prosesser ennå._")
    linjer += ["", "## Systemer", "", "| id | navn | kategori | antall begreper | beskrivelse |", "|---|---|---|---|---|"]
    for sid, sdok in systemer.items():
        antall = sum(1 for b in begreper.values() if sid in som_liste(b.fm.get("systemer")))
        linjer.append(f"| [{sid}]({sdok.rel}) | {celle(sdok.fm.get('navn'))} | {celle(sdok.fm.get('kategori'))} "
                      f"| {antall} | {celle(sdok.fm.get('beskrivelse'))} |")
    return "\n".join(linjer) + "\n"


# --- Oversikt ------------------------------------------------------------------

# Relasjoner som tegnes, og pilstil. se_ogsaa utelates for lesbarhetens skyld.
KANTSTIL = {
    "tilhorer": "-->", "del_av": "-->", "er_en": "-->", "avledet_av": "-->", "beskriver": "-->",
    "grain": "-->", "tid": "-->", "forveksles_med": "-.-", "erstattet_av": "-.->",
}
AVVIK_RE = re.compile(r"\*\*Avvik fra forretningsdefinisjon:\*\*\s*(.*?)(?=\n\s*-\s+\*\*|\n#|\Z)", re.DOTALL)


def _ref(verdi) -> str | None:
    m = HEL_LENKE_RE.match(str(verdi).strip())
    return m.group(1).strip() if m else None


def _kanter(dok: Dokument, begreper: dict) -> list[tuple[str, str, str]]:
    """(fra, til, etikett) for alle tegnbare koblinger fra et begrep."""
    fra = dok.fm["id"]
    kanter = []
    for rtype in RELASJONER:
        if rtype not in KANTSTIL:
            continue
        for v in som_liste(dok.fm.get(rtype)):
            til = _ref(v)
            if til in begreper:
                kanter.append((fra, til, rtype))
    for felt in REFERANSEFELT:
        til = _ref(dok.fm.get(felt, ""))
        if til in begreper:
            kanter.append((fra, til, "grain" if felt == "grain" else "tid"))
    return kanter


def _alle_kanter(begreper: dict) -> list[tuple[str, str, str]]:
    sett = set()
    for dok in begreper.values():
        for fra, til, etikett in _kanter(dok, begreper):
            if etikett == "forveksles_med":  # symmetrisk: tegn én gang
                fra, til = sorted((fra, til))
            sett.add((fra, til, etikett))
    return sorted(sett)


def _etikett(tekst) -> str:
    return '"' + str(tekst).replace('"', "#quot;") + '"'


# Relasjoner mellom entiteter/hendelser som tegnes i prosessdiagrammene
PROSESS_RELASJONER = ["tilhorer", "del_av", "er_en"]


def _mermaid_prosess(prosess: Dokument, begreper: dict) -> list[str]:
    domene = prosess.fm.get("domene")
    noder = sorted({b for b in (_ref(v) for v in som_liste(prosess.fm.get("begreper"))) if b in begreper})
    linjer = ["```mermaid", "flowchart LR"]
    for bid in noder:
        fm = begreper[bid].fm
        navn = fm.get("navn", bid) if fm.get("domene") == domene else f"{fm.get('navn', bid)} ({fm.get('domene')})"
        start, slutt = ("([", "])") if fm.get("type") == "hendelse" else ("[", "]")
        linjer.append(f"    {bid}{start}{_etikett(navn)}{slutt}")
    kanter = set()
    for bid in noder:
        for rtype in PROSESS_RELASJONER:
            for v in som_liste(begreper[bid].fm.get(rtype)):
                til = _ref(v)
                if til in noder:
                    kanter.add((bid, til, rtype))
    for fra, til, rtype in sorted(kanter):
        linjer.append(f"    {fra} -->|{rtype}| {til}")
    eksterne = [b for b in noder if begreper[b].fm.get("domene") != domene]
    if eksterne:
        linjer.append("    classDef ekstern fill:#f5f5f5,stroke:#999,color:#555,stroke-dasharray:3 3")
        linjer.append(f"    class {','.join(eksterne)} ekstern")
    linjer.append("```")
    return linjer


def _avvik(dok: Dokument) -> dict[str, str]:
    innhold = dok.seksjoner.get("Systemrepresentasjon", "")
    ut = {}
    for sid in dok.underseksjoner.get("Systemrepresentasjon", []):
        m = AVVIK_RE.search(_underseksjon(innhold, sid))
        if m:
            tekst = " ".join(m.group(1).split())
            if tekst and not tekst.lower().startswith("ingen kjente"):
                ut[sid] = tekst
    return ut


def _lenke(dok: Dokument) -> str:
    return f"[{dok.fm['id']}]({dok.rel})"


def _reflenke(verdi, begreper: dict) -> str:
    bid = _ref(verdi) if verdi else None
    return _lenke(begreper[bid]) if bid in begreper else celle(verdi)


def lag_oversikt(begreper: dict, domener: dict, systemer: dict, prosesser: dict) -> str:
    kanter = _alle_kanter(begreper)
    linjer = [
        "# Oversikt",
        "",
        "<!-- GENERERT av scripts/valider.py. Ikke rediger for hånd. -->",
        "",
        "Sammenhenger, måltall, systemavvik og uferdige begreper. Se [INDEKS.md](INDEKS.md) for alle begreper.",
        "",
        "**Prosessdiagrammene** viser entitetene `[ ]` og hendelsene `([ ])` som inngår i hver "
        "forretningsprosess (feltet `begreper` i `prosesser/<id>.md`), og relasjonene mellom dem: "
        "`tilhorer`, `del_av` og `er_en`. Pilene leses *fra → til*: `ordre --tilhorer--> kunde`. "
        "Grå boks med domenet i parentes = begrep fra et annet domene. Måltall, dimensjoner og "
        "klassifiseringer står i tabellene under.",
        "",
        "## Domenekart",
        "",
        "Antall koblinger mellom domener.",
        "",
        "```mermaid",
        "flowchart LR",
    ]
    for d, ddok in domener.items():
        linjer.append(f"    {d}[{_etikett(ddok.fm.get('navn', d))}]")
    mellom: dict[tuple[str, str], int] = {}
    for fra, til, _ in kanter:
        a, b = begreper[fra].fm.get("domene"), begreper[til].fm.get("domene")
        if a != b and a in domener and b in domener:
            mellom[(a, b)] = mellom.get((a, b), 0) + 1
    for (a, b), n in sorted(mellom.items()):
        linjer.append(f"    {a} -->|{n}| {b}")
    linjer.append("```")

    for d, ddok in domener.items():
        linjer += ["", f"## {d}", "", f"**{celle(ddok.fm.get('navn'))}**: {celle(ddok.fm.get('beskrivelse'))}", ""]
        mine = sorted((p for p in prosesser.values() if p.fm.get("domene") == d), key=lambda x: x.fm["id"])
        if not mine:
            linjer.append("_Ingen prosesser ennå._")
        for pdok in mine:
            linjer += ["", f"### {celle(pdok.fm.get('navn'))}", "",
                       f"[{pdok.fm['id']}]({pdok.rel}) ({celle(pdok.fm.get('status'))}): "
                       f"{celle(pdok.fm.get('kortdefinisjon'))}", ""]
            linjer += _mermaid_prosess(pdok, begreper)

    # Måltallsmatrise
    linjer += ["", "## Måltall", "",
               "Grunnlaget for mål i en semantisk modell. **semi_additiv** skal aldri summeres over tid, "
               "**ikke_additiv** skal aldri summeres (beregn fra teller og nevner).", "",
               "| måltall | domene | grain | tidsdimensjon | aggregering | additivitet | enhet | avledet_av | status |",
               "|---|---|---|---|---|---|---|---|---|"]
    maaltall = sorted((b for b in begreper.values() if b.fm.get("type") == "maaltall"),
                      key=lambda b: (b.fm.get("domene"), b.fm["id"]))
    for b in maaltall:
        fm = b.fm
        add = str(fm.get("additivitet", ""))
        add = add if add == "additiv" else f"**{add}**"
        avledet = ", ".join(_reflenke(v, begreper) for v in som_liste(fm.get("avledet_av")))
        linjer.append(f"| {_lenke(b)} | {celle(fm.get('domene'))} | {_reflenke(fm.get('grain'), begreper)} "
                      f"| {_reflenke(fm.get('tidsdimensjon'), begreper)} | {celle(fm.get('aggregering'))} "
                      f"| {add} | {celle(fm.get('enhet'))} | {avledet} | {celle(fm.get('status'))} |")

    # Systemdekning
    linjer += ["", "## Systemdekning", "", "Antall begreper per domene som er beskrevet i hvert system.", "",
               "| domene | " + " | ".join(systemer) + " |", "|---|" + "---|" * len(systemer)]
    for d in domener:
        tall = [sum(1 for b in begreper.values()
                    if b.fm.get("domene") == d and s in som_liste(b.fm.get("systemer"))) for s in systemer]
        linjer.append(f"| {d} | " + " | ".join(str(t) for t in tall) + " |")

    linjer += ["", "### Kjente avvik", "",
               "Der systemet ikke stemmer med forretningsdefinisjonen. Disse filtrene og korreksjonene "
               "må med når kildedata brukes.", ""]
    for sid in systemer:
        rader = [(b, _avvik(b)[sid]) for b in sorted(begreper.values(), key=lambda x: x.fm["id"]) if sid in _avvik(b)]
        if not rader:
            continue
        linjer += [f"#### {sid}", "", "| begrep | avvik |", "|---|---|"]
        linjer += [f"| {_lenke(b)} | {celle(tekst)} |" for b, tekst in rader]
        linjer.append("")

    # Uferdig
    linjer += ["## Uferdig", "", "Begreper og prosesser som ikke er godkjent, eller som har åpne spørsmål.", "",
               "| begrep | type | status | åpne spørsmål |", "|---|---|---|---|"]
    for b in sorted([*begreper.values(), *prosesser.values()], key=lambda x: x.fm["id"]):
        spm = re.sub(r"<!--.*?-->", "", b.seksjoner.get("Åpne spørsmål", ""), flags=re.DOTALL)
        antall = len(re.findall(r"^\s*[-*] ", spm, re.MULTILINE)) or (1 if spm.strip() else 0)
        if b.fm.get("status") != "godkjent" or antall:
            linjer.append(f"| {_lenke(b)} | {celle(b.fm.get('type', 'prosess'))} | {celle(b.fm.get('status'))} | {antall or ''} |")
    return re.sub(r"\n{3,}", "\n\n", "\n".join(linjer)) + "\n"


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
    prosesser = last_prosesser(res, begreper, domener)

    for a in res.advarsler:
        print(f"ADVARSEL  {a}")
    for f in res.feil:
        print(f"FEIL      {f}")
    if res.feil:
        print(f"\n{len(res.feil)} feil, {len(res.advarsler)} advarsler. INDEKS.md og OVERSIKT.md er ikke oppdatert.")
        return 1

    status = []
    utdatert = []
    for sti, lag in [(INDEKS, lag_indeks), (OVERSIKT, lag_oversikt)]:
        ny = lag(begreper, domener, systemer, prosesser)
        gammel = sti.read_text(encoding="utf-8") if sti.exists() else ""
        if ny == gammel:
            status.append(f"{sti.name} uendret")
        elif sjekk:
            utdatert.append(sti.name)
        else:
            sti.write_text(ny, encoding="utf-8")
            status.append(f"{sti.name} skrevet")
    if utdatert:
        for navn in utdatert:
            print(f"FEIL      {navn} er utdatert. Kjør: uv run scripts/valider.py")
        return 1
    print(f"OK: {len(begreper)} begreper, {len(prosesser)} prosesser, {len(res.advarsler)} advarsler. {', '.join(status)}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
