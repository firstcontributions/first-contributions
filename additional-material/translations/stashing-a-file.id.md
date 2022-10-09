# Stashing (Menyimpan)

Bagaimana semisal kamu sedang mengerjakan banyak koding pada suatu branch dan tiba-tiba kamu perlu ganti ke branch lain. Padahal kode program di branch yang sedang kamu kerjakan sekarang belum selesai, dan juga belum dilakukan testing sama sekali dan kemungkinan kamu juga belum tentu akan melakukan commit kode program tersebut. Tapi kamu tidak bisa berpindah ke branch lain, kalau kamu belum melakukan commit pada branch yang sedang kamu kerjakan itu. Git juga bakal ngelarang kamu break flow tersebut. Lalu apa yang harus kita lakukan? dan bagaimana kita menghindari commit yang tidak diperlukan, sambil kita bisa berpindah branch dan mengerjakan fitur lain? Inilah yang akan kita bahas pada Tutorial ini. 

## Stashing your work ( Menyimpan pekerjaanmu )

Mari asumsikan kita sedang mengerjakan branch pada suatu project, dimana kita harus merubah suatu files. Sekarang jika kamu menjalankan perintah ```git status``` kita akan lihat perubahan apa saja dalam files tersebut.

```
$ git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#      modified:   index.html
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#
#      modified:   lib/simplegit.rb
#
```

Sekarang kita mau pindah ke branch lain, tapi belum akan menjalankan perintah commit dan menyimpan state; jadi kita perlu menjalankan perintah stash istilahnya adalah "menyimpan sementara" terkait perubahan apa saja yang telah kita lakukan pada files tersebut. 
Untuk membuat stash baru pada stack (kumpulan stash), kita jalankan perintah ```git stash```

```
$ git stash
Saved working directory and index state \
  "WIP on master: 049d078 added the index file"
HEAD is now at 049d078 added the index file
(To restore them type "git stash apply")
```

Sekarang working directory kita akan bersih, lalu jalankan ```git status```

```
$ git status
# On branch master
nothing to commit, working directory clean
```

Sekarang kamu dapat berpindah ke branch manapun dan mengerjakannya hal lain; tenang perubahan yang ada di stash akan tersimpan di stack. Untuk melihat stash yang telah disimpan di stack kita bisa menjalankan perintah ```git stash list```:

```
$ git stash list
stash@{0}: WIP on master: 049d078 added the index file
stash@{1}: WIP on master: c264051 Revert "added file_size"
stash@{2}: WIP on master: 21d80a5 added number to log
```

Semisal kita mau menerapkan atau apply perubahan yang telah disimpan stash, kita dapat menggunakan perintah ```git stash apply```. Dengan menggunakan perintah tersebut kita dapat menerapkan ulang perubahan terbaru yang tersimpan di stash. Untuk menerapkan ulang perubahan secara spesifik untuk tiap stash, kita dapat memberikannya nama dengan cara berikut; ```git stash apply <stash-name>```, pada bagian ```<stash-name>``` tersebut kita berikan nama atau keterangan terkait perubahan apa yang akan disimpan oleh stash untuk nantinya dapat di re-apply atau diterapkan ulang.

```
$ git stash apply
# On branch master
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#
#      modified:   index.html
#      modified:   lib/simplegit.rb
#
```

Kamu dapat melihat git akan memodifikasi ulang file yang belum di commit saat kamu menyimpannya dalam stash. Semisal, kamu punya clean working directory saat kamu mencoba menerapkan stash, dan mencoba apply perubahan tersebut di satu branch yang sama; namun mempunyai suatu clean working directory dan menerapkan stash di satu branch yang sama adalah hal yang tidak diperlukan. Intinya penggunaan stash dilakukan saat kita perlu menyimpan suatu perubahan pada branch yang sedang kamu kerjakan dan nantinya kamu perlu berpindah ke branch lain, kemudian menerapkan perubahan pada branch tersebut. Kamu juga dapat melakukan perubahan pada files yang belum di-commit di working directory saat menerapkan stash, git akan memberikan peringatan merge conflicts jika perubahan yang dilakukan tidak berjalan dengan baik.

