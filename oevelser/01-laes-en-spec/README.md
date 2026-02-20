# Øvelse 1: Læs en spec — Hvad er det egentlig?

**Niveau:** Begynder  
**Tid:** Ca. 20–30 minutter  
**Kode:** Ikke nødvendigt  
**Forudsætninger:** Kiro installeret og åbnet i projektet

---

## Læringsmål

Når du er færdig med denne øvelse, kan du:
- Forklare hvad en spec er og hvad den bruges til
- Finde og åbne en spec i Kiro
- Identificere de vigtigste dele af en spec
- Stille Kiro spørgsmål om en spec og forstå svarene

---

## Baggrund: Hvad er en spec?

I spec-drevet udvikling starter alt med en **specifikation** — en struktureret beskrivelse af hvad et stykke software skal gøre. Tænk på det som en tegning, inden man bygger et hus.

I Kiro er en spec organiseret som en **mappe** med tre filer:

- **`requirements.md`** — hvad systemet skal kunne (krav og acceptkriterier)
- **`design.md`** — hvordan systemet skal bygges (datamodel, API-design, arkitektur)
- **`tasks.md`** — hvilke konkrete opgaver der skal udføres for at implementere specen

### Hvad er krav (requirements)?

Krav beskriver *hvad* systemet skal gøre. Der er to typer:
- **Funktionelle krav** — hvad systemet *skal kunne* (fx "systemet skal kunne oprette en fangst")
- **Ikke-funktionelle krav** — hvad systemet *skal opfylde* udover funktionalitet (fx hastighed, sikkerhed, sprog)

Hvert krav har **acceptkriterier** — konkrete, testbare betingelser der afgør om kravet er opfyldt.

### Hvad er design?

Designet beskriver *hvordan* kravene skal realiseres teknisk: datamodeller, API-endepunkter, filstruktur og arkitekturbeslutninger. En **datamodel** er en oversigt over de informationer systemet arbejder med — tænk på det som en skabelon for de data der gemmes.

### Hvad er Tasks?

Tasks-sektionen er en **opgaveliste** — en nedbrydning af specen i konkrete, afgrænsede implementeringsopgaver. Tænk på det som en to-do-liste for den der skal bygge systemet. Hver task beskriver ét stykke arbejde, fx "Implementér POST /fangster med validering". Tasks kan udføres af en udvikler manuelt, eller man kan bede Kiro om at udføre dem én ad gangen.

---

## Del 1: Find og åbn en spec (5 min)

1. I Kiro, kig i filpanelet til venstre
2. Udvid mappen `.kiro` → `specs` → `fangst-registrering`
3. Du ser tre filer: `requirements.md`, `design.md` og `tasks.md`
4. Åbn **`requirements.md`** først
5. Åbn også **`tasks.md`** og se hvordan specens krav er nedbrudt i konkrete opgaver

Du ser nu kravene for FangstLog-systemets centrale funktion: at registrere fangster.

---

## Del 2: Forstå specen (10 min)

Læs `requirements.md` og `design.md` igennem og besvar følgende spørgsmål for dig selv:

**Om kravene (requirements.md):**
1. Hvad sker der, hvis nogen prøver at registrere en fangst med en negativ mængde?
2. Hvad sker der, hvis nogen prøver at registrere en fangst med en dato i fremtiden?
3. Hvilke typer fisk er det tilladt at registrere?

**Om designet (design.md):**
4. Hvilke informationer indeholder en fangstregistrering?
5. Hvad genereres automatisk af systemet (og skal altså ikke angives af brugeren)?

**Om API'et (design.md):**
6. Hvad returnerer systemet, når man opretter en ny fangst?
7. Kan man hente fangster fra en bestemt periode? Hvordan?

---

## Del 3: Spørg Kiro (10 min)

Nu skal du bruge Kiro som sparringspartner. Åbn Kiro-chat (`Ctrl+L`) med specen åben, og prøv disse spørgsmål:

**Spørgsmål 1 — Forstå konteksten:**
```
Jeg kigger på specen i .kiro/specs/fangst-registrering/. 
Kan du forklare mig med enkle ord, hvad dette system skal bruges til, 
som om du forklarede det til en ikke-teknisk person?
```

**Spørgsmål 2 — Dyk ned i detaljer:**
```
I denne spec, hvad er forskellen på et "funktionelt krav" og et 
"ikke-funktionelt krav"? Giv et eksempel fra specen på hver type.
```

**Spørgsmål 3 — Tænk kritisk:**
```
Er der noget i denne spec, som du synes mangler, eller som du mener 
kunne skabe problemer, når man skal implementere den?
```

Læs Kiros svar og følg op med opfølgende spørgsmål, hvis der er noget du ikke forstår.

> 💡 **Tip:** Hvis Kiro giver lange eller upræcise svar, kan du prøve at starte en ny chat-session (`Ctrl+L` → klik på "+" for ny chat). Kiro fungerer bedst med friske samtaler.

---

## Del 4: Sammenlign to specs (5 min)

Åbn nu mappen **`rapport-generering`** og kig på dens `requirements.md`. Sammenlign den med fangst-registreringens krav.

Spørg Kiro:
```
Jeg har nu kigget på specs for både fangst-registrering og rapport-generering 
i .kiro/specs/. Hvilken af disse to specs beskriver funktionalitet som afhænger 
af den anden? Forklar hvorfor.
```

---

## Refleksion

Tænk over:
- Hvilke dele af en spec er lette at forstå, selv uden teknisk baggrund?
- Hvilke dele kræver mere teknisk viden?
- Hvad synes du er værdien i at have en spec, *inden* man begynder at skrive kode?

---

## ✅ Øvelsen er færdig, når du kan svare på:

- [ ] Hvad er formålet med en spec?
- [ ] Hvad er forskellen på funktionelle og ikke-funktionelle krav?
- [ ] Hvad er forskellen på requirements.md, design.md og tasks.md?
- [ ] Hvorfor er datamodellen vigtig?

---

**Næste skridt:** [Øvelse 2 — Bed Kiro om at skrive en spec →](../02-bed-kiro-skrive-spec/README.md)
