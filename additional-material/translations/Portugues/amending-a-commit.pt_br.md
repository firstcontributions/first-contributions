# Corrigindo um Commit

E se você fizer o commit de uma alteração para o seu repositório remoto, e posteriormente acabar percebendo que ele possui um erro na mensagem do commit, ou você se esqueceu de adicionar uma linha de código no seu commit mais recente?
Como você editaria isso? É isso que esse tutorial cobre.

## Alterando uma mensagem de commit recente após ter dado push para o Github

Para fazer isto sem abrir um arquivo:
*   Digite o comando ```git commit --amend -m "seguido da sua nova mensagem de commit"```
*   Execute ```git push origin <nome-da-branch>``` para fazer o commit das mudanças para o repositório.

Nota: Se você digitar apenas ```git commit --amend```, seu editor de texto abrirá te pedindo para editar a mensagem de commit.
Adicionar a flag ``-m`` previne isso.

## Fazendo modificações em um único commit

E se nós nos esquecermos de fazer uma pequena mudança em um arquivo, como adicionar uma única palavra, mas nós já demos push no commit para o nosso repositório remoto?

Para ilustrar, aqui está um log dos meus commits:
```
g56123f arquivo bot criado
a2235d atualizado contributor.md
a5da0d arquivo bot modificado
```

Supomos que eu esqueci de adicionar uma palavra no arquivo bot.

Há 2 modos de resolver esse problema. O primeiro é fazer um novo commit que contém a mudança, dessa forma:

```
g56123f arquivo bot criado
a2235d atualizado contributor.md
a5da0d arquivo bot modificado
b0ca8f adicionada palavra no arquivo bot
```

O segundo modo é corrigir o commit a5da0d, adicionar essa nova palavra e dar push para o Github como um único commit.
Essa ação soa melhor, já que é apenas uma pequena alteração.

Para fazer isso, nós faríamos o seguinte:
* Modificar o arquivo. Nesse caso, modificarei o arquivo bot para incluir a palavra que eu esqueci anteriormente.
* Em seguida, adicionar o arquivo para a área de preparação (*staging area*) com o comando ```git add <nome-do-arquivo>```

Normalmente, após adicionar arquivos na área de preparação, a próxima coisa que nós fazemos é entrar com o comando ```git commit -m "nossa mensagem de commit"```, certo?
Mas, como o que nós queremos fazer aqui é corrigir o commit anterior, nós ao invés disso iremos rodar:

* ```git commit --amend```
 Isso irá inicializar o editor de texto para que possamos editar a mensagem. Você decide se irá deixar a mensagem como ela estava antes, ou editá-la.
* Sair do editor salvando as alterações
* Dar push nas suas alterações com o comando ```git push origin <nome-da-branch>```

Dessa forma, ambas as alterações agora estarão em um único commit.
