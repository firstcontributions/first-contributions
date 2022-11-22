## Removendo o Branch do seu repositório

Se você seguiu o tutorial até agora, seu Branch `<add-seu-nome>` concluiu seu objetivo, e é hora de deletá-lo do seu repositório local. Isso não é necessário, mas o próprio nome desse Branch mostra como seu objetivo é específico. Sua vida pode ser tornada curta por causa dessa especificidade.

Primeiro, vamos mesclar o Branch `<add-seu-nome>` ao seu Branch principal (master), então vamos para ela:
```
git checkout master
```

Mescle `<add-seu-nome>` ao master:
```
git merge <add-seu-nome> master
```

Remova `<add-seu-nome>` do seu repositório local:
```
git branch -d <add-seu-nome>
```

Agora você deletou seu Branch local `<add-seu-nome>` e tudo está limpo e arrumado.
Nesse ponto, você ainda deve ter o Branch `<add-seu-nome>` no seu Fork. Antes de deletá-lo, lembre-se que você mandou um Pull Request para o meu repositório a partir desse Branch remoto. Então, a não ser que eu já tenha mesclado o Branch, não o delete.

Porém, se eu já tiver mesclado seu Branch e você quer deletar o Branch remoto, use:
```
git push origin --delete <add-seu-nome>
```

Agora, você sabe como arrumar seus Branches.
Com o tempo, muitos Commits serão adicionados ao meu repositório público. E os Branches principais (master) da sua máquina local e do seu Fork não estarão mais atualizados. Então, para manter seus repositórios sincronizados com o meu, siga os passos abaixo.

#### [Mantendo o seu Fork sincronizado com este repositório](keeping-your-fork-synced-with-this-repository.pt_br.md)
