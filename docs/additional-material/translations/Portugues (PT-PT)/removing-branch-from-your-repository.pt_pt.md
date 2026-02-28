## Eliminar o branch do teu repositório

Se seguiste o tutorial até aqui, o teu branch `<add-seu-nome>` já cumpriu o seu propósito, e é hora de o eliminar do teu repositório local. Não é obrigatório, mas este nome de branch costuma ser específico para a tua alteração.

Primeiro, vamos garantir que o branch foi mesclado no branch principal (master):

```
git checkout master
```

Mescla `<add-seu-nome>` no master:

```
git merge <add-seu-nome> master
```

Remove `<add-seu-nome>` do repositório local:

```
git branch -d <add-seu-nome>
```

Agora eliminaste o teu branch local `<add-seu-nome>`. Ainda podes ter o branch remoto no teu fork. Antes de o eliminar, lembra‑te que o PR foi enviado a partir desse branch remoto — não o apagues a menos que já tenha sido mesclado.

Se já foi mesclado e queres eliminar o branch remoto, usa:

```
git push origin --delete <add-seu-nome>
```

Agora sabes como gerir e limpar branches.
