[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Primeiras Contribuições

| <img alt="Visual Studio Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width="40"> | Visual Studio Code |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |

É difícil, sempre é difícil quando fazemos alguma coisa pela primeira vez. Especialmente quando você está colaborando, cometendo erros, não é nada confortável. No entanto, o open source é totalmente sobre colaboração e trabalho em equipe. Por isso, nós queremos simplificar a maneira como os novos colaboradores de código aberto aprendem e contribuem pela primeira vez.

Ler artigos e assistir a tutoriais até podem ajudar, mas o que é melhor do que fazer as coisas sem bagunçar nada. Este projeto tem como objetivo orientar & simplificar a forma como os iniciantes fazem a sua primeira contribuição. Lembre-se que você aprende melhor quando está relaxado. Se você deseja fazer sua primeira contribuição, basta seguir os passos abaixo. Nós prometemos a você que será divertido!

Se você não tem o Visual Studio 2017 na sua máquina, [instale-o](https://code.visualstudio.com/download).

**Nota:** Este tutorial foi feito utilizando o Visual Studio Code (Versão 1.27.2) no Windows 10. Mais tarde, neste tutorial, vamos utilizar alguns atalhos no teclado. Eles podem ser diferentes em outros sistemas operacionais (mac/OS/Linux) assim como em teclados de outras linguagens (UK, DE, etc). Você pode pesquisar na lista de atalhos, buscando por "atalhos" na Paleta de Comando.

## Faça o *Fork* deste repositório

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Faça um *fork* deste repositório clicando no botão *fork* (bifurcar) no canto superior direito desta página. Isso criará uma cópia deste repositório em sua conta do GitHub.

O GitHub rastreia a relação entre seu repositório e o original, o qual você fez o *fork*. Você pode pensar em seu repositório como uma cópia de trabalho.

Muitos dos repositórios matrizes do GitHub (ou seja, aqueles que não são *Fork* de nenhum outro repositório) tem um pequeno grupo de pessoas que podem fazer commits de modificações diretamente. Todos os outros contribuidores devem fazer um *for* do repositório e fazer alterações no *fork*, em seguida, devem criar um Pull Request para solicitar um *Merge* (mesclagem) das modificações feitas no repositório original.

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

## Create a branch

Open up the command palette again by pressing `F1`. Type in `branch` and select the `create branch` command from there. In the next step type in the name of your new branch, for example `add-david-kroell`. Press enter and the branch will be created. The branch is also already checked out. [What does checkout mean?](https://www.git-scm.com/docs/git-checkout)

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-branch.png" alt="Branches Command Palette" />

## Make necessary changes

Open `Contributors.md` and add your name anywhere in the file. This file contains GFM (GitHub Flavored Markdown) which is a proprietary flavor of the <a href="https://en.wikipedia.org/wiki/Markdown">markdown</a> syntax.

Copy one of the other contributors&apos; lines and modify it with your name to make sure you get the syntax right - it can be picky.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-changes.png" alt="Add your name" />

## Commit & Push changes to GitHub

On the left side of VS Code is a menu with 5 icons displayed. Select the version control/Source Control icon.
(Shortcut : Ctrl + Shift + G)

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-commit.png" alt="Commit changes" />

The file explorer displays all files which were changed after the last commit. By hovering the files and clicking the `+` (plus) the files are staged.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-commit1.png" alt="Stashed Files">

Type something in the line on top of the explorer and press the checkmark. The changes are now committed to your local copy. Now the changes have to be pushed back to GitHub.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-push.png" alt="Stashed Files">

Use the three-dot icon to open up the menu where you select the `Publish Branch` option. This should open up a dialog to put your GitHub credentials in.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-gh-auth.png" alt="Stashed Files">

## Submit your changes for review

At this point you have completed your change but it still only resides in your repo. This step will show you how to submit a request to the administrator of the top-level repo to merge your change.

In your repo on GitHub you'll see the `Compare & pull request` button next to the new branch notification. Click on that button.

<img src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Now submit the pull request.

<img src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Soon I'll be merging all your changes into the master branch of this project. You will get a notification email once the changes have been merged.

## Where to go from here?

Congrats! You have just completed the standard _fork -> clone -> edit -> PR_ workflow that you'll encounter often as a contributor!

Celebrate your contribution and share it with your friends and followers by going to [web app](https://firstcontributions.github.io#social-share).

You can join our slack team in case you need any help or have any questions. [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).


### [Additional material](../additional-material/git_workflow_scenarios/additional-material.md)

## Tutorials Using Other Tools
[Back to main page](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
