[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Primeiras Contribuições

| <img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/9/9c/IntelliJ_IDEA_Icon.svg" width="40"> | IntelliJ IDEA |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |


É difícil, sempre é difícil quando fazemos alguma coisa pela primeira vez. Especialmente quando você está colaborando, cometendo erros, não é nada confortável. No entanto, o open source é totalmente sobre colaboração & trabalho em equipe. Por isso, nós queremos simplificar a maneira como os novos colaboradores de código aberto aprendem & contribuem pela primeira vez.

Ler artigos & assistir a tutoriais até podem ajudar, mas o que é melhor do que fazer as coisas sem bagunçar nada. Este projeto tem como objetivo orientar & simplificar a forma como os iniciantes fazem a sua primeira contribuição. Lembre-se que você aprende melhor quando está relaxado. Se você deseja fazer sua primeira contribuição, basta seguir os passos abaixo. Nós prometemos a você que será divertido!

Se você ainda não tem o IntelliJ IDEA no seu computador, [instale-o](https://www.jetbrains.com/idea/download/#section=windows)
 
**Observação:** Este tutorial foi feito usando o IntelliJ IDEA (versão 2019.3.2) em um computador rodando Windows 10. Posteriormente neste tutorial, faremos uso de algumas teclas de atalho, que podem ser diferentes em outros sistemas operacionais (macOS / Linux).


## Faça o Fork deste repositório 

<img align="right" width="300" src="https://camo.githubusercontent.com/fcf9a4ed664cc63de2fcb14d1135072ba6d4c74a8e9bdb224ad6ab1e72600c3b/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f666f726b2e706e67" alt="fork this repository" />

Faça um *fork* deste repositório clicando no botão *fork* (bifurcar) no canto superior direito desta página. Isso criará uma cópia deste repositório em sua conta do GitHub.
 
O GitHub rastreia a relação entre seu repositório e o original, o qual você fez o *fork*. Você pode pensar em seu repositório como uma cópia de trabalho.

Muitos dos repositórios matrizes do GitHub (ou seja, aqueles que não são *Fork* de nenhum outro repositório) tem um pequeno grupo de pessoas que podem fazer commits de modificações diretamente. Todos os outros contribuidores devem fazer um *for* do repositório e fazer alterações no *fork*, em seguida, devem criar um Pull Request para solicitar um *Merge* (mesclagem) das modificações feitas no repositório original.


## Clone seu Repositório 

<img align="right" width="300" src="https://camo.githubusercontent.com/4c3f7f1bec4f04db40ecf58dc2e19c2d8992f100f3bbbc4767a9d20b29f4a43d/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f636c6f6e652e706e67" alt="clone this repository" />

O próximo passo será clonar seu repositório em sua máquina para que você possa modificá-lo. Visual Studio precisa da URL do seu repositório, portanto clique no botão "clone" e então clique no ícone "copy to clipboard".
 
**CUIDADO**: Um erro que os novatos costumam cometer é clonar o repo do qual você fez o fork, em vez de clonar seu repo. Verifique a barra de endereços do seu navegador e certifique-se de que você está clonando o seu repositório.
 
Agora abra o IntelliJ IDEA.
 
O IntelliJ IDEA permite que você faça um check out (em termos do Git clone) de um repositório existente e crie um novo projeto com base nos dados que você baixou.
 
No menu principal, escolha VCS | Get from Version Control ou, se nenhum projeto estiver aberto no momento, clique em Get from Version Control na tela inicial.
 
Na caixa de diálogo Get from Version Control dialog, especifique a URL do repositório remoto que deseja clonar (você pode clicar em Test para certificar-se de que a conexão com o repositório remoto pode ser estabelecida) ou selecione um dos serviços de hospedagem VCS à esquerda. Se você já estiver conectado ao serviço de hospedagem selecionado, a completion irá sugerir a lista de repositórios disponíveis que você pode clonar.
 
Clique em Clone. Se quiser criar um projeto IntelliJ IDEA com base nas fontes que você clonou, clique em Sim na caixa de diálogo de confirmação. O mapeamento de raiz do Git será automaticamente definido para o diretório raiz do projeto.
 
Se o seu projeto tiver submodelos, eles também serão clonados e automaticamente registrados como raízes do projeto.
 
**Importante**: certifique-se de que é o repositório é o fork e não o original, caso contrário, o procedimento não funcionará.


## Crie um branch 

No Git, o processo de branching (ramificação) é um mecanismo poderoso que permite divergir da linha principal de desenvolvimento, por exemplo, quando você precisa trabalhar em um recurso ou congelar um determinado estado de uma base de código para um release e assim por diante.
 
No IntelliJ IDEA, todas as operações com branches são realizadas no pop-up Git Branches. Para ativá-lo, clique no widget Git na barra de status ou pressione Ctrl + Shift + `.
 
O nome do branch atual é exibido no widget do Git na barra de status.
 
No pop-up branch, escolha Novo branch.
 
Na caixa de diálogo que é aberta, especifique o nome do branch e certifique-se de que a opção Checkout branch esteja selecionada se você quiser alternar para esse branch.
 
A nova ramificação começará a partir do HEAD atual. Se você deseja iniciar um branch de um commit anterior ao invés do branch atual HEAD, selecione este commit na aba Log da janela da ferramenta de Controle de Versão Alt + 9 e escolha New Branch no menu de contexto.


## Faça as alterações necessárias
Abra ``Contributors.md`` e adicione seu nome em qualquer lugar do arquivo. Este arquivo contém GFM (GitHub Flavored Markdown), que é um tipo proprietário da sintaxe de [markdown](https://pt.wikipedia.org/wiki/Markdown).
 
Copie uma das linhas de outros contribuidores e modifique-a com seu nome para ter certeza que você obteve a sintaxe correta.


## Commit & Push modificações para o GitHub

Selecione os arquivos que deseja commitar ou uma lista de alterações inteira na guia Local Changes da janela da ferramenta de controle de versão Alt + 9 e pressione Ctrl + K ou clique no botão Commit na barra de ferramentas.
 
A caixa de diálogo Commit Changes abrira e listara todos os arquivos que foram modificados desde o último commit, bem como todos os arquivos não versionados recém-adicionados.
 
Insira uma mensagem de commit que faça sentido.
 
Você pode clicar em Commit Message history (Confirmar histórico de mensagens) Ctrl + M para escolher na lista de mensagens de commits recentes.
 
Você também pode editar a mensagem de commit mais tarde, antes de enviar o commit.
 
Pressione Ctrl + Shift + K ou escolha VCS | Git | Push from the main menu. A caixa de diálogo Push Commits é aberta, mostrando todos os repositórios Git (para projetos de vários repositórios) e listando todos os commits feitos no branch atual em cada repositório desde o último push.


## Envie suas alterações para revisão

Neste ponto, você concluiu a alteração, mas ela ainda está apenas no seu repo. Esta etapa mostrará como enviar uma solicitação ao administrador do repo matriz para mesclar sua alteração.
 
Em seu repo no GitHub, você verá o botão `Compare & pull request` ao lado da notificação do novo branch, clique nesse botão.


<img src="https://camo.githubusercontent.com/ca3b1cefece5f3b9b3435020e6a357ca024cda5bd2b1e140a15170fcd1ec5381/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f636f6d706172652d616e642d70756c6c2e706e67" alt="create a pull request" />

Agora submeta o pull request. 

<img src="https://camo.githubusercontent.com/71401ba5551a64aeac3838825a52ce7a7597cd8b54a0d7200d9454e2cbfbb13f/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f7375626d69742d70756c6c2d726571756573742e706e67" alt="submit pull request" />

Em breve estarei mesclando todas as suas alterações no branch master deste projeto. Você receberá um e-mail de notificação assim que as alterações forem integradas.

## Para onde ir agora?

Parabéns! Você acabou de completar o padrão _fork -> clone -> edit -> PR_ workflow que você encontrará frequentemente como um contribuidor!
 
Comemore sua contribuição e compartilhe-a com seus amigos e seguidores acessando o [web app](https://firstcontributions.github.io/#social-share).
 
Você pode se juntar a nossa equipe slack caso precise de alguma ajuda ou tenha alguma dúvida. [Junte-se ao time slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).
 
Agora vamos começar a contribuir para outros projetos, compilamos uma lista de projetos com questões fáceis para você começar. [Confira a lista de projetos no web app](https://firstcontributions.github.io/#project-list).
 



### [Material Adicional](../../additional-material/translations/Portugues/additional-material.pt_br.md).

## Tutoriais usando outras ferramentas
[Voltar a página principal](https://github.com/firstcontributions/first-contributions/blob/master/translations/README.pt_br.md)

## Autopromoção
 
Se você gostou deste projeto, de star no GitHub. Se você gostou dessa tradução me siga no GitHub [Vitor Matias](https://github.com/VitorCMatias).
