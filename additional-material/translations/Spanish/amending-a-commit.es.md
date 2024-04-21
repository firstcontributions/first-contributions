# Modificar un commit

Imaginemos que has realizado un commit en tu repositorio remoto y luego te das cuenta de que hay un error tipográfico en el mensaje del commit o que olvidaste agregar una línea en tu commit más reciente. ¿Cómo corregir este error? Ese es el tema de este tutorial.

## Cambiar un mensaje de commit reciente después de haberlo enviado a GitHub
Para hacerlo sin siquiera abrir un archivo:
* Escribe el comando ```git commit --amend -m "seguido de tu nuevo mensaje de commit"```
* Lanza el comando ```git push origin <nombre-de-la-rama>``` para realizar un commit en el repositorio.

Nota: Si solo escribes ```git commit --amend```, se abrirá el editor de texto y te pedirá que modifiques el mensaje del commit. Agrega la opción ``-m`` para evitar pasar por el editor de texto.

## Modificar un commit específico

Entonces, ¿qué sucede si olvidas hacer un cambio menor en un archivo, como cambiar una palabra, y ya has enviado ese commit a nuestro repositorio remoto?

Para ilustrar esto, aquí tienes un registro de mis commits;
```
g56123f creación de un archivo bot
a2235d actualización de contributeur.md
a5da0d modificación del archivo bot
```
Imaginemos que olvidé agregar una palabra en el archivo bot.

Hay dos formas de resolver este problema. La primera es hacer un nuevo commit que contenga el cambio de esta manera:
```
g56123f creación de un archivo bot
a2235d actualización de contributeur.md
a5da0d modificación del archivo bot
b0ca8f agregado de una palabra en el archivo bot
```
La segunda forma es modificar el commit a5da0d y agregar esta nueva palabra, luego enviarlo a GitHub, todo en un solo commit. Esta segunda opción parece más adecuada, ya que es un cambio menor.

Para hacer esto, sigue estos pasos:
* Modifica el archivo. En nuestro caso, modifica el archivo bot para incluir la palabra olvidada.
* Luego, agrega el archivo a la zona de preparación con el comando ```git add <nombre-del-archivo>```

Normalmente, después de agregar archivos a la zona de preparación, ¿la siguiente etapa es ejecutar el comando git commit -m "nuestro mensaje de commit", verdad? Pero como lo que queremos aquí es modificar el commit anterior, en su lugar ejecutaremos los comandos:

* ```git commit --amend```
Esto abrirá el editor de texto que te pedirá que modifiques el mensaje. Puedes decidir si dejar el mensaje tal como está o cambiarlo.
* Sal del editor
* Envía tus cambios con el comando ```git push origin <nombre-de-la-rama>```

De esta manera, ambos cambios se encuentran en un solo commit.