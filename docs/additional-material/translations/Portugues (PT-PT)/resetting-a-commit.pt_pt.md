# Repor um commit (resetting a commit)

Para desfazer commits localmente podes usar `git reset`:

- `git reset --soft HEAD~1` — desfaz o último commit mas mantém as alterações staged.
- `git reset --mixed HEAD~1` — desfaz o commit e mantém as alterações no working tree.
- `git reset --hard HEAD~1` — desfaz o commit e descarta as alterações (perigoso).

Usa estas opções com cuidado, especialmente `--hard`.
