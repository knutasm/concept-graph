# Domener

Et domene er et område av virksomheten med sitt eget språk: et sett begreper som henger tett
sammen, og som én avdeling har ansvaret for. Hvert domene er en mappe under `begreper/`, og
`_domene.md` i mappen sier hva domenet dekker. Mal: [maler/domene.md](../maler/domene.md).
Be Claude om å "lage et nytt domene" eller "se over domenegrensene", så blir du guidet (skillen `domene`).

## Godt å vite

- **Et domene er et problemområde, ikke en avdeling eller et system.** Avdelinger omorganiseres og
  systemer byttes ut. Det virksomheten må kunne (salg, innkjøp, logistikk) består.
- **Hvert domene har sitt eget språk.** Samme ord kan bety ulike ting i ulike domener. Da er det to
  begreper, knyttet med `forveksles_med`. Se [godt-begrep.md](godt-begrep.md#samme-ord-ulik-betydning).
- **Eierskap følger oppstedet.** En entitet eller hendelse eies av domenet til prosessen der den
  oppstår. Andre domener lenker til den med relasjoner.
- **Grensene skal være tydelige.** Hver `_domene.md` sier hva som hører hjemme, og hva som hører
  til nabodomenene.

## Domenetype

Feltet `domenetype` sier hvor mye domenet betyr for konkurranseevnen, og dermed hvor mye omtanke
definisjonene trenger.

| Type | Betyr | Konsekvens for katalogen |
|---|---|---|
| `kjerne` | Det som gjør virksomheten unik, der den vinner eller taper mot konkurrentene | De strengeste definisjonene og grundigst godkjenning. Begrepene her er sjelden standard, og må formuleres av virksomheten selv |
| `stottende` | Nødvendig for driften, men ikke det kundene velger oss for | Vanlig grundighet. Definisjonene er ofte virksomhetsspesifikke |
| `generisk` | Det alle virksomheter gjør likt, ofte styrt av lov eller standard | Bruk den eksterne definisjonen (regnskapsregler, standarder) og vis til den, i stedet for å finne opp en egen |

## Begreper som mange domener bruker

Det finnes ikke noe felles domene for delte begreper. Også et begrep som alle bruker, har ett
domene som eier: domenet der det oppstår. En vare oppstår når den tas inn i sortimentet, og eies av
sortiment. Kalenderen og regnskapsperiodene eies av økonomi. De andre domenene
lenker til begrepene med relasjoner. Et felles domene blir fort et sted der ingen har ansvaret,
og der alle må bli enige før noe kan endres.

## Kobling mellom domener

Domenekartet i [OVERSIKT.md](../OVERSIKT.md) viser hvor mange relasjoner som går mellom domenene,
og under hvert domene står hvilke begreper det bruker fra andre domener.

- **Noen koblinger er normalt.** En leveranse hører til en ordre, selv om de ligger i hvert sitt domene.
- **Mange koblinger er et faresignal.** Bruker et domene mange begreper fra ett annet, ligger
  kanskje noen begreper i feil domene, eller grensen er trukket feil.
- **Koblinger begge veier** er et sterkere signal enn mange koblinger én vei.
- **Valideringen advarer** når et begrep oppstår i en prosess fra et annet domene.
