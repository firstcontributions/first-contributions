# Brisanje lokalno napravljene grane

Ovo će biti korisno ako slučajno napravite grešku pri spelovanju imena grane.

Ovo možete uraditi na *3* načina

```
git branch -D <branch_name>
```

```
git branch --delete --force <branch_name>  # Isto kao i -D
```

```
git branch --delete  <branch_name>         # Greška ako nije spojena
```

-D je skraćenica za --delete --force što označava brisanje grane čak iako nije spojena (forsiraj brisanje), ali možete koristiti i -d skraćenicu za --delete koja baca grešku ako grana nije spojena...
