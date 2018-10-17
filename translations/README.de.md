[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# First Contributions

<img align="right" width="300" src="../assets/fork.png" alt="Repository forken" />

Aller Anfang ist schwer. Gerade dann, wenn wir gemeinsam an etwas arbeiten, will niemand etwas Falsches tun. Aber Open Source dreht sich um Kooperation und lebt von den Beiträgen von vielen Freiwilligen. Deshalb haben wir es uns zur Aufgabe gemacht, neuen Mitgliedern in der Open-Source-Gemeinde ihre ersten Schritte so einfach wie möglich zu machen. 

Natürlich helfen die vorhandenen Artikel und Videoanleitungen. Aber was kann besser sein, als es einfach einmal auszuprobieren mit dem Wissen, dass man nichts kaputt machen kann? Diese Projekt will Anfängern zeigen, wie sie möglichst einfach ihren ersten Beitrag leisten. Bedenke: Je entspannter du bist, desto besser lernst du. Wenn du deinen ersten Beitrag leisten möchtest, folge diesen einfachen Schritten. Wir versprechen dir, es wird Spaß machen.


Wenn Git noch nicht installiert ist, [ installiere es ]( https://help.github.com/articles/set-up-git/ )

## Repository forken

Forke das Repository durch das Anklicken der Schaltfläche "Fork". Dadurch erhältst du deine eigenen Version des Projektes in deinem Profil.

## Repository klonen

<img align="right" width="300" src="../assets/clone.png" alt="Repository klonen" />

Klone das Repository auf deinen Computer. Klicke auf die Schaltfläche "Clone or download" und anschließend auf das "copy to clipboard" Symbol.

Öffne eine Kommandozeile und gib das folgende git Kommando ein:

```
git clone "Deine kopierte URL"
```
Statt 'Deine kopierte URL' (ohne Anführungszeichen) füge die Repository URL aus dem vorherigen Schritt ein.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="URL kopieren" />

Beispiel:
```
git clone https://github.com/dein-Name/first-contributions.git
```
An der Stelle 'dein-Name' muss dein Github Username stehen. Hier landet die Kopie deines first-contributions Repository von Github.

## Erstelle einen Branch

Wechsle zum Repository-Verzeichnis auf deinem Computer (falls du es nicht schon getan hast).

```
cd first-contributions
```
Erstelle nun einen Branch mit dem Befehl `git checkout` command.
```
git checkout -b <add-dein-Name>
```

Beispiel:
```
git checkout -b add-max-mustermann
```

## Mache die nötigen Änderungen und committe sie

Öffne `Contributors.md` in einem Text-Editor, füge deinen Namen hinzu und speichere die Datei. Gibst du in der Kommandozeile nun `git status` ein, siehst du die Änderungen. Füge die Änderungen mit dem Befehl `git add` hinzu.
```
git add Contributors.md
```

Nun committest du mit `git commit`.
```
git commit -m "Add <dein-Name> to Contributors list"
```
Ersetze `<dein-Name>` mit deinem Namen.

## Pushe die Änderung zu Github

Pushe die Änderungen mit `git push`.
```
git push origin <add-dein-Name>
```
Ersetze `<add-dein-Name>` mit dem Namen des Branches, den du zuvor erstellt hast.

## Sende deine Änderungen zum Review

Wenn du jetzt zu deinem Repository auf Github gehst, siehst du einen Knopf `Compare & pull request`. Klicke darauf.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="Erstelle einen pull request" />

Erstelle einen Pull Request.

<img style="float: right;" src="../assets/submit-pull-request.png" alt="Pull Request senden" />

Roshanjossey wird nun deine Änderungen in den Master Branch dieses Projekts mergen. Du erhältst eine E-Mail sobald dies geschehen ist. 

## Einen Branch aus deinem Repository löschen
Wenn du der Anleitung bis hierher gefolgt bist und dein Pull Request angenommen wurde, hat dein Branch `<add-dein-Name>` seinen Zweck erfüllt und wird nicht länger benötigt. Du kannst ihn in deiner lokalen Arbeitskopie löschen. Dies ist zwar nicht zwingend notwendig, hilft dir aber dabei den Überblick zu bewahren.

Lass uns dazu zuerst den Branch `<add-dein-Name>` aus deiner lokalen Arbeitskopie in deinen master Branch mergen. Dazu wechseln wir zuerst in den master:
```
git checkout master
```

Merge `<add-dein-Name>` zu Master deiner lokalen Arbeitskopie:
```
git merge <add-dein-Name> master
```

Lösche nun den Branch `<add-dein-Name>` in deiner Arbeitskopie:
```
git branch -d <add-dein-Name>
```

Damit hast du nun deinen Branch `<add-dein-Name>` in deiner lokalen Arbeitskopie gelöscht. In deinem öffentlichen Repository auf GitHub ist er aber weiterhin vorhanden. Wenn du ihn auch dort löschen möchtest, stelle zuerst sicher, dass du einen Pull Request gestellt hast und er von Roshanjossey angenommen wurde. Du solltest keine Branches löschen solange sie Änderungen enthalten, die nicht gemergt sind!

Um einen Branch auf GitHub zu löschen verwende folgenden Befehl:
```
git push origin --delete <add-dein-Name>
```

Nun weißt du, wie man Branches am Ende ihrer Lebenszeit löscht.

So wie du einen Pull Request gestellt hast, werden hoffentlich viele andere Entwickler einen Beitrag zum Projekt leisten. Sobald ein Pull Request angenommen wurde, sind die Änderungen im Master Branch des Projektes. In deinen Fork werden die Änderungen von anderen Freiwilligen aber nicht automatisch übernommen. Damit du immer die neuste Version hast, musst du regelmäßig synchronisieren. Wie dies geschieht wird im folgenden Kapitel erklärt.

## Halte deinen Fork synchron

Für die weiter Anleitung ist es wichtig den Ablauf einer vollen Synchronisation zu verstehen. In unserem Beispiel gibt es drei verschiedene Repositories: Das öffentliche Repository von Roshanjossey.
`github.com/Roshanjossey/first-contributions/`, dein öffentlicher Fork auf GitHub `github.com/dein-Name/first-contributions/` und die lokale Arbeitskopie auf deinem PC. Damit deine beiden Versionen synchron bleiben, müssen wir zuerst die Änderungen des öffentlichen Projektes von Roshanjossey holen (`fetch`) und mit deiner lokalen Arbeitskopie mergen. Im zweiten Schritt werden wir dann die Änderungen von deiner lokalen Arbeitskopie zu deinem öffentlichen GitHub Projekt pushen. Das ist wichtig, weil du nur für die Versionen auf deinem öffentlichen GitHub Projekt Pull Request stellen kannst.

Hier die Schritte für eine vollständige Synchronisation:

Stelle zuerst sicher, dass du im Master Branch deiner Arbeitskopie bist. Dies kannst du mit folgendem Befehl prüfen:
```
git status
```
Wenn du nicht im Master bist, dann wechsle mit folgendem Befehl:
```
git checkout master
```

Füge Roshanjossey Repository URL mit `upstream remote url` hinzu.

```
git remote add upstream https://github.com/Roshanjossey/first-contributions
```
Auf diese Weise sagst du Git, dass es noch eine andere Version dieses Projekts gibt, die wir upstream nennen. Lade nur die neueste Version dieses Repositories.
```
git fetch upstream
```

Hier laden wir alle Änderungen von Roshanjosseys Forks herunter (upstream). Danach müssen wir dessen Änderungen in den Master deiner lokalen Arbeitskopie mergen.
```
git rebase upstream/master
```
So wendest du alle Änderungen, die du heruntergeladen hast, im Master Branch an. Deine lokale Kopie hat nun den gleichen Stand, wie das öffentliche Repository. Wenn du den Master Branch jetzt pushst, ist auch dein Fork auf GitHub wieder aktuell.
```
git push origin master
```
Beachte, dass du hier zum Remote Namens origin pushst. Origin ist ein besonderer Name, er steht für das Projekt aus dem du initial mit git checkout geclont hast. Es ist also deine Kopie des Projektes auf GitHub.

## Tutorials mit anderen Tools

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|


## Wie geht es weiter?

Wenn du weitere Fragen hast kannst du Mitglied in unserem Slackteam werden. [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Hier sind einige Anfänger-Level Aufgaben (issues) in bekannten Repositories die du lösen kannst. Schau sie dir an und erfahre mehr darüber

|[![exercism](https://avatars2.githubusercontent.com/u/5624255?v=3&s=100)](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[![fun-retro](https://avatars3.githubusercontent.com/u/15913975?v=3&s=100)](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[<img width="100" src="https://cdn.worldvectorlogo.com/logos/react.svg">](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[![habitat](https://avatars1.githubusercontent.com/u/18171698?v=3&s=100)](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![scikit-learn](https://avatars0.githubusercontent.com/u/365630?v=3&s=100)](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[<img width="100" src="https://camo.githubusercontent.com/0f302c808c8457f6460913e33aed3478124612c2/687474703a2f2f6c65696e696e67656e2e6f72672f696d672f6c65696e696e67656e2e6a7067">](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[<img width="100" src="https://images.plot.ly/plotly-documentation/thumbnail/numpy-logo.jpg">](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[![elasticsearch](https://avatars2.githubusercontent.com/u/6764390?v=3&s=100)](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|---|---|---|---|---|---|---|---|
|[exercism](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[Fun Retros](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[react](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[habitat](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[scikit-learn](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[Leiningen](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[numpy](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[elasticsearch](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|[![homebrew](https://avatars2.githubusercontent.com/u/1503512?v=3&s=100)](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[![rust](https://avatars1.githubusercontent.com/u/5430905?v=3&s=100)](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[![vuejs](https://avatars1.githubusercontent.com/u/6128107?v=3&s=100)](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[![Suave](https://avatars2.githubusercontent.com/u/5822862?v=3&s=100)](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[![OpenRA](https://avatars3.githubusercontent.com/u/409046?v=3&s=100)](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![PowerShell](https://avatars0.githubusercontent.com/u/11524380?v=3&s=100)](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[![coala](https://avatars2.githubusercontent.com/u/10620750?v=3&s=100)](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[![moment](https://avatars2.githubusercontent.com/u/4129662?v=3&s=100)](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[homebrew](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[Rust](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[vuejs](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[Suave](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[OpenRA](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[PowerShell](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[coala](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[moment](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[![ava](https://avatars0.githubusercontent.com/u/8527916?v=3&s=100)](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[![freeCodeCamp](https://avatars0.githubusercontent.com/u/9892522?v=3&s=100)](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![webpack](https://avatars3.githubusercontent.com/u/2105791?v=3&s=100)](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[![hoodie](https://avatars1.githubusercontent.com/u/1888826?v=3&s=100)](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![pouchdb](https://avatars3.githubusercontent.com/u/3406112?v=3&s=100)](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[![neovim](https://avatars0.githubusercontent.com/u/6471485?v=3&s=100)](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[![babel](https://avatars2.githubusercontent.com/u/9637642?v=3&s=100)](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[<img width="100" src="https://github.com/adobe/brackets/blob/gh-pages/images/brackets_128.png?raw=true">](https://github.com/adobe/brackets/labels/Starter%20bug)|
|[ava](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[webpack](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[hoodie](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[pouchdb](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[neovim](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[babel](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[brackets](https://github.com/adobe/brackets/labels/Starter%20bug)|
| [![Node.js](https://avatars1.githubusercontent.com/u/9950313?v=3&s=100)](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|[<img width="100" src="https://github.com/Semantic-Org/Semantic-UI-React/raw/master/docs/app/logo.png">](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|
| [Node.js](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |[Semantic-UI-React](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |

[Tutorial for Github desktop app - English](github-desktop-tutorial.md)
