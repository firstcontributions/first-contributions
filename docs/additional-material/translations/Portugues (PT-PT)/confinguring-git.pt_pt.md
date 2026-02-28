# Configurar GIT

Ao tentares fazer um commit com o git pela primeira vez, podes ver uma mensagem como a seguinte:

```bash
$ git commit
*** Please tell me who you are.

Run:

git config --global user.email "you@example.com"
git config --global user.name "Your Name"

to set your account's default identity.
Omit "--global" to set the identity only in this repository
```

O Git precisa de saber quem és ao criar um commit. Quando trabalhas em colaboração, é importante identificar quem modificou o quê e quando; por isso o Git associa commits a um nome e um email.

### Configuração global
Para armazenar configurações globalmente utiliza:

```
git config --global <variable name> <value>
```

Por exemplo:

```
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

### Configuração por repositório
Estas configurações aplicam-se apenas ao repositório atual; são úteis quando precisas de usar identidades diferentes para projetos distintos.
