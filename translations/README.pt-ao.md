[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Primeiras Contribuições

Começando no **Mundo Open-source ?** Então aqui você tem a sua oportunidade de fazer a sua primeira contribuição open-source, Siga os passos abaixo e no final você terá provalmente ter feito a sua primeira contribuição 🙂

Primeiramente, vamos começar por instalar o [Git](https://pt.wikipedia.org/wiki/Git) para que seja possível continuar os passos abaixos descritos, você poderá fazer a instalação do git, caso não tenha  do através do link para a [Página de Instalação]( https://help.github.com/articles/set-up-git/ ).


## Faz Fork deste repositório
<img align="right" width="350" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork deste repositorio" />

Faz Fork clicando no botão "Fork" no topo desta página e de seguida click na opção *Create a new Fork(Criar novo fork, em português)*
<br></br><br></br>
## Clone o repositório

<img align="right" width="350" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clonar este repositório" />

Pós o fork, clone o repositorío para o seu dispositivo, Clicando no botão de *Code(código, em português)* e de seguida copiar o link, que aparecerá.

Abra o seu Terminal ou PowerShell e digite o seguinte:
```
git clone <Qui aqele link que copiaste>
```
 Para que fique assim:

> git clone https://github.com/firstcontributions/first-contributions.git

De seguida dê Enter


## Cria uma nova Branch

Abra a pasta que foi criada quando você fez o clone

Agora crie uma nova Branch usando o comando no terminal:  `git checkout`:
```
git checkout -b <add-teu-nome>
```

Por exemplo:
```
git checkout -b edgar-dikenge
```
Obs.: O nome do Branch não precisa de ter a sigla "add", mas neste caso é recomendável, porque a finalidade deste Branch é a de adicionar o teu nome a uma lista.

## Efetua as alterações necessárias e faz um Commit

Agora vá para ficheiro `Contributors.md` no teu editor de código e adicione o seu nome e salve o ficheiro. Se fores para o diretório do projeto e executares o comando `git status`, verás que há alterações. Adiciona essas alterações ao Branch que acabaste de criar utilizando o comando `git add`:
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

## E agora ?

Partilhe com seus amigos e seguidores [web app](https://firstcontributions.github.io/#social-share).

 Podes também juntar-te à nossa equipa no Slack caso precises de alguma ajuda ou tenhas alguma dúvida. [Junta-te à nossa equipa no Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Aqui tens mais suguestões para a sua próxima contribuição, Baza lá dar uma olhada:

### [ Material adicional ](../additional-material/translations/Portuguese/additional-material.pt_br.md)

## Tutoriais com outras ferramentas


| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
