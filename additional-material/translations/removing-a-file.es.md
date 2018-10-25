# Eliminar un archivo del control GIT

A veces puede ser necesario eliminar el archivo del control GIT, pero guardarlo en la computadora. Esto se puede lograr con el siguiente comando:

``git rm <archivo> --cached``

## Que paso?

GIT ya no controla los cambios en un archivo remoto. Desde el punto de vista de GIT, falta este archivo, pero si intenta localizar este archivo en el sistema de archivos, verá que aún está en su lugar.

Tenga en cuenta que en el comando anterior se usa la tecla `--cached`. Si no hubiéramos agregado esta clave, GIT eliminaría el archivo no solo del repositorio, sino también del sistema de archivos.

Si ejecuta el comando `git commit -m "Delete file1.js"` y luego lo lanza al repositorio remoto con el comando `git push origin master`, el archivo también se eliminará del repositorio remoto.

## Información adicional

-  Si desea eliminar más de un archivo, puede hacerlo enumerando todos los archivos en un solo comando:

    `git rm file1.js file2.js file3.js --cached`

-   Puede usar la signo (*) para eliminar archivos con nombres similares, por ejemplo, si desea eliminar todos los archivos .txt del repositorio local, escriba: 

    `git rm *.txt --cached`
