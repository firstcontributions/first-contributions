# Rebase vs Merge

`rebase` e `merge` são duas formas de integrar alterações entre branches.

- `merge`: cria um commit de merge que junta dois históricos, preservando a história de ambas as branches.
- `rebase`: aplica os commits de uma branch sobre outra, criando um histórico linear; pode exigir resolução de conflitos.

Escolhe `merge` se quiseres manter um histórico explícito de como as branches interagiram. Escolhe `rebase` para um histórico mais limpo e linear antes de submeter um pull request.
