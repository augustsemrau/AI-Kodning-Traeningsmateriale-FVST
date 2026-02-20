# Hints til Øvelse 3

Sidder du fast? Her er nogle hints der kan hjælpe dig videre — uden at afsløre løsningen.

---

## Hint 1: Kiro skriver ikke altid kode første gang

Hvis Kiro giver dig en forklaring i stedet for at skrive kode, så prøv at være mere direkte. Sig fx: "Implementér koden nu og skriv den i filen `app/src/main.py`." Kiro reagerer bedre på konkrete instruktioner end åbne spørgsmål.

---

## Hint 2: Hvis tests fejler

Kopiér hele fejloutputtet fra terminalen og send det til Kiro i chatten. Kiro er god til at læse fejlbeskeder og rette koden. Skriv fx: "Jeg fik denne fejl da jeg kørte pytest — kan du rette det?"

---

## Hint 3: FR-08 filtrering på fiskeart

Tænk over, hvordan de eksisterende query-parametre (`fra_dato`, `til_dato`) er implementeret i `GET /fangster`. Din nye parameter følger samme mønster — den skal bare filtrere på et andet felt. Kig på hvordan `fra_dato` bruges som inspiration.

---

## Hint 4: Applikationen starter ikke

Tjek at du har aktiveret conda-miljøet (`conda activate kiro-laering`) og at du står i `app/`-mappen, når du kører `uvicorn src.main:app --reload`.

---

## Hint 5: Import-fejl (ModuleNotFoundError)

Hvis du ser `ModuleNotFoundError`, skyldes det sandsynligvis én af to ting:

1. Du kører uvicorn fra den forkerte mappe. Du skal stå i `app/`-mappen (ikke i `app/src/`).
2. Der mangler en `__init__.py`-fil. Python bruger disse filer til at markere mapper som "pakker". Der bør ligge en `__init__.py` i både `app/src/` og `app/tests/`. Hvis de mangler, opret dem som tomme filer:
   ```bash
   touch app/src/__init__.py
   touch app/tests/__init__.py
   ```

---

## Hint 6: Kiro mister kontekst

Hvis Kiro begynder at give mærkelige eller upræcise svar, er det sandsynligvis fordi samtalen er blevet for lang. Start en ny chat-session (`Ctrl+L` → klik på "+" for ny chat) og giv Kiro kontekst igen ved at referere til specen og de relevante filer.

> 💡 **Tip:** Når du starter en ny session, kan du bede Kiro om at læse `tasks.md` for at se hvad der allerede er gjort: "Læs .kiro/specs/fangst-registrering/tasks.md og fortæl mig hvilke tasks der mangler." Tasks markeret med `[x]` er færdige, `[ ]` mangler stadig.
