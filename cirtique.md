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


---

## Anbefalinger: Hvad kan inkorporeres fra teamets steering-filer

Teamets `steering-templates/`-mappe indeholder 5 steering-filer og 6 templates fra det rigtige Fiskeristyrelsen-migrationsprojekt (Oracle Forms → Node.js/LoopBack). De er stærkt domænespecifikke, men indeholder flere generelle principper der ville styrke læringsforløbet.

### Anbefaling 1: Inkludér en `.kiro/steering/`-eksempel i projektet

**Kilde:** Alle 5 steering-filer bruger Kiros steering-system med `inclusion: always` front-matter.

**Problem:** Læringsforløbet nævner aldrig steering-filer. Deltagerne lærer om specs, men ikke om den anden store Kiro-mekanisme: steering. Det er en væsentlig mangel, da steering er det der gør Kiro-workflows reproducerbare og konsistente på tværs af sessioner.

**Forslag:** Opret en simpel `.kiro/steering/coding-standards.md` med grundlæggende regler for projektet, fx:
- "Fejlmeddelelser skal være på dansk"
- "Brug in-memory storage (ikke database)"
- "Alle API-endepunkter skal have docstrings"

Tilføj en kort sektion i øvelse 2 eller 3 der forklarer hvad steering er, og bed deltagerne åbne filen og se hvordan den påvirker Kiros output. Dette giver deltagerne forståelse for at Kiro kan konfigureres med vedvarende regler — ikke kun per-chat instruktioner.

### Anbefaling 2: Task-status og optionelle tasks fra `task-execution-rules.md`

**Kilde:** `task-execution-rules.md` definerer et klart system for task-status (`[ ]`, `[x]`, `[-]`) og optionelle tasks markeret med `*`.

**Problem:** Øvelse 3 beder deltagerne tilføje en task til `tasks.md`, men forklarer ikke task-status-systemet. Deltagerne ved ikke at Kiro automatisk opdaterer `[x]` når en task er færdig, eller at `*` markerer optionelle tasks.

**Forslag:** Tilføj en kort forklaring i øvelse 3 (Del 1) om task-status-syntaksen:
```
Bemærk: I tasks.md bruges [ ] for ufærdige tasks og [x] for færdige. 
Kiro opdaterer automatisk status når den implementerer en task. 
Tasks markeret med * er optionelle — Kiro spørger dig før den starter dem.
```

Overvej også at markere 1-2 tasks i `fangst-registrering/tasks.md` som optionelle (`*`) så deltagerne kan opleve mekanismen i praksis.

### Anbefaling 3: Gated workflow-konceptet fra `endpoint-conversion-workflow.md`

**Kilde:** `endpoint-conversion-workflow.md` definerer en 10-trins workflow med obligatoriske "gates" — checkpoints der skal bestås før man kan fortsætte.

**Problem:** Læringsforløbet præsenterer spec-drevet udvikling som en lineær proces (requirements → design → tasks → kode). I virkeligheden bruger teamet gates og checkpoints for at sikre kvalitet undervejs.

**Forslag:** Tilføj et "Checkpoint"-koncept i øvelse 3. Efter Del 2 (kør applikationen) og før Del 4 (tilføj ny funktionalitet), indsæt en checkpoint-task i `tasks.md`:
```markdown
- [ ] 5. Checkpoint: Verificer at alle eksisterende tests er grønne
```

Forklar kort at i rigtige projekter bruger man checkpoints til at sikre at alt fungerer før man bygger videre. Dette afspejler teamets faktiske praksis uden at introducere den fulde kompleksitet af 10-trins gated workflows.

### Anbefaling 4: Test-organisering fra `test-patterns.md`

**Kilde:** `test-patterns.md` definerer klare regler for test-filnavne, assertion-patterns og test-placering.

**Problem:** Øvelse 3 beder Kiro om at skrive tests, men giver ingen guidance om hvor de skal placeres eller hvordan de skal struktureres. Deltagerne lærer ikke at test-organisering er en bevidst beslutning.

**Forslag:** Tilføj en kort bemærkning i øvelse 3 om test-konventioner:
```
Bemærk: Vi placerer tests i app/tests/ med navnekonventionen test_<feature>.py. 
I større projekter bruger man steering-filer til at definere test-patterns 
så Kiro konsistent placerer og navngiver tests korrekt.
```

### Anbefaling 5: Spec-templates fra `implementation-task.md` og `master-plan.md`

**Kilde:** Teamet bruger detaljerede templates til at standardisere specs på tværs af repositories.

**Problem:** Øvelse 2 beder deltagerne om at generere en spec fra bunden, men viser ikke at man i praksis ofte bruger templates som udgangspunkt. Templates sikrer at vigtige sektioner ikke glemmes.

**Forslag:** Nævn kort i øvelse 2 at teams ofte bruger spec-templates:
```
I rigtige projekter bruger man ofte spec-templates der sikrer at alle 
vigtige sektioner er med (requirements, design, tasks, test-strategi). 
Kiro kan bruge templates fra steering-filer som udgangspunkt.
```

Dette behøver ikke være en hands-on øvelse — bare en awareness-note der viser at spec-drevet udvikling skalerer via standardisering.

### Anbefaling 6: Verifikation mod autoritative kilder fra `response-format-validation.md`

**Kilde:** `response-format-validation.md` kræver at response-formater verificeres mod autoritative kilder (XSLT, Java Mapper, model-klasser) — aldrig baseret på antagelser.

**Problem:** Læringsforløbet har ingen øvelse der træner deltagerne i at verificere AI-genereret kode mod en autoritativ kilde. Deltagerne lærer at generere kode, men ikke at validere den systematisk.

**Forslag:** Tilføj en mini-øvelse i øvelse 3 (Del 2) hvor deltagerne sammenligner Kiros genererede response-format med specens definition:
```
Sammenlign response-formatet fra Swagger UI med det der er defineret i 
.kiro/specs/fangst-registrering/design.md. Er de identiske? 
Hvis ikke, hvad er forskellen?
```

Dette introducerer princippet om at AI-output altid skal verificeres mod specen — den "autoritative kilde" i dette læringsforløb.

---

### Samlet vurdering af steering-filerne

De 5 steering-filer og 6 templates er stærkt specialiserede til Oracle Forms → LoopBack-migrationen. De er **ikke egnede til direkte brug** i læringsforløbet, men de indeholder **6 generelle principper** der kan inkorporeres i forenklet form:

| Princip | Kilde | Foreslået integration |
|---------|-------|-----------------------|
| Steering som konfiguration | Alle steering-filer | Ny `.kiro/steering/` eksempel + forklaring |
| Task-status og optionelle tasks | `task-execution-rules.md` | Forklaring i øvelse 3 + `*`-markering i tasks |
| Gated checkpoints | `endpoint-conversion-workflow.md` | Checkpoint-task i øvelse 3 |
| Test-organisering | `test-patterns.md` | Bemærkning om test-konventioner i øvelse 3 |
| Spec-templates | `implementation-task.md`, `master-plan.md` | Awareness-note i øvelse 2 |
| Verifikation mod autoritativ kilde | `response-format-validation.md` | Mini-øvelse i øvelse 3 |

Disse 6 tilføjelser ville give deltagerne et mere realistisk billede af hvordan spec-drevet AI-udvikling fungerer i praksis, uden at overbelaste et begynder-venligt forløb.

