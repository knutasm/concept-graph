---
id: varemottak
navn: Varemottak
type: hendelse
domene: innkjop
kortdefinisjon: At varer fra en innkjøpsordre er mottatt og kontrollert på et av våre lagre eller hos kunden.
synonymer: [mottak, inngående levering, goods receipt]
status: godkjent
eier: Innkjøpsavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-11
systemer: [lagerstyringssystem, erp]
kilde: lagerstyringssystem
tilhorer: ["[[innkjopsordre]]"]
tidspunkt: "[[mottaksdato]]"
identifiseres_ved: mottaksnummer
---
# Varemottak

## Definisjon

At [[vare]]r fra en [[innkjopsordre]] er mottatt og kontrollert, enten på et av våre [[lager]] eller,
ved direktelevering, hos [[kunde]]n. En innkjøpsordre kan leveres i flere varemottak.

## Forretningsregler

- Et varemottak er registrert når varene er kontrollert, ikke når bilen ankommer.
- Ved direktelevering regnes kundens kvittering som varemottak.

## Systemrepresentasjon

### lagerstyringssystem

- **Representasjon:** Mottaksregistreringer på lagrene.
- **Identifikasjon:** Mottaksnummer.
- **Avvik fra forretningsdefinisjon:** Direkteleveranser finnes ikke her.

### erp

- **Representasjon:** Direkteleveranser registreres som mottak i ERP når kundens kvittering er mottatt.
- **Avvik fra forretningsdefinisjon:** Kvitteringen registreres ofte flere dager etter faktisk levering.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Innkjøpssjef |
