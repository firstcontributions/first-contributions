# Eliminar um branch localmente

Isto é útil quando criaste um branch com um nome com erro de digitação ou que já não precisas.

Existem *3* formas principais de o fazer:

```
git branch -D <branch_name>
```

```
git branch --delete --force <branch_name>  # igual a -D
```

```
git branch --delete <branch_name>         # erro se não estiver mesclado
```

`-D` é equivalente a `--delete --force` e elimina o branch mesmo que não esteja mesclado. Usa `-d` para recusar eliminar branches que não foram mesclados.
