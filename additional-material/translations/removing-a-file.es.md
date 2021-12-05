# Remover un archivo de Git

Algunas veces, podrías dear remover un archivo de Git sin borrarlo de tu computadora. Puedes lograr esto usando los siguientes comandos:
``git rm <file> --cached``

## Qué es lo que Pasa?

Git no seguirá registrando los cambios hechos en el archivo removido. Por lo que sabe Git, es como si el archivo hubiera sido eliminado. SI trataras de localizar el archivo en tu sistema de archivos, notará que el archivo sigue allí.

Observe en el ejemplo anterior, el comando `--cached` es usado. Si no usáramos ese comando, Git va a remover el archivo no solo del repo, sino también de su sistema de archivos.

Si confirma el cambio con `git commit -m "Remove file1.js"` y lo envia a un repositorio remoto usando `git push origin master`, el repositorio remoto va a remover el archivo.

## Funciones adicionales

- Is desea remover has de un archive, suede incluirlos todos en el miso comando:

    `git rm file1.js file2.js file3.js --cached`

- Puede utilizar (*) para remover archives simulates. Por ejemplo, is desea remover todos los archives .txt de su repositorio local:

    `git rm *.txt --cached`
