[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Primeiras Contribucións

É difícil. Sempre é difícil a primeira vez que fas algo. Especialmente cando estás colaborando, equivocarse non é algo agradable. Pero no *open source* (o código abierto) todo trata de colaboración e de traballar xuntos. Quixemos simplificar a forma na que novos contribuidores *open-source* aprenden y contribúen pola primeira vez.

Ler artículos e ver titoriais pode axudar, pero que haberá mellor que facer as cousas sen derramar nada?. Iste proxecto enfócase en prover unha guía e en simplificar a forma na que os novatos fan a súa primeira contribución. Lembra que mentres máis relaxado esteas, mellor aprenderás. Se queres facer a túa primeira contribución só tés que seguir os sinxelos pasos que se amosan a continuación. E prometemosche que será entretido.

<img align="right" width="300" src="../assets/fork.png" alt="fork de éste repositorio" />

Se aínda non tés git na túa máquina, [ instálao ]( https://help.github.com/articles/set-up-git/ )

## Bifurca(*Fork*) este repositorio

Fai un *fork* (bifurcación) deste repo facendo click no botón "Fork" que está na cima desta páxina.
Isto creará unha copia deste repositorio na túa conta.

## Clona(*Clone*) o repositorio

<img align="right" width="300" src="../assets/clone.png" alt="clonar este repositorio" />

A continuación clona este repo no teu equipo. Fai click no botón "*Clone*" e despois na icona para copiar ó portapapeis (clipboard)

Abre a túa consola ou terminal e executa o seguinte comando de git:

```
git clone "url que copiache"
```
Onde "url que copiache" (sen as comiñas) é a url  deste repositorio. Mira os pasos previos para obter a url.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copiar URL a clipboard" />

Por exemplo:
```
git clone https://github.com/o-teu-nome/first-contributions.git
```
Onde "o-teu-nome" é o teu usuario de GitHub. Aquí estarás copiando os contidos do repositorio first-contributions en GitHub para o teu computador.

## Crear unha póla(*Branch*)

Cambia ó directorio do repositorio no teu computador (se é que non estás xa nel).

```
cd first-contributions
```

Agora crea unha branch (póla) usando o comando `git checkout`

```
git checkout -b <engade-o-teu-nome>
```

Por exemplo
```
git checkout -b engade-María-Soliña
```

(O nome da branch non ten que incluir necesariamente a palabra 'engade', pero resulta razoable se consideramos que o propósito desta póla é engadir o teu nome a unha lista).

## Fai os trocos necesarios e efectúa(*Commit*) eses trocos

Agora abre o arquivo `Contributors.md` nun editor de texto, engade o teu nome e despois garda o arquivo. Se vas ó directorio do proxecto e executas `git status`, verás que hai trocos. Agrega eses trocos usando o comando `git add`  tal como se amosa:
```
git add Contributors.md
```

Agora podes facer commit sobre os trocos co comando `git commit`
```
git commit -m "Add <o-teu-nome> to Contributors list"
```
cambiando `<o-teu-nome>` polo teu nome.

## Envía (*Push*) os teus trocos a GitHub

Fai un  *push* dos teus trocos usando o comando `git push`
```
git push origin <engade-o-teu-nome>
```
cambiando `<engade-o-teu-nome>` polo nome da branch que creaches antes.

## Envía os teus trocos para seren revisados

Se vas ó teu repositorio en GitHub, verás un botón `Compare & pull request`. Fai click nese botón:

<img style="float: right;" src="../assets/compare-and-pull.png" alt="crea unha pull request" />

Agora crea e envía a pull request:

<img style="float: right;" src="../assets/submit-pull-request.png" alt="sube a pull request" />

Axiña fusionarei os teus trocos (facendo *merge*) na master branch deste proxecto. Recibirás unha notificación por correo cando los trocos xa estean fusionados.

### [ Material adicional ](../additional-material/git_workflow_scenarios/additional-material.md)

## Titoriais con outras ferramentas


|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="../assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

## Onde ir dende aquí?

Tamén poderías unirte á nosa *equipa* en Slack no caso de que necesites axuda ou teñas algunha pregunta. [Únete ó noso Slack](https://firstcontributors.slack.com/join/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)
