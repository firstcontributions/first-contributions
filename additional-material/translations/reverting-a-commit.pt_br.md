## Reverter Commit

Para reverter um commit, crie um novo commit que irá desfazer todas as mudanças feitas no commit anterior. É como executar ``` CTRL + Z ``` no git .

Reverter uma mudança no Git é relativamente fácil, porque todo commit que enviamos para o repositório remoto é associado à sua única chave alfanumérica SHA (Secure Hash Algorithm). Isso significa que podemos reverter cada commit se tivermos apenas o seu SHA. Em qualquer caso, precisamos ter cuidado ao recuperar, porque podemos danificar o repositório.

Para selecionar o SHA para um commit específico que você deseja desfazer, um log de todos os commits que você criou até agora será útil. Para fazer isso, execute o seguinte comando: ``` git log --oneline ```. O comando ``` git log ``` também retornaria SHA, mas em um formato maior. Usando o sinalizador ``` --oneline ``` o Git informa que queremos uma impressão transparente em uma linha.

Os sete primeiros caracteres que aparecem quando você executa esse comando são chamados de hashes de confirmação abreviados.

Por exemplo, esta é a saída do ``` git log --oneline ``` para este repositório:

```
389004d added spacing in title
c1b9fc1 Merge branch 'master' into tutorials
77eaafd added tutorial for reverting a commit
```

Isso nos mostra que com o ``` git log --oneline ```, podemos obter uma lista de todos os commits feitos no repositório com os 7 primeiros caracteres do seu SHA.


Bem, agora podemos tentar excluir o "added spacing in title" com os seguintes passos:

- Copie o SHA do commit, neste caso ``` 389004d ```.
- Em seguida, use o comando ``` git revert 389004d ```.

Isso abre um editor de texto e solicita que você edite a mensagem de confirmação. Você pode optar por deixar a mensagem padrão, que começa com a palavra Reverter, ou pode alterar o comentário de acordo com suas preferências.

- Em seguida, salve e feche o editor de texto.
- Volte para a linha de comando.
- Use o comando ``` git push origin <nome-do-branch> ``` para enviar alterações para o GitHub.

As alterações serão então desfeitas. Nesse caso, o repositório retornaria ao status do commit ``` c1b9fc1 ```.