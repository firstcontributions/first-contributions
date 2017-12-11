[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" src="https://firstcontributions.herokuapp.com/badge.svg">](https://firstcontributions.herokuapp.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)


# Dein erstes Mitwirken

Aller Anfang ist immer schwer. Vor allem wenn du mit anderen zusammenarbeitest, ist es nicht gerade angenehm Fehler zu machen. Aber bei Open Source dreht es sich ausschließlich darum, gemeinsam zu arbeiten. Wir möchten es für Neueinsteiger in Sachen Open Source so einfach wie möglich machen, die Vorgänge zu lernen und zum ersten Mal beizutragen.

Artikel zu lesen und Tutorials anzusehen kann zwar helfen, aber was kann besser sein als wirklich das Zeug umzusetzen ohne etwas kaputt zu machen? Dieses Projekt hat es sich zum Ziel gesetzt, Richtlinien bereitzustellen und den ersten Beitrag eines Neulings zu einem Kinderspiel werden zu lassen. Denk dran: je entspannter du bist, desto einfacher lernst du. Falls du also herausfinden willst, wie man seinen ersten Beitrag (*contribution*) durchführt, folge einfach diesen einfachen Schritten. Wir versprechen, es wird dir Spaß machen!

#### *Read this in [other languages](LANGUAGES.md)*

<img align="right" width="300" src="../assets/fork.png" alt="Die Repository forken" />

Falls du `git` noch nicht auf deinem Computer hast, [installiere es]( https://help.github.com/articles/set-up-git/)!

## Diese Repository forken

Forke diese Repo (*repository*), indem du oben auf dieser Seite auf den `Fork`-Button klickst. Dies erstellt eine Kopie dieser Repository in deinem Account.

## Klone die Repository

<img align="right" width="300" src="../assets/clone.png" alt="Repository klonen" />

Jetzt klonst du diese Repository auf deinen Rechner. Klicke dazu auf den `Clone or download`-Button und dann auf das *In die Zwischenablage*-Icon.

Jetzt öffne ein Terminal (auch *Kommandozeile*) und führe den folgenden `git`-Befehl aus:

```
git clone "die soeben kopierte URL"
```

Wobei "die soeben kopierte URL" (ohne die Anführungszeichen) die URL zu dieser Repository ist. Die haben wir ja im vorherigen Schritt kopiert.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="URL in die Zwischenablage" />

Das sieht zum Beispiel so aus:

```
git clone https://github.com/DEIN-USERNAME/first-contributions.git
```

Wobei `DEIN-USERNAME` eben dein GitHub-Username ist. Hiermit kopierst du die Inhalte deiner `first-contributions`-Repository von GitHub auf deinen Rechner.

## Erstelle einen Branch

Gehe dazu zuerst in das Verzeichnis der Repository, falls du da nicht sowieso schon bist:

```
cd first-contributions
```

Jetzt erstellst du mit dem `git checkout`-Befehl einen neuen Branch:

```
git checkout -b add-DEIN-NAME
```

Also zum Beispiel:

```
git checkout -b add-max-mustermann
```

(Der Name des Branch muss nicht das Wort *add* beinhalten. Er sollte aber beschreibend für die Funktion des Branches sein und da wir unseren Namen hinzufügen wollen… du verstehst schon.)

## Führe die gewünschten Änderungen durch und committe sie

Öffne nun die `Contributors.md`-Datei in einem Texteditor, füge deinen Namen unten an und dann speichere die Datei. Wenn du im Terminal nun in das Projektverzeichnis gehst und den Befehl `git status` ausführst, wirst du sehen, dass es Änderungen gab. Füge diese Änderungen nun mit `git add` zum Branch hinzu, den du vorhin erstellt hast:

```
git add Contributors.md
```

Nun bestägige (*commit*) dieser Änderungen über den `git commit`-Befehl:

```
git commit -m "Add <DEIN-NAME> to Contributors list"
```

… und natürlich fügst du für `<DEIN-NAME>` deinen Namen ein.

## Änderungen auf GitHub pushen

Pushe deine Änderungen nun auf deine GitHub-Repository mit dem `git push`-Befehl:

```
git push origin add-DEIN-NAME
```

… wobei `add-DEIN-NAME` der Name des Branches ist, den du vorhin erstellt hast.

## Reiche deine Änderungen zur Überprüfung ein

Wenn du nun deine Repository auf GitHub besuchst, wirst du einen `Compare & pull request`-Button sehen. Klick da mal drauf!

<img style="float: right;" src="../assets/compare-and-pull.png" alt="pull request erstellen" />

Sende das Formular nun ab, um einen *pull request* zu erstellen.

<img style="float: right;" src="../assets/submit-pull.png" alt="pull request absenden" />

Bald werde ich deine Änderungen in den `master`-Branch dieses Projekts mergen. Dabei wirst du eine Benachrichtigung per Mail bekommen, sobald das passiert ist.

## Und wie geht's nun weiter?

Freue dich über deine Beteiligung und teile es mit deinen Freunden und Followern über die [web app](https://roshanjossey.github.io/first-contributions/#social-share)!

Du kannst unserem Slack-Team beitreten, falls du noch bei irgendetwas Hilfe benötigst oder du eine Frage hast. [Dem Slack-Team beitreten](https://firstcontributions.herokuapp.com).

Jetzt bist du bereit, um auch bei anderen Projekten mitzuwirken. Wir haben eine Liste an Projekten angefertigt, die kleine Änderungen für den Einstieg bereitstellen. Zieh dir die [Projektliste in der web app](https://roshanjossey.github.io/first-contributions/#project-list) rein!

### [Zusätzlicher Stoff](../additional-material/additional-material.md)

## Tutorial mit anderen Tools (Englisch)

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.microsoft.com/net/images/vslogo.png" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="../assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|

## Eigenwerbung

Falls dir dieses Projekt gefallen hat, *star* es auf [GitHub](https://github.com/Roshanjossey/first-contributions).
Und falls du gerade richtig wohltätig bist, folge [Roshan](https://roshanjossey.github.io/) auf [Twitter](https://twitter.com/sudo__bangbang) und
[GitHub](https://github.com/roshanjossey).
