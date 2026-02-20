# Requirements: Rapportgenerering

## Oversigt

Denne spec beskriver funktionaliteten til at generere opsummerende rapporter over fangstdata. Rapporter er beregnet til at give fiskerikontrollanter og ledere et hurtigt overblik over aktivitet i en given periode.

## Funktionelle krav

1. Systemet skal kunne generere en perioderapport for et givet datointerval
   - Acceptance Criteria:
     - GET /rapporter/periode accepterer påkrævede query-parametre fra_dato og til_dato
     - Returnerer en PeriodeRapport med opsummerede data for det angivne interval

2. Perioderapporten skal indeholde total fangstmængde pr. fiskeart
   - Acceptance Criteria:
     - Feltet fordeling_pr_art indeholder en dict med fiskeart som nøgle og samlet kg som værdi
     - Kun arter med registreringer i perioden medtages

3. Perioderapporten skal indeholde antal registreringer pr. fartøj
   - Acceptance Criteria:
     - Feltet fordeling_pr_fartoej indeholder en dict med fartøjsnavn som nøgle og antal registreringer som værdi

4. Perioderapporten skal indeholde den fiskeart med størst samlet fangst
   - Acceptance Criteria:
     - Feltet mest_fanget_art indeholder navnet på den art med højest samlet maengde_kg
     - Er null hvis der ikke er data i perioden

5. Systemet skal returnere en tom rapport (med nuller) hvis der ikke er data i perioden
   - Acceptance Criteria:
     - total_registreringer = 0, total_maengde_kg = 0.0
     - fordeling_pr_art og fordeling_pr_fartoej er tomme dicts
     - mest_fanget_art er null

6. Rapporten skal kunne returneres som JSON eller som CSV
   - Acceptance Criteria:
     - Valgfri query-parameter format med værdier "json" (standard) eller "csv"
     - CSV-format indeholder opsummering og fordeling pr. art

7. fra_dato skal være før eller lig med til_dato
   - Acceptance Criteria:
     - Returnerer 422 med fejlmeddelelse "fra_dato skal være før eller lig med til_dato" hvis fra_dato > til_dato

## Ikke-funktionelle krav

8. Rapporten skal genereres uden eksterne afhængigheder — kun ud fra eksisterende fangstdata
   - Acceptance Criteria:
     - Beregning sker direkte fra in-memory fangstdata

9. Svartid må ikke overstige 1 sekund for op til 10.000 registreringer
   - Acceptance Criteria:
     - Rapporten genereres inden for 1 sekund med 10.000 fangster i hukommelsen
