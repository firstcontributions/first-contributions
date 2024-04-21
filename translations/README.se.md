[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# First Contributions

Det är alltid svårt första gången man gör något och speciellt när du samarbetar med andra kan det vara extra känsligt att göra misstag. Vi vill göra det lättare för dig att lära dig hur man bidrar till ett öppet källkods-projekt.

Att läsa artiklar och titta på handledningar kan så klart hjälpa men det är alltid bättre att göra det på riktigt. Detta projeket har som syfte att tillhandahålla en guide och göra det enkelt för nybörjare att göra sina första bidrag. Om du är ute efter att göra ditt första bidrag kan du följa stegen nedan.


#### *Om du inte känner dig bekväm med kommandoraden, [så finns en vägledning här.](#Handledningar-för-andra-verktyg)*


<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Om du inte har git installerat [så installera det]( https://help.github.com/articles/set-up-git/ )

## Gör en Fork på detta repository

Forka repot genom att klicka på fork-knappen överst på denna sida.
Detta kommer att skapa en kopia av repot i ditt GitHub-konto.

## Klona repository

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Klona repot till din dator. Gå till ditt GitHub-konto och klicka på clone-knappen och klicka sedan på *copy to clipboard*-ikonen.

Öppna en terminal och kör följande kommando:

```
git clone "url you just copied"
```
där "url you just copied" (utan citat-tecken) är URL:en för detta repo (din fork för detta projekt). Se föregående steg för att hitta URL:en.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Till exempel:
```
git clone https://github.com/this-is-you/first-contributions.git
```
där `this-is-you` är ditt användarnamn på GitHub. På detta sätt kopierar du innehållet i repot till din dator.

## Skapa en branch

Gå till repo-katalogen på din dator (om du inte redan står i den katalogen):

```
cd first-contributions
```

Nu skapar du en branch genom att använda `git checkout`-kommandot:
```
git checkout -b <lägg till ditt branch-namn>
```

Till exempel:
```
git checkout -b mitt-tillag
```

## Gör de ändringar du vill göra och commita dem

Nu öppnar du `Contributors.md` i en text-editor och lägger till ditt namn. Lägg inte till något i början eller slutet av dokumentet utan lägg till någonstans mitt emellan. Spara filen.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Ge kommando `git status` i projektkatalogen för att se de ändringar du gjort.


Lägg till dina ändringar genom att använda kommando `git add -A`:

```
git add Contributors.md
```

Commita dina ändringar genom att använda `git commit`:
```
git commit -m "Add <your-name> to Contributors list"
```
ersätt `<your-name>` med ditt namn.

## Pusha ändringar till GitHub

Pusha dina ändringar genom att använda kommando `git push`:
```
git push origin <add-your-branch-name>
```
ersätt `<add-your-branch-name>` med det branch-namn du använt tidigare.

## Skicka iväg dina ändringar för granskning

Om du navigerar till ditt repo på GitHub kan du se en knapp med texten `Compare & pull request`. Klicka på den.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Skicka iväg din s.k. pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Snart kommer jag införa dina ändringar i huvudprojektet. Du kommer att få ett e-mail så fort dina ändringar blivit införda.

## Hur går man vidare?

Gratulerar! Du har just genomfört standardprocessen för _fork -> clone -> edit -> PR_, en process du kommer att stöta på ofta!

Fira genom att dela med dina vänner och följare genom att gå till [web app](https://firstcontributions.github.io/#social-share).

Behöver du hjälp eller vill du ställa frågor så kan du gå med i vår slack-grupp. [Gå med i slack-gruppen](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Nu kan du gå vidare genom att bidra i andra projekt. Vi har sammanställt en lista med enkla uppgifter som du kan starta med. Kolla in [projektlistan i webbapplikationen](https://firstcontributions.github.io/#project-list).

### [Ytterligare material](../additional-material/git_workflow_scenarios/additional-material.md)


## Handledningar för andra verktyg

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
