# Compreender o .gitignore

O ficheiro `.gitignore` indica ao Git quais ficheiros e pastas devem ser ignorados.

Exemplos comuns a ignorar: `node_modules/`, ficheiros de ambiente `.env`, ficheiros de IDE (`.vscode/`).

Para remover ficheiros já versionados após adicionar ao `.gitignore`:

```
git rm -r --cached .
git add .
git commit -m "Atualizar .gitignore"
```
