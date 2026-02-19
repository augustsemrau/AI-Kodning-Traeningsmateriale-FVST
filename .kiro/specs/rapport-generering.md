# Spec: Rapportgenerering

## Oversigt

Denne spec beskriver funktionaliteten til at generere opsummerende rapporter over fangstdata. Rapporter er beregnet til at give fiskerikontrollanter og ledere et hurtigt overblik over aktivitet i en given periode.

---

## Krav

### Funktionelle krav

| ID | Beskrivelse | Prioritet |
|----|-------------|-----------|
| FR-01 | Systemet skal kunne generere en perioderapport for et givet datointerval | Høj |
| FR-02 | Perioderapporten skal indeholde total fangstnmæde pr. fiskeart | Høj |
| FR-03 | Perioderapporten skal indeholde antal registreringer pr. fartøj | Høj |
| FR-04 | Perioderapporten skal indeholde den fiskeart med størst samlet fangst | Middel |
| FR-05 | Systemet skal returnere en tom rapport (med nuller) hvis der ikke er data i perioden | Middel |
| FR-06 | Rapporten skal kunne returneres som JSON eller som CSV | Lav |

### Ikke-funktionelle krav

| ID | Beskrivelse |
|----|-------------|
| NFR-01 | Rapporten skal genereres uden eksternt afhængigheder — kun ud fra eksisterende fangstdata |
| NFR-02 | Svartid må ikke overstige 1 sekund for op til 10.000 registreringer |

---

## Datamodel

### PeriodeRapport

```
PeriodeRapport
├── periode_fra: date
├── periode_til: date
├── genereret_tidspunkt: datetime
├── total_registreringer: int
├── total_maengde_kg: float
├── fordeling_pr_art: dict[fiskeart → float]  (kg pr. art)
├── fordeling_pr_fartoej: dict[fartoej_navn → int]  (antal registreringer)
└── mest_fanget_art: string | null  (null hvis ingen data)
```

---

## API-endepunkter

### GET /rapporter/periode
Genererer en perioderapport.

**Query parametre:**
- `fra_dato` (påkrævet): ISO-dato, fx `2024-01-01`
- `til_dato` (påkrævet): ISO-dato, fx `2024-03-31`
- `format` (valgfri): `json` (standard) eller `csv`

**Eksempel-request:**
```
GET /rapporter/periode?fra_dato=2024-01-01&til_dato=2024-03-31
```

**Succesfuldt svar (200 OK) — JSON:**
```json
{
  "periode_fra": "2024-01-01",
  "periode_til": "2024-03-31",
  "genereret_tidspunkt": "2024-04-01T09:00:00",
  "total_registreringer": 47,
  "total_maengde_kg": 12340.5,
  "fordeling_pr_art": {
    "torsk": 5400.0,
    "sild": 3200.5,
    "makrel": 2100.0,
    "rødspætte": 1640.0
  },
  "fordeling_pr_fartoej": {
    "Havørnen": 12,
    "Nordsøen II": 8,
    "Strandlyst": 27
  },
  "mest_fanget_art": "torsk"
}
```

**Succesfuldt svar (200 OK) — CSV:**
```
periode_fra,periode_til,total_registreringer,total_maengde_kg,mest_fanget_art
2024-01-01,2024-03-31,47,12340.5,torsk

art,maengde_kg
torsk,5400.0
sild,3200.5
...
```

**Fejlsvar (422) — hvis fra_dato er efter til_dato:**
```json
{
  "fejl": "fra_dato skal være før eller lig med til_dato"
}
```

---

## Beregningslogik

Rapporten beregnes direkte fra de eksisterende fangstregistreringer i hukommelsen (ingen database). Algoritmen er:

1. Filtrer alle fangster inden for [fra_dato, til_dato] (begge inklusive)
2. Summer `maengde_kg` grupperet på `fiskeart` → `fordeling_pr_art`
3. Tæl antal registreringer grupperet på `fartoej_navn` → `fordeling_pr_fartoej`
4. Sum alle mængder → `total_maengde_kg`
5. Find arten med højest samlet mængde → `mest_fanget_art`

---

## Tasks

- [ ] Implementér PeriodeRapport datamodel
- [ ] Implementér beregningslogik som separat service-funktion
- [ ] Implementér GET /rapporter/periode (JSON-format)
- [ ] Tilføj CSV-format understøttelse
- [ ] Håndtér edge case: tomt datointerval
- [ ] Håndtér edge case: fra_dato > til_dato
- [ ] Skriv enhedstest for beregningslogikken
- [ ] Skriv integrationstest for API-endepunktet
