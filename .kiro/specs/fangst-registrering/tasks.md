# Tasks: Fangstregistrering

## Implementeringsopgaver

Tasks er de konkrete implementeringsopgaver der skal udføres for at realisere denne spec.
Hver task kan udføres af en udvikler eller af Kiro. Rækkefølgen er en anbefaling.

- [ ] 1. Implementér datamodel med Pydantic
  - [ ] 1.1 Opret FiskearterEnum med tilladte fiskearter
  - [ ] 1.2 Opret FangstInput model (request body)
  - [ ] 1.3 Opret FangstRegistrering model (inkl. auto-genererede felter)
- [ ] 2. Opret in-memory storage (dict) til fangster
- [ ] 3. Implementér POST /fangster med validering
  - [ ] 3.1 Implementér endpoint der modtager FangstInput
  - [ ] 3.2 Tilføj validering: afvis negativ/nul mængde (FR-06)
  - [ ] 3.3 Tilføj validering: afvis fremtidig dato (FR-07)
  - [ ] 3.4 Returnér 201 med FangstRegistrering
- [ ] 4. Implementér GET /fangster med dato-filtrering
  - [ ] 4.1 Implementér endpoint der returnerer alle fangster
  - [ ] 4.2 Tilføj valgfri query-parametre fra_dato og til_dato
- [ ] 5. Implementér GET /fangster/{id}
- [ ] 6. Implementér DELETE /fangster/{id}
- [ ] 7. Skriv tests for alle endepunkter
  - [ ] 7.1 Test oprettelse af fangst (succes)
  - [ ] 7.2 Test hentning af alle fangster (tom liste og med data)
  - [ ] 7.3 Test dato-filtrering
  - [ ] 7.4 Test hentning af enkelt fangst (succes og 404)
  - [ ] 7.5 Test sletning af fangst (succes og 404)
- [ ] 8. Skriv tests for valideringsregler
  - [ ] 8.1 Test afvisning af negativ mængde (FR-06)
  - [ ] 8.2 Test afvisning af nul mængde (FR-06)
  - [ ] 8.3 Test afvisning af fremtidig dato (FR-07)
  - [ ] 8.4 Test afvisning af ugyldig fiskeart

## Checkpoint

Verificer at alle tests er grønne inden du fortsætter med eventuelle udvidelser:
```bash
cd app && pytest tests/ -v
```

## Optionelle udvidelser

- [ ]* 9. Tilføj filtrering på fiskeart i GET /fangster
- [ ]* 10. Tilføj sortering af fangster (efter dato eller mængde)
