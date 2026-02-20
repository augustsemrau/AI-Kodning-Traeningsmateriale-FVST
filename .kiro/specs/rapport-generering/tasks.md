# Tasks: Rapportgenerering

## Implementeringsopgaver

- [ ] 1. Implementér PeriodeRapport datamodel
- [ ] 2. Implementér beregningslogik som separat service-funktion
  - [ ] 2.1 Filtrer fangster på dato-interval
  - [ ] 2.2 Beregn fordeling pr. art (sum af maengde_kg)
  - [ ] 2.3 Beregn fordeling pr. fartøj (antal registreringer)
  - [ ] 2.4 Find mest fanget art
  - [ ] 2.5 Håndtér tomt resultat (nuller og null)
- [ ] 3. Implementér GET /rapporter/periode (JSON-format)
- [ ] 4. Tilføj CSV-format understøttelse
- [ ] 5. Håndtér edge case: tomt datointerval (ingen data i perioden)
- [ ] 6. Håndtér edge case: fra_dato > til_dato (returnér 422)
- [ ] 7. Skriv enhedstest for beregningslogikken
- [ ] 8. Skriv integrationstest for API-endepunktet
