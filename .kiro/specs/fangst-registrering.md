# Spec: Fangstregistrering

## Oversigt

Denne spec beskriver funktionaliteten til at registrere, hente og slette fangster i FangstLog-systemet. En "fangst" repræsenterer en fiskers indberetning af hvad der er landet på én fisketur.

---

## Krav

### Funktionelle krav

| ID | Beskrivelse | Prioritet |
|----|-------------|-----------|
| FR-01 | Systemet skal kunne modtage en ny fangstregistrering med dato, fartøjsnavn, fisker-ID, fiskeart og mængde i kg | Høj |
| FR-02 | Systemet skal returnere en unik ID for hver registrering | Høj |
| FR-03 | Systemet skal kunne hente en liste af alle registreringer, filtreret på dato-interval | Høj |
| FR-04 | Systemet skal kunne hente én specifik registrering ud fra dens ID | Middel |
| FR-05 | Systemet skal kunne slette en registrering ud fra dens ID | Middel |
| FR-06 | Systemet skal afvise registreringer med negativ mængde | Høj |
| FR-07 | Systemet skal afvise registreringer med fremtidig dato | Høj |

### Ikke-funktionelle krav

| ID | Beskrivelse |
|----|-------------|
| NFR-01 | API'et skal svare inden for 500ms under normal belastning |
| NFR-02 | Alle API-svar skal returneres som JSON |
| NFR-03 | Fejlsvar skal indeholde en beskrivende fejlmeddelelse på dansk |

---

## Datamodel

### Fangst (FangstRegistrering)

```
FangstRegistrering
├── id: string (UUID, auto-genereret)
├── dato: date (påkrævet, må ikke være fremtidig)
├── fartoej_navn: string (påkrævet, max 100 tegn)
├── fisker_id: string (påkrævet, format: "FIS-XXXX")
├── fiskeart: string (påkrævet, se tilladte værdier nedenfor)
├── maengde_kg: float (påkrævet, skal være > 0)
└── registreret_tidspunkt: datetime (auto-sat ved oprettelse)
```

**Tilladte fiskearter:**
- `torsk`
- `sild`
- `makrel`
- `rødspætte`
- `kuller`
- `andet`

---

## API-endepunkter

### POST /fangster
Opretter en ny fangstregistrering.

**Request body:**
```json
{
  "dato": "2024-03-15",
  "fartoej_navn": "Havørnen",
  "fisker_id": "FIS-0042",
  "fiskeart": "torsk",
  "maengde_kg": 340.5
}
```

**Succesfuldt svar (201 Created):**
```json
{
  "id": "a3f8c1d2-...",
  "dato": "2024-03-15",
  "fartoej_navn": "Havørnen",
  "fisker_id": "FIS-0042",
  "fiskeart": "torsk",
  "maengde_kg": 340.5,
  "registreret_tidspunkt": "2024-03-15T14:23:11"
}
```

**Fejlsvar (422 Unprocessable Entity):**
```json
{
  "fejl": "Mængde skal være større end 0"
}
```

---

### GET /fangster
Henter alle fangstregistreringer, med valgfri filtrering.

**Query parametre:**
- `fra_dato` (valgfri): ISO-dato, fx `2024-01-01`
- `til_dato` (valgfri): ISO-dato, fx `2024-12-31`

**Svar (200 OK):**
```json
[
  { ... },
  { ... }
]
```

---

### GET /fangster/{id}
Henter én specifik registrering.

**Svar (200 OK):** Fangst-objekt  
**Fejlsvar (404 Not Found):** `{"fejl": "Fangst ikke fundet"}`

---

### DELETE /fangster/{id}
Sletter en registrering.

**Svar (204 No Content):** Ingen body  
**Fejlsvar (404 Not Found):** `{"fejl": "Fangst ikke fundet"}`

---

## Tasks

- [ ] Implementér datamodel med Pydantic
- [ ] Opret in-memory storage (dict) til fangster
- [ ] Implementér POST /fangster med validering
- [ ] Implementér GET /fangster med dato-filtrering
- [ ] Implementér GET /fangster/{id}
- [ ] Implementér DELETE /fangster/{id}
- [ ] Skriv tests for alle endepunkter
- [ ] Skriv tests for valideringsregler (FR-06, FR-07)
