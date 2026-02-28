# Repor um branch (resetting a branch)

Se precisares de retroceder o histórico de um branch para um estado anterior, podes usar `git reset`.

- `git reset --hard <commit>`: move o ponteiro do branch para `<commit>` e descarta alterações não confirmadas (irá perder trabalho não guardado).
- `git reset --soft <commit>`: move o ponteiro do branch mas mantém as alterações do índice e do working tree para que possas recommitar.

Usa estas operações com cuidado, especialmente com `--hard`, pois elas alteram o histórico local.
