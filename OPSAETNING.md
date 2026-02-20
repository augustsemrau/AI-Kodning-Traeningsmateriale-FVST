# Opsætningsvejledning

Denne guide hjælper dig med at sætte dit arbejdsmiljø op, så du er klar til at arbejde med Kiro og dette læringsforløb.

Du behøver ca. **15–20 minutter** første gang.

---

## Forudsætninger

Du skal have følgende installeret på din computer:

- **Kiro** — download fra [kiro.dev](https://kiro.dev) (gratis at downloade)
- **conda** — enten via [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (anbefalet, lille) eller [Anaconda](https://www.anaconda.com/) (større)
- **Git** — til at klone dette repository (eller download som ZIP)

Har du ikke conda? Se afsnittet [Installer conda](#installer-conda) nedenfor.

---

## Trin 1: Hent dette repository

**Mulighed A — Med Git (anbefalet):**
```bash
git clone <repository-url>
cd kiro-laeringsforloeb
```

**Mulighed B — Download ZIP:**
1. Download og pak ZIP-filen ud
2. Åbn en terminal og naviger til mappen:
```bash
cd sti/til/kiro-laeringsforloeb
```

---

## Trin 2: Åbn mappen i Kiro

1. Start Kiro
2. Vælg **File → Open Folder** (eller `Ctrl+K Ctrl+O`)
3. Vælg mappen `kiro-laeringsforloeb`

Du bør nu se filstrukturen i venstre panel.

---

## Trin 3: Sæt det virtuelle miljø op med Kiro

Nu kommer det smarte: vi beder Kiro om at sætte miljøet op for os.

1. Åbn Kiro's chat-panel (klik på chat-ikonet til venstre, eller tryk `Ctrl+L`)
2. Skriv følgende besked til Kiro:

```
Jeg har åbnet dette repository. Hjælp mig med at oprette et conda virtuelt miljø 
til dette projekt og installer de nødvendige Python-pakker fra requirements.txt. 
Kør kommandoerne i terminalen.
```

Kiro vil herefter:
- Læse `requirements.txt`
- Foreslå og køre kommandoer til at oprette miljøet
- Aktivere miljøet

> 💡 **Tip:** Hvis Kiro beder om tilladelse til at køre kommandoer, skal du godkende det. Du kan altid se præcis hvad den vil gøre, inden du godkender.

**Alternativt — gør det selv manuelt:**
```bash
conda create -n kiro-laering python=3.11 -y
conda activate kiro-laering
pip install -r requirements.txt
```

---

## Trin 4: Konfigurer AWS Bedrock i Kiro

Kiro bruger Claude via AWS Bedrock som sprogmodel. Din organisation har adgang til dette.

1. Åbn Kiro-indstillinger: **Kiro → Settings** (eller `Ctrl+,`)
2. Søg efter "Bedrock" eller "Model Provider"
3. Vælg **AWS Bedrock** som provider
4. Indtast dine AWS-credentials (spørg din projektleder eller systemadministrator, hvis du ikke har disse)

> ⚠️ **Vigtigt:** Del aldrig dine AWS-credentials med andre eller commit dem til Git. De skal kun stå i Kiros indstillinger lokalt på din computer.

Har du problemer med adgang? Kontakt Kim eller den tekniske ansvarlige på projektet.

---

## Trin 5: Verificer at alt virker

### 5a: Tjek at Python-miljøet fungerer

Åbn en terminal i Kiro (`Ctrl+ø` eller **Terminal → New Terminal**) og kør:

```bash
conda activate kiro-laering
cd app
pytest tests/test_placeholder.py -v
```

Du bør se output der ligner:
```
tests/test_placeholder.py::test_placeholder PASSED
```

Hvis du ser fejl som `ModuleNotFoundError` eller `command not found`, tjek [Fejlfinding](#fejlfinding) nedenfor.

### 5b: Tjek at Kiro kan se projektet

Åbn Kiro's chat og skriv:

```
Hej! Kan du se filerne i dette repository? Beskriv kort hvad du ser i roden af projektet.
```

Svarer Kiro fornuftigt og nævner filer som `README.md`, `app/` og `.kiro/`? Så er du klar til at begynde!

---

## Installer conda

Har du ikke conda installeret?

1. Gå til [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)
2. Download installationsprogrammet til dit styresystem (Windows, Mac eller Linux)
3. Følg installationsguiden
4. Åbn en ny terminal/kommandoprompt og tjek at det virkede:
```bash
conda --version
```

---

## Fejlfinding

**"conda: command not found"**
→ Conda er ikke i din PATH. Prøv at genstarte terminalen, eller geninstaller Miniconda og sæt "Add to PATH" til ved installation.

**Kiro kan ikke forbinde til AWS Bedrock**
→ Tjek følgende:
1. Er dine AWS-credentials korrekte? Prøv at logge ind på AWS Console i en browser for at verificere.
2. Har din bruger adgang til Bedrock-tjenesten? Spørg din systemadministrator.
3. Er du på det rigtige AWS-region? Bedrock er ikke tilgængeligt i alle regioner.
4. Prøv at genstarte Kiro — nogle gange hjælper det.
5. Kontakt den tekniske ansvarlige hvis ovenstående ikke løser problemet.

**Pakker kan ikke installeres**
→ Tjek at du har aktiveret conda-miljøet (`conda activate kiro-laering`) inden du kører `pip install`.

**"ModuleNotFoundError" når du kører tests eller applikationen**
→ Tjek at:
1. Du har aktiveret conda-miljøet (`conda activate kiro-laering`)
2. Du står i `app/`-mappen (ikke i `app/src/`)
3. Der findes `__init__.py`-filer i både `app/src/` og `app/tests/` (de bør allerede være der)

---

Klar? Gå til [Øvelse 1 →](./oevelser/01-laes-en-spec/README.md)
