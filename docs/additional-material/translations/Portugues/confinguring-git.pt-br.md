# Configurando GIT

A primeira vez que você tentar fazer um commit usando git, deve ter recebido uma como esta:

```bash
$ git commit
*** Please tell me who you are.

Rode:

git config --global user.email "you@example.com"
git config --global user.name "Your Name"

Para definir a identidade padrão da sua conta.
Omita “--global” para definir a identidade apenas nesse repositório
```

o Git precisa saber quem você é ao criar um commit. Quando você está trabalhando colaborativamente, deve ser capaz de ver quem modificou quais partes do projeto e quando, e assim, o git foi projetado para criar commits vinculados a um nome e um email.

Existem várias maneiras de fornecer o comando `git commit` com seu email e nome. Veremos algumas delas a seguir.


### Configuração global
Quando você armazena algo na configuração global, fica acessível em todos os sistemas e repositórios nos quais você trabalha. Essa é principal forma e funciona para a maioria dos casos de uso.

Para armazenar algo na configuração use o comando `config` da seguinte maneira:

`$ git config --global <variable name> <value>`

No caso dos detalhes do usuário, nós os executamos da seguinte maneira:

```
$ git config --global user.email "you@example.com"
$ git config --global user.name "Your Name"
```

### Configuração do repositório

Como o nome diz, essas configurações tem como alvo seu repositório atual. Se você quiser se comprometer com um repositório específico, por exemplo, um projeto relacionado a trabalho, com o email de sua empresa, então você pode usar esse método.

Para armazenar algo na configuração do repositório, você usa o comando `config` omitindo a sinalização `--global`, da seguinte forma:

`$ git config <variable name> <value>`

No caso dos detalhes do usuário, nós o executamos da seguinte maneira:

```
$ git config user.email "you@alternate.com"
$ git config user.name "Your Name"
```

### Configuração da linha de comando

Esse tipo de configuração tem como alvo apenas o comando atual. Todos os comandos git usam argumentos `-c` antes do verbo de ação para definir dados de configurações temporários

Para armazenar algo na configuração da linha de comando. Execute seu comando da seguinte maneira:

`$ git -c <variable-1>=<value> -c <variable-2>=<value> <command>`

No exemplo citado, executaríamos o comando commit da seguinte forma:

`git -c user.name='Your Name' -c user.email='you@example.com' commit -m "Your commit message"`

### Nota sobre precedência

Entre os três metodos descritos aqui, a ordem de precedência é `linha de comando > repositório > global`. Isso significa que, se uma variável for configurada na linha de comando e também globalmente, o valor da linha de comando será usado para a operação.

## Além dos detalhes do usuário:

Nós lidamos apenas com os detalhes do usuário até agora, enquanto trabalhamos com a configuração. No entanto, existem várias outras opcões disponíveis. Algumas delas são:

1. `core.editor` - para especificar o nome do editor usado para escrever mensagens de commit etc
2.  `commit.template` - para especificar um arquivo no sistema como o modelo de commit inicial
3.  `color.ui` - para especificar um valor booleano para usar cores na saída do git

Nós abstraimos alguns detalhes para facilitar o entendimento. Para ler mais, acesse:

[git-scm.com](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration).