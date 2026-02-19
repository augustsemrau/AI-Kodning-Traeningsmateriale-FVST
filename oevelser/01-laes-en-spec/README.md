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

En god spec indeholder typisk:
- **Oversigt** — hvad handler denne spec om?
- **Krav** — hvad *skal* systemet kunne? (funktionelle krav)
- **Krav** — hvad *skal* systemet opfylde? (ikke-funktionelle krav som hastighed, sikkerhed)
- **Datamodel** — hvilke data arbejder systemet med?
- **API-endepunkter** — hvordan "taler" man med systemet?
- **Tasks** — hvilke konkrete opgaver skal løses for at implementere specen?

---

## Del 1: Find og åbn en spec (5 min)

1. I Kiro, kig i filpanelet til venstre
2. Udvid mappen `.kiro` → `specs`
3. Åbn filen **`fangst-registrering.md`**

Du ser nu en spec for FangstLog-systemets centrale funktion: at registrere fangster.

---

## Del 2: Forstå specen (10 min)

Læs specen igennem og besvar følgende spørgsmål for dig selv (du behøver ikke at skrive dem ned):

**Om kravene:**
1. Hvad sker der, hvis nogen prøver at registrere en fangst med en negativ mængde?
2. Hvad sker der, hvis nogen prøver at registrere en fangst med en dato i fremtiden?
3. Hvilke typer fisk er det tilladt at registrere?

**Om datamodellen:**
4. Hvilke informationer indeholder en fangstregistrering?
5. Hvad genereres automatisk af systemet (og skal altså ikke angives af brugeren)?

**Om API'et:**
6. Hvad returnerer systemet, når man opretter en ny fangst?
7. Kan man hente fangster fra en bestemt periode? Hvordan?

---

## Del 3: Spørg Kiro (10 min)

Nu skal du bruge Kiro som sparringspartner. Åbn Kiro-chat (`Ctrl+L`) med specen åben, og prøv disse spørgsmål:

**Spørgsmål 1 — Forstå konteksten:**
```
Jeg kigger på filen .kiro/specs/fangst-registrering.md. 
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

---

## Del 4: Sammenlign to specs (5 min)

Åbn nu **`rapport-generering.md`** og sammenlign den med `fangst-registrering.md`.

Spørg Kiro:
```
Jeg har nu kigget på både fangst-registrering.md og rapport-generering.md. 
Hvilken af disse to specs beskriver funktionalitet som afhænger af den anden? 
Forklar hvorfor.
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
- [ ] Hvad betyder "Tasks"-sektionen i en spec?
- [ ] Hvorfor er datamodellen vigtig?

---

**Næste skridt:** [Øvelse 2 — Bed Kiro om at skrive en spec →](../02-bed-kiro-skrive-spec/README.md)
