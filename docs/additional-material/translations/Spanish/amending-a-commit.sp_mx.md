# Arreglando un compromiso (Commit)

¿Qué sucede si confirmas un cambio en tu repositorio remoto y luego te das cuenta de que tiene un error en el mensaje de confirmación o si olvidaste agregar una línea de código en tu confirmación más reciente?
¿Cómo editarías esto? Eso es lo que cubre este tutorial.

## Cambiar un mensaje de confirmación reciente después de enviarlo a Github

Para hacer esto sin abrir un archivo:
* Ingresa el comando ```git commit --amend -m "seguido de su nuevo mensaje de confirmación"```
* Ejecuta ```git push origin <branch-name>``` para confirmar los cambios en el repositorio.

Nota: Si simplemente escribiste ```git commit --amend```, se abrirá el editor de texto y te pedirá que edites el mensaje de confirmación.
Agregar el indicador ``-m`` evita esto.

## Realizar cambios en una sola confirmación

¿Qué pasa si nos olvidamos de hacer un pequeño cambio en un archivo, como agregar una sola palabra, pero ya hemos enviado la confirmación a nuestro repositorio remoto?

Para ilustrar, aquí hay un registro de mis confirmaciones:
```bash
g56123f creó el archivo bot
a2235d actualizado colaborador.md
archivo bot modificado a5da0d
```

Supongamos que olvidé agregar una palabra en el bot.

Hay 2 formas de resolver este problema. La primera es hacer una nueva confirmación que contenga el cambio, como esta:

```bash
g56123f creó el archivo bot
a2235d actualizado colaborador.md
archivo bot modificado a5da0d
b0ca8f agregó una palabra en el archivo bot
```

La segunda forma es corregir la confirmación a5da0d, agregar esta nueva palabra y enviarla a Github como una confirmación única.
Esta acción suena mejor ya que es sólo un pequeño cambio.

Para ello haríamos lo siguiente:
* Modificar el archivo. En ese caso, modificaré el archivo del bot para incluir la palabra que omití antes.
* A continuación, agregue el archivo al área de preparación (*staging area*) con el comando ```git add <filename>```

Normalmente, después de agregar archivos al área de preparación, lo siguiente que hacemos es ingresar el comando ```git commit -m "our commit message"```, ¿verdad?
Pero como lo que queremos hacer aquí es arreglar la confirmación anterior, ejecutaremos en su lugar:

* ```git commit --amend```
  Esto iniciará el editor de texto para que podamos editar el mensaje. Tú decides si dejar el mensaje como estaba antes o editarlo.
* Salir del editor guardando los cambios
* Empuja tus cambios con el comando ```git push origin <branch-name>```

De esa manera, ambos cambios ahora estarán en una sola confirmación.