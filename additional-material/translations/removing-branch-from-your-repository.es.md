## Removiendo la rama de tu repositorio

Si has seguido el tutorial hasta ahora, tu rama `<add-tu-nombre>` ha completado su objetivo, y es el momento de borrarlo de su repositorio local. Esto no es necesario, pero el propio nombre de esta rama muestra cómo su objetivo es específico. Su vida se puede hacer corta debido a esa especificidad.

Primero, vamos a fusionar (hacer merge) la rama `<add-tu-nombre>` con su Branch principal (master), entonces vamos a ella:
```
git checkout master
```

Hacer merge de tu rama `<add-seu-nome>` hacia master:
```
git merge <add-tu-nombre> master
```

Elimina `<add-seu-nome>` do seu repositório local:
```
git branch -d <add-tu-nombre>
```

Ahora ya has borrado tu rama local `<add-su-nombre>` y todo está limpio y ordenado.
En ese punto, todavía debes tener la rama `<add-su-nombre>` en su Fork. Antes de borrarlo, recuerde que envió un Pull Request a este repositorio desde esta rama remota. Entonces, a menos que ya hayas fusionado la rama, no debes borrarla.

Sin embargo, si ya has fusionado tu rama y deseas borrar la rama remota, utiliza:
```
git push origin --delete <add-tu-nombre>
```

Ahora, tu sabes cómo arreglar tus ramas.
Con el tiempo, muchos Commits se añaden a este repositorio público. Y las ramas principales (master) de tu máquina local y de tu Fork no estarán más actualizados. Entonces, para mantener tus repositorios sincronizados con este, siga los pasos a continuación.

#### [Manteniendo su Fork sincronizado con este repositorio](keeping-your-fork-synced-with-this-repository.pt_br.md)
