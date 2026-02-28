# Corrigir um Commit

E se tiveres feito um commit no repositório remoto e depois reparares que a mensagem do commit está errada, ou esqueceste de adicionar uma linha? Como corrigir isso? Este tutorial explica.

## Alterar uma mensagem de commit recente após teres dado push para o GitHub

Para o fazer sem abrir um editor:

- Usa `git commit --amend -m "nova mensagem de commit"`
- Em seguida `git push origin <nome-da-branch>` para enviar o commit alterado para o repositório remoto.

Nota: Se executares apenas `git commit --amend`, o teu editor abrirá para editares a mensagem. A flag `-m` evita isso.

## Fazer modificações num único commit

Se esqueceste de adicionar uma pequena alteração e já deste push, podes fazer um novo commit com a alteração ou emendar o commit antigo para incorporar a alteração num único commit.

Exemplo de solução com `--amend` e push.
