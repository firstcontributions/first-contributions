# Membatalkan Commit Lokal (Undo local commits)

Untuk membatalkan commit lokal, yang perlu Anda lakukan adalah
```bash
git reset
```
Perintah ini akan me-reset staging area Anda ke commit terakhir Anda, tetapi perubahan yang Anda buat pada direktori kerja (working directory) Anda tidak akan berubah. Jadi, Anda masih dapat melakukan commit ulang terhadap apa yang telah Anda ubah.
Atau, jika Anda hanya ingin menghapus satu file dari commit Anda sebelumnya. Maka, Anda dapat melakukan perintah di bawah ini
```bash
git reset <file>
```
Perintah tersebut hanya akan menghapus file yang ditentukan dari staging area, tetapi perubahan yang dilakukan pada file tersebut akan tetap ada.

Contoh penggunaan ```git reset```
```bash
# Membuat perubahan pada index.php dan tutorial.php
# Menambahkan file ke staging area
$ git add .
# Teringat bahwa kedua file perlu di-commit secara terpisah
# Unstage tutorial.php
$ git reset tutorial.php
# Commit index.php terlebih dahulu
$ git commit -m "Changed index.php"
# Sekarang commit tutorial.php
$ git add tutorial.php
$ git commit -m "Changed tutorial.php"
```

Katakanlah Anda telah mengacaukan repository lokal Anda dan Anda hanya ingin me-reset-nya kembali ke commit terakhir Anda.
Maka, Anda dapat menjalankan perintah di bawah ini.
```bash
git reset --hard
```
Perintah ini tidak hanya akan me-reset staging area Anda, tetapi juga mengembalikan semua perubahan pada file-file Anda ke commit terakhir Anda.
Mode ```--hard``` memberitahu Git untuk membatalkan semua perubahan di direktori kerja juga.
Anda hanya boleh menjalankan ini ketika Anda benar-benar yakin ingin membuang seluruh pengembangan lokal Anda.

Contoh penggunaan ```git reset --hard```
```bash
# Memutuskan untuk memulai eksperimen gila
# Membuat file baru 'crazy.php' dan menambahkan beberapa kode ke dalamnya
# Commit crazy.php
$ git add crazy.php
$ git commit -m "Started a crazy dev"
# Mengedit file crazy.php lagi dan mengubah banyak file lain
# Commit semua file yang dilacak
$ git add .
$ git commit -m "Continued dev"
# Setelah diuji, semuanya menjadi kacau
# Memutuskan untuk menghapus semuanya
$ git reset --hard HEAD~2
```
Perintah ```git reset --hard HEAD~2``` memindahkan branch saat ini mundur sebanyak 2 titik commit, pada saat yang sama membatalkan semua perubahan yang telah Anda buat dan menghapus 2 snapshot yang baru saja kita buat dari riwayat (history) proyek.

P.s. Jangan pernah melakukan ```git reset --hard``` jika Anda sudah men-push (mendorong) commit Anda ke repository bersama karena ini akan menyebabkan masalah bagi semua orang di repository tersebut.
