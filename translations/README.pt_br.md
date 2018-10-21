[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png" alt="Junte-se à nós no Slack">](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Primeiras Contribuições

É difícil. É sempre difícil fazer algo pela primeira vez. Especialmente quando se está colaborando, cometer erros não é algo agradável. Mas *open source* (código aberto) se trata de colaboração e de trabalharmos juntos. Queremos simplificar a forma com que novos colaboradores *open source* aprendem e contribuem pela primeira vez.

Ler artigos e ver tutoriais pode ajudar, mas o que é melhor do que realmente pôr a mão na massa em um ambiente prático? Este projeto visa guiar e simplificar a forma com que os novatos fazem a sua primeira contribuição. Se quiser fazer a sua primeira contribuição, siga os passos abaixo.

#### *Se você não se sente confortável com linha de comando, [aqui estão alguns tutoriais de ferramentas gráficas.]( #tutoriais-com-outras-ferramentas)*


#### *Ler em [outros idiomas](../translations/Translations.md)* 

[🇮🇳](translations/README.hi.md)
[🇲🇲](translations/README.mm_unicode.md)
[🇮🇩](translations/README.id.md)
[🇫🇷](translations/README.fr.md)
[🇪🇸](translations/README.es.md)
[<img src="assets/catalan1.png" width="22">](translations/README.ca.md)
[🇳🇱](translations/README.nl.md)
[🇱🇹](translations/README.lt.md)
[🇷🇺](translations/README.ru.md)
[:slovakia:](translations/README.slk.md)
[🇯🇵](translations/README.ja.md)
[🇻🇳](translations/README.vn.md)
[🇵🇱](translations/README.pl.md)
[🇮🇷](translations/README.fa.md)
[🇮🇷](translations/README.fa.en.md)
[🇰🇷 🇰🇵](translations/README.ko.md)
[🇩🇪](translations/README.de.md)
[🇩🇰](translations/README.da.md)
[🇨🇳](translations/README.chs.md)
[🇹🇼](translations/README.cht.md)
[🇬🇷](translations/README.gr.md)
[🇪🇬](translations/README.eg.md)
[🇸🇦](translations/README.ar.md)
[🇺🇦](translations/README.ua.md)
[🇧🇷](translations/README.pt_br.md)
[🇵🇹](translations/README.pt-pt.md)
[🇮🇹](translations/README.it.md)
[🇹🇭](translations/README.th.md)
[🏴](translations/README.gl.md)
[🇵🇰](translations/README.ur.md)
[:bangladesh:](translations/README.bn.md)
[🇲🇩 🇷🇴](translations/README.ro.md)
[🇹🇷](translations/README.tr.md)
[🇸🇪](translations/README.se.md)
[:slovenia:](translations/README.sl.md)
[🇮🇱](translations/README.hb.md)
[🇨🇿](translations/README.cs.md)
[<img src="assets/pirate.png" width="22">](translations/README.en-pirate.md)
[🇲🇽](translations/README.mx.md)



<img align="right" width="300" src="../assets/fork.png" alt="fork deste repositório" />

Se não possui o git em sua máquina, [instale-o aqui]( https://help.github.com/articles/set-up-git/ ).

## Faça um Fork deste repositório

Faça um Fork clicando no botão "Fork" no topo desta página. Isto irá criar uma cópia deste repositório na sua conta.

## Clone o repositório

<img align="right" width="300" src="../assets/clone.png" alt="clonar este repositório" />

Agora clone este repositório para a sua máquina. Clique no botão "Clone or download" e, em seguida, clique no ícone "Copy to clipboard" para copiar a URL.

Abra seu terminal e execute o seguinte comando do git:
```
git clone "url que copiou"
```
onde "url que copiou" (sem as aspas) é a URL deste repositório. Consulte as etapas anteriores para obter a URL.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copiar URL" />

Por exemplo:
```
git clone https://github.com/seu-usuario/first-contributions.git
```
onde "seu-usuário" é o seu usuário do GitHub. Aqui você está copiando o conteúdo do repositório first-contributions para o seu computador.

## Crie um Branch

Vá para o diretório do repositório no seu computador (caso você não esteja lá):
```
cd first-contributions
```

Agora crie um Branch usando o comando `git checkout`:
```
git checkout -b <add-seu-nome>
```

Por exemplo:
```
git checkout -b add-alonzo-church
```
Obs.: O nome do Branch não precisa ter a sigla "add", mas nesse caso é recomendável, porque a finalidade deste Branch é a de adicionar o seu nome a uma lista.

## Efetue as alterações necessárias e faça um Commit

Agora abra o arquivo `Contributors.md` em seu editor de código, adicione o seu nome a ele e salve o arquivo. 

<img align="right" width="450" src="../assets/git-status.png" alt="git status" />

Se você for para o diretório do projeto e executar o comando `git status`, verá que há alterações. Adicione essas alterações ao Branch que você acabou de criar utilizando o comando `git add`:
```
git add Contributors.md
```
Agora faça um Commit dessas alterações utilizando o comando `git commit`:
```
git commit -m "Add <seu-nome> to Contributors list"
```
preenchendo `<seu-nome>` com o seu nome.

## Faça um Push das alterações para o GitHub

Faça um Push utilizando o comando `git push`:
```
git push origin <add-seu-nome>
```
substituindo `<add-seu-nome>` pelo nome do Branch que você criou anteriormente.

## Envie suas alterações para serem revisadas

Se você for para o seu repositório no GitHub, verá um botão `Compare & pull request`. Clique nesse botão.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="Crie um Pull Request" />

Agora envie um Pull Request.

<img style="float: right;" src="../assets/submit-pull-request.png" alt="Envie o Pull Request" />

Logo estarei mesclando ('mergeando') as suas mudanças no Branch principal (master) deste projeto. Você receberá um e-mail de notificação quando as alterações forem mescladas.

## Para onde ir a partir daqui?

Parabéns! Você completou o fluxo de trabalho básico _fork -> clone -> edit -> PR_ que você encontrará frequentemente como contribuidor!

Celebre sua contribuição e compartilhe com seus amigos e seguidores no [app web](https://roshanjossey.github.io/first-contributions/#social-share).

Você também pode se juntar à nossa equipe no Slack caso precise de alguma ajuda ou tenha alguma dúvida. [Junte-se à nossa equipe no Slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Agora você pode colaborar com outros projetos. Nós compilamos uma lista de projetos com problemas simples que você pode começar. Verifique [a lista de projetos no web app](https://roshanjossey.github.io/first-contributions/#project-list).

### [ Material adicional ](../additional-material/translations/additional-material.pt_br.md)


## Tutoriais usando outras ferramentas

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="../assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

## Autopromoção

Se você gostou deste projeto, favorite-o com um estrela no [GitHub](https://github.com/Roshanjossey/first-contributions).
Se estiver se sentindo especialmente caridoso, siga [Roshan](https://roshanjossey.github.io/) no
[Twitter](https://twitter.com/sudo__bangbang) e
[GitHub](https://github.com/roshanjossey).

<a href="http://saasgrids.com"> <img alt="http://saasgrids.com" src="../assets/saasgrids-banner.png" width="500"></a>
