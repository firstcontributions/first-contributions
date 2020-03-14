
# Remover un archivo de Git

Algunas veces, puede ser que quieras remover un archivo de Git, pero no borrarlo de tu computadora. Puedes lograr esto usando el próximo comando:

``git rm <file> --cached``

## Que ocurrió?

Git no va a guardar o mantener los cambios hechos en el archivo removido. En cuanto a Git se refiere, es como si hubieras borrado el archivo. Si localizas el archivo en tus archivos de sistema, te darás cuenta de que todavía esta ahí.

Date cuenta de que en el ejemplo arriba, la bandera `--cached` es usada. Si no agregáramos esta bandera, Git removería el archivo no solo del repositorio, pero también de tus archivos de sistema.

Si haces Commit al cambio con `git commit -m "Remove file1.js"` y lo empujaras al repositorio remoto usando `git push origin master`, el repositorio remoto también removería el archivo.


## Herramientas adicionales 
- Si quieres remover más de un archivo, puedes incluirlos todos en el mismo comando:
    
    `git rm file1.js file2.js file3.js --cached` 

- Puedes usar una carta comodín (*) para remover archivos adicionales. Por ejemplo, si te gustaría remover todos los archivos .txt de tu repositorio local: 
    
    `git rm *.txt --cached`

