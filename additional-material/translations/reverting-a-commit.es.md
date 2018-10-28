# Revirtiendo un commit

Restaurar una confirmación significa crear una nueva confirmación que elimine los cambios que hicimos en la confirmación anterior. Es como hacer CTRL + Z en Git.

Regresar/restaurar un commit en Git es relativamente fácil porque cada confirmación que enviamos al repositorio remoto está asociada con su única clave alfanumérica SHA (algoritmo de hash seguro). Esto significa que puedo revertir cada commit tan solo teninedo su SHA. En cualquier caso, debemos tener cuidado al recuperarlo porque podemos dañar el repositorio.

Para poder seleccionar el SHA del commit específico que queremos eliminar, obtenemos una muy buena lista de todos los commits que hicimos. Esta lista se obtiene mediante este comando: ```git log``` o ```git log --oneline ``` El comando git log también devolverá SHA, pero en un formato más largo. Al usar la bandera ```--oneline ```  Git le dice que queremos que nos muestre el commit en una sola línea.

Los primeros 7 caracteres de cada fila de impresión se denominan el SHA abrevido del commit

por ejemplo, este es la impresion despues de ```git log --oneline ``` para un repositorio:
```
389004d added spacing in title
c1b9fc1 Merge branch 'master' into tutorials
77eaafd added tutorial for reverting a commit
```


Bueno, ahora podemos tratar de eliminar el commit "added spacing in title" con los siguientes pasos:

*   copiar el SHA del commit, en este caso ```389004d```
*   Luego usamos el comando ```git revert 389004d```


Ahora nuestro editor de texto comienza y nos invita a editar el comentario de commit.
Puede elegir dejar el mensaje de Git predeterminado, que comienza con la palabra `Revert`, o puede cambiar el comentario de acuerdo con sus preferencias.

*   Luego, guardamos y cerramos el editor de texto.
*   Regresar a la línea de comando.
*   Usamos el comando ```git push origin <branch-name>``` Para enviar los cambios

Y eso es todo, los cambios serán eliminados. En este caso, el repositorio se devolverá al estado en la confirmación ```c1b9fc1```.