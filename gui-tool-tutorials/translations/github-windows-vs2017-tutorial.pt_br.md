[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
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

O próximo passo será clonar seu repositório em sua máquina para que você possa modificá-lo. Visual Studio precisa da URL do seu repositório, portanto clique no botão "clone" e então clique no ícone "copy to clipboard".

**CUIDADO:** Um erro que os novatos cometem com frequência é clonar o repositório do qual você fez o fork, ao invés de clonar seu repositório. Verifique a barra de endereços do seu navegador e certifique-se de que você está clonando o seu repositório.

Agora é a hora de ir para o Visual Studio 2017! Você estará trabalhando na aba *Team Explorer* na maior parte do tutorial. Se ela não estiver aberta por padrão, clique em `View > Team Explorer` para abrí-la.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-01-clone1.png" alt="Team Explorer" />

*Team Explorer* tem muitas áreas e muitos botões de navegação, localizados no topo para te ajudar a achar essas diferentes áreas. Para clonar o repositório, você vai precisar estar na *Connect view*, que deve ser a padrão. Se você não conseguir ver o botão *clone*, clique no botão verde, em formato de tomada, no topo.

Click the `Clone` option under **Local Git Repositories** and paste the URL to your repo in the text box.  This should be the URL you copied to your clipboard from GitHub previously.

Clique na opção `Clone` abaixo de **Local Git Repositories** e cole a URL do seu repositório na caixa de texto. Essa URL tem que ser a mesma que você copiou no GitHub anteriormente.

Clique no botão `Clone` para iniciar o processo.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-02-clone2.png" alt="Clone repo" />

Quando o processo estiver completo, você será movido para a aba *Solution Explorer*, onde você poderá ver o conteúdo do repositório clonado. O seu parecerá um pouco diferente da foto abaixo, por que os arquivos estão em constante mudança!

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-03-clone3.png" alt="Solution Explorer" />

## Crie uma *branch*

Clique de volta na aba *Team Explorer* e use o a seleção principal de navegação para mostrar as *Branchs* disponíveis.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-04-branch1.png" alt="Branches view" />

Você deve ver o repositório **first-contributions** e a branch padrão, que é chamada `main`. Clique com o botão direito na `main` e escolha `New Local Branch From...`.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-05-branch2.png" alt="New branch" />

Dê à sua branch um nome como `add-<seu_nome_aqui>` por exemplo: `add-alonzo-church`.

Deixe a caixa de seleção `Checkout branch` marcada e clique no botão `Create Branch`.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-06-branch3.png" alt="Create branch" />

Você deverá ver a sua branch nova na lista.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-07-branch4.png" alt="See new branch" />

## Faça as mudanças necessárias

Abra o arquivo `Contributors.md` e adicione o seu nome no fim da lista. Esse arquivo contém GFM (GitHub Flavored Markdown), que é uma função nativa da sintaxe do <a href="https://en.wikipedia.org/wiki/Markdown">markdown</a>.

Copie uma das outras linhas dos contribuidores e modifique-a com o seu nome. Tenha certeza que a sintaxe está correta - ela pode ser exigente.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-08-change1.png" alt="Add your name" />

## Commit & Push changes to GitHub

Volte para a aba *Team Explorer* e navegue para a aba *Changes*.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-09-commit1.png" alt="Changes" />

Coloque a informação que você queira, poste o seu *commit* e clique em `Save`. O Visual Studio relembrará isso para futuros *commits*.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-10-commit2.png" alt="Git user information" />

**NOTA:** Visual Studio usa uma pasta escondida, chamada `.vs` para salvar suas configurações e preferências pessoais. O conteúdo desta pasta **não deverá ser salvo no Git**.
Se ela não estiver sido ingnorada ainda, você deve informar ao Git para ignorar essa pasta, com o intuito dela não ser mandada para o repositório.

Essa pasta já foi ignorada neste repositório, então você não tem que realizar este passo. Ele está aqui somente para você ter uma referência para projetos futuros.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-11-commit3.png" alt="Ignore vs folder" />

Agora você deve ver uma lista de arquivos modificados e uma caixa de texto para digitar um cometário do *commit*. Os comentários devem ser breves, mas concretos. Não tem nada pior do que ler um comentário de um *commit* e ver algo como: `"Eu atualizei algumas coisas"`. Tire alguns segundos para realizar o seu *commit*. O seu time vai agradecer bastante mais tarde e você pode até agradecer a você mesmo!

Clique em `Commit All and Push` para realizar um *commit* local e fazer um *push* das suas mudanças para o seu repositório, tudo em um único passo.

**NOTA:** Um *Commit* pode ser realizado separadamente de um *Push*. Fazemos os dois juntos por conveniência. As mudanças realizadas e salvas em *commits* locais não serão refletidos no teu repositório no GitHub até que você faça um *Push*.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-12-commit4.png" alt="Commit and Push" />

A primeira vez que você realizar um *Push* para o GitHub, Visual Studio solicitará as suas credenciais do GitHub. Depois disso, ele as guardará no *cache*, para que você não precise realizar isso frequentemente.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-13-commit5.png" alt="Login" />

Depois de realizar uma operação de *Push*, abra o seu repositório no GitHub e deverá ver uma mensagem indicando um *push* recente de uma *branch*.

Você pode ver suas mudanças abrindo a seleção `Branch: main` e selecionando a sua `branch`. Parabéns! Você pode compartilhar a URL da `branch` com o mundo e mostrar o seu progresso!

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-14-commit6.png" alt="View pushed branch on GitHub" />

## Submeta as suas mudanças para uma revisão

Neste ponto, você completou as mudanças, mas elas ainda estão somente no seu repositório. Esse passo te mostrará como submeter essas mudanças para um administrador para que ele possa fazer um *merge* das tuas mudanças.

No seu repositório no GitHub, você verá o botão `Compare & pull request` próximo à notificação da *branch*. Cloque nesse botão.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/compare-and-pull.png" alt="create a pull request" />

Agora submeta o *Pull Request*.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/submit-pull-request.png" alt="submit pull request" />

Assim que possível, essas mudanças serão *mergeadas* para a `main branch` deste projeto. Você será notificado via email, quando essa movimentação for realizada.

## Para onde ir daqui?

Parabéns! Você acabou de completar o fluxo de trabalho *fork -> clone -> edit -> PR* que vocẽ vai realizar frequentemente como um contribuidor!

Celebre a sua contribuição e compartilhe-a com os seus amigos e seguidores indo para o [web app](https://firstcontributions.github.io#social-share).

You can join our slack team in case you need any help or have any questions. [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Você pode se juntar à nossa comunidade no slack, caso precise de alguma ajuda ou tenha alguma dúvida.

[Faça parte da nossa comunidade no Slack!](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)


### [Material adicional](../additional-material/git_workflow_scenarios/additional-material.md)

## Tutoriais utilizando outras ferramentas
[Retorne para a página principal](https://github.com/firstcontributions/first-contributions/blob/master/translations/README.pt_br.md)
