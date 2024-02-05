# Mengatur Ulang Sebuah commit

`reset` adalah perintah yang dapat digunakan ketika kita ingin memindahkan repositori kembali ke commit sebelumnya, membuang semua perubahan yang dibuat setelah commit tersebut.<br/>
Perbedaan utama antara mengatur ulang dan mengembalikan commit adalah bahwa git reset `unstages a file and bring our changes back to the working directory`
dan git revert `removes the commits from the remote repository`. <br/>

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
