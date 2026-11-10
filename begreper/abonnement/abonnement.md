---
id: abonnement
navn: Abonnement
type: entitet
domene: abonnement
kortdefinisjon: En løpende avtale med en kunde om levering mot en fast pris per periode, til den sies opp.
synonymer: [løpende avtale, subscription]
status: godkjent
eier: Kundeservice
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-10
systemer: [abonnementssystem]
relasjoner:
  tilhorer: [kunde]
identifiseres_ved: abonnementsnummer
---
# Abonnement

## Definisjon

En løpende avtale med en [[kunde]] om å levere en vare eller tjeneste mot en fast pris per periode,
til avtalen sies opp.

## Forretningsregler

- Et abonnement er aktivt fra startdato til og med siste dag kunden har betalt for.
- Prøveperioder uten betaling er ikke abonnement.

## Systemrepresentasjon

### abonnementssystem

- **Representasjon:** Abonnementsregisteret.
- **Identifikasjon:** Abonnementsnummer.
- **Avvik fra forretningsdefinisjon:** Prøveperioder ligger som abonnementer med pris 0 og må filtreres bort. Oppsagte abonnementer har status aktiv ut oppsigelsestiden, og det stemmer med definisjonen.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Kundeservice |
