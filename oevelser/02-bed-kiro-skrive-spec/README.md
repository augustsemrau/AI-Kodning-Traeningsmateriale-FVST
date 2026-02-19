# Øvelse 2: Bed Kiro om at skrive en spec

**Niveau:** Let øvet  
**Tid:** Ca. 30–45 minutter  
**Kode:** Minimal (du læser Python, men skriver det ikke selv)  
**Forudsætninger:** Øvelse 1 gennemført

---

## Læringsmål

Når du er færdig med denne øvelse, kan du:
- Formulere en kravbeskrivelse til Kiro på naturligt sprog
- Bede Kiro om at omsætte krav til en færdig spec i Kiro-format
- Vurdere og kritisere en AI-genereret spec
- Iterere på en spec i dialog med Kiro

---

## Baggrund: Kiro som spec-forfatter

En af de mest værdifulde ting ved Kiro er, at den kan hjælpe med at *skrive* specs — ikke kun implementere dem. Det er særligt nyttigt når:

- Man har en klar idé om hvad et system skal gøre, men ikke ved hvordan man formulerer det teknisk
- Man vil sikre at kravene er komplette og ikke mangler noget åbenlyst
- Man vil have et startpunkt, som man kan raffinere

Din opgave er at beskrive en ny feature til FangstLog, og derefter lade Kiro skrive specen — og så kritisk evaluere resultatet.

---

## Den nye feature: Fartøjskartotek

FangstLog mangler en funktion til at holde styr på **fartøjer** (både). Lige nu er et fartøj bare et navn på en fangstregistrering. Vi vil gerne have et egentligt **fartøjskartotek**, hvor man kan:

- Registrere et fartøj med navn, registreringsnummer og ejer
- Slå et fartøj op ud fra registreringsnummer
- Se hvilke fangster der er knyttet til et bestemt fartøj
- Opdatere oplysninger om et fartøj

---

## Del 1: Skriv dit krav til Kiro (10 min)

Åbn Kiro-chat og send følgende besked (du er velkommen til at tilpasse den):

```
Vi arbejder på FangstLog-systemet, som er beskrevet i .kiro/specs/fangst-registrering.md.

Jeg vil gerne tilføje et fartøjskartotek til systemet. Her er mine krav på naturligt sprog:

- Man skal kunne registrere et fartøj med: navn, registreringsnummer (format: "DN-XXXX"), 
  ejerens navn og fartøjets type (fiskekutter, jolle, trawler eller andet)
- Registreringsnummeret skal være unikt
- Man skal kunne slå et fartøj op med dets registreringsnummer  
- Man skal kunne hente en liste af alle fartøjer
- Man skal kunne opdatere oplysninger om et fartøj (navn, ejer, type — men ikke registreringsnummer)
- Man skal kunne slette et fartøj, men kun hvis det ikke har tilknyttede fangster

Kan du skrive en komplet spec til denne feature i Kiro-format 
(som de specs der allerede findes i .kiro/specs/)?
Gem den som .kiro/specs/fartoej-kartotek.md
```

Vent på Kiros svar og lad den skrive filen.

---

## Del 2: Evaluer specen (15 min)

Åbn den nyoprettede fil `.kiro/specs/fartoej-kartotek.md` og gennemgå den kritisk.

Tjek følgende:

**Fuldstændighed:**
- [ ] Er alle 5 funktioner fra kravbeskrivelsen med?
- [ ] Er der API-endepunkter for alle funktioner?
- [ ] Er der en Tasks-sektion?

**Konsistens med eksisterende specs:**
- [ ] Matcher formatet de eksisterende specs (fangst-registrering.md)?
- [ ] Er fejlmeddelelser på dansk?
- [ ] Er datamodellen beskrevet?

**Kvalitet:**
- [ ] Er kravet om at man ikke kan slette et fartøj med fangster håndteret?
- [ ] Er validering af registreringsnummer-format (DN-XXXX) nævnt?
- [ ] Er der ikke-funktionelle krav?

Skriv ned (evt. i en kommentar eller i chatten) hvad du mener mangler eller er uklart.

---

## Del 3: Iterer med Kiro (10 min)

Send en opfølgende besked til Kiro med de mangler eller forbedringer du har identificeret. For eksempel:

```
Tak for specen. Jeg har et par kommentarer:

1. Kravet om at man ikke kan slette et fartøj med tilknyttede fangster 
   er ikke nævnt under Tasks — kan du tilføje det?
2. Kan du tilføje et eksempel på et fejlsvar for forsøg på at registrere 
   et fartøj med et registreringsnummer der allerede eksisterer?
3. [Evt. dine egne observationer]

Opdater filen .kiro/specs/fartoej-kartotek.md med disse ændringer.
```

Se den opdaterede spec og vurder om dine kommentarer er blevet adresseret.

---

## Del 4: Reflektér over processen (5 min)

Spørg Kiro:
```
Hvad er fordelene og ulemperne ved at lade en AI skrive en spec, 
sammenlignet med at en menneske skriver den?
Hvad bør man særligt være opmærksom på?
```

---

## ✅ Øvelsen er færdig, når:

- [ ] Du har filen `.kiro/specs/fartoej-kartotek.md` i projektet
- [ ] Du har identificeret mindst 2 ting at forbedre i Kiros første udkast
- [ ] Du har itereret på specen mindst én gang
- [ ] Du kan beskrive hvornår det giver mening at lade Kiro skrive en spec

---

**Næste skridt:** [Øvelse 3 — Udvid en feature →](../03-udvid-feature/README.md)
