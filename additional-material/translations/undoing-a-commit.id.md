# Membatalkan commit lokal

Yang perlu Anda lakukan untuk membatalkan komit lokal adalah:

```
git reset
```

Perintah ini akan mengatur ulang status antrian ke komit terakhir Anda, tetapi perubahan akan tetap ada di lingkungan kerja. Jika mau, Anda dapat membuat ulang komit dengan perubahan ini.
Alternatifnya, Anda hanya dapat menghapus satu file dari komit sebelumnya. Anda menggunakan perintah:

```
git reset <file>
```

Perintah hanya akan menghapus file tertentu dari antrian, tetapi perubahan yang dibuat pada file akan tetap ada.

Contoh penggunaan `git reset`:

```
# Lakukan perubahan pada index.php dan tutorial.php
# Tambahkan file ke dalam staging area
$ git add .
# Ingatlah bahwa kedua file harus dikomit secara terpisah
# Hapus file dari staging area tutorial.php
$ git reset tutorial.php
# Commit file index.php terlebih dahulu
$ git commit -m "Changed index.php"
# Commit file tutorial.php sekarang
$ git add tutorial.php
$ git commit -m "Changed tutorial.php"
```

Misalkan Anda telah merusak repositori lokal Anda dan ingin mengatur ulang ke komit terakhir Anda.
Anda dapat menggunakan perintah di bawah ini:

```
git reset --hard
```

Perintah tersebut akan mengosongkan antrian dan juga mengembalikan semua perubahan file ke status di komit terakhir.
Pilihan `--hard` memberi tahu Git bahwa dia juga perlu menghapus semua perubahan di lingkungan kerja.
Gunakan perintah ini hanya jika Anda yakin ingin menghapus semua perubahan yang dibuat sejak komit terakhir!

Contoh penggunaan perintah `git reset --hard`:

```
# Memutuskan untuk memulai eksperimen gila
# Buat file baru 'crazy.php' dan tambahkan beberapa kode ke dalamnya
# Commit pada file crazy.php
$ git add crazy.php
$ git commit -m "Started a crazy dev"
# Edit file crazy.php lagi dan ubah banyak file lainnya
# Commit pada semua file
$ git add .
$ git commit -m "Continued dev"
# Uji dan selesaikan
# Memutuskan untuk menghapus semuanya
$ git reset --hard HEAD~2
```

Perintah `git reset --hard HEAD~2` memindahkan cabang saat ini kembali dengan 2 commit dan pada saat yang sama mengembalikan semua perubahan ke titik ini. Dan 2 riwayat commit yang ditambahkan sebelumnya dihapus dari riwayat proyek..

P.s: Jika Anda menjalankan perintah `git reset --hard` saat Anda telah mendorong ke repositori bersama, Anda tidak boleh menjalankannya karena dapat menyebabkan masalah bagi semua orang yang menggunakan repositori!
