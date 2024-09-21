[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png" alt="Junte-se a nós no Slack">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Primeiras Contribuições

Este projeto visa facilitar o caminho e guiar os iniciantes em suas primeiras contribuições. Se você deseja fazer a sua primeira contribuição, siga os passos abaixo.

_Se você não se sente confortável com linhas de comando, [aqui estão alguns tutoriais utilizando ferramentas gráficas.](#Tutoriais-usando-outras-ferramentas)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork deste repositório" />

#### Se não tem git em sua máquina, [instale-o](https://help.github.com/articles/set-up-git/).

## Faça um _Fork_ deste repositório

Faça um _Fork_ clicando no botão **_Fork_** no topo da página inicial do repositório. Isso criará uma cópia deste repositório em sua conta.

## Clone o repositório

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clonar este repositório" />

Agora clone o _fork_ do repositório para a sua máquina.
Vá pra sua conta no GitHub, abra o _fork_ deste repositório, clique no botão **_Code_** e, em seguida, clique no ícone **_Copy to clipboard_** para copiar o endereço.

Abra um terminal e execute o seguinte comando do git:

```bash
git clone "endereço copiado"
```

onde "endereço copiado" (sem as aspas) é a URL deste repositório (seu fork deste projeto). Consulte as etapas anteriores para obter a URL.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copiar endereço" />

Por exemplo:

```bash
git clone https://github.com/seu-usuario/first-contributions.git
```

onde `seu-usuário` é o seu usuário do GitHub. Aqui você estará copiando o conteúdo do repositório **_first-contributions_** para o seu computador.

## Crie um _branch_

Acesse o diretório do repositório no seu computador (caso você não esteja nele):

```bash
cd first-contributions
```

Agora crie um _branch_ usando o comando `git switch`:

```bash
git switch -c seu-novo-branch
```

Por exemplo:

```bash
git switch -c add-nome-sobrenome
```

Obs.: O nome do _branch_ não precisa ter a sigla "add", mas nesse caso é recomendável, porque a finalidade deste _branch_ é adicionar o seu nome à lista de contribuidores.

## Efetue as alterações necessárias e faça _commit_ dessas alterações

Agora, abra o arquivo `Contributors.md` em seu editor de código e adicione o seu nome a ele. Não o adicione no início ou no final do arquivo. Coloque-o em qualquer lugar no meio. Agora, salve o arquivo.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Se você for para o diretório do projeto e executar o comando `git status`, verá que existem alterações. Adicione essas alterações ao _branch_ que você acabou de criar utilizando o comando `git add`:

```bash
git add Contributors.md
```

Agora, confirme essas alterações usando o comando `git commit`:

```bash
git commit -m "Add <seu-nome> to Contributors list"
```

substituindo `<seu-nome>` pelo seu nome.

## Envie as alterações para o GitHub

Envie suas alterações usando o comando `git push`:

```bash
git push origin <nome-da-sua-branch>
```

substituindo `<nome-da-sua-branch>` pelo nome do _branch_ que você criou anteriormente.

## Submeta suas alterações para revisão

Se você for para o seu repositório no GitHub, verá um botão **_Compare & pull request_**. Clique nesse botão.

<img src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="Crie um Pull Request" />

Agora envie o **_pull request_**.

<img src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="Envie o Pull Request" />

Logo eu estarei mesclando (fazendo _merge_) as suas alterações no _branch_ principal (_main_) deste projeto. Você receberá um e-mail de notificação quando as alterações forem mescladas.

## Para onde ir agora?

Parabéns! Você acabou de completar o fluxo de trabalho básico _fork_ -> _clone_ -> _edit_ -> _pull request_ que você encontrará frequentemente como contribuidor!

Celebre sua contribuição e compartilhe com seus amigos e seguidores na [aplicação web](https://firstcontributions.github.io/#social-share).

Você pode se juntar-se à nossa equipe no Slack caso precise de alguma ajuda ou tenha alguma dúvida. [Junte-se à nossa equipe no Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Agora vamos colocá-lo para contribuir com outros projetos. Nós compilamos uma lista de projetos com problemas simples nos quais você pode começar a trabalhar. Verifique [a lista de projetos na aplicação web](https://firstcontributions.github.io/#project-list).

### [ Material adicional ](../additional-material/translations/Portuguese/additional-material.pt-br.md)

## Tutoriais usando outras ferramentas

| <a href="../gui-tool-tutorials/translations/Portuguese/github-desktop-tutorial.pt-br.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/translations/Portuguese/github-windows-vs2017-tutorial.pt-br.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/translations/Portuguese/github-windows-intellij-tutorial.pt-br.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [GitHub Desktop](../gui-tool-tutorials/translations/Portuguese/github-desktop-tutorial.pt-br.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/translations/Portuguese/github-windows-vs2017-tutorial.pt-br.md)                                                                                                       | [IntelliJ IDEA](../gui-tool-tutorials/translations/Portuguese/github-windows-intellij-tutorial.pt-br.md)                                                                                                                                                          |
