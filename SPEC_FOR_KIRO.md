# Spec: Komplet Generering af Kiro-Læringsforløb

## Oversigt

Denne spec beskriver alle komponenter i `kiro-laeringsforloeb` repositoryet der **skal genereres eller verificeres af Kiro**, inden læringsforløbet er klar til brug. Specen er skrevet til August (AI/Prompt Engineer hos Trustworks) og bruges som arbejdsdokument under færdiggørelse og test af forløbet.

Filer markeret med ✅ er allerede oprettet af Claude. Filer markeret med 🔧 skal Kiro generere eller verificere.

---

## Allerede oprettede filer ✅

```
README.md
OPSAETNING.md
requirements.txt
app/src/__init__.py
app/src/main.py                     (skelet — Kiro udfylder i øvelse 3)
app/src/models.py                   (skelet — Kiro udfylder i øvelse 3)
app/tests/__init__.py
app/tests/test_placeholder.py       (skelet — Kiro erstatter i øvelse 3)
.kiro/specs/fangst-registrering.md
.kiro/specs/bruger-autentificering.md
.kiro/specs/rapport-generering.md
oevelser/01-laes-en-spec/README.md
oevelser/02-bed-kiro-skrive-spec/README.md
oevelser/03-udvid-feature/README.md
oevelser/04-node-refaktorering/README.md
SPEC_FOR_KIRO.md                    (denne fil)
```

---

## Filer der skal genereres 🔧

### 1. `.gitignore`

**Beskrivelse:** Standard `.gitignore` til Python, Node.js og Kiro.

**Indhold skal inkludere:**
- Python: `__pycache__/`, `*.pyc`, `.pytest_cache/`, `.env`, `*.egg-info/`
- Node.js: `node_modules/`, `dist/`, `.env`
- Kiro: `.kiro/settings/` (men *ikke* `.kiro/specs/` — specs skal være i git)
- conda: `env/`, `.conda/`
- OS: `.DS_Store`, `Thumbs.db`

---

### 2. `app/pytest.ini`

**Beskrivelse:** Pytest-konfiguration så tests kan køres fra `app/`-mappen.

**Indhold:**
```ini
[pytest]
testpaths = tests
pythonpath = .
```

---

### 3. `app/src/main.py` — Fuldt implementeret version

**Beskrivelse:** Komplet FastAPI applikation med alle endepunkter fra `fangst-registrering.md`.

**Krav:**
- Implementér alle 4 endepunkter: POST /fangster, GET /fangster, GET /fangster/{id}, DELETE /fangster/{id}
- In-memory storage som dict: `fangster: dict[str, FangstRegistrering] = {}`
- Validering af FR-06 (negativ mængde) og FR-07 (fremtidig dato) med HTTPException(422)
- Fejlmeddelelser på dansk
- Dato-filtrering på GET /fangster (fra_dato, til_dato som Query parametre)
- Importer modeller fra `models.py`

**Bemærkning til August:** Denne fil *overskriver* det eksisterende skelet. Den bruges som "fasit" til øvelse 3 og kan gemmes separat som `app/src/main_facit.py` til selvevaluering.

---

### 4. `app/src/models.py` — Fuldt implementeret version

**Beskrivelse:** Pydantic-datamodeller baseret på `fangst-registrering.md`.

**Krav:**
- `FiskearterEnum` (str enum med de 6 tilladte fiskearter)
- `FangstInput` (request body model — ingen id eller tidspunkt)
- `FangstRegistrering` (fuld model inkl. auto-genereret id og tidspunkt)

---

### 5. `app/tests/test_fangster.py` — Fulde tests

**Beskrivelse:** Komplet testsuite med pytest + httpx TestClient.

**Krav — tests skal dække:**
- POST /fangster: succesfuld oprettelse, returnerer korrekte felter, returnerer 201
- POST /fangster: afvisning ved negativ mængde (FR-06), returnerer 422
- POST /fangster: afvisning ved fremtidig dato (FR-07), returnerer 422
- POST /fangster: ugyldig fiskeart returnerer fejl
- GET /fangster: returnerer tom liste når ingen fangster
- GET /fangster: returnerer alle fangster
- GET /fangster: dato-filtrering virker korrekt
- GET /fangster/{id}: returnerer korrekt fangst
- GET /fangster/{id}: returnerer 404 for ukendt id
- DELETE /fangster/{id}: sletter fangst, returnerer 204
- DELETE /fangster/{id}: returnerer 404 for ukendt id

