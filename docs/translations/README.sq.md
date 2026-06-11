# First Contributions - Albanais

> **Mirësevini në projektin First Contributions!**

## Çfarë është First Contributions?

First Contributions është një projekt i hapur për të ndihmuar programuesit e rinj të bëjnë kontributin e tyre të parë në projekte me kod burim të hapur. Kjo ulej një udhëzues hap pas hapi për të demonstruar si të fork-i, clone-i, shtoni, commit-i, dhe push një ndryshim.

## Si të filloni?

1. **Fork** projektin.
2. **Clone** fork-un në makinën tuaj lokale.
3. Krijoni një degë për ndryshimin tuaj.
4. Bëni ndryshime të vogla (p.sh., përmirësoni dokumentacionin).
5. **Commit** dhe **push** ndryshimet.
6. Krijoni një **Pull Request** në repositorin origjinal.

## Udhëzues hap pas hapi

### 1. Fork projekti

> Klikoni butonin **Fork** në krye të faqes së projektit në GitHub.

### 2. Clone projektin në lokale

```bash
git clone https://github.com/<your-username>/first-contributions.git
cd first-contributions
```

### 3. Krijoni një degë të re

```bash
git checkout -b shtesa-editimi
```

### 4. Bëni ndryshime

Modifikoni ose shtoni dokumentacion, për shembull:

- Përmirësoni README.
- Shtoni shembuj të rinj.

### 5. Commit ndryshimet

```bash
git add .
git commit -m "Shtove përmirësime në README"
```

### 6. Push në fork-un tuaj

```bash
git push origin shtesa-editimi
```

### 7. Krijoni Pull Request

> Shkoni te faqja e fork-ut tuaj në GitHub dhe klikoni **Compare & pull request**.

## Shty ndryshimet në GitHub

Nëse merr ndonjë gabim gjatë shtyrjes, kliko këtu:

<details>
<summary>Shih detajet e gabimit</summary>

```bash
fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'
```

Ky gabim ndodh kur kredencialet e GitHub nuk janë të konfiguruara si duhet.

#### Zgjidhjet e mundshme

- Sigurohuni që po përdorni tokenin e **Personal Access Token (PAT)** në vend të fjalëkalimit.
- Kontrolloni që token-i të ketë të drejtat **repo**.
- Përdorni **Git Credential Manager** për të menaxhuar kredencialet tuaja.

</details>

## Kontributet e mëparshme

Ju mund të shikoni kontributet e mëparshme në seksionin **Contributors** për të parë se si të kontribuoni në mënyrë të suksesshme.

---

**Faleminderit për kontributin tuaj!**
