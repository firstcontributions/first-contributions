# Menghapus sebuah local Branch 

Guide ini akan menjadi hal yang mudah jika kamu sering secara tidak sengaja salah dalam menyebutkan nama suatu branch.

Hal ini dapat diatasi dengan 3 cara 

```
git branch -D <branch_name>
```

```
git branch --delete --force <branch_name>  # Same as -D
```

```
git branch --delete  <branch_name>         # Error on unmerge
```

-D yang merupakan singkatan dari --delete --force yang akan melakukan delete atau menghapus suatu branch bahkan jika branch tersebut belum dilakukan merge, istilahnya (hapus dengan paksa); tetapi kamu juga dapat menggunakan -d yang merupakan singkatan dari --delete dimana akan memunculkan error jika terjadi status merge dari branch terkatit...
