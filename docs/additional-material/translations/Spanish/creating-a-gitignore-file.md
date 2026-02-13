# .gitignore

El archivo .gitignore es un archivo de texto que le indica a Git qué archivos o carpetas ignorar en un proyecto.

Un archivo .gitignore local generalmente se coloca en el directorio raíz de un proyecto. También puedes crear un archivo .gitignore global, y cualquier entrada en ese archivo será ignorada en todos tus repositorios de Git.

## ¿Por qué .gitignore?
Ahora te preguntarás por qué querrías que Git ignorara ciertos archivos y carpetas. Es porque no quieres que archivos como los de construcción, archivos de caché, otras configuraciones locales como los módulos de Node, archivos de compilación, archivos temporales que crean los IDEs, etc., sean rastreados por Git. Normalmente se utiliza para evitar comprometer archivos transitorios de tu directorio de trabajo que no son útiles para otros colaboradores.

## Empezando
Para crear un archivo .gitignore local, crea un archivo de texto y nómbralo .gitignore (recuerda incluir el . al principio). Luego edita este archivo según sea necesario. Cada nueva línea debe listar un archivo o carpeta adicional que deseas que Git ignore.

Las entradas en este archivo también pueden seguir un patrón de coincidencia.

```


* se utiliza como un comodín
/ se utiliza para ignorar nombres de ruta relativos al archivo .gitignore
# se utiliza para agregar comentarios a un archivo .gitignore

Este es un ejemplo de cómo podría verse el archivo .gitignore:

# Ignorar archivos del sistema de Mac
.DS_store

# Ignorar la carpeta node_modules
node_modules

# Ignorar todos los archivos de texto
*.txt

# Ignorar archivos relacionados con claves API
.env

# Ignorar archivos de configuración de SASS
.sass-cache

```
Para agregar o cambiar tu archivo .gitignore global, ejecuta el siguiente comando:
git config --global core.excludesfile ~/.gitignore_global

```
Esto creará el archivo ~/.gitignore_global. Ahora puedes editar ese archivo de la misma manera que un archivo .gitignore local. Todos tus repositorios de Git ignorarán los archivos y carpetas listados en el archivo .gitignore global.

## Cómo deshacer el seguimiento de archivos previamente comprometidos desde un nuevo .gitignore

Para deshacer el seguimiento de un solo archivo, es decir, dejar de rastrear el archivo pero no eliminarlo del sistema, usa:
git rm --cached filename
```

Para deshacer el seguimiento de todos los archivos en .gitignore:

Primero, confirma cualquier cambio de código pendiente y luego ejecuta:
git rm -r --cached
```

Esto elimina cualquier archivo cambiado del índice (área de preparación), luego ejecuta:
git add .

```
Confirma:
git commit -m ".gitignore ahora está funcionando."
```

Para deshacer ```git rm --cached filename```, usa git ```add filename```.
