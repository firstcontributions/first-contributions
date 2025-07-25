[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Primeiras Contribuições

| <img alt="Visual Studio Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width="40"> | Visual Studio Code |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |

É difícil, sempre é difícil quando fazemos alguma coisa pela primeira vez. Especialmente quando você está colaborando, cometendo erros, não é nada confortável. No entanto, o open source é totalmente sobre colaboração e trabalho em equipe. Por isso, nós queremos simplificar a maneira como os novos colaboradores de código aberto aprendem e contribuem pela primeira vez.

Ler artigos e assistir a tutoriais até podem ajudar, mas o que é melhor do que fazer as coisas sem bagunçar nada. Este projeto tem como objetivo orientar & simplificar a forma como os iniciantes fazem a sua primeira contribuição. Lembre-se que você aprende melhor quando está relaxado. Se você deseja fazer sua primeira contribuição, basta seguir os passos abaixo. Nós prometemos a você que será divertido!

Se você não tem o Visual Studio 2017 na sua máquina, [instale-o](https://code.visualstudio.com/download).

**Nota:** Este tutorial foi feito utilizando o Visual Studio Code (Versão 1.27.2) no Windows 10. Mais tarde, neste tutorial, vamos utilizar alguns atalhos no teclado. Eles podem ser diferentes em outros sistemas operacionais (mac/OS/Linux) assim como em teclados de outras linguagens (UK, DE, etc). Você pode pesquisar na lista de atalhos, buscando por "atalhos" na Paleta de Comando.

## Faça o *Fork* deste repositório

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Faça um *fork* deste repositório clicando no botão *fork* (bifurcar) no canto superior direito desta página. Isso criará uma cópia deste repositório em sua conta do GitHub.

O GitHub rastreia a relação entre seu repositório e o original, o qual você fez o *fork*. Você pode pensar em seu repositório como uma cópia de trabalho.

Muitos dos repositórios matrizes do GitHub (ou seja, aqueles que não são *Fork* de nenhum outro repositório) tem um pequeno grupo de pessoas que podem fazer commits de modificações diretamente. Todos os outros contribuidores devem fazer um *fork* do repositório e fazer alterações no *fork*, em seguida, devem criar um Pull Request para solicitar um *Merge* (mesclagem) das modificações feitas no repositório original.

Se um dos administradores do repositório gostar e aprovar as tuas mudanças, eles *mergearão* e você ganhará fama e fortuna imediatamente! Abaixo, há mais detalhes sobre como fazer isso.

## Clone o seu repositório

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />


O próximo passo será clonar seu repositório em sua máquina para que você possa modificá-lo. Visual Studio precisa da URL do seu repositório, portanto clique no botão "clone" e então clique no ícone "copy to clipboard".

**CUIDADO:** Um erro que os novatos cometem com frequência é clonar o repositório do qual você fez o fork, ao invés de clonar seu repositório. Verifique a barra de endereços do seu navegador e certifique-se de que você está clonando o seu repositório.

Agora, abra o Visual Studio Code. A página principal do VS Code vai minimizar. A partir daí, pressione `F1` para abrir a barra mostrada abaixo. Perceba que já existe um `>` (maior que) no campo de texto. Você pode também chegar até o prompt de entrada pressionando `CTRL-P` e então inserindo o caracter `>`.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone.png" alt="Clone Popup (Command Popup)" />

Você pode notar que já aí já existem alguns comandos de sugestão abaixo. Esses são os seus comandos utilizados recentemente. Então, apenas ignore-os.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone1.png" alt="Clone repo" />

Agora, digite `git clone`, apenas `git` ou `clone` (isso funcionará como uma pesquisa).
Selecione a opção `Git: Clone` e então aperte `Enter`.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone2.png" alt="Paste Repository URL in" />

Cole a URL do seu repositório e aperte `Enter`. Isso vai abrir o Explorador de Arquivo onde você pode escolher onde o repositório Git será armazenado.

**Importante**: Tenha certerza que este é o repositório *forkeado* e não é o original. Se não, não funcionará.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone3.png" alt="Status popup" />

Você pode ver uma janela do status no canto inferior direito do Visual Studio Code. Depois de finalizado esse processo, você pode abrir o repositório clonado (agora, uma pasta na sua máquina) e usar os botões no diálogo.

## Crie uma *branch*

Abra a Paleta de Comando novamente, pressionando `F1`. Digite nele `branch` e selecione o comando `create branch` a partir das sugestões. No próximo passo, digite o nome da sua nova *branch*, por exemplo: `add-david-kroell`. Presione `Enter` e a *branch* será criada. A *branch* também está preparada para o *check out*. [*O que isso significa?*](https://www.git-scm.com/docs/git-checkout)

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-branch.png" alt="Branches Command Palette" />

## Faça as mudanças necessárias

Abra o arquivo `Contributors.md` e adicione o seu nome no fim da lista. Esse arquivo contém GFM (GitHub Flavored Markdown), que é uma função nativa da sintaxe do <a href="https://en.wikipedia.org/wiki/Markdown">markdown</a>.

Copie uma das outras linhas dos contribuidores e modifique-a com o seu nome. Tenha certeza que a sintaxe está correta - ela pode ser exigente.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-changes.png" alt="Add your name" />

## Faça um *Commit* & um *Push* das suas mudanças para o GitHub

No lado esquerdo do VS Code tem um menu com 5 ícones a amostra. Selecione o ícone de `Controle de Versão/Controle da Fonte`.
(Atalho : Ctrl + Shift + G)

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-commit.png" alt="Commit changes" />

O Explorador de arquivos mostra todos os arquivos que foram mudados depois do último commit. Sobrepondo o mouse nos arquivos e clicando no `+` (mais) os arquivos serão colocados no *stage*.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-commit1.png" alt="Stashed Files">

Escreva algo na caixa de texto, no topo do explorador e pressione o botão de *check*. As mudanças agora foram *commitadas* para a sua cópia local. Agora, as mudanças tem que serem mandadas para o GitHub.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-push.png" alt="Stashed Files">

Use o ícone dos três pontos para abrir o menu onde você selecionará a opção `Publicar Branch`. Isso deve abrir uma caixa de diálogo para colocar as tuas credenciais do GitHub.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-gh-auth.png" alt="Stashed Files">

## Submeta suas mudanças para uma revisão

Nesse ponto, você completou suas mudanças, mas elas ainda estão no seu repositório. Esse passo vai mostrar para você como submeter uma requisição para o administrador do repositório original para *mergear* suas mudanças.

No seu repositório no GitHub você verá o botão `Compare & Pull request` próximo a notificação da branch. Clique nesse botão.

<img src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Agora, submeta o *pull request*.

<img src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Breve as suas mudanças serão *mergeadas* na branch `master` desse projeto. Você será notificado por email uma vez que as mudanças forem *mergeadas*.

## Para onde ir ?


Parabéns! Você acabou de completar o fluxo de trabalho *fork -> clone -> edit -> PR* que vocẽ vai realizar frequentemente como um contribuidor!

Celebre a sua contribuição e compartilhe-a com os seus amigos e seguidores indo para o [web app](https://firstcontributions.github.io#social-share).

Você pode se juntar à nossa comunidade no slack, caso precise de alguma ajuda ou tenha alguma dúvida.

[Faça parte da nossa comunidade no Slack!](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)


### [Material adicional](../additional-material/git_workflow_scenarios/additional-material.md)

## Tutoriais utilizando outras ferramentas

[Retorne para a página principal](https://github.com/firstcontributions/first-contributions/blob/master/translations/README.pt_br.md)
