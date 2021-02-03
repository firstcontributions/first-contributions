[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-kpbyrmkk-JDkRtchcvRvQ0qK4iPmyvA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Prvi doprinos

Cilj ovog projekta je olakšati početnicima put prema prvom doprinosu. Želite li se upustiti u izradu svog prvog doprinosa, pratite ove korake.

_Ako ne želite raditi u naredbenom retku, [ovdje](#upute-za-druge-alate) možete pronaći upute za rad s drugim alatima._

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### Ako nemate git na svom računalu, [instalirajte ga](https://help.github.com/articles/set-up-git/).

## Napravite fork ovog repozitorija

Napravite fork ovog repozitorija klikom na fork gumb na vrhu ove stranice.
To će stvoriti kopiju ovog repozitorija na vašem računu.

## Klonirajte repozitorij

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

A sad klonirajte _forkani_ repozitorij na svoje računalo. Odite na svoj GitHub račun, otvorite _forkani_ repozitorij, pritisnite na gumb Code te na ikonu za kopiranje.

Otvorite terminal i upišite sljedeće git naredbe:

```
git clone "url koji ste kopirali"
```

gdje "url koji ste kopirali" (bez navodnika) označava url ovog repozitorija koji ste _forkali_ u prošlom koraku.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Na primjer:

```
git clone https://github.com/ovo-ste-vi/first-contributions.git
```

gdje je `ovo-ste-vi` vaše GitHub korisničko ime. Ovako kopirate sadržaj repozitorija first-contributions na vaše računalo.

## Stvorite granu

Prebacite se u mapu repozitorija na vašem računalu (ako već niste u njoj):

```
cd first-contributions
```

Zatim stvorite granu koristeći `git checkout` naredbu:

```
git checkout -b ime-vase-nove-grane
```

Na primjer:

```
git checkout -b add-rudjer-boskovic
```

(Ime ove grane ne mora sadržavati riječ _add_ u sebi, ali ima smisla uključiti je jer je svrha ove grane dodati svoje ime u listu.)

## Napravite potrebne promjene i pohranite ih u novi čvor

Otvorite `Contributors.md` datoteku u uređivaču teksta i dodajte svoje ime u nju. Ne stavljajte svoje ime na kraj ili početak, stavite ga bilo gdje između. Zatim spremite datoteku.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Ako odete u mapu projekta i izvršite naredbu `git status`, vidjet ćete da ima promjena.

Dodajte te promjene u granu koju ste napravili koristeći naredbu `git add`:

```
git add Contributors.md
```

Sad izvršite naredbu `git commit` da biste dodali novi čvor u projekt:

```
git commit -m "Add <vase-ime> to Contributors list"
```

gdje umjesto `<vase-ime>` upisujete svoje ime.

## Pošaljite promjene na GitHub

Pošaljite svoje promjene koristeći naredbu `git push`:

```
git push origin <ime-vase-grane>
```

gdje ćete promijeniti `<ime-vase-grane>` s pravim imenom grane koju ste napravili.

## Predajte svoje promjene na pregled

Ako odete u svoj repozitorij na GitHubu, vidjet ćete gumb `Compare & pull request`. Pritisnite taj gumb.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Sad predajte _pull request_.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Ubrzo ću spojiti vaše promjene s glavnom granom ovog projekta. Dobit ćete obavijest na e-mail jednom kad se promjene spoje.

## A što dalje?

Čestitamo! Završili ste standardni _fork -> clone -> edit -> pull request_ tok rada s kojim ćete se često susretati doprinoseći raznim projektima! 

Proslavite svoj doprinos i podijelite ga s prijateljima odlaskom na [web aplikaciju](https://firstcontributions.github.io/#social-share).

Možete se i pridružiti našem Slack timu ako trebate kakvu pomoć ili imate pitanja. [Pridruži se Slack timu](https://join.slack.com/t/firstcontributors/shared_invite/zt-kpbyrmkk-JDkRtchcvRvQ0qK4iPmyvA).

A sad započnimo s doprinosima na drugim projektima. Napravili smo listu projekata s jednostavnim problemima na kojima možete započeti. Provjerite [listu projekata u web aplikaciji](https://firstcontributions.github.io/#project-list).

### [Dodatni materijali](../additional-material/git_workflow_scenarios/additional-material.md)

## Upute za druge alate

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="./assets/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/IntelliJ_IDEA_Logo.svg" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                               | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                   |
