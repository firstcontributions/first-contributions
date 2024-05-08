[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Primeiras Contribuições

É difícil. É sempre difícil fazer algo pela primeira vez. Especialmente quando se está a colaborar, errar não é algo agradável. Mas *open source* (código aberto) trata-se de colaboração e de trabalharmos juntos. Queremos simplificar a forma com que novos colaboradores *open source* aprendem e contribuem pela primeira vez.

Ler artigos e ver tutoriais pode ajudar, mas nada melhor do que realmente "pôr a mão na massa" sem estragar nada. Este projecto visa simplificar a forma com que os novatos fazem a sua primeira contribuição. Lembre-se: quanto mais relaxado(a) estiveres, melhor aprenderás. Se quiseres fazer a tua primeira contribuição, siga os passos abaixo. Nós prometemos, será divertido.

Se ainda não tens o git na tua máquina, [instala-o aqui]( https://help.github.com/articles/set-up-git/ ).

## Faz Fork deste repositório
<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork deste repositorio" />

Faz Fork clicando no botão "Fork" no topo desta página. Esta operação criará uma cópia deste repositório na tua conta.
<br></br><br></br>
## Clona o repositório

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clonar este repositório" />

Agora clona este repositório para a tua máquina local. Clique no botão "Clone or download" e, em seguida, clica no ícone "Copy to clipboard" para copiar o URL.

Abre o teu terminal e executa o comando seguinte:
```
git clone "url que copiou"
```
onde "url que copiou" (sem as aspas) é o URL deste repositório. Consulte as etapas anteriores para obter o URL.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copiar URL" />

Por exemplo:
```
git clone https://github.com/este-é-voce/first-contributions.git
```
onde "este-é-voce" é o teu nome de usuário do GitHub. Aqui estás a copiar o conteúdo do repositório first-contributions para o teu computador.

## Cria um Branch

Vá para o diretório do repositório no teu computador (caso ainda não estejas lá):
```
cd first-contributions
```

Agora crie um novo Branch usando o comando `git checkout`:
```
git checkout -b <add-teu-nome>
```

Por exemplo:
```
git checkout -b add-alonzo-church
```
Obs.: O nome do Branch não precisa de ter a sigla "add", mas neste caso é recomendável, porque a finalidade deste Branch é a de adicionar o teu nome a uma lista.

## Efetua as alterações necessárias e faz um Commit

Agora abra o ficheiro `Contributors.md` no teu editor de código, adiciona o teu nome e guarda o ficheiro. Se fores para o diretório do projeto e executares o comando `git status`, verás que há alterações. Adiciona essas alterações ao Branch que acabaste de criar utilizando o comando `git add`:
```
git add Contributors.md
```
Agora faz um Commit dessas alterações utilizando o comando `git commit`:
```
git commit -m "Add <Teu-nome> to Contributors list"
```
substitui `<Teu-nome>` pelo teu nome ou nickname.

## Faz um Push das alterações para o GitHub

Faz um Push utilizando o comando `git push`:
```
git push origin <add-teu-nome>
```
substitui `<add-teu-nome>` pelo nome do Branch que criaste anteriormente.

## Envia as tuas alterações para serem revistas

Se fores para o teu repositório no GitHub, verás um botão `Compare & pull request`. Clica nesse botão.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="Cria um Pull Request" />

Agora envia um Pull Request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="Envia um pull request" />

Quando puder incorporarei as tuas mudanças no Branch principal (master) deste projeto. Vais receber um e-mail de notificação quando as alterações forem incorporadas.

## Para onde ir a partir daqui?

Celebra as tuas contribuições e partilha-as com amigos e seguidores através da [web app](https://firstcontributions.github.io/#social-share).

 Podes também juntar-te à nossa equipa no Slack caso precises de alguma ajuda ou tenhas alguma dúvida. [Junta-te à nossa equipa no Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Aqui estão alguns repositórios com Issues a nível de principiante em que tu podes ajudar a resolver. Vai em frente e clica nos repositórios para saber mais.

### [ Material adicional ](../additional-material/translations/Portugues/additional-material.pt_br.md)

## Tutoriais com outras ferramentas


| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |

