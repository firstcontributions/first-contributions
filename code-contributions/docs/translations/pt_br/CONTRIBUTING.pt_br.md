# Passos para Contribuir

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

## Faça um Fork desse repositório clicando no botão Fork

## Clone o repositório que você fez.

Dentro do seu repositório que você fez o fork, click no botão "Code". Selecione a aba SSH e clique no botão `copy to clipboard`.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />
Abra um terminal e execute o seguinte comando do git:

```bash
git clone "url_que_copiou"
```

> [!IMPORTANT]
> Nos passos seguintes, quando vir <seu-github-id> você deve substituí-lo pelo seu ID do GitHub.  
> Por exemplo, se o seu ID do GitHub for `aaronsw`,  
> `git switch -c add-<your-github-id>` torna-se `git switch -c add-aaronsw`  
> `contributors/<your-github-id>.html` torna-se `contributors/aaronsw.html`

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

## Criando um Branch

Acesse o diretório do repositório no seu computador (caso você não esteja nele):

```bash
cd code-contributions
```

Agora crie um Branch usando o comando `git switch`:

```bash
git switch -c add-<your-github-id>
```


## Create your card

Você pode adicionar seu cartão como um arquivo HTML no diretório contributors. Crie um arquivo com seu nome de usuário dentro do diretório contributors. Você pode copiar o seguinte modelo para começar:

`contributors/<your-github-id>.html`
```html
<article>
  <h3>Your username</h3>
  <p>A small bio about you (optional)</p>
  <h4>Programming languages I use</h4>
  <section class="container">
    <div class="badge" style="background-color: #3874a4; color: white">
      Python
    </div>
    <div class="badge" style="background-color: #f7df1e; color: black;">
      JavaScript
    </div>
  </section>

  <h4>Tools I use</h4>
  <section class="container">
    <img
      class="icon"
      src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/bash/bash-original.svg"
    />
    <img
      class="icon"
      src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linux/linux-original.svg"
    />
  </section>
</article>
<style>
  body {
    font-family: sans-serif;
  }
  .container {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
  }
  .badge {
    padding: 0.5rem;
    border-radius: 0.25rem;
  }
  .icon {
    width: 2rem;
  }
</style>

```
## Adicione seu cartão à lista de colaboradores

Adicione o nome do arquivo que você criou no arquivo: `scripts/contributors.js`.

`scripts/contributors.js`
```js
const contributorFiles = [
  "<your-github-id>.html", // adicione aqui o nome do seu arquivo
  "roshanjossey.html",
  "gokultp.html",
];
```

## Visualize suas alterações em um navegador da web

Você pode ver suas alterações abrindo o arquivo `index.html` em um navegador. Você deve conseguir ver o novo cartão que adicionou nos passos anteriores.

Você pode continuar a fazer alterações no seu cartão e atualizar a aba do navegador para ver essas mudanças.

## Faça um Commit com as suas alterações

Adicione essas alterações ao Branch que você acabou de fazer utilizando o comando `git add`

```bash
git add contributors/<your-github-id>.html
```

Agora confirme essas alterações usando o comando: `git commit`

```bash
git commit -m "add <your-github-id>"
```

## Faça um Push das alterações para o GitHub

```bash
git push -u origin add-<your-github-id>
```

## Envie suas alterações para serem revisadas

Se você for para o seu repositório no GitHub, verá um botão `Compare & pull request`. Clique nesse botão.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Agora envie um Pull Request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Logo estará mesclando ('mergeando') as suas mudanças no Branch principal (main) deste projeto. Você receberá um e-mail de notificação quando as alterações forem mescladas.
