# Gitflow

Gitflow é um modelo de branching que define roles e regras para gerir lançamentos e desenvolvimento.

Principais conceitos:
- `master`: código de produção.
- `develop`: integração de funcionalidades.
- `feature/*`: desenvolvimento de novas funcionalidades a partir de `develop`.
- `release/*`: preparar uma nova versão a partir de `develop`.
- `hotfix/*`: correções urgentes a partir de `master`.

Gitflow é útil para projetos com ciclos de lançamento planeados, mas pode tornar o histórico mais complexo.
