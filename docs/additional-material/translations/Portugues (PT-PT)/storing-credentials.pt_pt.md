# Armazenar credenciais

Para evitar inserir as credenciais repetidamente, podes armazená‑las localmente:

- No Linux/macOS: `git config --global credential.helper cache` ou `store`.
- No Windows: usa o `Git Credential Manager` que integra com o Windows Credential Store.

Avalia os riscos de segurança ao escolher armazenar credenciais em texto claro (`store`).
