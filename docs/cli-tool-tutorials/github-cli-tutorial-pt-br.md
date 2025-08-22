[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Primeiras Contribuições

| <img alt="GitHub Desktop" src="https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png" width="200"> | GitHub Interface de Linha de Comandos (CLI) |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|

Esse guia é para nós, os nerdes de terminal, que querem fazer tudo no terminal, e graças a [Github-CLI](https://cli.github.com/), podemos alcançar isso, lembrando que sua primeira contribuição deve ser divertida, recompensadora, e uma motivação para seguir em frente!

Esse guia é um pouco mais desafiador desde que já não estamos utilizando nenhum interface gráfico, mas é ainda bem divertido e você com certeza consegui acompanhar!

O primeiro requisito é para ter:
- Git instalado (como instalar git [git](https://git-scm.com/downloads))
- Ter uma conta no GitHub

Agora precisamos instalar a ferramenta `github-cli` no nosso sistema seguindo o [documentação oficial](https://docs.github.com/pt/github-cli/github-cli/quickstart)

Depois disso, precisamos fazer login no CLI, só executar esse comando:
```bash 
gh auth login
```

Segue as instruções e estamos prontos!

# Fork esse repositório
É tão fácil quanto executar este comando:

```bash
gh repo fork firstcontributions/first-contributions
```
**Importante: Ele vai incitar para você se gostaria de clonar também, selecione a opção "yes"**

# Cria o seu branch 
Vamos fazer esse próximo passo com o git, so insira esse comando substituindo o nome pelo seu nome, por exemplo: 
```bash 
git switch -c add-john-doe
```

# Faça as mudanças necessários e commit as mudanças 
Agora você pode abrir a pasta `Contributors.md` em um editor de texto e adicione o seu nome na pasta. Coloca o seu nome em qualque lugar entre o começo e o final, aí salva a pasta. 

No diretório do projeto execute `git status` e você verá as mudanças.
![image-git](https://camo.githubusercontent.com/a35c4722d7aab337eefc655d1488f7b4dc038508e6adaf5e88e2e052a976f010/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f6769742d7374617475732e706e67)

Adicione essas mudanças no branch que você acabou de criar usando`git add` command:
`git add Contributors.md` 

Agora commit essas mudanças usando o comando `git commit`: 
`git commit -m "Add seu-nome à lista de colaboradores` substituindo `seu-nome` pelo seu nome.

# Push as mudanças para o github 
Push as suas mudanças usando o comando `git push`:

```
git push origin -u seu-nome-branch
```

replacing `seu-nome-branch` com o nome do branch que você criou anterioramente. 

<details>
<summary> <strong>Se você receber algum erro durante o push, clique aqui:</strong></summary>

- ### Erro de Autenticação
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Por favor veja https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ para mais informações.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  Vá para o [Tutorial do GitHub](https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) sobre como gerar e configurar uma chave SSH para sua conta.

</details>

# Enviando suas mudanças para revisão
Executando esse comando no diretório do nosso repositório vai criar um pull request para revisão:

```bash 
gh pr create --repo firstcontributions/first-contributions
```

Depois disso envia o seu pull request.

Você pode utilizar o comando `gh status` para  
You can use the command `gh status` para ver sua solicitação pull mencionada em ação.

## Para onde ir a partir daqui? 

Parabéns! Você acaba de completar o wokflow de standard _fork -> clone -> edit -> pull request_ que você encontrará frequentemente como colaborador!

Comemore sua contribuição e compartilhe-a com seus amigos e seguidores acessando [web app](https://firstcontributions.github.io/#social-share).

Você pode se juntar à nossa equipe do Slack se precisar de ajuda ou tiver alguma dúvida. [Junte-se à equipe do Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA).

Agora vamos começar a contribuir para outros projetos. Compilamos uma lista de projetos com problemas fáceis nos quais você pode começar. Confira [the list of projects in the web app](https://firstcontributions.github.io/#project-list).

### [Material Adicional](additional-material/git_workflow_scenarios/additional-material.md)

## Tutorias Utilizando Outras Ferramentas

[Voltar à página principal](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
