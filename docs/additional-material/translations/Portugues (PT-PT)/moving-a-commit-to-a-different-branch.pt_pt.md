# Movendo um commit para outra branch
E se, depois de teres efetuado um commit, perceberes que o fizeste na branch errada? Como corrigir isso? Este tutorial explica.

## Mover os últimos commits para uma branch existente
Para isso, executa:

```git reset HEAD~ --soft``` - Anula o último commit, mantendo as alterações.
```git stash``` - Guarda o estado atual do diretório.

```git checkout name-of-the-correct-branch``` - Alterna para a branch correta.
```git stash pop``` - Recupera o estado guardado.
```git add .``` - Ou adiciona ficheiros individualmente.
```git commit -m "your message here"``` - Faz o commit das alterações.

Agora as tuas alterações estão na branch correta.

### Mover o último commit para uma branch nova
Para isso:
```git branch newbranch``` - Cria uma nova branch, mantendo todos os commits.
```git reset --hard HEAD~#``` - Retrocede a branch # commits (atenção: estes commits vão sair da branch atual).
```git checkout newbranch``` - Vai para a nova branch que contém os commits.

Lembra-te: qualquer alteração não comitada será PERDIDA.
