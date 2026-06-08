[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![Licenca: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Pomagači](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Prvi doprinosi

| <img alt="GitHub Desktop" src="https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png" width="200"> | GitHub komandno-linijski interfejs (CLI) |
| ------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |

Ovo je vodič za nas, **terminal entuzijaste**, koji žele da rade sve u terminalu. Zahvaljujući [GitHub CLI-ju](https://cli.github.com/), to možemo i ostvariti. Zapamtite — vaš prvi doprinos treba da bude **zabavan, koristan i motivišući** da nastavite dalje!

Ovaj vodič je malo zahtjevniji jer **uopšte ne koristimo grafički interfejs**, ali je i dalje veoma zabavan i sigurno ga možete pratiti.

Prvi uslovi su:

* Instaliran **Git** (kako instalirati [git](https://git-scm.com/downloads))
* **GitHub nalog**

Sada je potrebno da instaliramo alat `github-cli` na naš sistem prateći [zvaničnu dokumentaciju](https://github.com/cli/cli#installation).

Nakon toga, potrebno je da se prijavimo putem CLI-ja, pa unesite ovu komandu:

```bash
gh auth login
```

Pratite uputstva i spremni smo!

# Forkujte ovaj repozitorijum

Jednostavno pokrenite ovu komandu:

```bash
gh repo fork firstcontributions/first-contributions
```

**Važno: Bićete upitani da li želite i da klonirate repozitorijum — izaberite opciju „yes“**

# Kreirajte svoju granu (branch)

Ovaj korak radimo pomoću Git-a. Unesite sljedeću komandu i zamijenite ime svojim imenom, na primjer:

```bash
git switch -c add-john-doe
```

# Napravite potrebne izmjene i sačuvajte ih

Sada možete otvoriti fajl `Contributors.md` u tekst editoru i dodati svoje ime. Stavite ime bilo gdje između početka i kraja fajla, zatim sačuvajte fajl.

U direktorijumu projekta pokrenite `git status` i vidjećete izmjene. <img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Dodajte izmjene u granu koju ste upravo kreirali koristeći komandu `git add`:
`git add Contributors.md`

Sada sačuvajte izmjene koristeći komandu `git commit`:
`git commit -m "Add your-name to Contributors list"`
zamijenite `your-name` svojim imenom.

# Pošaljite izmjene na GitHub

Pošaljite izmjene koristeći komandu `git push`:

```
git push origin -u your-branch-name
```

zamijenite `your-branch-name` imenom grane koju ste ranije kreirali.

<details>
<summary> <strong>Ako dobijete greške prilikom slanja, kliknite ovdje:</strong> </summary>

* ### Greška pri autentifikaciji

     <pre>remote: Podrška za autentifikaciju lozinkom je uklonjena 13. avgusta 2021. Molimo koristite personalni pristupni token.
  remote: Više informacija: https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>

  Pogledajte [GitHub vodič](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) o generisanju i podešavanju SSH ključa za vaš nalog.

</details>

# Pošaljite izmjene na pregled

Pokretanjem ove komande u direktorijumu repozitorijuma možete kreirati **pull request** za pregled:

```bash
gh pr create --repo firstcontributions/first-contributions
```

Nakon toga pošaljite pull request.

Možete koristiti komandu `gh status` da vidite status vašeg pull requesta.

## Kuda dalje?

Čestitamo! 🎉 Upravo ste završili standardni proces
*fork → clone → edit → pull request* koji ćete često sretati kao saradnik!

Proslavite svoj doprinos i podijelite ga sa prijateljima i pratiocima putem [web aplikacije](https://firstcontributions.github.io/#social-share).

Ako želite još vježbe, pogledajte [code contributions](https://github.com/roshanjossey/code-contributions).

Sada možete početi da doprinosite i drugim projektima. Pripremili smo listu projekata sa lakim zadacima za početnike. Pogledajte [listu projekata u web aplikaciji](https://firstcontributions.github.io/#project-list).

### [Dodatni materijal](https://github.com/firstcontributions/first-contributions/blob/main/docs/additional-material/git_workflow_scenarios/additional-material.md)

[Povratak na glavnu stranicu](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
