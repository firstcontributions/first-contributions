[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Primeiras Contribuições

| <img alt="SourceTree" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-logo.png" width="200"> | Atlassian Sourcetree |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |

É difícil. Sempre é difícil, quando você faz algo pela primeira vez. Especialmente quando você está colaborando, cometer erros não é uma coisa confortável. Mas o código aberto é tudo sobre colaboração e trabalhar juntos. Queremos simplificar a maneira como novos contribuintes de código aberto aprendem e contribuem pela primeira vez.

Ler artigos e assistir a tutoriais pode ajudar, mas o que é melhor do que realmente fazer as coisas sem estragar nada? Este projeto tem como objetivo fornecer orientação e simplificar a forma como os novatos fazem sua primeira contribuição. Lembre-se de que quanto mais relaxado você estiver, melhor você aprenderá. Se você está procurando fazer sua primeira contribuição, basta seguir os passos simples abaixo. Prometemos que será divertido.

## Sourcetree

Observe que este tutorial é para MacOS. Ele é semelhante ao Sourcetree no Windows, mas algumas coisas podem ser diferentes.

<!--
	****************************************
	*** Este tutorial está comentado até que ***
	*** um tutorial para Windows possa ser criado***
	****************************************
Observe que este tutorial é para MacOS. Consulte o [Tutorial para Windows]() para o Sourcetree, caso queira usar no Windows.
-->

Baixe [Sourcetree](https://www.sourcetreeapp.com), instale e abra-o.

Você deve ver o diálogo modal "Sourcetree".

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-1-main.png" alt="SourceTree Main" />

A partir daqui, você deve clicar em "Remote". Se esta for a primeira instalação, provavelmente você ainda não conectou sua conta do GitHub. Faça isso clicando no botão "Conectar".

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-2-main-connect.png" alt="SourceTree Connect" />

O diálogo *Contas* aparecerá. Clique em "Adicionar" no canto inferior esquerdo. Depois, selecione as configurações apropriadas para adicionar o GitHub (ou qualquer outra conta que você queira) ao cliente. Após selecionar suas configurações para o GitHub, clique em "Conectar Conta".

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-4-accounts-add.png" alt="SourceTree Connect Add" />

Isso abrirá uma página no seu navegador. Siga os passos fornecidos para autorizar sua conta.

## Fazer um Fork deste repositório

Faça o fork deste repositório clicando no botão de fork no topo desta página. <img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/fork.png" alt="fork this repository" />
Isso criará uma cópia deste repositório na sua conta.

## Clonar o repositório

No Sourcetree, clique no botão "Remote". Isso deve carregar todos os seus repositórios do GitHub, que estão listados no GitHub.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-5-cloning.png" alt="clone this repository" />

Depois de clicar no botão "Clonar", você será apresentado a outra visão para definir várias opções.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-6-cloning-confirm.png" alt="clone this repository" />

1. **URL de origem:** Este campo é preenchido automaticamente e você não precisa alterá-lo. Ele é a URL de onde o seu projeto do GitHub reside.

2. **Caminho de destino:** Este é o local físico no seu computador onde este projeto será salvo.

3. **Nome:** Este é um "Bookmark" para como o Sourcetree vai referenciar seu projeto. Pense nisso como um atalho.

*Nota: Normalmente os valores padrões nesses campos estão corretos.*

**Quando você estiver satisfeito, clique em "Clonar"**

Isso abrirá o navegador de repositórios principal para o seu repositório!

## Criar um branch

Clique no botão de branch na barra de ferramentas.

Nomeie seu branch como "add-your-name-to-contribution", por exemplo: "add-sally-to-contribution".

Para fazer isso, clique em **Branch (1)** que abrirá o diálogo de nomeação. Depois **Adicione seu nome (2)** como descrito. Por fim, clique em **Criar Branch**. Isso criará o branch com o nome que você escolheu.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-7-branching.png" alt="name your branch" />

## Faça as alterações necessárias e faça o commit

Agora abra o arquivo `Contributors.md` em um editor de texto e adicione seu nome a ele, com o link da sua URL do Github, depois salve o arquivo.

Você deverá ver e revisar o arquivo que foi alterado e decidir o que deseja adicionar ao stage. Fazer o stage é importante para informar ao git exatamente quais alterações de arquivo você quer associar a este commit.

*Nota: Se você não ver a diferença dos arquivos, clique em **Arquivos não commitados** na parte superior do seu diálogo.*

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-8-viewing-changed-files.png" alt="edit some file(s)" />

Depois clique no botão **Commit** no topo esquerdo do diálogo. Isso mostrará a área de stage.

Clique na *caixinha* para **adicionar** o arquivo à área de stage. Então, insira uma mensagem de commit.

*Nota: Você também pode selecionar arquivos (tanto nas áreas de stage quanto nas não stage) e adicionar/remover arquivos das respectivas áreas usando a barra de espaço.*

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-9-committing.png" alt="stage your changes" />

Após adicionar suas alterações e uma mensagem de commit, você pode pressionar o botão **Commit** para finalizar o commit.

Parabéns, você fez o commit de todas as alterações na sua cópia local do seu branch do fork do first-contributions. Agora, siga em frente!

## Enviar as alterações para o GitHub

Agora você está pronto para enviar suas alterações para o GitHub. Isso será feito no seu próprio fork do projeto. Siga os passos para enviar o seu branch. Primeiro, clique em **Push (1)**, isso abrirá o diálogo de envio/push. **Clique (2)** na caixinha do branch que você deseja enviar. Selecione **OK (3)** e isso enviará o seu commit para o GitHub.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-10-pushing.png" alt="origin or branch" />

## Submeter suas alterações para revisão

Se você for até o seu repositório no GitHub, verá o botão `Compare & pull request`. Clique nesse botão.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/compare-and-pull.png" alt="create a pull request" />

Agora envie o pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/submit-pull-request.png" alt="submit pull request" />

Em breve, eu estarei mesclando todas as suas alterações no branch master deste projeto. Você receberá um e-mail de notificação assim que as alterações forem mescladas.

## Onde ir a partir daqui?

Parabéns! Você acabou de completar o fluxo padrão *fork -> clone -> edit -> PR* que você encontrará frequentemente como contribuidor!

Celebre sua contribuição e compartilhe com seus amigos e seguidores indo para [web app](https://firstcontributions.github.io/#social-share).

Você pode se juntar ao nosso time do Slack caso precise de ajuda ou tenha alguma dúvida. [Junte-se ao time do Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

### [Material adicional](../../../additional-material/translations/Portugues/additional-material.pt_br.md)

## Tutoriais Usando Outras Ferramentas

[Voltar para a página principal](https://github.com/firstcontributions/first-contributions/blob/main/docs/translations/README.pt_br.md#tutoriais-usando-outras-ferramentas)

---

Essa é a tradução do conteúdo que você forneceu! Se precisar de mais alguma coisa, é só avisar.
