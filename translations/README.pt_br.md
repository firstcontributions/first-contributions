[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png" alt="Junte-se à nós no Slack">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Primeiras Contribuições

Este projeto visa facilitar o caminho e guiar os iniciantes em suas primeiras contribuições. Se você deseja fazer a sua primeira contribuição, siga os passos abaixo.

#### _Se não se sente confortável com a linha de comando, [aqui estão alguns tutoriais de ferramentas gráficas.](#Tutoriais-usando-outras-ferramentas)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork deste repositório" />

Se não possui o git em sua máquina, [instale-o aqui](https://help.github.com/articles/set-up-git/).

## Faça um _Fork_ deste repositório

Faça um _Fork_ clicando no botão "_Fork_" no topo desta página, uma cópia deste repositório será criada em sua conta.

## Clone o repositório

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clonar este repositório" />

Agora clone este repositório para a sua máquina. Clique no botão "_Code_" e, em seguida, clique no ícone "_Copy to clipboard_" para copiar a URL.

Abra um terminal e execute o seguinte comando do git:

```
git clone "url que copiou"
```

onde "url que copiou" (sem as aspas) é a URL deste repositório (seu fork deste projeto). Consulte as etapas anteriores para obter a URL.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copiar URL" />

Por exemplo:

```
git clone https://github.com/seu-usuario/first-contributions.git
```

onde "seu-usuário" é o seu usuário do _GitHub_. Aqui você estará copiando o conteúdo do repositório _first-contributions_ para o seu computador.

## Crie um Branch

Acesse o diretório do repositório no seu computador (caso você não esteja nele):

```
cd first-contributions
```

Agora crie um _Branch_ usando o comando `git switch`:

```
git switch -c <add-seu-nome>
```

Por exemplo:

```
git switch -c add-andre-oliveira
```

Obs.: O nome do _Branch_ não precisa ter a sigla "add", mas nesse caso é recomendável, porque a finalidade deste _Branch_ é a de adicionar o seu nome à uma lista.

## Efetue as alterações necessárias e faça um _Commit_

Agora, abra o arquivo `Contributors.md` em seu editor de código e adicione o seu nome a ele. Não o adicione no início ou no final do arquivo. Coloque-o em qualquer lugar no meio. Agora, salve o arquivo.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Se você for para o diretório do projeto e executar o comando `git status`, verá que há alterações. Adicione essas alterações ao _Branch_ que você acabou de criar utilizando o comando `git add`:

```
git add Contributors.md
```

Agora, confirme essas alterações usando o comando git commit `git commit`:

```
git commit -m "Add <seu-nome> to Contributors list"
```

substituindo `<seu-nome>` pelo seu nome.

## Faça um Push das alterações para o _GitHub_

Envie suas alterações usando o comando `git push`:

```
git push origin <nome-da-sua-branch>
```

substituindo `<nome-da-sua-branch>` pelo nome do _Branch_ que você criou anteriormente.

## Envie suas alterações para serem revisadas

Se você for para o seu repositório no _GitHub_, verá um botão `Compare & pull request`. Clique nesse botão.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="Crie um Pull Request" />

Agora envie um _Pull Request_.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="Envie o Pull Request" />

Logo estará mesclando ('mergeando') as suas mudanças no _Branch_ principal (main) deste projeto. Você receberá um e-mail de notificação quando as alterações forem mescladas.

## Para onde ir a partir daqui?

Parabéns! Você completou o fluxo de trabalho básico _fork -> clone -> edit -> PR_ que você encontrará frequentemente como contribuidor!

Celebre sua contribuição e compartilhe com seus amigos e seguidores no [app web](https://firstcontributions.github.io/#social-share).

Você também pode se juntar à nossa equipe no _Slack_ caso precise de alguma ajuda ou tenha alguma dúvida. [Junte-se à nossa equipe no Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Agora você pode colaborar com outros projetos. Nós compilamos uma lista de projetos com problemas simples que você pode começar. Verifique em [a lista de projetos no web app](https://firstcontributions.github.io/#project-list).

### [ Material adicional ](../additional-material/translations/Portugues/additional-material.pt_br.md)

## Tutoriais usando outras ferramentas

| <a href="../gui-tool-tutorials/translations/github-desktop-tutorial.pt_br.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/translations/github-windows-intellij-tutorial.pt_br.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [GitHub Desktop](../gui-tool-tutorials/translations/github-desktop-tutorial.pt_br.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/translations/github-windows-vs2017-tutorial.pt_br.md)                                                                                                       | [IntelliJ IDEA](../gui-tool-tutorials/translations/github-windows-intellij-tutorial.pt_br.md)                                                                                                                                                          |
