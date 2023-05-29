[![Amor pelo Código Aberto](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-old-version-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![Licença: MIT](https://img.shields.io/badge/Licença-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Contribuidores de Código Aberto](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Primeiras Contribuições

| <img alt="Git Bash" src="https://cdn.icon-icons.com/icons2/2699/PNG/512/git_scm_logo_icon_170096.png" width="200"> | Edição Git Bash |
| ------------------------------------------------------------------------------------------------------------------ | ---------------- |

É difícil. Sempre é difícil fazer algo pela primeira vez. Principalmente quando se trata de colaborar, cometer erros não é algo confortável. Mas o código aberto é tudo sobre colaboração e trabalho em conjunto. Queríamos simplificar a forma como novos contribuidores de código aberto aprendem e contribuem pela primeira vez.

Ler artigos e assistir a tutoriais pode ajudar, mas nada é melhor do que realmente fazer as coisas sem bagunçar nada. Este projeto tem como objetivo fornecer orientações e simplificar a forma como os novatos fazem sua primeira contribuição. Lembre-se de que quanto mais relaxado você estiver, melhor aprenderá. Se você está procurando fazer sua primeira contribuição, siga os passos simples abaixo. Prometemos que será divertido.

Se você não tem o Git Bash em seu computador com Windows, [instale-o](https://git-scm.com/download/win).

<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/fork.png" alt="fork this repository" />

## Faça um Fork deste repositório

Faça um fork deste repositório clicando no botão de fork no canto superior direito desta página.
Isso criará uma cópia deste repositório em sua conta.

## Clone o repositório

Agora clone este repositório em sua máquina.

IMPORTANTE: NÃO CLONE O REPOSITÓRIO ORIGINAL. Vá para o seu fork e clone-o.

Para clonar o repositório, clique em "Code" e depois copie a sequência abaixo.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-clone-1.png" alt="copy string" />

Abra o aplicativo Git Bash que você acabou de baixar. Deve parecer com a imagem abaixo se estiver em um computador com Windows.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-1.png" alt="open git bash terminal" />

Vá para a pasta em que deseja salvar este projeto usando o seguinte comando

`cd <pasta>`

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-t

utorial/gb-terminal-2.png" alt="cd into a folder" />

Use a sequência que você copiou na etapa anterior para clonar o repositório usando o seguinte comando

`git clone <url-do-repo>`

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-clone-2.png" alt="clone the repository" />

Vá para o diretório onde o repositório está e abra-o no VS Code para fazer suas alterações.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-3.png" alt="cd into the newly cloned repo" />

## Crie um branch

Agora crie um branch usando o seguinte comando simples. Este comando não apenas cria um branch para você, mas também permite que você mude para esse branch.

```
git checkout -b <nome-do-branch>
```

Nomeie seu branch `<adicionar-seu-nome>`. Por exemplo, "add-james-smith"

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-branch.png" alt="create a branch" />

## Faça as alterações necessárias e faça commit dessas alterações

Agora abra o arquivo `Contributors.md` em um editor de texto, vá até o final da página e adicione seu nome a ele, depois salve o arquivo.

Exemplo: Se o seu nome for James Smith, deve ficar assim:

\[James Smith](https://github.com/jamessmith)

Você pode ver que há alterações em Contributors.md simplesmente executando o seguinte comando

`git status`

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-status.png" alt="check the status" />

Agora faça commit dessas alterações:

Primeiro, adicione a alteração que você fez à área de staging usando

`git add nome-do-arquivo`

Em seguida, escreva uma mensagem de commit usando este comando

`git commit -m "Adicionar seu-nome à lista de contribuidores"`

Substitua `<seu-nome>` pelo seu nome.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-commit.png" alt="commit changes" />

Para verificar se o seu commit foi feito, você pode executar o comando simples `git log --oneline`.

## Envie as alterações para o GitHub

Uma vez concluídas as etapas acima, você pode enviar suas alterações usando este comando

`git push origin <nome-do-branch>`

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-push.png" alt="push changes" />

## Envie suas alterações para revisão

Se você acessar seu repositório no GitHub, verá o botão `Compare & pull request`. Clique nesse botão.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/compare-and-pull.png" alt="create a pull request" />

Agora envie o pull request.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/submit-pull-request.png" alt="submit pull request" />

Em breve, vou mesclar todas as suas alterações no branch principal deste projeto. Você receberá um e-mail de notificação assim que as alterações forem mes