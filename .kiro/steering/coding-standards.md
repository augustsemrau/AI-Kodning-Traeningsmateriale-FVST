---
inclusion: always
---

# Kodestandarder for FangstLog

Disse regler gælder for al kode i FangstLog-projektet.

## Sprog
- Alle fejlmeddelelser skal være på dansk
- Variabelnavne og funktionsnavne må gerne være på dansk (fx `opret_fangst`, `maengde_kg`)

## Arkitektur
- Brug in-memory storage (Python dict) — ingen database
- Alle API-endepunkter skal have docstrings der beskriver funktionaliteten

## Fejlhåndtering
- Fejlsvar skal følge formatet: `{"detail": {"fejl": "beskrivelse"}}`
- Brug HTTPException med passende statuskoder (422 for validering, 404 for ikke fundet)

## Test
- Tests placeres i `app/tests/` med navnekonventionen `test_<feature>.py`
- Brug pytest + httpx TestClient til API-tests
- Ryd in-memory storage mellem tests med en autouse-fixture
