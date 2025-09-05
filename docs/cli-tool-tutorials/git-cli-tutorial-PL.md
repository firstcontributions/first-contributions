[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# First Contributions

| <img alt="GitHub Desktop" src="https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png" width="200"> | GitHub Command Line Interface (CLI) |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |

To jest przewodnik dla nas, geeków terminala, którzy chcą robić wszystko w terminalu. Dzięki [Github-CLI](https://cli.github.com/), możemy to osiągnąć, pamiętając, że Twoja pierwsza kontrybucja powinna być przyjemna, satysfakcjonująca i motywować do dalszego działania\!

Ten przewodnik jest nieco trudniejszy, ponieważ w ogóle nie używamy żadnego interfejsu graficznego, ale nadal jest naprawdę fajny i na pewno możesz za nim podążać\!

Pierwszymi wymaganiami jest posiadanie:

  - zainstalowanego Git (jak zainstalować [git](https://git-scm.com/downloads))
  - konta Github

Teraz musimy zainstalować narzędzie `github-cli` w naszym systemie, postępując zgodnie z [oficjalną dokumentacją](https://github.com/cli/cli#installation).

Następnie musimy zalogować się w CLI, więc wprowadź to polecenie:

```bash
gh auth login
```

Postępuj zgodnie z instrukcjami i gotowe\!

-----

# Fork this repository

To jest tak proste, jak uruchomienie tego polecenia:

```bash
gh repo fork firstcontributions/first-contributions
```

**Ważne: Zostaniesz zapytany, czy chcesz również sklonować, wybierz opcję "yes".**

-----

# Create your branch

Ten krok wykonamy za pomocą git, więc wprowadź to polecenie, zastępując `name` swoim imieniem, na przykład:

```bash
git switch -c add-john-doe
```

-----

# Make necessary changes and commit those changes

Teraz możesz otworzyć plik `Contributors.md` w edytorze tekstu i dodać do niego swoje imię. Wstaw swoje imię w dowolnym miejscu między początkiem a końcem, a następnie zapisz plik.

W katalogu projektu wykonaj `git status`, a zobaczysz zmiany.
\<img align="right" width="450" src="[https://firstcontributions.github.io/assets/Readme/git-status.png](https://firstcontributions.github.io/assets/Readme/git-status.png)" alt="git status" /\>

Dodaj te zmiany do właśnie utworzonej gałęzi za pomocą polecenia `git add`:
`git add Contributors.md`

Teraz zatwierdź te zmiany za pomocą polecenia `git commit`:
`git commit -m "Add your-name to Contributors list"`
zastępując `your-name` swoim imieniem.

-----

# Push changes to github

Wypchnij swoje zmiany za pomocą polecenia `git push`:

```
git push origin -u your-branch-name
```

zastępując `your-branch-name` nazwą gałęzi, którą utworzyłeś wcześniej.

\<details\>
\<summary\> \<strong\>Jeśli podczas wypychania wystąpią błędy, kliknij tutaj:\</strong\> \</summary\>

  - ### Authentication Error

     \<pre\>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see [https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/](https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/) for more information.
  fatal: Authentication failed for '[https://github.com/](https://github.com/)\<your-username\>/first-contributions.git/'\</pre\>
  Przejdź do [tutoriala GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) dotyczącego generowania i konfigurowania klucza SSH na swoim koncie.

\</details\>

-----

# Submit your changes for review

Teraz, uruchamiając to polecenie w katalogu naszego repozytorium, możemy utworzyć pull request do przeglądu:

```bash
gh pr create --repo firstcontributions/first-contributions
```

Następnie wyślij pull request.

Możesz użyć polecenia `gh status`, aby zobaczyć swój pull request w akcji.

-----

## Where to go from here?

Gratulacje\! Właśnie ukończyłeś standardowy cykl pracy *fork -\> clone -\> edit -\> pull request*, który często napotkasz jako kontrybutor\!

Uczcij swój wkład i podziel się nim ze znajomymi i obserwującymi, przechodząc do [web app](https://firstcontributions.github.io/#social-share).

Możesz dołączyć do naszego zespołu na Slacku, jeśli potrzebujesz pomocy lub masz pytania. [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA).

Teraz zacznijmy kontrybuować do innych projektów. Zebraliśmy listę projektów z prostymi problemami, od których możesz zacząć. Sprawdź [the list of projects in the web app](https://firstcontributions.github.io/#project-list).

### [Additional material](https://www.google.com/search?q=additional-material/git_workflow_scenarios/additional-material.md)

-----

## Tutorials Using Other Tools

[Back to main page](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)