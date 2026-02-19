# Spec: Brugerautentificering

## Oversigt

Denne spec beskriver et simpelt autentificeringslag til FangstLog-systemet. Formålet er at sikre, at kun autoriserede brugere kan oprette og slette fangstregistreringer. Læsning er offentlig tilgængelig.

> **Bemærkning:** Denne spec beskriver en forenklet autentificeringsmodel til læringsformål. Et produktionssystem ville anvende OAuth2/JWT og integration med eksisterende identity providers.

---

## Krav

### Funktionelle krav

| ID | Beskrivelse | Prioritet |
|----|-------------|-----------|
| FR-01 | Systemet skal understøtte brugerlogin med brugernavn og adgangskode | Høj |
| FR-02 | Ved succesfuldt login returneres et token med 8 timers gyldighed | Høj |
| FR-03 | POST og DELETE på /fangster kræver gyldigt token i Authorization-header | Høj |
| FR-04 | GET-endepunkter er tilgængelige uden autentificering | Høj |
| FR-05 | Udløbne eller ugyldige tokens afvises med 401-fejl | Høj |
| FR-06 | Der skal eksistere mindst én foruddefineret testbruger | Middel |

### Ikke-funktionelle krav

| ID | Beskrivelse |
|----|-------------|
| NFR-01 | Adgangskoder må aldrig gemmes i plaintext |
| NFR-02 | Token-formatet skal være JWT (JSON Web Token) |
| NFR-03 | Fejlmeddelelser ved auth-fejl må ikke afsløre om brugernavnet eller adgangskoden var forkert |

---

## Datamodel

### Bruger

```
Bruger
├── bruger_id: string (UUID)
├── brugernavn: string (unikt)
├── adgangskode_hash: string (bcrypt-hash)
└── rolle: enum [fisker, administrator]
```

### Token-payload

```
TokenPayload
├── sub: string (bruger_id)
├── brugernavn: string
├── rolle: string
├── iat: int (udstedt tidspunkt, Unix timestamp)
└── exp: int (udløbstidspunkt, Unix timestamp)
```

---

## API-endepunkter

### POST /auth/login
Logger en bruger ind og returnerer et JWT-token.

**Request body:**
```json
{
  "brugernavn": "fiskerjens",
  "adgangskode": "hemmelig123"
}
```

**Succesfuldt svar (200 OK):**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "udloeber": "2024-03-15T22:00:00",
  "brugernavn": "fiskerjens",
  "rolle": "fisker"
}
```

**Fejlsvar (401 Unauthorized):**
```json
{
  "fejl": "Ugyldigt brugernavn eller adgangskode"
}
```

---

### GET /auth/mig
Returnerer oplysninger om den aktuelt indloggede bruger (kræver token).

**Svar (200 OK):**
```json
{
  "bruger_id": "...",
  "brugernavn": "fiskerjens",
  "rolle": "fisker"
}
```

---

## Foruddefinerede testbrugere

Disse brugere skal oprettes ved systemstart (seed-data):

| Brugernavn | Adgangskode | Rolle |
|------------|-------------|-------|
| `admin` | `admin123` | administrator |
| `fiskerjens` | `torsk456` | fisker |

> ⚠️ Disse credentials er kun til testbrug i dette læringsforløb.

---

## Tasks

- [ ] Installer og konfigurer `python-jose` (JWT) og `passlib` (bcrypt)
- [ ] Implementér Bruger-datamodel
- [ ] Implementér password-hashing hjælpefunktioner
- [ ] Opret seed-data med testbrugere
- [ ] Implementér POST /auth/login
- [ ] Implementér JWT-token generering og validering
- [ ] Implementér GET /auth/mig med token-validering
- [ ] Tilføj autentificeringsmiddleware til POST/DELETE /fangster
- [ ] Skriv tests for login-flow
- [ ] Skriv tests for afvisning af ugyldige tokens
