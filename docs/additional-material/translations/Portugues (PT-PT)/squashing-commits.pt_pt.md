# Juntar commits (squash)

`Squash` significa combinar vários commits em um só, normalmente durante um rebase interativo.

Exemplo com rebase interativo:

```
git rebase -i HEAD~3
# marca os commits a juntar como "squash" ou "fixup"
```

Isto é útil para limpar o histórico e apresentar uma única alteração coesa num pull request.
