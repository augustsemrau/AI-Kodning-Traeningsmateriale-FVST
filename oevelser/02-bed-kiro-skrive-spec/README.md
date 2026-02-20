# Øvelse 2: Bed Kiro om at skrive en spec

**Niveau:** Let øvet  
**Tid:** Ca. 30–45 minutter  
**Kode:** Minimal (du læser Python, men skriver det ikke selv)  
**Forudsætninger:** Øvelse 1 gennemført

---

## Læringsmål

Når du er færdig med denne øvelse, kan du:
- Formulere en kravbeskrivelse til Kiro på naturligt sprog
- Bede Kiro om at omsætte krav til en færdig spec
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
Vi arbejder på FangstLog-systemet, som er beskrevet i .kiro/specs/fangst-registrering/.

Jeg vil gerne tilføje et fartøjskartotek til systemet. Her er mine krav på naturligt sprog:

- Man skal kunne registrere et fartøj med: navn, registreringsnummer (format: "DN-XXXX"), 
  ejerens navn og fartøjets type (fiskekutter, jolle, trawler eller andet)
- Registreringsnummeret skal være unikt
- Man skal kunne slå et fartøj op med dets registreringsnummer  
- Man skal kunne hente en liste af alle fartøjer
- Man skal kunne opdatere oplysninger om et fartøj (navn, ejer, type — men ikke registreringsnummer)
- Man skal kunne slette et fartøj, men kun hvis det ikke har tilknyttede fangster

Skriv en komplet spec til denne feature i Kiro-format 
(en mappe med requirements.md, design.md og tasks.md under .kiro/specs/).
Opret den som .kiro/specs/fartoej-kartotek/
```

> 💡 **Tip:** Du er velkommen til at tilpasse denne besked med dine egne ord. Prøv at se om Kiro forstår dig, selv hvis du formulerer det anderledes.

> 💡 **Tip:** Hvis Kiro forklarer specen i chatten i stedet for at oprette filer, sig: "Opret filerne nu i .kiro/specs/fartoej-kartotek/".

> **Bemærk:** Kiro bruger sit spec-system med separate filer (requirements.md, design.md, tasks.md) i en mappe. De eksisterende specs i `.kiro/specs/` følger dette format. Kiro bør oprette den nye spec i samme struktur.

Vent på Kiros svar og lad den skrive filen.

---

## Del 2: Evaluer specen (15 min)

Åbn den nyoprettede spec-mappe og gennemgå den kritisk.

Tjek følgende:

**Fuldstændighed:**
- [ ] Er alle 6 funktioner fra kravbeskrivelsen med i requirements.md?
- [ ] Er der API-endepunkter i design.md for alle funktioner?
- [ ] Er der en tasks.md med opgaver?

**Konsistens med eksisterende specs:**
- [ ] Matcher formatet de eksisterende specs (fangst-registrering/)?
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

Opdater specen med disse ændringer.
```

Se den opdaterede spec og vurder om dine kommentarer er blevet adresseret.

> 💡 **Tip:** Hvis Kiro begynder at give upræcise svar eller glemmer kontekst, start en ny chat-session. Lange samtaler kan gøre Kiro mindre præcis.

---

## Del 4: Reflektér over processen (5 min)

Spørg Kiro:
```
Hvad er fordelene og ulemperne ved at lade en AI skrive en spec, 
sammenlignet med at en menneske skriver den?
Hvad bør man særligt være opmærksom på?
```

---

## Godt at vide: Spec-templates og steering

I rigtige projekter bruger man ofte **spec-templates** — standardskabeloner der sikrer at vigtige sektioner altid er med (requirements, design, tasks, test-strategi). Templates gør det lettere at skrive konsistente specs på tværs af et team.

Kiro understøtter også **steering-filer** — vedvarende regler der påvirker Kiros opførsel i alle samtaler. Prøv at åbne filen `.kiro/steering/coding-standards.md` og se hvilke regler der er defineret for dette projekt. Steering-filer er det der gør Kiro-workflows reproducerbare og konsistente — i modsætning til instruktioner du giver i en enkelt chat-session.

Steering-filer har forskellige **inklusionstyper** der styrer hvornår de er aktive:
- **Always** (standard) — sendes med i *hver* samtale med Kiro
- **fileMatch** — inkluderes kun når en fil der matcher et bestemt mønster læses ind (fx `fileMatchPattern: 'README*'`)
- **Manual** — inkluderes kun når du eksplicit refererer til dem med `#` i chatten

I dette projekt bruger `coding-standards.md` typen "always", så reglerne altid er aktive.

---

## ✅ Øvelsen er færdig, når:

- [ ] Du har en fartøjskartotek-spec i projektet
- [ ] Du har identificeret mindst 2 ting at forbedre i Kiros første udkast
- [ ] Du har itereret på specen mindst én gang
- [ ] Du kan beskrive hvornår det giver mening at lade Kiro skrive en spec

---

**Næste skridt:** [Øvelse 3 — Udvid en feature →](../03-udvid-feature/README.md)
