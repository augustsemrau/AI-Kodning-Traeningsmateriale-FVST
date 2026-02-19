# Øvelse 4: Node.js Refaktorering — Migrer en feature

**Niveau:** Avanceret  
**Tid:** Ca. 60–90 minutter  
**Kode:** Node.js/TypeScript + Jest  
**Forudsætninger:** Øvelse 1–3 gennemført, Node.js installeret

---

## Læringsmål

Når du er færdig med denne øvelse, kan du:
- Bruge en eksisterende spec som fundament for en sprogmigration
- Bede Kiro om at oversætte implementering fra Python til Node.js
- Skrive en migrerings-spec der beskriver både kilde- og målarkitektur
- Arbejde med Kiro i et Node.js/TypeScript projekt
- Vurdere AI-genereret kode kritisk i en migreringssammenhæng

---

## Baggrund: Refaktorering med AI

Dette er kernen i Fiskeristyrelsen-projektet: at tage eksisterende systemer og modernisere dem til ny teknologi. I den virkelige verden er kilden Oracle Forms — her er kilden vores Python/FastAPI applikation. Princippet er det samme:

1. Vi har **eksisterende funktionalitet** (Python)
2. Vi har **en spec** der beskriver hvad systemet gør
3. Vi beder Kiro om at **implementere den samme spec** i et nyt teknologistack (Node.js/Express/TypeScript)
4. Vi verificerer at den nye implementering opfører sig identisk med den gamle

Specen er vores **"sandhedskilde"** — den er uafhængig af implementeringssproget.

---

## Forudsætninger: Node.js setup

Tjek at Node.js er installeret:
```bash
node --version  # skal være v18 eller nyere
npm --version
```

Har du ikke Node.js? Bed Kiro om hjælp:
```
Jeg har ikke Node.js installeret. Kan du guide mig til at installere det 
på mit styresystem?
```

---

## Del 1: Opret Node.js projektstruktur (15 min)

Bed Kiro om at sætte Node.js projektet op:

```
Vi skal bygge en Node.js/TypeScript version af FangstLog API'et.

Opret en projektstruktur i mappen app-node/ med:
- Express.js som web-framework
- TypeScript med strict mode
- Jest som test-framework
- Nodemon til udvikling

Projektet skal have samme API-struktur som beskrevet i 
.kiro/specs/fangst-registrering.md

Opret package.json, tsconfig.json og en basiskonfiguration der kan 
køres med: npm install && npm run dev
```

Lad Kiro oprette filerne og kør derefter:
```bash
cd app-node
npm install
```

---

## Del 2: Skriv en migrerings-spec (20 min)

Før Kiro implementerer koden, skal vi skrive en spec der beskriver migreringen. Dette er vigtigt fordi:

- Det tvinger os til at tænke over hvad der *ændrer* sig vs. hvad der *forbliver det samme*
- Det giver os et dokument vi kan referere til, hvis noget går galt
- Det er god praksis i et rigtigt moderniseringsprojekt

Bed Kiro om at hjælpe:

```
Jeg vil skrive en migrerings-spec der beskriver overflytningen af 
fangst-registrering fra Python/FastAPI til Node.js/Express/TypeScript.

Brug .kiro/specs/fangst-registrering.md som udgangspunkt, men skriv en 
ny spec i .kiro/specs/fangst-registrering-nodejs.md der:

1. Beskriver kildeteknologi (Python/FastAPI) og målteknologi (Node.js/Express/TypeScript)
2. Markerer hvilke krav der er uændrede (samme funktionalitet, nyt sprog)
3. Beskriver Node.js-specifikke implementeringsvalg (fx TypeScript interfaces i stedet for Pydantic models)
4. Inkluderer en migrations-checkliste

Hold API-kontrakten (endepunkter, request/response format) identisk med den originale spec.
```

Gennemgå den genererede spec og tilret evt. inden du fortsætter.

---

## Del 3: Implementér i Node.js (20 min)

Nu implementerer vi. Send til Kiro:

```
Implementér .kiro/specs/fangst-registrering-nodejs.md i app-node/ mappen.

Krav:
- Brug TypeScript interfaces (ikke klasser) til datamodeller
- In-memory storage med et Map<string, FangstRegistrering>
- Samme API-endepunkter og response-format som Python-versionen
- Samme valideringsregler (FR-06: ingen negativ mængde, FR-07: ingen fremtidig dato)
- Fejlmeddelelser på dansk
- Jest-tests for alle endepunkter og valideringsregler

Strukturér koden i:
- src/models/fangst.ts (TypeScript interfaces)
- src/storage/fangstStore.ts (in-memory storage)
- src/routes/fangster.ts (Express routes)
- src/app.ts (Express app)
- src/server.ts (start-fil)
- tests/fangster.test.ts (Jest tests)
```

---

## Del 4: Krydstest de to implementeringer (15 min)

Kør begge API'er og test at de opfører sig identisk.

**Python API (terminal 1):**
```bash
conda activate kiro-laering
cd app
uvicorn src.main:app --port 8000 --reload
```

**Node.js API (terminal 2):**
```bash
cd app-node
npm run dev  # kører typisk på port 3000
```

Test begge med de samme requests. Brug fx `curl` eller Kiro-chat til at hjælpe dig med at formulere requests:

```
Kan du give mig curl-kommandoer til at teste følgende mod begge API'er 
(port 8000 for Python, port 3000 for Node.js)?

1. Opret en fangst (Havørnen, FIS-0001, torsk, 200 kg, dagens dato)
2. Hent alle fangster
3. Forsøg at oprette en fangst med -5 kg mængde
4. Forsøg at oprette en fangst med en dato i morgen
```

Er svarene identiske? Hvis ikke — hvad er forskelligt?

---

## Del 5: Refleksion og dokumentation (10 min)

Spørg Kiro:

```
Baseret på det vi har lavet i denne øvelse:

1. Hvad er de vigtigste udfordringer ved at bruge AI til at migrere kode 
   fra ét programmeringssprog til et andet?

2. Hvad er spec'ens rolle i at sikre at den migrerede version er korrekt?

3. Hvad ville du anbefale som næste skridt, hvis vi skulle migrere 
   autentificeringsspecen (bruger-autentificering.md) til Node.js?
```

---

## ✅ Øvelsen er færdig, når:

- [ ] Node.js projektet kører uden fejl (`npm run dev`)
- [ ] Alle Jest-tests er grønne (`npm test`)
- [ ] Du har testet begge API'er med de samme inputs og fået identiske svar
- [ ] Du har `.kiro/specs/fangst-registrering-nodejs.md`
- [ ] Du kan forklare hvad spec'ens rolle er i en migreringsproces

---

## Videre fra her

Du har nu gennemgået hele spektret fra spec-læsning til migrering. De næste naturlige skridt i et rigtigt projekt ville være:

- **Autentificering i Node.js** — migrer `bruger-autentificering.md`
- **Rapporter i Node.js** — migrer `rapport-generering.md`
- **Database-integration** — byt in-memory storage ud med en rigtig database
- **CI/CD pipeline** — automatiser test og deployment

---

*Tillykke — du har gennemført læringsforløbet!* 🎉
