# Configurando o ambiente do Git

Quando você tentou se comprometer com o Git pela primeira vez, pode ser possível exibir a seguinte mensagem:

```bash
$ git commit

*** Insira credencias de acesso.

Execute

git config --global user.email "email"
git config --global user.name "nome de usuario"

para definir a identidade padrão da sua conta.
Cancelar --global para definir a identidade apenas neste repositório.
```

O Git precisa saber quem você é, para criar commit. Quando você trabalha em um grupo com mais pessoas, você deve sempre saber quem fez as alterações no projeto e quando você o fez. Para este propósito, o Git foi criado de tal forma que o commit-i estava ligado ao nome e ao e-mail.

Existem várias maneiras de dar seu nome e e-mail ao comando `git commit`, e vamos revisar algumas delas nas seguintes linhas.

### Configuração Global

Quando você salva algo em uma configuração global (configuração global), essa configuração está disponível para todos os repositórios em que você está trabalhando. Esse método é recomendado e funciona na maioria dos casos.

Para salvar algo em uma configuração global, use o comando `config`:

`$ git config --global <variable name> <value>`

No caso de dados do usuário:

```
$ git config --global user.email "you@example.com"
$ git config --global user.name "Your Name"
```

### Configuração do repositório

Como o nome indica, essas configurações são limitadas a apenas um repositório. Se você deseja se comprometer com um repositório específico, digamos um projeto oficial, com seu próprio e-mail, use este método.

Para salvar algo na configuração do repositório, use o comando `config` e solte o sinalizador` --global`:


`$ git config <variable name> <value>`

No caso de dados do usuário:

```
$ git config user.email "you@alternate.com"
$ git config user.name "Your Name"
```

### Configuração de linha de comando

Essas configurações são limitadas apenas à linha de comando atual. Todos os comandos do Git aceitam o prefixo `-c` antes do verbo do comando. Isso cria uma configuração temporária.

Para salvar algo na configuração da linha de comando:

`$ git -c <variable-1>=<value> -c <variable-2>=<value> <command>`

Em nosso exemplo, o comando commit deve ser usado da seguinte maneira:

`git -c user.name='Your Name' -c user.email='you@example.com' commit -m "Your commit message"`

### Sobre os benefícios

A seqüência de uso entre os métodos mencionados acima é o seguinte `command-line> repository> global`. Isso significa que, se a variável for armazenada na linha de comando e globalmente, o valor na configuração da linha de comando será usado.

## Extra

Até agora, trabalhamos apenas com as configurações do usuário, mas ainda há algumas outras configurações. Alguns deles são:

1.  `core.editor` - para determinar o editor de texto usado para escrever comentários, etc.
2.  `commit.template` - para determinar o arquivo no sistema a ser usado como o commit inicial para commit.
3.  `color.ui` - para determinar o valor booleano para usar cores na saída do Git.

Nós simplificamos alguns dos detalhes para facilitar a compreensão. Você pode ler mais sobre [git-scm.com](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration).
