# Desfazer um commit

Para reverter alterações locais recentes podes usar:

- `git revert <commit>` — cria um novo commit que inverte o commit especificado.
- `git reset --soft HEAD~1` — remove o último commit mantendo as alterações staged.

Escolhe a abordagem adequada conforme se trata de alterações publicadas ou apenas locais.
