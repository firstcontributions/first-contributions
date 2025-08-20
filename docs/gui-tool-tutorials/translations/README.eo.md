[![Amo al Malferma Kodo](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![Licenco: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Helpantoj de Malferma Kodo](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Unuaj Kontribuoj

Estas malfacile. Iam estas malfacile la unua fojo kiam vi faras ion, speciale kiam vi kunlaboras kun aliaj, ĉar fari erarojn ne estas agrable. Nia celo estas simpligi la manieron en kiu novaj kontribuantoj de _malferma kodo_ lernas kaj kontribuas unue.

Legi artikolojn kaj rigardi tutoriaojn povas helpi, sed kio estas pli bona ol fari aferojn en praktika medio? Ĉi tiu projekto celas esti gvidilo kaj simpligi la manieron en kiu komencantoj faras sian unuan kontribuon. Se vi volas fari vian unuan kontribuon, sekvu la paŝojn kiuj estas montritaj sube.

#### *Se vi ne estas konata kun la komandlinio, [jen tutoriaj uzante ilojn kun Grafika Interfaco (GUI)](#Tutoriales-con-otras-herramientas)*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork de este repositorio" />

Se vi ne havas git-on en via komputilo, vi povas trovi instrukciojn por instali ĝin [ĉi tie]( https://docs.github.com/es/get-started/quickstart/set-up-git ).

## Forku (*Fork*) ĉi tiun deponejon

Forku ĉi tiun deponejon klakante la butonon "*Fork*" en la supraj dekstra flanko de ĉi tiu paĝo.
Tio kreos kopion de ĉi tiu deponejo en via konto.

## Klono (*Clone*) la forkan deponejon

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="kloni ĉi tiun deponejon" />

Nun klono ĉi tiun deponejon al via komputilo. Iru al via GitHub-konto, klaku sur la butono "*clone or download*" kaj poste klaku sur la ikono por *kopii al la poŝtelefono*.

Malfermu vian konsolon aŭ terminalon kaj rulu la jenan git-an komandon:

```bash
git clone "url you just copied"
```

Kie estas "la URL kiun vi ĵus kopis" (sen la duobla cita signo) estas la *URL* de ĉi tiu deponejo (via fork de ĉi tiu projekto). Rigardu la antaŭajn paŝojn por akiri la *URL*-on.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="kopii la URL-on al la poŝtelefono" />

Ekzemple:

```bash
git clone git@github.com:this-is-you/first-contributions.git
```

La parto kun `este-eres-tu` estos anstataŭigita per via GitHub-uzantonomo. Ĉi tie vi kopias la enhavon de la deponejo *first-contributions* de GitHub al via komputilo.

## Krei branĉon (*Branch*)

Shanĝu al la dosierujo de la deponejo sur via komputilo (se vi ne jam estas tie):

```bash
cd first-contributions
```

Nun kredu branĉon (*branch*) uzante la komandon `git checkout`:

```bash
git switch -c your-new-branch-name
```

Ekzemple:

```bash
git switch -c add-alonzo-church
```

(La nomo de la branĉo ne devas enhavi la vorton *add*, sed estas racionebla ĉar la celo de tiu ĉi branĉo estas aldoni vian nomon al la listo.)

## Faru la necesajn ŝanĝojn kaj konfirmu (*Commit*) tiujn ŝanĝojn

Malfermu la dosieron `Contributors.md` en teksta redaktilo kaj aldonu vian nomon. Ne aldonu ĝin aŭ en la komenco aŭ en la fino de la dosiero, sed faru tion ie interne. Konservu la dosieron.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Se vi iras al la projekta dosierujo kaj ekzekutas la komandon `git status`, vi vidos ke estas ŝanĝoj.

Aldonu tiujn ŝanĝojn al la branĉo kiun vi kreis antaŭe uzante la komandon `git add`:


```bash
git add Contributors.md
```

Nun konfirmu tiujn ŝanĝojn uzante la komandon `git commit`:


```bash
git commit -m "Aldonu <via-nomo> al la listo de Kontribuantoj"
```

anstataŭigu `<via-nomo>` per via nomo.

## Puŝu (*Push*) viajn ŝanĝojn al GitHub

Puŝu viajn ŝanĝojn uzante la komandon `git push`:


```bash
git push -u origin your-branch-name
```


Anstataŭigu `<aldonu-la-nomon-de-la-branĉo>` per la nomo de la branĉo kiun vi kreis antaŭe.

## Submetu (*Submit*) viajn ŝanĝojn por revizio

Se vi iras al via deponejo en GitHub, vi vidos butonon `Compare & pull request`. Klaku sur tiu butono.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="krei pull request" />

Nun sendu la *pull request*.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="sendi pull request" />

Baldaŭ mi unuos viajn ŝanĝojn (faros *merge*) kun la ĉefa branĉo de tiu ĉi projekto. Vi ricevos retmesaĝon kiam la ŝanĝoj estos unuitaj.

## Kie iri de ĉi tie?

Gratulojn! Vi ĵus finis la regulan _fork -> clone -> redaktu -> pull request_ fluon kiun vi ofte renkontos kiel kontribuanto!

Festu vian kontribuon kaj dividiĝu kun viaj amikoj kaj sekvantoj irante al [rete apikaĵo](https://firstcontributions.github.io/#social-share).

Vi ankaŭ povas aliĝi al nia Slack-teamo se vi bezonas helpon aŭ havas demandojn. [Aliĝu al nia Slack-teamo](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Nun komencu kontribui al aliaj projektoj. Ni kolektis liston de projektoj kun facilaj problemoj, por ke vi povu ekhavi. Rigardu [la liston de projektoj en la rete apikaĵo](https://firstcontributions.github.io/#project-list).

### [Plia materialo](../additional-material/git_workflow_scenarios/additional-material.md)

## Tutoriaj uzante aliajn ilojn

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
