# First Contributions

<img align="right" width="300" src="../assets/fork.png" alt="Repository forken" />

Aller Anfang ist schwer. Gerade dann, wenn wir gemeinsam an etwas arbeiten, will niemand etwas Falsches tun. Aber Open Source dreht sich um Kooperation und lebt von den Beiträgen von vielen Freiwilligen. Deshalb haben wir es uns zur Aufgabe gemacht, neuen Mitgliedern in der Open Source Gemeinde ihre ersten Schritte so einfach wie möglich zu gestalten.

Natürlich helfen die vorhandenen Artikel und Videoanleitungen. Aber was kann besser sein, als es einfach einmal auszuprobieren mit dem Wissen, dass man nichts kaputt machen kann? Dieses Projekt zeigt Anfängern, wie sie möglichst einfach ihren ersten Beitrag leisten. Bedenke: Je entspannter du bist, desto besser lernst du. Wenn du deinen ersten Beitrag leisten möchtest, folge diesen einfachen Schritten. Wir versprechen dir, es wird Spaß machen.

| Country | Translated Link |
| --- | --- |
| English | [English](README.md) |
| 🇮🇳 India | [Hindi](translations/README.hi.md) |
| 🇲🇲 Myanmar | [Myanmar Unicode](translations/README.mm_unicode.md) |
| 🇮🇩 Indonesian | [Indonesian](translations/README.id.md) |
| 🇫🇷 French | [French](translations/README.fr.md) |
| 🇪🇸 Spain | [Spanish](translations/README.es.md) |
| 🇳🇱 Dutch | [Dutch](translations/README.nl.md) |
| 🇷🇺 Russian | [Russian](translations/README.ru.md) |
| 🇯🇵 Japan | [Japanese](translations/README.ja.md) |
| 🇻🇳 Vietnam | [Vietnamese](translations/README.vn.md) |
| 🇵🇱 Poland | [Polish](translations/README.pl.md) |
| 🇱🇹 Lithuania | [Lithuanian](translations/README.lt.md) |
| 🇰🇷 South Korea, 🇰🇵 North Korea | [Korean](translations/README.ko.md) |
| 🇩🇪 Germany | [German](translations/README.de.md) |
| 🇨🇳 China | [Simplified Chinese](translations/README.chs.md), [Traditional Chinese](translations/README.cht.md) |
| 🇬🇷 Greece | [Greek](translations/README.gr.md) |
| العربية | [العربية](translations/README.ar.md) |
| 🇺🇦 Ukraine | [Ukrainian](translations/README.ua.md) |
| 🇵🇹 Portugal, 🇧🇷 Brazil | [Português/Brasil](translations/README.pt_br.md) |
| 🇮🇹 Italy | [Italian](translations/README.it.md)
| 🇹🇭 Thailand | [ภาษาไทย](translations/README.th.md) |
| 🏴󠁥󠁳󠁧󠁡󠁿 Galicia | [Galician](translations/README.gl.md) |
| 🇵🇰 Pakistan | [Urdu](translations/README.ur.md) |
| :bangladesh: Bangladesh | [Bangla](translations/README.bn.md) |
| :moldova: Moldova, :romania: Romania | [Romanian](translations/README.ro.md)|

