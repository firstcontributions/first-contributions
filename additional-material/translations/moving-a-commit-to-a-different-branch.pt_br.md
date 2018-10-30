# Movendo um commit para outro branch

E se você fez um commit e depois percebeu que mudou o branch errado? Como corrigir esse erro? Essa questão é respondida por esta instrução.

## Mover os commits mais recentes para um branch existente

Você faz isso com os seguintes comandos:

``` git reset HEAD~ --soft ``` - Desfaz o último commit, as alterações permanecem disponíveis. 
``` git stash ``` - Registre o status do diretório e salve-o em stash.

``` git checkout nome-do-branch-correto ``` - Muda para outro branch.
``` git stash pop ``` - Retorna o último estado salvo. 
``` git add . ``` - Adicione arquivos individuais. 
``` git commit -m "sua mensagem aqui" ``` - Salve e faça alterações de confirmação.

Agora, suas alterações estão no ramo certo.

### Mova os commits mais recentes para o novo branch

Você pode fazer isso com os seguintes comandos:
``` git branch novobranch ``` - Cria um novo branch, salvando todos os commits.
``` git reset --hard HEAD~[n] ``` - Retorna o ramo mestre de volta para n commits. Tenha em mente que as alterações contidas nesses commits serão completamente removidas do branch master.
``` git checkout newbranch ``` - Muda para o ramo que você criou. Este ramo agora contém todos os commits.

Lembre-se: Quaisquer alterações que não foram incluídas no commit serão completamente PERDIDAS.
