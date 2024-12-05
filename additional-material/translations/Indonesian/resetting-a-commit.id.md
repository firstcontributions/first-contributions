# Mengatur Ulang Sebuah commit

`git reset` adalah perintah yang dapat digunakan ketika kita ingin memindahkan repositori kembali ke _commit_ sebelumnya, membuang semua perubahan yang dibuat setelah _commit_ tersebut.<br/>

Perbedaan utama antara mengatur ulang dan mengembalikan _commit_ adalah bahwa `git reset` menghapus tahapan berkas dan membawa perubahan Anda ke direktori kerja
dan `git revert` menghapus _commit_ dari repositori remote.<br/>

`git reset` dapat dicapai dengan menggunakan perintah berikut:

- Perintah berikut ini akan memberikan ringkasan dari semua commit dengan menggunakan dua parameter berikut:

  - Tujuh karakter pertama dari commit hash - inilah yang perlu kita rujuk dalam perintah **reset**.
  - Pesan commit

  ```
  git log --oneline
  ```

- Seseorang dapat mengatur ulang repositori kembali ke commit tertentu menggunakan perintah berikut: <br />
  `git reset commithash`
  di mana commithash adalah 7 karakter pertama dari hash commit yang kami temukan di log
