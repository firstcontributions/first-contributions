# Batalkan komit tempatan

Untuk membatalkan komit setempat, semua yang anda perlu lakukan ialah
```
git reset
```

Perintah ini akan menetapkan semula kawasan pementasan kamu kepada komit terbaru kamu, tetapi perubahan yang kamu buat ke direktori kerja kamu tidak akan berubah. Jadi, kamu masih boleh membuat semula apa yang telah kamu ubah.
Atau, jika kamu hanya mahu mengeluarkan satu fail dari komit kamu sebelum ini. Kemudian, kamu boleh melakukan arahan di bawah
```
git reset <file>
```
Arahan tersebut akan memadam hanya fail yang ditentukan dari kawasan pementasan, tetapi perubahan yang dibuat pada fail masih tetap.

Example of ```git reset``` usage
```
# Make changes in index.php and tutorial.php
# Add files into the staging area
$ git add .
# Remembered both files need to be committed separately
# Unstage tutorial.php
$ git reset tutorial.php
# Commit index.php first
$ git commit -m "Changed index.php"
# Commit tutorial.php now
$ git add tutorial.php
$ git commit -m "Changed tutorial.php"
```

Katakan jika kamu telah merosakkan repositori tempatan kamu dan anda hanya mahu menetapkannya semula kepada komit terakhir anda.
Kemudian, anda boleh menjalankan arahan di bawah.
```
git reset --hard
```
Perintah itu bukan sahaja menetapkan semula kawasan pementasan anda, tetapi juga memulihkan semua perubahan pada fail ke komit terakhir anda.
Mod ```--hard``` memberitahu Git untuk membatalkan semua perubahan dalam direktori kerja juga.
Anda hanya harus menggunakan ini apabila anda benar-benar pasti membuang seluruh pembangunan tempatan anda.

Example of ```git reset --hard``` usage
```
# Decided to start a crazy experiment
# Create a new file 'crazy.php' and add some code to it
# Commit crazy.php
$ git add crazy.php
$ git commit -m "Started a crazy dev"
# Edit crazy.php file again and changed a lot other files
# Commit all tracked files
$ git add .
$ git commit -m "Continued dev"
# Tested and things went out of hand
# Decided to remove the whole things
$ git reset --hard HEAD~2

```Reset git - HEAD HEAD~2``` menggerakkan cawangan semasa mundur oleh komit dalam masa yang sama membalikkan semua perubahan yang telah kamu buat dan mengeluarkan 2 snapshot yang baru saja kami buat dari sejarah projek.
P.S Jangan sekali-kali menggunakan ```git reset --hard``` jika anda telah menolak komit anda ke repositori yang dikongsi kerana ia akan menyebabkan masalah kepada semua orang di repositori itu.
