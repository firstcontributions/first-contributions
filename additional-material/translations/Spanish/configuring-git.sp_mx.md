# Configurando Git

La primera vez que intentes comprometerte usando git, deberías obtener uno como este:

```bash
$ git commit
*** Por favor dime quién eres.

Rode:

git config --global usuario.correo electrónico "usted@ejemplo.com"
git config --global user.name "Su nombre"

Para configurar su identidad de cuenta predeterminada.
Omita "--global" para establecer la identidad solo en ese repositorio
```

Git necesita saber quién es usted al crear una confirmación. Cuando trabajas en colaboración, deberías poder ver quién modificó qué partes del proyecto y cuándo, por lo que git está diseñado para crear confirmaciones vinculadas a un nombre y correo electrónico.

Hay varias formas de proporcionar el comando `git commit` con su correo electrónico y nombre. Veremos algunos de ellos a continuación.


### Configuración global
Cuando almacena algo en la configuración global, es accesible en todos los sistemas y repositorios en los que trabaja. Esta es la forma principal y funciona para la mayoría de los casos de uso.

Para almacenar algo en la configuración use el comando `config` de la siguiente manera:

`$ git config --global <variable name> <value>`

En el caso de los datos del usuario, los ejecutamos de la siguiente manera:

```
$ git config --global usuario.correo electrónico "usted@ejemplo.com"
$ git config --global user.name "Su nombre"
```

### Configuración del repositorio

Como su nombre lo indica, estas configuraciones apuntan a su repositorio actual. Si desea comprometerse con un repositorio específico, por ejemplo, un proyecto relacionado con el trabajo, con el correo electrónico de su empresa, puede utilizar este método.

Para almacenar algo en la configuración del repositorio, usa el comando `config` omitiendo el indicador `--global`, así:

`$ git config <variable name> <value>`

En el caso de los datos del usuario, lo ejecutamos de la siguiente manera:

```
$ git config user.email "usted@alternate.com"
$ git config user.name "Tu nombre"
```

### Configuración de la línea de comando

Este tipo de configuración solo tiene como objetivo el comando actual. Todos los comandos de git usan argumentos `-c` antes del verbo de acción para establecer datos de configuración temporales

Para almacenar algo en la configuración de la línea de comando. Ejecute su comando de la siguiente manera:

`$ git -c <variable-1>=<value> -c <variable-2>=<value> <command>`

En el ejemplo anterior, ejecutaríamos el comando de confirmación de la siguiente manera:

`git -c user.name='Su nombre' -c user.email='you@example.com' commit -m "Su mensaje de confirmación"`

### Nota sobre precedencia

Entre los tres métodos descritos aquí, el orden de prioridad es "línea de comando > repositorio > global". Esto significa que si se establece una variable en la línea de comando y también globalmente, el valor de la línea de comando se usará para la operación.

## Además de los detalles del usuario:

Hasta ahora solo nos hemos ocupado de los detalles del usuario mientras trabajamos en la configuración. Sin embargo, hay varias otras opciones disponibles. Algunos de ellos son:

1. `core.editor`: para especificar el nombre del editor utilizado para escribir mensajes de confirmación, etc.
2. `commit.template`: para especificar un archivo en el sistema como plantilla de confirmación inicial
3. `color.ui`: para especificar un valor booleano para usar colores en la salida de git

Hemos resumido algunos detalles para facilitar la comprensión. Para leer más, visite:

[git-scm.com](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration).