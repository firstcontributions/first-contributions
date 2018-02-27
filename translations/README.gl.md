[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" src="https://firstcontributions.herokuapp.com/badge.svg">](https://firstcontributions.herokuapp.com)

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

<img style="float: right;" src="../assets/submit-pull.png" alt="sube a pull request" />

Axiña fusionarei os teus trocos (facendo *merge*) na master branch deste proxecto. Recibirás unha notificación por correo cando los trocos xa estean fusionados.

### [ Material adicional ](additional-material/additional-material.md)

## Titoriais con outras ferramentas


|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://camo.githubusercontent.com/4dc59d7919925e4ebab5a98180b2a9d21446ca53/68747470733a2f2f6c68362e676f6f676c6575736572636f6e74656e742e636f6d2f30657865323578584f7263566e726e33544964736735342d344677684341716f466d6f3545494d795a7443464e39706d763633484e427375457939643771656a7158782d486c49615159342d42526b6c6a6636373d77313336362d68363239" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/../assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

## Onde ir dende aquí?

Tamén poderías unirte á nosa *equipa* en Slack no caso de que necesites axuda ou teñas algunha pregunta. [Únete ó noso Slack](https://firstcontributions.herokuapp.com)

Aquí hai algúns *issues* para principiantes en repositorios populares que poderías resolver. Anímate e vai a eses repos para aprender máis:

|[![exercism](https://avatars2.githubusercontent.com/u/5624255?v=3&s=100)](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[![fun-retro](https://avatars3.githubusercontent.com/u/15913975?v=3&s=100)](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[<img width="100" src="https://cdn.worldvectorlogo.com/logos/react.svg">](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[![habitat](https://avatars1.githubusercontent.com/u/18171698?v=3&s=100)](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![scikit-learn](https://avatars0.githubusercontent.com/u/365630?v=3&s=100)](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[<img width="100" src="https://camo.githubusercontent.com/0f302c808c8457f6460913e33aed3478124612c2/687474703a2f2f6c65696e696e67656e2e6f72672f696d672f6c65696e696e67656e2e6a7067">](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[<img width="100" src="https://images.plot.ly/plotly-documentation/thumbnail/numpy-logo.jpg">](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[![elasticsearch](https://avatars2.githubusercontent.com/u/6764390?v=3&s=100)](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|---|---|---|---|---|---|---|---|
|[exercism](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[Fun Retros](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[react](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[habitat](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[scikit-learn](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[Leiningen](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[numpy](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[elasticsearch](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|[![homebrew](https://avatars2.githubusercontent.com/u/1503512?v=3&s=100)](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[![rust](https://avatars1.githubusercontent.com/u/5430905?v=3&s=100)](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[![vuejs](https://avatars1.githubusercontent.com/u/6128107?v=3&s=100)](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[![Suave](https://avatars2.githubusercontent.com/u/5822862?v=3&s=100)](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[![OpenRA](https://avatars3.githubusercontent.com/u/409046?v=3&s=100)](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![PowerShell](https://avatars0.githubusercontent.com/u/11524380?v=3&s=100)](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[![coala](https://avatars2.githubusercontent.com/u/10620750?v=3&s=100)](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[![moment](https://avatars2.githubusercontent.com/u/4129662?v=3&s=100)](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[homebrew](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[Rust](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[vuejs](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[Suave](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[OpenRA](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[PowerShell](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[coala](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[moment](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[![ava](https://avatars0.githubusercontent.com/u/8527916?v=3&s=100)](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[![freeCodeCamp](https://avatars0.githubusercontent.com/u/9892522?v=3&s=100)](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![webpack](https://avatars3.githubusercontent.com/u/2105791?v=3&s=100)](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[![hoodie](https://avatars1.githubusercontent.com/u/1888826?v=3&s=100)](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![pouchdb](https://avatars3.githubusercontent.com/u/3406112?v=3&s=100)](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[![neovim](https://avatars0.githubusercontent.com/u/6471485?v=3&s=100)](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[![babel](https://avatars2.githubusercontent.com/u/9637642?v=3&s=100)](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[<img width="100" src="https://github.com/adobe/brackets/blob/gh-pages/images/brackets_128.png?raw=true">](https://github.com/adobe/brackets/labels/Starter%20bug)|
|[ava](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[webpack](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[hoodie](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[pouchdb](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[neovim](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[babel](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[brackets](https://github.com/adobe/brackets/labels/Starter%20bug)|
| [![Node.js](https://avatars1.githubusercontent.com/u/9950313?v=3&s=100)](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|[<img width="100" src="https://github.com/Semantic-Org/Semantic-UI-React/raw/master/docs/app/logo.png">](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|
| [Node.js](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |[Semantic-UI-React](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |
