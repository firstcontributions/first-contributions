# Configurando git

A primeira vez que tentou comitar usando git, você pode ter recebido uma resposta como a abaixo:

```bash
$ git commit
*** Por favor, me diga quem você é.

Run

git config --global user.email "voce@exemplo.com"
git config --global user.name "Seu nome"

para definir sua conta como identidade padrão.
Omit --global para definir a identidade apenas neste repositório.
```

O Git precisa saber quem você é quando você cria um commit. Quando você está trabalhando colaborativamente, você deve ser capaz de ver quem modificou quais partes do projeto e quando, e assim, o git foi projetado para criar commits vinculados a um nome e um email.

Existem várias maneiras de fornecer o comando `git commit` com seu e-mail e nome, e vamos ver algumas delas abaixo.

### Configuração Global

Quando você armazena algo na configuração global, é acessível ao sistema em todos os repositórios em que você trabalha. Essa é a maneira preferida e funciona para a maioria dos casos de uso.

Para armazenar algo na configuração global, você usa o comando `config` da seguinte maneira:

`$ git config --global <nome da variável> <valor>`

In the case of user details, we run it as follows:
No caso dos detalhes do usuário, nós executamos da forma abaixo:

```
$ git config --global user.email "voce@exemplo.com"
$ git config --global user.name "Seu nome"
```

### Configuração do Repositório

Como o nome diz, essas configurações estão no escopo do seu repositório atual. Se você quiser comiitar em um repositório específico, digamos, um projeto relacionado ao trabalho, com o e-mail da sua empresa, você poderá usar esse método.

Para armazenar algo na configuração do repositório, você usa o comando `config` usando o sinalizador` --global` da seguinte maneira:

`$ git config <nome da variável> <valor>`

No caso dos detalhes do usuário, nós executamos da forma abaixo:

```
$ git config user.email "voce@exemplo.com"
$ git config user.name "Seu nome"
```

### Configuração de linha de comando

Esse tipo de configuração é definido apenas para o escopo atual. Todos os comandos git recebem argumentos `-c` antes do verbo de ação para definir dados de configuração temporários.

Para armazenar algo na configuração da linha de comando, execute seu comando da seguinte maneira:

`$ git -c <variavel-1>=<valor> -c <variavel-2>=<valor> <comando>`

Em nosso exemplo, nós executaríamos o comando commit da seguinte forma:

`git -c user.name='Seu nome' -c user.email='voce@exemplo.com' commit -m "Sua mensagem de commit"`

### Nota sobre Precedência

Entre os três métodos descritos aqui, a ordem de precedência é `linha de comando > repositório > global`. Isso significa que, se uma variável for configurada na linha de comando e também globalmente, o valor da linha de comando será usado para a operação.


## Além dos detalhes do usuário

Nós lidamos apenas com os detalhes do usuário até agora, enquanto trabalhamos com a configuração. No entanto, existem várias outras opções de configuração disponíveis. Alguns deles são:

1. `core.editor` - para especificar o nome do editor usado para escrever mensagens de commit, etc.
2. `commit.template` - para especificar um arquivo no sistema como o modelo de commit inicial.
3. `color.ui` - para especificar um valor booleano para usar cores na saída do git.

Nós abstraímos alguns detalhes para facilitar a compreensão. Para ler mais, vá para [git-scm.com] (https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration).