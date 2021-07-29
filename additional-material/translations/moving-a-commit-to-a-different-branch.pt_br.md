# Movendo um commit para outra branch
E se apenas depois de ter realizado o commit de uma alteração, vocẽ perceber que fez esse commit na branch errada?
Como você poderia corrigir isso? É sobre isso que este tutorial se trata.

## Movendo os últimos commits para uma branch existente
Para fazer isso, digite:


```git reset HEAD~ --soft``` - Desfaz o último commit, mas mantém as alterações disponíveis.
```git stash``` - Grava o estado do diretório.

```git checkout name-of-the-correct-branch``` - Alterna para a outra branch.
```git stash pop``` - Recupera o último estado salvo.
```git add .``` - Ou tente adicionar arquivos individualmente.
```git commit -m "your message here"``` - Faça o commit das alterações.  

Agora suas alterações estão na branch correta

### Movendo o último commit para uma branch nova
Para fazer isso, digite:
```git branch newbranch``` -  Cria uma nova branch, mantendo todos os commits.
```git reset --hard HEAD~#``` - Retrocede a branch uma quantidade # de commits. Atenção, estes commits serão removidos da branch.
```git checkout newbranch``` - Vá para a nova branch que você criou, ela possuíra todos os commits.

Lembre-se: Qualquer alteração não comitada será PERDIDA.
