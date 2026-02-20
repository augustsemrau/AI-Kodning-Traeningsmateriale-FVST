# Requirements: Fangstregistrering

## Oversigt

Denne spec beskriver funktionaliteten til at registrere, hente og slette fangster i FangstLog-systemet. En "fangst" repræsenterer en fiskers indberetning af hvad der er landet på én fisketur.

## Funktionelle krav

1. Systemet skal kunne modtage en ny fangstregistrering med dato, fartøjsnavn, fisker-ID, fiskeart og mængde i kg
   - Acceptance Criteria:
     - POST /fangster accepterer en JSON body med felterne: dato, fartoej_navn, fisker_id, fiskeart, maengde_kg
     - Alle felter er påkrævede
     - fartoej_navn må maks være 100 tegn
     - fisker_id skal have formatet "FIS-XXXX" (fire cifre)
     - fiskeart skal være en af: torsk, sild, makrel, rødspætte, kuller, andet

2. Systemet skal returnere en unik ID for hver registrering
   - Acceptance Criteria:
     - Hvert oprettet fangst-objekt får tildelt et UUID som id
     - id og registreret_tidspunkt genereres automatisk af systemet

3. Systemet skal kunne hente en liste af alle registreringer, filtreret på dato-interval
   - Acceptance Criteria:
     - GET /fangster returnerer en liste af alle fangster
     - Valgfri query-parametre fra_dato og til_dato filtrerer på dato (begge inklusive)
     - Uden filtre returneres alle fangster

4. Systemet skal kunne hente én specifik registrering ud fra dens ID
   - Acceptance Criteria:
     - GET /fangster/{id} returnerer fangst-objektet
     - Returnerer 404 med fejlmeddelelse "Fangst ikke fundet" hvis id ikke eksisterer

5. Systemet skal kunne slette en registrering ud fra dens ID
   - Acceptance Criteria:
     - DELETE /fangster/{id} sletter fangsten og returnerer 204 No Content
     - Returnerer 404 med fejlmeddelelse "Fangst ikke fundet" hvis id ikke eksisterer

6. Systemet skal afvise registreringer med negativ eller nul mængde
   - Acceptance Criteria:
     - POST /fangster returnerer 422 med fejlmeddelelse "Mængde skal være større end 0" hvis maengde_kg <= 0

7. Systemet skal afvise registreringer med fremtidig dato
   - Acceptance Criteria:
     - POST /fangster returnerer 422 med fejlmeddelelse "Dato må ikke være i fremtiden" hvis dato > dags dato

## Ikke-funktionelle krav

8. API'et skal svare inden for 500ms under normal belastning
   - Acceptance Criteria:
     - Alle endepunkter svarer inden for 500ms med in-memory storage

9. Alle API-svar skal returneres som JSON
   - Acceptance Criteria:
     - Content-Type header er application/json på alle svar

10. Fejlsvar skal indeholde en beskrivende fejlmeddelelse på dansk
    - Acceptance Criteria:
      - Alle fejlmeddelelser er på dansk
      - Fejlsvar følger formatet: {"detail": {"fejl": "beskrivelse"}}
