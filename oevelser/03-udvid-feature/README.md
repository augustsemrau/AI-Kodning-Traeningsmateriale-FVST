# Øvelse 3: Udvid en feature — Fra spec til kode til test

**Niveau:** Øvet  
**Tid:** Ca. 45–60 minutter  
**Kode:** Python (FastAPI) — du læser, vurderer og kører kode  
**Forudsætninger:** Øvelse 1 og 2 gennemført, conda-miljø aktiveret

---

## Læringsmål

Når du er færdig med denne øvelse, kan du:
- Bede Kiro om at implementere kode baseret på en eksisterende spec
- Køre den genererede kode og dens tests
- Identificere problemer i AI-genereret kode
- Tilpasse en spec og se effekten på den genererede kode

---

## Baggrund: Spec → Kode → Test

I de forrige øvelser har vi kun arbejdet med specs som tekst. Nu tager vi det næste skridt: vi beder Kiro om at *implementere* en spec — altså skrive den faktiske kode.

Arbejdsflowet er:
1. Vi har en spec (allerede skrevet)
2. Kiro genererer kode baseret på specen
3. Kiro genererer tests
4. Vi kører tests for at verificere at koden opfører sig som specen siger
5. Hvis noget ikke stemmer, justerer vi spec eller kode

---

## Startpunkt: Et applikationsskelet

Projektet indeholder allerede et minimalt skelet i `app/src/`. Undersøg det:

```
app/
├── src/
│   ├── __init__.py        ← Python-pakke markør (rør ikke denne)
│   ├── main.py            ← FastAPI applikation (kun et velkomst-endepunkt)
│   └── models.py          ← Pydantic datamodeller (tom — kun TODO-kommentarer)
├── tests/
│   ├── __init__.py        ← Python-pakke markør (rør ikke denne)
│   └── test_placeholder.py ← Placeholder-test (erstattes med rigtige tests)
└── pytest.ini             ← Pytest-konfiguration
```

Åbn `app/src/main.py` og `app/src/models.py` og se at de kun indeholder skelet-kode med TODO-kommentarer. Det er Kiros opgave at udfylde dem.

---

## Del 1: Lad Kiro implementere fangst-registrering (20 min)

Åbn Kiro-chat og send:

```
Kig på specen i .kiro/specs/fangst-registrering/ og det eksisterende 
applikationsskelet i app/src/.

Implementér specen fuldt ud:
1. Udfyld models.py med Pydantic-datamodeller fra specen
2. Implementér alle API-endepunkter i main.py med in-memory storage
3. Sørg for at alle valideringsregler fra specen er implementeret (FR-06, FR-07)
4. Skriv tests i app/tests/test_fangster.py der dækker alle endepunkter 
   og valideringsreglerne

Følg specens krav præcist og returner fejlmeddelelser på dansk.
```

Vent mens Kiro skriver koden. Det kan tage 1–2 minutter.

> 💡 **Tip:** Hvis Kiro giver dig en forklaring i stedet for at skrive kode, prøv at være mere direkte: "Implementér koden nu og skriv den i filerne." Kiro reagerer bedre på konkrete instruktioner.

---

## Del 2: Kør applikationen (10 min)

Aktivér conda-miljøet og kør applikationen:

```bash
conda activate kiro-laering
cd app
uvicorn src.main:app --reload
```

> ⚠️ **Vigtigt:** Du skal stå i `app/`-mappen (ikke i `app/src/`) når du kører uvicorn. Ellers får du `ModuleNotFoundError`.

Åbn din browser på `http://localhost:8000/docs` — her finder du automatisk genereret dokumentation (Swagger UI) for alle endepunkter.

Prøv manuelt at:
1. Oprette en fangst via POST /fangster
2. Hente listen af fangster via GET /fangster
3. Prøve at oprette en fangst med negativ mængde — hvad sker der?
4. Prøve at oprette en fangst med en dato i fremtiden — hvad sker der?

---

## Del 3: Kør tests (10 min)

Stop applikationen (`Ctrl+C`) og kør tests:

```bash
cd app
pytest tests/ -v
```

Du bør se en liste af tests med grønt (passed) eller rødt (failed).

Hvis der er fejlende tests, send output til Kiro:
```
Jeg kørte tests og fik følgende output:
[indsæt output her]

Kan du forklare hvad der fejler og rette det?
```

> 💡 **Tip:** Hvis samtalen med Kiro er blevet lang og svarene upræcise, start en ny chat-session og giv Kiro kontekst igen ved at referere til specen og de relevante filer.

---

## Del 4: Tilføj en ny funktionalitet via spec-ændring (15 min)

Nu skal du *selv* ændre en spec og se effekten. Vi tilføjer muligheden for at **søge i fangster på fiskeart**.

Åbn `.kiro/specs/fangst-registrering/requirements.md` og tilføj følgende nye krav i bunden:

```markdown
11. Systemet skal understøtte filtrering af fangster på fiskeart
    - Acceptance Criteria:
      - GET /fangster accepterer en valgfri query-parameter `fiskeart`
      - Når fiskeart er angivet, returneres kun fangster med den pågældende fiskeart
```

Åbn også `.kiro/specs/fangst-registrering/tasks.md` og tilføj en ny task:
```markdown
- [ ] 9. Implementér fiskeart-filtrering i GET /fangster
```

Gem filerne, og send derefter til Kiro:
```
Jeg har opdateret specen i .kiro/specs/fangst-registrering/ med et nyt krav 
om filtrering på fiskeart. Implementér denne ændring i app/src/main.py 
og tilføj en test for den nye funktionalitet.
```

Kør tests igen og verificer at den nye funktionalitet virker.

---

## ✅ Øvelsen er færdig, når:

- [ ] Applikationen kører uden fejl
- [ ] Alle tests er grønne
- [ ] Du har testet validering manuelt i Swagger UI
- [ ] Du har tilføjet FR-08 og fået Kiro til at implementere det
- [ ] Du kan forklare sammenhængen mellem spec, kode og tests

---

**Næste skridt:** [Øvelse 4 — Node.js refaktorering →](../04-node-refaktorering/README.md)
