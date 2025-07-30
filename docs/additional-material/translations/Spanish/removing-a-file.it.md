# Eliminando un archivo de Git

A veces, puedes querer eliminar un archivo de Git, pero no borrarlo de tu computadora. Puedes hacerlo usando el siguiente comando:

``git rm <file> --cached``

## Entonces, ¿qué ocurrió?

Git ya no controlará los cambios en el archivo eliminado. Para Git, es como si hubieras eliminado el archivo. Si localizas el archivo en tu sistema de archivos, notarás que aún está allí.

Ten en cuenta que en el ejemplo anterior se utiliza la opción `--cached`. Si no agregas esta opción, Git eliminará el archivo no solo del repositorio, sino también de tu sistema de archivos.

Si confirmas el cambio con `git commit -m"Remove file1.js"` y lo envías al repositorio remoto usando `git push origin master`, el repositorio remoto eliminará el archivo.

## Características adicionales

- Si deseas eliminar más de un archivo, puedes incluirlos todos en el mismo comando:

    `git rm file1.js file2.js file3.js --cached`

- Puedes usar el carácter comodín (*) para eliminar todos los archivos similares. Por ejemplo, si deseas eliminar todos los archivos .txt de tu repositorio local:

    `git rm *.txt --cached`
