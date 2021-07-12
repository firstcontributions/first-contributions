## Mantendo o seu Fork sincronizado com este repositório

Primeiro, o fluxo para uma sincronização completa precisa ser entendido. Nesse cenário, temos 3 repositórios diferentes: o meu repositório público no Github `github.com/Roshanjossey/first-contributions/`, seu Fork no GitHub `github.com/Seu-Nome/first-contributions/` e o repositório local, no qual você deve trabalhar. Esse tipo de cooperação é típica de projetos de *open source* (código aberto) e é chamado de `Triangle Workflows`.

<img style="float;" src="https://firstcontributions.github.io/assets/additional-material/triangle_workflow.png" alt="triangle workflow" />

Para manter seus dois repositórios atualizados com meu repositório público, o primeiro passo é dar um Fetch (buscar) e então um Merge (mesclar) do repositório público ao seu repositório local.
O segundo passo é fazer um Push do repositório local para o seu Fork no GitHub. Como vimos anteriormente, é somente a partir do seu Fork que você consegue fazer um Pull Request. Por isso, esse Fork é o último repositório a ser atualizado.

Agora, vamos ver como fazer isso:

Primeiro, você precisa estar em seu Branch principal (master). Para saber em qual Branch você está, verifique a primeira linha que aparece como resultado do seguinte comando:
```
git status
```
Se você não está no master, vá para ele:
```
git checkout master
```

Em seguida, você deve adicionar meu repositório público ao seu git com `add upstream url-remoto`:
```
git remote add upstream https://github.com/Roshanjossey/first-contributions
```
Esta é uma forma de dizer ao Git que existe uma outra versão deste projeto na URL especificada e estamos chamando-a de `upstream`. Agora busque a nova versão do meu repositório:
```
git fetch upstream
```

Aqui você está buscando todas as mudanças no meu Fork (o remoto `upstream`). Agora, você precisa mesclá-lo ao repositório público no seu Branch principal.
```
git rebase upstream/master
```
Aqui você está aplicando todas as mudanças que buscou ao seu Branch principal (master). Seu repositório local agora está atualizado. Por último, se você fizer um Push do seu Branch master para o seu Fork, seu GitHub também terá as alterações:
```
git push origin master
```
Note que aqui você está fazendo um Push para o repositório remoto chamado `origin`.

Agora, todos os seus repositórios estão atualizados. Bom trabalho! Você deve seguir esses passos sempre que seu repositório no GitHub avisar que está alguns Commits atrás do meu repositório.
