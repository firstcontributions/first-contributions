[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Primeres Contribucions

És difícil. Sempre ho és quan es fa algo per primera vegada. Especialment quan es col·labora amb altres, ja que efectuar errades no es gens agradable. Es vol simplificar la manera en que els col·laboradors de codi obert aprenen i contribueixen per primera vegada.

Llegir articles i mirar tutorials pot ser d'ajuda, però què millor que fer les coses en un entorn de pràctiques? Aquest projecte és una guia, simplificant la forma de fer la primera contribució per als principiants. Si vol fer la primera contribució, segueixi les instruccions que es mostren a continuació: 

#### *Si no està còmode amb la línia d'ordres, [aquí hi ha tutorials utilitzant eines amb Interfaç Gràfica (GUI)]( #tutorials-using-other-tools )*

#### *Llegir en [altres idiomes](Translations.md).*

[🇮🇳](README.hi.md) [🇲🇲](README.mm_unicode.md) [🇮🇩](README.id.md) [🇫🇷](README.fr.md) [🇪🇸](README.es.md) [🇳🇱](README.nl.md) [🇷🇺](README.ru.md) [🇯🇵](README.ja.md) [🇻🇳](README.vn.md) [🇵🇱](README.pl.md) [🇮🇷](README.fa.md) [🇮🇷](README.fa.en.md) [🇰🇷 🇰🇵](README.ko.md) [🇩🇪](README.de.md) [🇨🇳](README.chs.md) [🇹🇼](README.cht.md) [🇬🇷](README.gr.md) [🇺🇦](README.ua.md) [🇧🇷](README.pt_br.md) [🇵🇹](README.pt-pt.md) [🇮🇹](README.it.md) [🇹🇭](README.th.md) [🏴󠁥󠁳󠁧󠁡󠁿](README.gl.md) [🇵🇰](README.ur.md) [:bangladesh:](README.bn.md) [🇲🇩 🇷🇴](README.ro.md) [🇹🇷](README.tr.md) [🇸🇪](README.se.md) [🇮🇱](README.hb.md)

<img align="right" width="300" src="../assets/fork.png" alt="fer fork d'aquest repsoitori" />

Si no disposa de git en el seu ordinador, [instal·leu-lo]( https://help.github.com/articles/set-up-git/).

## Bifurca (*Fork*) aquest respositori

Faci un *fork* d'aquest repositori clicant al botó "*Fork*" a la part superior dreta d'aquesta pàgina.
Això crearà una còpia d'aquest repositori en el seu compte.

## Clone the repository

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

Now clone this repo to your machine. Go to your GitHub account, click on the clone button and then click the *copy to clipboard* icon.

Open a terminal and run the following git command:

```
git clone "url you just copied"
```
where "url you just copied" (without the quote marks) is the url to this repository(your fork of this project). See the previous steps to obtain the url.

<img align="right" width="300" src="assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

For example:
```
git clone https://github.com/this-is-you/first-contributions.git
```
where `this-is-you` is your GitHub username. Here you're copying the contents of the first-contributions repository in GitHub to your computer.

## Create a branch

Change to the repository directory on your computer (if you are not already there):

```
cd first-contributions
```
Now create a branch using the `git checkout` command:
```
git checkout -b <add-your-new-branch-name>
```

For example:
```
git checkout -b add-alonzo-church
```
(The name of the branch does not need to have the word *add* in it, but it's a reasonable thing to include because the purpose of this branch is to add your name to a list.)

## Make necessary changes and commit those changes

Now open `Contributors.md` file in a text editor, add your name to it. Don't add it at the beginning or end of the file. Put it anywhere in between. Now, save the file. 

<img align="right" width="450" src="assets/git-status.png" alt="git status" />


If you go to the project directory and execute the command `git status`, you'll see there are changes. 


Add those changes to the branch you just created using the `git add` command:

```
git add Contributors.md
```

Now commit those changes using the `git commit` command:
```
git commit -m "Add <your-name> to Contributors list"
```
replacing `<your-name>` with your name.

## Push changes to GitHub

Push your changes using the command `git push`:
```
git push origin <add-your-branch-name>
```
replacing `<add-your-branch-name>` with the name of the branch you created earlier.

## Submit your changes for review

If you go to your repository on GitHub, you'll see a  `Compare & pull request` button.  Click on that button.

<img style="float: right;" src="assets/compare-and-pull.png" alt="create a pull request" />

Now submit the pull request.

<img style="float: right;" src="assets/submit-pull.png" alt="submit pull request" />

Soon I'll be merging all your changes into the master branch of this project. You will get a notification email once the changes have been merged.

## Delete the branch after pull request has been merged

You can safely delete your branch `<add-your-branch-name>` after the pull request has been merged. You'll see a button to delete the branch:

<img style="float: right;" src="assets/delete-branch-after-pr.png" alt="delete branch after PR is merged" />

If the Pull Request was closed without being merged, GitHub will warn you about deleting unmerged commits and the button will look like this:

<img style="float: right;" src="assets/delete-branch-warning.png" alt="delete branch after PR is not merged" />

## Where to go from here?

Congrats!  You just completed the standard _fork -> clone -> edit -> PR_ workflow that you'll encounter often as a contributor!

Celebrate your contribution and share it with your friends and followers by going to [web app](https://roshanjossey.github.io/first-contributions/#social-share).

You could join our slack team in case you need any help or have any questions. [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Now let's get you started with contributing to other projects. We've compiled a list of projects with easy issues you can get started on. Check out [the list of projects in web app](https://roshanjossey.github.io/first-contributions/#project-list).

### [Additional material](additional-material/git_workflow_scenarios/additional-material.md)


## Tutorials Using Other Tools

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|

## Self-Promotion

If you liked this project, star it on [GitHub](https://github.com/Roshanjossey/first-contributions).
If you're feeling especially charitable, follow [Roshan](https://roshanjossey.github.io/) on
[Twitter](https://twitter.com/sudo__bangbang) and
[GitHub](https://github.com/roshanjossey).

<a href="http://saasgrids.com"> <img alt="https://app.saasgrids.com" src="assets/saasgrids-banner.png" width="500"></a>