Perubahan apapun yang telah kamu kerjakan pada seluruh file dapat di terapkan ulang, tetapi perubahan yang dilakukan pada file saat mode staged tidak dapat dilakukan. Untuk melakukanya kamu perlu menjalankan perintah ```git stash apply``` dengan ```--index``` untuk memberitahu perintah yang dijalankan tersebut dapat menerapkan ulang perubahan pada mode staged. Jikalau kamu hendak menjalankannya, kamu akan kembali kekondisi awal sebelum dilakukan perubahan:

```
$ git stash apply --index
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#      modified:   index.html
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#
#      modified:   lib/simplegit.rb
#
```

Perintah apply hanya menerapkan perubahan yang disimpan, tetapi kamu masih memiliki stash tersebut dalam stack. Jikalau kita mau menghapusnya, kamu dapat menjalankan perintah ```git stash drop``` dengan mencantumkan nama dari stash yang akan dihapus.

```
$ git stash list
stash@{0}: WIP on master: 049d078 added the index file
stash@{1}: WIP on master: c264051 Revert "added file_size"
stash@{2}: WIP on master: 21d80a5 added number to log
$ git stash drop stash@{0}
Dropped stash@{0} (364e91f3f268f0900bc3ee613f9f733e82aaed43)
```

Kamu juga dapat mejalankan perintah ```git stash pop``` untuk mengembalikan state terbaru yang telah disimpan dan kemudian menghapus stash tersebut.

## Un-applying a Stash (Membatalkan perintah Stash) 

Dalam kasus tertentu kamu mau melakukan perubahan dari stash yang telah disimpan, dan melakukan hal tertentu, tapi belum mau menerapkan perubahan pada stash tersebut. Git tidak menyediakan perintah seperti ```git unapply```, tapi hal tersebut dapat dilakukan dengan hanya memanggil ulang perubahan terkait pada stash yang ada dan menerapkanya dengan urutan terbalik:

```$ git stash show -p stash@{0} | git apply -R```

Perlu diperhatikan jika kamu tidak memberitahu secara spesifik suatu stash, Git akan menganggap stash tersebut adalah stash yang terbaru:

```$ git stash show -p | git apply -R```

Kamu mungkin mau membuat sebuah alias sehinga nantinya dapat dipanggil secara efektif dengan perintah ```stash-unapply``` untuk digunakan di Git. Contohnya:

```
$ git config --global alias.stash-unapply '!git stash show -p | git apply -R'
$ git stash apply
$ #... work work work
$ git stash-unapply
```

## Creating a Branch from Stash (Membuat sebuah Branch dari Stash)

Jika kamu mau menyimpan perubahan di stash, dan membiarkanya tersimpan dalam kurun waktu tertentu, kemudian melanjutkan kembali kerjaan pada branch yang telah disimpan perubahanya di stash, kemungkinan kamu akan menjumpai permasalahan atau problem jikalau hendak menerapkan stash yang telah disimpan tersebut. Jika perubahan tersebut mencoba untuk memodifikasi file yang sebelumnya telah kamu modifikasi dahulu, kamu bakal mendapatkan peringatan merge conflict dan kamu harus mengatasinya. Jika kamu mau dengan mudah untuk menerapkan kembali perubahan yang tersimpan di stash, kamu dapat menjalankan perintah ```git stash branch```, perintah tersebut akan meng-create atau membuatkan branch baru untuk mu, cek ulang commit yang ada dimana kamu menyimpan perubahan dalam stash, dan menerapkan ulang perubahan tersebut, kemudian hapus stash tersebut jikalau perubahan dapat dilakukan dengan sukses.

```
$ git stash branch testchanges
Switched to a new branch "testchanges"
# On branch testchanges
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#      modified:   index.html
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#
#      modified:   lib/simplegit.rb
#
Dropped refs/stash@{0} (f0dfc4d5dc332d1cee34a634182e168c4efc3359)
```

Perintah tersebut adalah shortcut untuk mengembalikan perubahan yang telah tersimpan dalam stash sekaligus membuat branch baru.