Falls `git` noch nicht installiert ist, [installiere es]( https://help.github.com/articles/set-up-git/)!

## Repository forken

Forke das Repository durch Klicken auf den Button "Fork". Dadurch enthältst du deine eigene Version des Projektes in deinem Profil.

## Repository klonen

<img align="right" width="300" src="../assets/clone.png" alt="Repository klonen" />

Klone das Repository auf deinen Computer. Klicke dazu auf den Button "Clone or download" und anschließend auf das "copy to clipboard"-Symbol.

Öffne eine Kommandozeile gib das folgende `git`-Kommando ein:

```
git clone Deine-kopierte-URL
```
Statt `Deine-kopierte-URL` fügst du die Repository-URL aus dem vorherigen Schritt ein.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="URL kopieren" />

Beispiel:

```
git clone https://github.com/dein-Username/first-contributions.git
```

An der Stelle `dein-Username` muss dein GitHub-Username stehen. Hier landet die Kopie deiner `first-contributions`-Repository von GitHub.

## Erstelle einen Branch

Wechsle ins Repository-Verzeichnis auf deinem Computer (falls du es nicht schon getan hast).

```
cd first-contributions
```

Erstelle nun einen Branch mit dem Befehl `git checkout command`:

```
git checkout -b <add-dein-Name>
```

Beispiel:

```
git checkout -b add-max-mustermann
```

## Führe die nötigen Änderungen durch und committe sie

Öffne `Contributors.md` in einem Texteditor, füge deinen Namen hinzu und speichere die Datei. Gibst du in der Kommandozeile nun `git status` ein, siehst du deine Änderungen. Füge diese Änderungen mit dem Befehl `git add Dateiname` hinzu.

```
git add Contributors.md
```

Nun committest du mit `git commit`:

```
git commit -m "Add <dein-Name> to Contributors list"
```

Ersetze `<dein-Name>` mit deinem Namen.

## Pushe die Änderungen zu GitHub

Pushe die Änderungen mit `git push`:

```
git push origin <add-dein-Name>
```

Ersetze `<add-dein-Name>` mit dem Namen des Branches, den du zuvor erstellt hast.

## Sende deine Änderungen zur Review

Wenn du jetzt zu deiner Repository auf GitHub gehst, siehst du einen Knopf `Compare & pull request`. Klicke darauf!

<img style="float: right;" src="../assets/compare-and-pull.png" alt="Erstelle einen pull request" />

Erstelle hierdurch einen *pull request*:

<img style="float: right;" src="../assets/submit-pull.png" alt="Pull Request senden" />

*Roshanjossey* wird nun deine Änderungen in den Master-Branch seines Projekts mergen. Du erhälst eine E-Mail, sobald dies geschehen ist.

## Einen Branch aus deiner Repository löschen

Wenn du der Anleitung bis hierhin gefolgt bist und dein *pull request* angenommen wurde, hat dein Branch `<add-dein-Name>` seinen Zweck erfüllt und wird nicht länger benötigt. Du kannst ihn in deiner lokalen Arbeitskopie löschen. Dies ist zwar nicht zwingend notwendig, hilft dir aber dabei den Überblick zu bewahren.

Lass uns dazu zuerst den Branch `<add-dein-Name>` aus deiner lokalen Arbeitskopie in deinen `master`-Branch mergen. Dazu wechseln wir zuerst in den `master`:

```
git checkout master
```

Merge `<add-dein-Name>` zu `master` deiner lokalen Arbeitskopie:

```
git merge <add-dein-Name> master
```

Lösche nun den Branch `<add-dein-Name>` in deiner Arbeitskopie:

```
git branch -d <add-dein-Name>
```

Damit hast du nun den Branch `<add-dein-Name>` aus deiner lokalen Arbeitskopie gelöscht. In deiner öffentlichen Repository auf GitHub ist er aber weiterhin vorhanden. Wenn du ihn auch dort löschen möchtest, stelle zuerst sicher, dass du einen *pull request* gestellt hast und dass dieser von *Roshanjossey* angenommen wurde. Du solltest keinen Branch löschen, solange dieser Änderungen enthält, die noch nicht gemergt wurden!

Um einen Branch aus deiner GitHub-Repository zu löschen, verwende folgenden Befehl:

```
git push origin --delete <add-dein-Name>
```

Nun weißt du, wie man Branches am Ende ihrer Lebenszeit löscht.

So wie du einen *pull request* gestellt hast, werden hoffentlich viele andere Entwickler einen Beitrag zum Projekt leisten. Sobald ein *pull request* angenommen wurde, sind die Änderungen im `master`-Branch des Projektes. In deinen Fork werden die Änderungen von anderen Freiwilligen aber nicht automatisch übernommen. Damit du immer die neueste Version hast, musst du regelmäßig synchronisieren. Wie dies geschieht, wird im folgenden Kapitel erklärt.

## Halte deinen Fork synchron

Für die weitere Anleitung ist es wichtig, den Ablauf einer vollen Synchronisation zu verstehen. In unserem Beispiel gibt es drei verschiedene Repositorys:

- Die öffentliche Repository von *Roshanjossey*
(`github.com/Roshanjossey/first-contributions/`),
- dein öffentlicher Fork auf GitHub (`github.com/dein-Name/first-contributions/`) und
- die lokale Arbeitskopie auf deinem PC.

Damit deine beiden Versionen synchron bleiben, müssen wir zuerst die Änderungen des öffentlichen Projektes von *Roshanjossey* holen (`fetch`) und mit deiner lokalen Arbeitskopie mergen. Im zweiten Schritt werden wir dann die Änderungen von deiner lokalen Arbeitskopie zu deinem öffentlichen GitHub-Projekt pushen. Das ist wichtig, weil du nur für die Versionen auf deinem öffentlichen GitHub-Projekt *pull requests* stellen kannst.

Hier die Schritte für eine vollständige Synchronisation:

Stelle zuerst sicher, dass du im `master`-Branch deiner Arbeitskopie bist. Dies kannst du mit folgendem Befehl prüfen:

```
git status
```
Falls du nicht im Master bist, dann wechsle mit folgendem Befehl:

```
git checkout master
```

Füge *Roshanjosseys* Repository-URL mit `upstream remote url` hinzu:

```
git remote add upstream https://github.com/Roshanjossey/first-contributions
```

Auf diese Weise sagst du Git, dass es noch eine andere Version dieses Projekts gibt, die wir `upstream` nennen. Lade nun die neueste Version dieser Repository:

```
git fetch upstream
```

Hier laden wir alle Änderungen von *Roshanjosseys* Repository herunter (`upstream`). Danach müssen wir dessen Änderungen in den `master` deiner lokalen Arbeitskopie mergen:

```
git rebase upstream/master
```

So wendest du alle Änderungen, die du heruntergeladen hast, im `master`-Branch an. Deine lokale Kopie hat nun den gleichen Stand wie die öffentliche Repository. Wenn du den `master`-Branch jetzt pushst, ist auch dein Fork auf GitHub wieder aktuell:

```
git push origin master
```

Beachte, dass du hier zum Remote `origin` pushst. `origin` ist ein besonderer Name, denn er steht für das Projekt, aus dem du ursprünglich mit `git clone <...>` heruntergeladen hast. Es ist also deine Kopie des Projektes auf GitHub.

## Tutorials mit anderen Tools (Englisch)

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.microsoft.com/net/images/vslogo.png" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|


## Wie geht's weiter?

Falls du weitere Fragen hast, kannst du Mitglied in unserem Slackteam werden. [Join slack team](https://firstcontributions.herokuapp.com) (Englisch)

Hier sind einige Anfänger-Level-Aufgaben (*issues*) in bekannten Repositorys, die du bestimmt lösen kannst. Schau sie dir an und erfahre mehr darüber:

|[![exercism](https://avatars2.githubusercontent.com/u/5624255?v=3&s=100)](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[![fun-retro](https://avatars3.githubusercontent.com/u/15913975?v=3&s=100)](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[<img width="100" src="https://cdn.worldvectorlogo.com/logos/react.svg">](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[![habitat](https://avatars1.githubusercontent.com/u/18171698?v=3&s=100)](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![scikit-learn](https://avatars0.githubusercontent.com/u/365630?v=3&s=100)](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[<img width="100" src="https://camo.githubusercontent.com/0f302c808c8457f6460913e33aed3478124612c2/687474703a2f2f6c65696e696e67656e2e6f72672f696d672f6c65696e696e67656e2e6a7067">](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[<img width="100" src="https://images.plot.ly/plotly-documentation/thumbnail/numpy-logo.jpg">](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[![elasticsearch](https://avatars2.githubusercontent.com/u/6764390?v=3&s=100)](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|---|---|---|---|---|---|---|---|
|[exercism](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[Fun Retros](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[react](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[habitat](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[scikit-learn](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[Leiningen](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[numpy](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[elasticsearch](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|[![homebrew](https://avatars2.githubusercontent.com/u/1503512?v=3&s=100)](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[![rust](https://avatars1.githubusercontent.com/u/5430905?v=3&s=100)](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[![vuejs](https://avatars1.githubusercontent.com/u/6128107?v=3&s=100)](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[![Suave](https://avatars2.githubusercontent.com/u/5822862?v=3&s=100)](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[![OpenRA](https://avatars3.githubusercontent.com/u/409046?v=3&s=100)](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![PowerShell](https://avatars0.githubusercontent.com/u/11524380?v=3&s=100)](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[![coala](https://avatars2.githubusercontent.com/u/10620750?v=3&s=100)](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[![moment](https://avatars2.githubusercontent.com/u/4129662?v=3&s=100)](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[homebrew](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[Rust](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[vuejs](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[Suave](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[OpenRA](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[PowerShell](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[coala](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[moment](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[![ava](https://avatars0.githubusercontent.com/u/8527916?v=3&s=100)](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[![freeCodeCamp](https://avatars0.githubusercontent.com/u/9892522?v=3&s=100)](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![webpack](https://avatars3.githubusercontent.com/u/2105791?v=3&s=100)](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[![hoodie](https://avatars1.githubusercontent.com/u/1888826?v=3&s=100)](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![pouchdb](https://avatars3.githubusercontent.com/u/3406112?v=3&s=100)](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[![neovim](https://avatars0.githubusercontent.com/u/6471485?v=3&s=100)](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[![babel](https://avatars2.githubusercontent.com/u/9637642?v=3&s=100)](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[<img width="100" src="https://github.com/adobe/brackets/blob/gh-pages/images/brackets_128.png?raw=true">](https://github.com/adobe/brackets/labels/Starter%20bug)|
|[ava](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[webpack](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[hoodie](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[pouchdb](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[neovim](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[babel](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[brackets](https://github.com/adobe/brackets/labels/Starter%20bug)|
| [![Node.js](https://avatars1.githubusercontent.com/u/9950313?v=3&s=100)](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|[<img width="100" src="https://github.com/Semantic-Org/Semantic-UI-React/raw/master/docs/app/logo.png">](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|
| [Node.js](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |[Semantic-UI-React](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |

[Tutorial für die GitHub-Desktop-App - Englisch](github-desktop-tutorial.md)