**Bemærkning:** Disse tests bruges som "fasit" og kan sammenlignes med hvad øvelse 3-deltagere genererer med Kiro.

---

### 6. `oevelser/03-udvid-feature/hints.md`

**Beskrivelse:** Hint-fil til øvelse 3 for dem der sidder fast. Skal *ikke* afsløre løsningen, men give nudges.

**Format:**
```markdown
# Hints til Øvelse 3

## Hint 1: Kiro skriver ikke altid kode første gang
[hint om at iterere]

## Hint 2: Hvis tests fejler
[hint om at sende fejloutput til Kiro]

## Hint 3: FR-08 filtrering
[hint om query parameter syntax uden at give løsningen]
```

---

### 7. `oevelser/04-node-refaktorering/package-template.json`

**Beskrivelse:** En skabelon `package.json` til øvelse 4 som et startpunkt, så Kiro ikke skal starte fra nul.

**Krav:**
- Afhængigheder: express, typescript, @types/express, @types/node
- Dev-afhængigheder: jest, ts-jest, @types/jest, nodemon, ts-node
- Scripts: `dev`, `build`, `test`, `start`

---

### 8. `INSTRUKTION_TIL_UNDERVISER.md`

**Beskrivelse:** Intern vejledning til August (eller den der faciliterer forløbet) med noter om sværhedsgrad, kendte faldgruber og forslag til tilpasning.

**Indhold skal dække:**
- Estimeret tidsplan for hvert øvelsesmodul
- Kendte steder hvor Kiro typisk giver mangelfulde svar (og hvad man gør)
- Forslag til hvordan man tilpasser sværhedsgraden op/ned
- Notater om hvad Kim (ikke-teknisk) bør fokusere på vs. en ny udvikler
- Anbefalinger til gruppestørrelse og facilitering

---

## Verifikationsopgaver for August 🧪

Når ovenstående er genereret, skal August verificere følgende:

### Teknisk verifikation
- [ ] `conda create -n kiro-laering python=3.11 && conda activate kiro-laering && pip install -r requirements.txt` kører uden fejl
- [ ] `cd app && uvicorn src.main:app --reload` starter uden fejl
- [ ] `cd app && pytest tests/ -v` → alle tests grønne
- [ ] Swagger UI på `http://localhost:8000/docs` viser alle endepunkter korrekt
- [ ] Manuel test af valideringsregler via Swagger UI

### Pædagogisk verifikation
- [ ] Øvelse 1 kan gennemføres af en ikke-teknisk person (Kim-test)
- [ ] Øvelse 2 giver Kiro nok kontekst til at skrive en meningsfuld spec
- [ ] Øvelse 3's Kiro-instruktioner er præcise nok til at give ensartet output
- [ ] Øvelse 4 kan gennemføres med Node.js v18+ og npm v9+
- [ ] Tidsestimaterne i øvelserne er realistiske

### Indholdsverifikation
- [ ] Alle specs er konsistente med hinanden (ingen modstridende krav)
- [ ] Fiskeristyrelsen-konteksten er tydelig men fiktiv i alt materiale
- [ ] AWS Bedrock/Kiro-instruktioner er korrekte og opdaterede
- [ ] Ingen rigtige persondata, credentials eller systemoplysninger er inkluderet

---

## Kendte åbne spørgsmål

Disse punkter bør afklares af August inden lancering:

1. **Kiro-version:** Er der specifikke Kiro-versionskrav til at spec-workflow fungerer som beskrevet?
2. **AWS Bedrock adgang:** Skal brugerne have individuelle AWS-credentials, eller bruges en delt profil?
3. **Conda vs. venv:** Er conda standard på projektets computere, eller bør vi tilbyde venv som alternativ?
4. **Netværksadgang:** Kræver Kiro internetadgang under øvelserne, eller kan det fungere offline?

---

*Senest opdateret: Februar 2026 | Trustworks / IT-fundament projektet*
