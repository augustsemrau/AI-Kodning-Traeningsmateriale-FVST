# Design: Rapportgenerering

## Oversigt

Rapportgenerering er en read-only feature der beregner opsummerende statistik fra eksisterende fangstdata. Den afhænger af fangst-registrering modulet for data.

## Datamodel

### PeriodeRapport
Pydantic BaseModel:
- `periode_fra`: date
- `periode_til`: date
- `genereret_tidspunkt`: datetime (auto-sat)
- `total_registreringer`: int
- `total_maengde_kg`: float
- `fordeling_pr_art`: dict[str, float] (fiskeart → kg)
- `fordeling_pr_fartoej`: dict[str, int] (fartøjsnavn → antal)
- `mest_fanget_art`: str | None (None hvis ingen data)

## Beregningslogik

Rapporten beregnes direkte fra de eksisterende fangstregistreringer i hukommelsen. Algoritmen er:

1. Filtrer alle fangster inden for [fra_dato, til_dato] (begge inklusive)
2. Summer `maengde_kg` grupperet på `fiskeart` → `fordeling_pr_art`
3. Tæl antal registreringer grupperet på `fartoej_navn` → `fordeling_pr_fartoej`
4. Sum alle mængder → `total_maengde_kg`
5. Find arten med højest samlet mængde → `mest_fanget_art`

Beregningslogikken implementeres som en separat service-funktion der kan enhedstestes uafhængigt af API-laget.

## API-design

### GET /rapporter/periode → 200 OK / 422
- Query params: `fra_dato` (påkrævet), `til_dato` (påkrævet), `format` (valgfri: "json" eller "csv")
- Validerer at fra_dato <= til_dato
- Kalder beregningsservice
- Returnerer PeriodeRapport som JSON eller CSV

### CSV-format
```
periode_fra,periode_til,total_registreringer,total_maengde_kg,mest_fanget_art
2024-01-01,2024-03-31,47,12340.5,torsk

art,maengde_kg
torsk,5400.0
sild,3200.5
```

## Fejlhåndtering

```json
{
  "detail": {
    "fejl": "fra_dato skal være før eller lig med til_dato"
  }
}
```

## Afhængigheder

- Afhænger af fangst-registrering modulets in-memory storage (importerer `fangster` dict fra main.py)
