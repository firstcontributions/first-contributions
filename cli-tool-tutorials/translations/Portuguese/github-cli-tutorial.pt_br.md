[![Amor pelo Código Aberto](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![Licença: MIT](https://img.shields.io/badge/Licença-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Contribuidores de Código Aberto](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Primeiras Contribuições

| <img alt="GitHub Desktop" src="https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png" width="200"> | GitHub Command Line Interface (CLI) |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|

Este é um guia para nós, os entusiastas do terminal, que querem fazer tudo no terminal e, graças ao [Github-CLI](https://cli.github.com/), podemos fazer isso. Lembre-se de que sua primeira contribuição deve ser divertida, gratificante e motivadora para continuar!

Este guia é um pouco mais desafiador, pois não estamos usando nenhuma interface gráfica, mas ainda é muito divertido e você definitivamente pode segui-lo!

O primeiro requisito é ter:
- Git instalado (como instalar o [git](https://git-scm.com/downloads))
- Conta no Github

Agora precisamos instalar a ferramenta `github-cli` em nosso sistema, seguindo a [documentação oficial](https://github.com/cli/cli#installation).

Depois disso, precisamos fazer login na CLI, então digite este comando:
```bash 
gh auth login
```

Siga as instruções e estaremos prontos!

# Fork deste repositório
É tão fácil quanto executar este comando:

```bash
gh repo fork firstcontributions/first-contributions
```
**Importante: Ele perguntará se você deseja cloná-lo também, selecione a opção "yes" (sim)**

# Crie sua branch
Vamos fazer esta etapa com o git, então digite este comando, substituindo o nome pelo seu nome, por exemplo:
```bash 
git switch -c add-john-doe
```

# Faça as alterações necessárias e faça o commit dessas alterações
Agora você pode abrir o arquivo `Contributors.md` em um editor de texto e adicionar seu nome a ele. Coloque seu nome em qualquer lugar entre o início e o final e salve o arquivo.

No diretório do projeto, execute `git status` e você verá as alterações.
![image-git](https://camo.githubusercontent.com/a35c4722d7aab337eefc655d1488f7b4dc038508