---
id: leveranse
navn: Leveranse
type: hendelse
domene: logistikk
kortdefinisjon: At varer fra en ordre er overlevert til kunden, enten hentet på utsalgssted eller levert til byggeplass.
synonymer: [utlevering, forsendelse, delivery]
status: godkjent
eier: Logistikkavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-11
systemer: [lagerstyringssystem, erp]
kilde: lagerstyringssystem
tilhorer: ["[[ordre]]"]
tidspunkt: "[[leveringsdato]]"
identifiseres_ved: pakkseddelnummer
---
# Leveranse

## Definisjon

At [[vare]]r fra en [[ordre]] er overlevert til [[kunde]]n. Det skjer på tre måter: kunden henter på
et utsalgssted, vi kjører til byggeplass eller kundens adresse, eller [[leverandor]]en leverer direkte.
En ordre kan leveres i flere leveranser.

## Forretningsregler

- En leveranse er gjennomført når kunden har kvittert, ikke når varene er plukket eller sendt.
- Inkluderer: direkteleveranser fra leverandør.

## Systemrepresentasjon

### lagerstyringssystem

- **Representasjon:** Utleveringer og forsendelser fra egne lagre.
- **Identifikasjon:** Pakkseddelnummer.
- **Avvik fra forretningsdefinisjon:** Registrerer når varene er sendt, ikke når kunden har kvittert. Direkteleveranser mangler.

### erp

- **Representasjon:** Direkteleveranser, registrert når kundens kvittering kommer.
- **Avvik fra forretningsdefinisjon:** Kvitteringen registreres ofte flere dager for sent.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Logistikksjef |
