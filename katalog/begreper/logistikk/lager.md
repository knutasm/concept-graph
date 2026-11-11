---
id: lager
navn: Lager
type: entitet
domene: logistikk
kortdefinisjon: Et fysisk sted der vi oppbevarer varer for salg, dvs. sentrallageret eller et utsalgssted.
synonymer: [lagersted, utsalgssted, filial, warehouse]
status: godkjent
eier: Logistikkavdelingen
gyldig_fra: 2023-01-01
sist_oppdatert: 2026-11-10
systemer: [lagerstyringssystem, erp]
identifiseres_ved: lagernummer
---
# Lager

## Definisjon

Et fysisk sted der vi oppbevarer [[vare]]r for salg. Det er sentrallageret, som forsyner byggeplasser
og utsalgssteder, og utsalgsstedene, der håndverkere henter varer selv.

## Forretningsregler

- Ekskluderer: varer i transitt mellom lagre, returer som ikke er kontrollert, og varer i karantene. De er ikke tilgjengelige for salg.
- Ekskluderer: containere og mellomlagre på byggeplass. Varene der er levert til kunden.

## Systemrepresentasjon

### lagerstyringssystem

- **Representasjon:** Lagerregisteret.
- **Identifikasjon:** Lagernummer.
- **Avvik fra forretningsdefinisjon:** Har i tillegg virtuelle lagre for transitt, retur og karantene. De må filtreres bort.

### erp

- **Representasjon:** Lagerkoder på varebeholdning og ordre.
- **Identifikasjon:** Samme lagernummer som i lagerstyringssystemet.
- **Avvik fra forretningsdefinisjon:** Har de samme virtuelle lagrene.

## Historikk

| Gyldig fra | Endring | Besluttet av |
|---|---|---|
| 2023-01-01 | Opprettet | Logistikksjef |
