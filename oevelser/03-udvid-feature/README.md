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

## Startpunkt: En delvist eksisterende applikation

Projektet indeholder allerede en simpel skelet-applikation i `app/src/`. Undersøg den:

```
app/
├── src/
│   ├── main.py          ← FastAPI applikation (tom/minimal)
│   └── models.py        ← Pydantic datamodeller (tom/minimal)
└── tests/
    └── test_placeholder.py
```

---

## Del 1: Lad Kiro implementere fangst-registrering (20 min)

Åbn Kiro-chat og send:

```
Kig på specen i .kiro/specs/fangst-registrering.md og den eksisterende 
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

---

## Del 2: Kør applikationen (10 min)

Aktivér conda-miljøet og kør applikationen:

```bash
conda activate kiro-laering
cd app
uvicorn src.main:app --reload
```

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

---

## Del 4: Tilføj en ny funktionalitet via spec-ændring (15 min)

Nu skal du *selv* ændre en spec og se effekten. Vi tilføjer muligheden for at **søge i fangster på fiskeart**.

Åbn `.kiro/specs/fangst-registrering.md` og tilføj følgende til listen af query-parametre under `GET /fangster`:

```markdown
- `fiskeart` (valgfri): filtrer på fiskeart, fx `torsk`
```

Tilføj også et nyt krav under Funktionelle krav:

```markdown
| FR-08 | Systemet skal understøtte filtrering af fangster på fiskeart | Middel |
```

Og en ny task:
```markdown
- [ ] Implementér fiskeart-filtrering i GET /fangster
```

Gem filen, og send derefter til Kiro:
```
Jeg har opdateret .kiro/specs/fangst-registrering.md med et nyt krav (FR-08) 
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
