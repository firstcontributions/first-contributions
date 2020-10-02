# Movendo um commit para outra branch
E se apenas depois de ter realizado o commit de uma alteração, vocẽ perceber que fez esse commit na branch errada?
Como você poderia corrigir isso? É sobre isso que este tutorial se trata.

# Moving a commit to a different branch
What if you commit a change, and then realize that you committed to a different branch?
How can you change that? This is what this tutorial covers.

## Movendo os últimos commits para uma branch existente
Para fazer isso, digite:

## Moving the latest commits to an existing branch
To do this, type:

```git reset HEAD~ --soft``` - Desfaz o último commit, mas mantém as alterações disponíveis.
```git stash``` - Grava o estado do diretório.

```git checkout name-of-the-correct-branch``` - Alterna para a outra branch.
```git stash pop``` - Recupera o último estado salvo.
```git add .``` - Ou tente adicionar arquivos individualmente.
```git commit -m "your message here"``` - Faça o commit das alterações.  

Agora suas alterações estão na branch correta

```git reset HEAD~ --soft``` - Undoes the last commit, but leave the changes available.  
```git stash``` - Records the state of the directory.  

```git checkout name-of-the-correct-branch``` - Switches to another branch.
```git stash pop``` - Removes latest stashed state.  
```git add .``` - Or try adding individual files.  
```git commit -m "your message here"``` - Saves and Commits the changes.  

Now your changes are on the correct branch


### Movendo o último commit para uma branch nova
Para fazer isso, digite:
```git branch newbranch``` -  Cria uma nova branch, mantendo todos os commits.
```git reset --hard HEAD~#``` - Retrocede a branch uma quantidade # de commits. Atenção, estes commits serão removidos da branch.
```git checkout newbranch``` - Vá para a nova branch que você criou, ela possuíra todos os commits.

Lembre-se: Qualquer alteração não comitada será PERDIDA.

### Moving the latest commits to a new Branch
To do this, type:  
```git branch newbranch``` -  Creates a new Branch. Saving all the Commits.  
```git reset --hard HEAD~#``` - Move master back by # commits. Remember, these commits will be gone from master  
```git checkout newbranch``` - Goes to the branch you created. It will have all the commits.  

Remember: Any changes not committed will be LOST.
