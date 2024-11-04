# Eliminando una rama creada localmente

Esto será útil cuando accidentalmente escribiste mal el nombre de una rama.

Esto se puede hacer de *3* maneras:

```
git branch -D <nombre_rama>
```

```
git branch --delete --force <nombre_rama>  # Igual que -D
```

```
git branch --delete <nombre_rama>          # Error si no está fusionada
```

-D significa --delete --force, que eliminará la rama incluso si no está fusionada (eliminación forzada), pero también puedes usar -d, que significa --delete, y generará un error según el estado de fusión de la rama...