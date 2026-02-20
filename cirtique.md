# Critique: Kiro Spec-Drevet Udvikling Læringsforløb

Gennemgået som en begynderudvikler der skal lære at arbejde med AI og Kiro.

---

## Overordnet vurdering

Forløbet er velstruktureret og har en klar progression fra "læs og forstå" til "implementér selv". Sproget er venligt og tilgængeligt. Men der er en række steder hvor en begynder ville gå i stå, blive forvirret, eller miste tillid til materialet.

---

## Kritikpunkter

### 1. ✅ RETTET — Specs-formatet matcher ikke Kiros faktiske spec-system

De tre spec-filer i `.kiro/specs/` er enkle markdown-filer. Kiros rigtige spec-system bruger en mappe pr. feature med `requirements.md`, `design.md` og `tasks.md`.

**Fix:** Tilføjet en bemærkning i toppen af alle tre spec-filer der forklarer at formatet er forenklet til læringsformål, og at Kiros native system bruger en mappestruktur. Tilføjet tilsvarende note i øvelse 1.

### 2. ✅ RETTET — Øvelse 2 beder om at gemme en fil i et format Kiro ikke naturligt producerer

**Fix:** Opdateret øvelse 2 med en bemærkning der forklarer at Kiro kan foreslå sit eget format, og at begge formater er fine. Fjernet den rigide instruktion om filnavn.

### 3. ⏭️ IGNORERET — Conda-miljønavnet er inkonsistent

Skyldes brugerens personlige steering-konfiguration, ikke et problem i kursusmaterialet.

### 4. ✅ RETTET — Øvelse 3 antager at koden ikke allerede er implementeret

**Fix:** Gjort `main.py` og `models.py` faktisk minimale (kun skelet med TODO-kommentarer). Nu matcher kodebasen øvelsens beskrivelse.

### 5. ✅ RETTET — `test_placeholder.py` er overflødig og forvirrende

**Fix:** Fjernet `test_fangster.py` (den fulde testsuite). Nu er `test_placeholder.py` den eneste testfil, som øvelse 3 beskriver.

### 6. ✅ RETTET — Øvelse 3 filstruktur-oversigt er misvisende

**Fix:** Opdateret filstrukturen i øvelse 3 til at matche den faktiske (nu minimale) kodebase, inkl. `__init__.py`-filer.

### 7. ✅ RETTET — Manglende `__init__.py` i filstruktur-oversigten

**Fix:** Tilføjet `__init__.py`-filer til filstrukturen i README.md, øvelse 3, og tilføjet et hint i hints.md der forklarer hvad `__init__.py` er og hvordan man opretter dem.

### 8. ✅ RETTET — Øvelse 4 mangler reference til `package-template.json`

**Fix:** Tilføjet eksplicit reference til `package-template.json` i øvelse 4, Del 1, med instruktion om at bruge den som udgangspunkt. Også tilføjet `jest.config.ts` til listen af filer Kiro skal oprette.

### 9. ✅ RETTET — Ingen verifikation af opsætning før øvelserne

**Fix:** Tilføjet "Trin 5a" i OPSAETNING.md der kører `pytest tests/test_placeholder.py -v` for at verificere at Python-miljøet fungerer, med forventet output.

### 10. ✅ RETTET — Fejlmeddelelser i koden matcher ikke altid spec-formatet

**Fix:** Opdateret alle tre spec-filer til at vise det faktiske response-format med `detail`-wrapperen, med en bemærkning der forklarer at FastAPI tilføjer denne automatisk.

### 11. ✅ RETTET — `INSTRUKTION_TIL_UNDERVISER.md` er synlig for deltagerne

**Fix:** Flyttet filen til `.facilitator/INSTRUKTION_TIL_UNDERVISER.md` og tilføjet `.facilitator/` til `.gitignore`. Fjernet referencen fra README.md's filstruktur.

### 12. ✅ RETTET — Ingen fejlhåndtering for AWS Bedrock-forbindelsesproblemer

**Fix:** Udvidet fejlfindingssektionen i OPSAETNING.md med 5 konkrete troubleshooting-trin for AWS Bedrock-problemer.

### 13. ✅ RETTET — Rapport-specen har en stavefejl

**Fix:** Rettet "fangstnmæde" til "fangstmængde" i rapport-generering.md FR-02.

### 14. ✅ RETTET — Øvelse 1 refererer til "Tasks-sektionen" uden at forklare det

**Fix:** Tilføjet en "Hvad er Tasks?" sektion i øvelse 1's baggrundstekst der forklarer konceptet i ikke-tekniske termer. Også tilføjet en kort forklaring i Tasks-sektionen i alle tre spec-filer.

### 15. ✅ RETTET — Ingen guidance om hvornår man skal starte en ny chat

**Fix:** Tilføjet tips om at starte ny chat-session i øvelse 1 (Del 3), øvelse 2 (Del 3), og øvelse 3 (Del 3). Tilføjet et dedikeret "Hint 6: Kiro mister kontekst" i hints.md.

---

## Positive aspekter

- Sproget er venligt, inkluderende og ikke-intimiderende
- Progressionen fra læsning → generering → implementering → migrering er logisk
- Hints-filen til øvelse 3 er en god idé
- Differentiering efter deltagertype (Kim, ny udvikler, erfaren) i underviser-instruktionen er gennemtænkt
- Brug af et domæne (fiskeri/fangst) der er relevant for målgruppen er smart
- Advarslerne om AI-begrænsninger og datasikkerhed er passende og velplacerede

---

## Samlet konklusion

14 af 15 kritikpunkter er rettet. Det ene ignorerede punkt (#3) skyldes brugerens personlige konfiguration og er ikke et problem i kursusmaterialet. Den vigtigste rettelse var at bringe kodebasen i sync med øvelsernes forventninger ved at gøre `main.py` og `models.py` minimale.
