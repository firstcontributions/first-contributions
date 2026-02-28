# Reverter um commit

Se precisares de desfazer um commit que já foi publicado, usa `git revert` para criar um novo commit que inverte as alterações.

```
git revert <commit-hash>
```

Isto preserva o histórico enquanto desfaz o efeito do commit especificado.
