[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Primeiras Contribuições

| <img alt="Visual Studio Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width="40"> | Visual Studio Code |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |


É difícil. É sempre difícil a primeira vez que você faz algo. Especialmente quando você está colaborando, cometer erros não é uma coisa confortável. Mas o código aberto tem tudo a ver com colaboração e trabalho em conjunto. Queríamos simplificar a maneira como os novos colaboradores de código aberto aprendem e contribuem pela primeira vez.

Ler artigos e assistir a tutoriais pode ajudar, mas o que é melhor do que realmente fazer as coisas sem estragar nada. Este projeto visa fornecer orientação e simplificar a maneira como os novatos fazem sua primeira contribuição. Lembre-se, quanto mais relaxado você estiver, melhor você aprenderá. Se você está procurando fazer sua primeira contribuição, basta seguir os passos simples abaixo. Nós prometemos a você, vai ser divertido.

Se você não tiver o Visual Studio Code em sua máquina, [instale-o](https://code.visualstudio.com/download).

**Atenção:** Este tutorial foi feito usando o Visual Studio Code (Versão 1.27.2) em uma máquina Windows 10. Mais adiante neste tutorial, usaremos alguns atalhos de teclado. Eles podem diferir em outros sistemas operacionais (macOS/Linux), bem como no idioma do teclado (UK, DE, etc). Você pode percorrer sua lista de atalhos pesquisando "atalho" na Paleta de Comandos.

## Fork este repositório

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Fork este repositório clicando no botão fork no canto superior direito desta página. Isso criará uma cópia deste repositório em sua conta do GitHub.

O GitHub acompanha o relacionamento entre seu repositório e aquele do qual você o bifurcou. Você pode pensar em seu repositório como uma cópia de trabalho.

A maioria dos repositórios de alto nível do GitHub (ou seja, aqueles que não são bifurcados de nenhum outro repositório) têm uma pequena equipe principal de pessoas que podem confirmar alterações diretamente. Todos os outros contribuidores devem bifurcar o repositório e fazer alterações na bifurcação e, em seguida, criar uma solicitação de pull para solicitar que suas alterações sejam mescladas novamente no repositório de nível superior. Se o administrador de repo de nível superior gostar das alterações, elas serão mescladas e você ganhará fama e fortuna instantâneas! Mais sobre como fazer isso mais tarde.

## Clone seu repositório

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

A próxima etapa é clonar seu repositório para sua máquina para que você possa começar a fazer alterações. O VS Code precisa do URL do seu repositório, então clique no botão "clone" e depois clique no ícone "copiar para a área de transferência".

**CUIDADO:** Um erro que os novos contribuidores costumam cometer é clonar o repositório que você bifurcou _de_ em vez de clonar seu repositório. Verifique a barra de endereços do seu navegador e certifique-se de estar clonando seu repositório.

Agora abra o Visual Studio Code. A página de boas-vindas do VS Code aparecerá. A partir daí, pressione `F1` para abrir a barra mostrada abaixo. Observe que já existe um sinal `>` (maior que) no campo de texto. Você também pode acessar o prompt de entrada pressionando `CTRL-P` e digite o caractere `>`.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone.png" alt="Clone Popup (Command Popup)" />

Você pode notar que já existem alguns comandos obscuros listados abaixo. Esses são meus comandos usados recentemente. Então, simplesmente não se importe com eles.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone1.png" alt="Clone repo" />

Agora digite `git clone`, apenas `git` ou `clone` (funciona como uma pesquisa).
Selecione a entrada `Git: Clone` e pressione `Entrar`

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone2.png" alt="Colar URL do repositório" />

Cole a URL do seu repositório e pressione `Entrar`. Isso abrirá um File Explorer onde você pode escolher onde o repositório Git deve ser armazenado.

**Importante**: Certifique-se de que é o repositório bifurcado e não o original, caso contrário não funcionará.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone3.png" alt="Status popup" />

Você deve ver um pop-up de status no canto inferior direito do Visual Studio Code. Depois de terminar, você pode abrir o repositório clonado (agora uma pasta em sua máquina) usando os botões da caixa de diálogo.

## Criar uma branch

Abra a paleta de comandos novamente pressionando `F1`. Digite `branch` e selecione o comando `criar branch` a partir daí. Na próxima etapa digite o nome do seu novo branch, por exemplo `add-david-kroell`. Pressione enter e a ramificação será criada. A filial também já foi verificada. [O que significa checkout?](https://www.git-scm.com/docs/git-checkout)

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-branch.png" alt="Branches Command Palette" />

## Faça as alterações necessárias

Abra `Contributors.md` e adicione seu nome em qualquer lugar do arquivo. Este arquivo contém GFM (GitHub Flavored Markdown), que é um sabor proprietário da sintaxe <a href="https://en.wikipedia.org/wiki/Markdown">markdown</a>.

Copie um dos outros contribuidores&apos; linhas e modifique-o com seu nome para ter certeza de obter a sintaxe correta - pode ser exigente.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-changes.png" alt="Add your name" />

## Confirmar e enviar alterações para o GitHub

No lado esquerdo do VS Code há um menu com 5 ícones exibidos. Selecione o ícone de controle de versão/Controle de origem.
(Atalho: Ctrl + Shift + G)

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-commit.png" alt="Commitar alterações" />

O explorador de arquivos exibe todos os arquivos que foram alterados após o último commit. Ao passar o mouse sobre os arquivos e clicar em `+` (mais), os arquivos são encenados.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-commit1.png" alt="Arquivos guardados">

Digite algo na linha na parte superior do explorer e pressione a marca de seleção. As alterações agora estão confirmadas em sua cópia local. Agora as alterações precisam ser enviadas de volta ao GitHub.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-push.png" alt="Arquivos guardados">

Use o ícone de três pontos para abrir o menu onde você seleciona a opção `Publicar Branch`. Isso deve abrir uma caixa de diálogo para colocar suas credenciais do GitHub.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-gh-auth.png" alt="Arquivos guardados">

## Envie suas alterações para revisão

Neste ponto, você concluiu sua alteração, mas ela ainda reside apenas em seu repositório. Esta etapa mostrará como enviar uma solicitação ao administrador do repositório de nível superior para mesclar sua alteração.

Em seu repositório no GitHub, você verá o botão `Comparar & pull request` ao lado da nova notificação de branch. Clique nesse botão.

<img src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="crie uma pull request" />

Agora envie a solicitação PR - pull request.

<img src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Em breve estarei mesclando todas as suas alterações no branch master deste projeto. Você receberá um e-mail de notificação assim que as alterações forem mescladas.

## Para onde ir a partir daqui?

Parabéns! Você acabou de concluir o fluxo de trabalho padrão _fork -> clone -> editar -> PR_ que você encontrará frequentemente como colaborador!

Comemore sua contribuição e compartilhe com seus amigos e seguidores acessando [aplicativo da web](https://firstcontributions.github.io#social-share).

Você pode se juntar à nossa equipe do slack caso precise de ajuda ou tenha alguma dúvida. [Junte-se à equipe do Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

### [Material adicional](../additional-material/translations/additional-material.pt_br.md)

## Tutoriais usando outras ferramentas
[Back to main page](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
