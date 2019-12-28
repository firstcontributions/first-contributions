# Membuat perubahan kecil (Amend) sebuah Commit

Bayangkan saat anda commit sebuah perubahan ke repositori remote dan kemudian menyadari bahwa anda memiliki typo di pesan commit atau anda lupa untuk menambah sebuah baris di commit terbaru anda.
Bagaimana cara anda mengeditnya ? Ini yang akan dibahas oleh tutorial ini. 

## Mengubah sebuah pesan commit paling baru setelah anda mengunggahnya ke Github 
Untuk melakukan ini tanpa membuka sebuah file:
*   Ketikkan ```git commit --amend -m "diikuti oleh pesan commit yang baru"```
*   Jalankan ```git push origin <branch-name>``` untuk meng-commit perubahan ke repositori.

Note: Jika anda hanya mengetikkan ```git commit --amend```, editor teks anda akan terbuka dan mempersilakan anda untuk mengedit pesan commit.
Menambahkan opsi ``-m`` akan mencegah hal tersebut.

# Memodifikasi sebuah Commit

Jadi, bagaimana jika kita lupa untuk membuat perubahan kecil pada sebuah file seperti mengubah sebuah kata dan kita sudah mengunggah commit tersebut ke repositori remote kita ?

Untuk memberi ilustrasi, berikut log dari commit saya:
```
g56123f membuat file bot file
a2235d memperbarui contributor.md
a5da0d memodifikasi bot file
```
Mari kita katakan saya lupa untuk menambah satu kata ke dalam bot file

Ada 2 cara untuk mengubahnya. Yang pertama adalah membuat sebuah commit yang baru yang berisi perubahan yang diperlukan seperti:
```
g56123f membuat file bot file
a2235d memperbarui contributor.md
a5da0d memodifikasi bot file
b0ca8f menambah satu kata ke botfile
```
Cara kedua adalah dengan membuat perubahan kecil (amend) pada commit a5da0d, menambah satu kata dan mengunggahnya ke Github sebagai sebuah commit yang sama.
Cara kedua terdengar lebih baik karena kita hanya melakukan perubahan kecil / minor. 

Untuk melakukan hal ini, kita akan melakukan hal berikut:
*   Modifikasi file yang perlu diubah. Dalam kasus ini, saya akan mengubah file untuk memasukkan kata yang tidak ada sebelumnya.
*   Kemudian, tambahkan file ke area staging dengan ```git add <filename>```

Biasanya setelah menambahkan file ke area staging, yang akan kita lakukan setelahnya adalah git commit -m "our commit message" kan ? Tapi karena yang akan kita lakukan adalah memperbaiki commit sebelumnya, kita akan menjalankan 

* ```git commit --amend```
 Ini akan membuka editor teks yang akan mempersilakan anda untuk mengubah pesan commit. Anda dapat memilih untuk membiarkan pesan tersebut apa adanya atau mengubahnya.
* Keluar dari editor
* Unggah perubahan yang anda lakukan dengan ```git push origin <branch-name>```

Dengan cara ini, dua perubahan akan dijadikan sebagai satu commit.
