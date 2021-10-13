# Utilizando stash

E se você estiver trabalhando em um grande código e de repente precisar mudar o branch do qual está trabalhando atualmente para algum outro branch. Como o código não está completo e sem nenhum teste, você provavelmente não deseja commita-lo. Mas você não pode mover para o outro branch sem comprometer as mudanças, o Git não vai deixar você quebrar esse fluxo. O que fazemos então? Como evitamos um commit desnecessário, ao mesmo tempo em que podemos pular branches? Isso é o que este tutorial cobre.

## Salvando seu trabalho em um stash

Vamos supor que você esteja trabalhando em um branch de projeto no qual alterou alguns arquivos. Agora, se você executar o ```git status```, poderá ver as mudanças nos arquivos.

```
$ git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#      modified:   index.html
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#
#      modified:   lib/simplegit.rb
#
```

Agora você quer trocar de branch, mas não quer submeter as mudanças ainda; então você iria deixar as mudanças em um stash.
Para salvar suas alterações para mais tarde, execute: ```git stash```:

```
$ git stash
Saved working directory and index state \
  "WIP on master: 049d078 added the index file"
HEAD is now at 049d078 added the index file
(To restore them type "git stash apply")
```


Agora que seu diretório de trabalho está limpo, use ```git status``` :

```
$ git status
# On branch master
nothing to commit, working directory clean
```


Agora você pode mudar para qualquer branch e fazer seu trabalho; suas alterações escondidas são armazenadas na forma de uma pilha. Para ver quais stashes você armazenou na pilha, você pode usar ```git stash list```:

```
$ git stash list
stash@{0}: WIP on master: 049d078 added the index file
stash@{1}: WIP on master: c264051 Revert "added file_size"
stash@{2}: WIP on master: 21d80a5 added number to log
```

No caso de você querer reaplicar as alterações que acabou de esconder, você pode usar o comando ```git stash apply```. Usando este comando, você pode reaplicar o arquivo escondido mais recente. Para reaplicar qualquer outro arquivo, você pode especificá-lo nomeando-o como: ```git stash apply <stash-name>```, no lugar de ```<stash-name>``` escreva o nome de o estoque que você precisa reaplicar.

```
$ git stash apply
# On branch master
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#
#      modified:   index.html
#      modified:   lib/simplegit.rb
#
```

Você pode ver que git modifica novamente o arquivo que você descomprimiu quando salvou o stash. Nesse caso, você tinha um diretório de trabalho limpo quando tentou aplicar o stash e tentou aplicá-lo no mesmo branch de onde o salvou; mas ter um diretório de trabalho limpo e aplicá-lo no mesmo branch não são necessários para aplicar um stash com sucesso. Você pode salvar um esconderijo em uma ramificação, alternar para outra ramificação posteriormente e reaplicar as alterações na nova ramificação. Você também pode ter arquivos modificados e descomprimidos em seu diretório de trabalho ao aplicar um stash, git fornece conflitos de mesclagem se algo não for mais aplicável de forma limpa.

As alterações feitas em seus arquivos são reaplicadas, mas o arquivo que você testou não foi refeito. Para fazer isso, você precisa executar o comando ```git stash apply``` com um``` --index``` para dizer ao comando para reaplicar as mudanças testadas. Se você tivesse executado isso, você teria retornado à sua posição original:

```
$ git stash apply --index
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#      modified:   index.html
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#
#      modified:   lib/simplegit.rb
#
```

O comando aplicar aplica apenas o trabalho escondido, mas você ainda o tem em sua pilha. Para removê-lo, você pode executar ```git stash drop``` com o nome do stash a ser removido.

```
$ git stash list
stash@{0}: WIP on master: 049d078 added the index file
stash@{1}: WIP on master: c264051 Revert "added file_size"
stash@{2}: WIP on master: 21d80a5 added number to log
$ git stash drop stash@{0}
Dropped stash@{0} (364e91f3f268f0900bc3ee613f9f733e82aaed43)
```

Você pode usar ```git stash pop``` para remover o stash das últimas alterações e removê-lo da pilha do seu stash.

## Removendo stash aplicado

Em alguns casos, você deseja aplicar as alterações do stash, fazer algum trabalho, mas aplicar as alterações que vieram originalmente do stash. Git não fornece comandos como ```git unapply```, mas é possível obter esse efeito simplesmente recuperando o patch associado a um stash e aplicando-o ao contrário:

```$ git stash show -p stash@{0} | git apply -R```

Novamente, se você não especificar um stash, o Git assume o stash mais recente:

```$ git stash show -p | git apply -R```

Você pode querer criar um alias e adicionar efetivamente um comando ```stash-unapply``` ao seu Git. Por exemplo:

```
$ git config --global alias.stash-unapply '!git stash show -p | git apply -R'
$ git stash apply
$ #... work work work
$ git stash-unapply
```

## Criando branch a partir de um stash

Se você esconder algum trabalho, deixe-o lá por um tempo e continue no ramo de onde escondeu o trabalho, você pode ter problemas para reaplicar o trabalho. Se o apply tentar modificar um arquivo que você modificou, você terá um conflito de mesclagem e terá que resolvê-lo. Se você quiser uma maneira mais fácil de testar as alterações escondidas novamente, você pode executar ```git stash branch```, que cria um novo branch para você, verifica o commit em que você estava quando escondeu seu trabalho, reaplica seu trabalho lá e, em seguida, descarta o estoque se for aplicado com sucesso:

```
$ git stash branch testchanges
Switched to a new branch "testchanges"
# On branch testchanges
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#      modified:   index.html
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#
#      modified:   lib/simplegit.rb
#
Dropped refs/stash@{0} (f0dfc4d5dc332d1cee34a634182e168c4efc3359)
```

Este é um bom atalho para recuperar facilmente o trabalho armazenado e trabalhar nele em um novo branch.