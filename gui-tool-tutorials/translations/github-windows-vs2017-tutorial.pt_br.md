[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Primeiras Contribuições

|<img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Visual_Studio_2017_logo_and_wordmark.svg/2000px-Visual_Studio_2017_logo_and_wordmark.svg.png" width="200">|Visual Studio 2017 Edition|
|---|---|

É difícil. Sempre é difícil fazer algo pela primeira vez. Especialmente quando você está colaborando, cometer erros não é confortável. Mas o open sourece tem tudo a ver com colaboração e trabalho em equipe. Nós queremos simplificar a maneira de aprendizagem aos novos contribuidores de open source e ajudar em sua primeira contribuição.

Lendo artigos e olhando tutoriais podem ajudar, mas o que é melhor do que realmente fazer as coisas sem estragar nada.
Esse projeto visa em providenciar uma orientação e simplificar a maneira dos novatos a conseguirem a sua primeira contribuição. 
Lembre-se, quanto mais relaxado melhor será o aprendizado. Se você está procurando em fazer a sua primeira contribuição, siga esses passos abaixo. Nós prometemos a você que vai ser divertido.

Se você não possui o Visual Studio 2017 na sua máquina, [instale-o aqui](https://www.visualstudio.com/downloads/).

## Faça um Fork deste repositório

<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/fork.png" alt="fork this repository" />

Para fazer um Fork deste repositório, basta clicar no botão de fork no topo da página. Isso criará uma cópia do repositório na
sua conta GitHub.

O GitHub acompapanhará o seu Fork e o repositório principal. Em outras palavras, podemos afirmar que o seu Fork é uma cópia do repositório principal.

Os respositórios de mais alto nível do GitHub (exemplo: aqueles que não há um fork de nenhum outro repositório), tem uma pequena equipe principal de pessoas que podem diretamente fazer os seus commits. Os outros contribuidores deverão criar um Fork do respositório e fazer as mudanças nesse Fork, em seguida criar um Pull Request perguntando se essas mudanças poderão ser mescladas no repositório de alto nível. Se o administrador do repositório gostar das alterações ele irá mesclar as modificações e você ganhará instantaneamente fama e fortuna! Abaixo há um tutorial de como realizar.

## Clone o seu repositório

<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/clone.png" alt="clone this repository" />

O próximo passo é clonar o seu repositório na sua máquina para começar a sua contribuição. O Visual Studio precisa da URL do seu repositório, então clique o botão "Clone" e depois clique no ícone "Copy to clipboard".

**CUIDADO** Um erro que os novatos cometem frequentemente é clonar o repositório original e não o Fork criado do repositório.
Verifique o endereço na barra de navegação e certifique-se de estar clonando o seu Fork.

Está na hora de entrar no Visual Studio 2017! Na maior parte do tutorial, você trabalhará na aba Team Explorer. Se não abrir de primeira, tente apertar `View > Team Explorer` para abrir. 

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-01-clone1.png" alt="Team Explorer" />

O Team Explorer tem muitas formas distintas de visualizar os arquivos e também botões de navegação localizado no topo para ajudar você em encontrar diferentes áreas. Para clonar o repositório, você precisa estar na opção Connect, que deveria estar como padrão. Se você não conseguir encontrar o botão "Clone", clique no plugue verde que está no topo.

Clique na opção `Clone` que está abaixo do **Local Git Repositories** e cole a URL do repositório na caixa de texto. Essa URL é o que você copiou no Clipboard do GitHub.

Clique no botão `Clone` para iniciar o processo 

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-02-clone2.png" alt="Clone repo" />

Quando o processo estiver completo você será deslocado para a aba Solution Explorer, onde conseguirá ver o conteúdo do repositório. Na sua tela será diferente da foto, pois as coisas mudam!

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-03-clone3.png" alt="Solution Explorer" />

## Crie uma Branch

Clique para voltar a aba Team Explorer e use o menu dropdown de navegação principal para abrir a opção "Branches".

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-04-branch1.png" alt="Branches view" />

Você encontrará o repositório **first-contributions** e a branch padrão, chamado  `master`. Apertando com botão direito do mouse no `master`, escolha `New Local Branch From...`.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-05-branch2.png" alt="New branch" />

Nomeie a sua branch como `add-<seu_nome_aqui>`, por exemplo: `add-alonzo-church`.

Deixe a área `Checkout branch` e clique o botão `Create Branch`.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-06-branch3.png" alt="Create branch" />

Você encontrará a sua nova branch na lista.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-07-branch4.png" alt="See new branch" />

## Faça mudanças necessárias

Abra o `Contributors.md` e adicione o seu nome no final da lista. Esse arquivo contém GFM (GitHub Flavored Markdown) que é uma propriedade de sintaxe do <a href="https://en.wikipedia.org/wiki/Markdown">markdown</a>.

Copie uma linha de um dos contribuidores e modifique com o seu nome para ter certeza que conseguiu a sintaxe certa - pode ser um pouco exigente. 

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-08-change1.png" alt="Add your name" />

## Commit e Push nas suas modificações no GitHub 

Mude de volta para aba Team Explorer e escolha a opção Changes.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-09-commit1.png" alt="Changes" />

Coloque a informação que você quer postar no seu commit e clique `Save`. O Visual Studio lembrará para o seus futuros commits. 

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-10-commit2.png" alt="Git user information" />

**AVISO** O Visual Studio usa pastas ocultas denomindas de `.vs` para guardar suas configurações e preferências pessoais.
O conteúdo dessa pasta **não deverá ser salvo no Git**. Se você não avisou o Git para ignorar essa pasta, avise-o mais rápido possível para não ser mandado no repositório.

Essa pasta já está ignorada nesse repositório, então você não precisa fazer esse passo...é só um cuidado para os seus futuros projetos. 

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-11-commit3.png" alt="Ignore vs folder" />

Agora você conseguirá ver a lista dos arquivos modificados e uma caixa de texto para comentar o seu commit. Os comentários deverão ser breve, porém minuciosos. Não tem nada pior que ler um comentário de um commit e ver isso: `"Eu atualizei algumas coisas"`. Leve alguns segundos para descrever o seu commit. Mais tarde a sua equipe vai agradecer, e você pode até agradecer a si mesmo!

Clique `Commit All and Push` para realizar um commit local e, em seguida, realize um push nas suas modificações para o seu repositório, isso tudo em um passo.

**AVISO** O commit pode ser realizado separadamente do push. Por conveniência nós fazemos os dois. Os commits são registrados na sua máquina, porém precisa realizar o push para mandar as modificações no GitHub.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-12-commit4.png" alt="Commit and Push" />

A primeira vez que você faz um push no GitHub, o Visual Studio vai perguntar sobre as suas credenciais do GitHub.
Normalmente, são armazenados em cache então provavelmente não aparecerá com muita frequência.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-13-commit5.png" alt="Login" />

Após realizar o push, abra o seu repositório no GitHub e aparecerá uma menssagem informando que houve um push em uma branch recentemente. 

Você pode ver as suas alterações abrindo o menu dropdown `Branch: master` e seleciona a sua nova branch. Parabéns, agora você consegue compartilhar a URL da branch ao mundo para mostrar o seu progresso. 

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-14-commit6.png" alt="View pushed branch on GitHub" />

## Envie as suas modificações para serem revisadas

Até aqui você terminou as suas modificações, porém ainda só está no seu repositório. Este passo mostrará como enviar uma solicitação ao administrador, para mesclar as suas alterações ao repositório de alto nível. 

No seu repositório do GitHub você vai ver um botão escrito: `Compare & pull request`, que fica ao lado da notificação da nova branch. Clique nesse botão.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/compare-and-pull.png" alt="create a pull request" />

Agora envie esse Pull Request.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/submit-pull-request.png" alt="submit pull request" />

Logo irei mesclar todas as suas mudanças na branch master do projeto. Você receberá uma notificação pelo e-mail quando as alterações forem mescladas.

## Onde eu posso ir a partir daqui?

Parabéns! Você completou o fluxo de trabalho básico _fork -> clone -> edit -> PR_, onde você encontrará muito como contribuidor.

Celebre a sua contribuição e compartilhe com seus amigos e seguidores no [web app](https://firstcontributions.github.io#social-share).

Caso precise de ajuda ou tenha alguma pergunta, você pode se juntar à nossa equipe Slack. [Junte-se à equipe Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).


### [Material Adicional](../additional-material/git_workflow_scenarios/additional-material.md)

## Tutoriais usando outras ferramentas
[Voltar para página principal](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
