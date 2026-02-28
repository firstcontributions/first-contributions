# Manter o teu Fork sincronizado com este repositório

Primeiro, é importante perceber o fluxo de sincronização. Neste cenário existem três repositórios distintos: o repositório público no GitHub `github.com/Roshanjossey/first-contributions/`, o teu fork `github.com/Seu-Nome/first-contributions/` e o repositório local onde trabalhas. Este tipo de colaboração é típica em projetos de código aberto e é designada por `Triangle Workflows`.

Para manter os teus repositórios atualizados com o repositório público, o primeiro passo é fazer um fetch e depois um merge (ou rebase) do repositório público para o teu repositório local. O segundo passo é fazer push do repositório local para o teu fork no GitHub. É a partir do fork que podes abrir um Pull Request.

Exemplo de passos:

1. Assegura-te de que estás na branch principal (master):

```
git status
```

2. Se não estiveres na `master`, vai para ela:

```
git checkout master
```

3. Adiciona o repositório original como `upstream`:

```
git remote add upstream https://github.com/Roshanjossey/first-contributions
```

4. Busca as alterações do upstream:

```
git fetch upstream
```

5. Aplica as alterações ao teu branch principal (ex.: rebase):

```
git rebase upstream/master
```

6. Faz push do teu master para o teu fork:

```
git push origin master
```

Agora os teus repositórios estarão atualizados. Segue estes passos sempre que o teu fork estiver "atrás" do repositório original.
