# Design: Fangstregistrering

## Oversigt

FangstLog API er en FastAPI-applikation med in-memory storage til registrering af fangster. Systemet eksponerer et REST API med CRUD-operationer og validering.

## Datamodel

### FiskearterEnum
Enum med tilladte fiskearter:
- `torsk`, `sild`, `makrel`, `rødspætte`, `kuller`, `andet`

### FangstInput (request body)
Pydantic BaseModel til oprettelse af en fangst:
- `dato`: date (påkrævet)
- `fartoej_navn`: str (påkrævet, max_length=100)
- `fisker_id`: str (påkrævet, regex pattern: `^FIS-\d{4}$`)
- `fiskeart`: FiskearterEnum (påkrævet)
- `maengde_kg`: float (påkrævet)

### FangstRegistrering (fuld model)
Pydantic BaseModel med alle felter inkl. auto-genererede:
- `id`: str (UUID, auto-genereret via default_factory)
- `dato`: date
- `fartoej_navn`: str
- `fisker_id`: str
- `fiskeart`: FiskearterEnum
- `maengde_kg`: float
- `registreret_tidspunkt`: datetime (auto-sat via default_factory)

## API-design

### POST /fangster → 201 Created
- Modtager FangstInput
- Validerer: maengde_kg > 0 (FR-06), dato <= i dag (FR-07)
- Opretter FangstRegistrering med auto-genereret id og tidspunkt
- Gemmer i in-memory dict
- Returnerer det fulde FangstRegistrering-objekt

### GET /fangster → 200 OK
- Query params: `fra_dato` (optional date), `til_dato` (optional date)
- Filtrerer listen af fangster på dato-interval (begge inklusive)
- Returnerer liste af FangstRegistrering

### GET /fangster/{id} → 200 OK / 404
- Slår op i dict på id
- Returnerer FangstRegistrering eller 404 med fejlmeddelelse

### DELETE /fangster/{id} → 204 No Content / 404
- Slår op i dict på id
- Sletter fra dict eller returnerer 404 med fejlmeddelelse

## Storage

In-memory storage via Python dict: `fangster: dict[str, FangstRegistrering] = {}`

Nøgle er fangstens UUID (str), værdi er FangstRegistrering-objektet.

## Fejlhåndtering

Alle fejl returneres via FastAPI HTTPException med `detail`-nøgle:
```json
{
  "detail": {
    "fejl": "Beskrivende fejlmeddelelse på dansk"
  }
}
```

## Filstruktur

```
app/
├── src/
│   ├── __init__.py
│   ├── main.py        ← FastAPI app, endpoints, validering
│   └── models.py      ← Pydantic modeller (FangstInput, FangstRegistrering, FiskearterEnum)
├── tests/
│   ├── __init__.py
│   └── test_fangster.py  ← Tests for alle endpoints og valideringsregler
└── pytest.ini
```
