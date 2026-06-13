# Mengubah Commit (Amending a Commit)

Bagaimana jika Anda melakukan commit perubahan ke remote repository Anda namun kemudian menyadari bahwa ada kesalahan ketik (typo) pada pesan commit atau Anda lupa menambahkan satu baris kode pada commit terakhir Anda?
Bagaimana cara mengubahnya? Inilah yang dibahas dalam tutorial ini.

## Mengubah pesan commit terakhir setelah melakukan push ke Github

Untuk melakukan ini tanpa membuka file:
*   Ketik ```git commit --amend -m "diikuti dengan pesan commit baru Anda"```
*   Jalankan ```git push origin <nama-branch>``` untuk melakukan commit perubahan tersebut ke repository.

Catatan: Jika Anda hanya mengetikkan ```git commit --amend```, teks editor Anda akan terbuka dan meminta Anda untuk mengedit pesan commit.
Menambahkan flag ``-m`` mencegah hal tersebut.

## Memodifikasi satu commit

Lalu, bagaimana jika kita lupa membuat perubahan kecil pada suatu file seperti mengubah satu kata dan kita sudah terlanjur melakukan push commit tersebut ke remote repository kita?

Sebagai ilustrasi, berikut adalah riwayat (log) commit saya:
```
g56123f create file bot file
a2235d updated contributor.md
a5da0d modified bot file
```
Katakanlah saya lupa menambahkan satu kata ke file `bot file`

Ada 2 cara untuk mengatasi hal ini. Cara pertama adalah dengan membuat commit yang sepenuhnya baru yang berisi perubahan tersebut seperti ini:
```
g56123f create file botfile
a2235d updated contributor.md
a5da0d modified botfile
b0ca8f added single word to botfile
```
Cara kedua adalah dengan mengubah (amend) commit `a5da0d`, menambahkan kata baru tersebut, dan melakukan push ke Github sebagai satu commit.
Cara kedua terdengar lebih baik karena ini hanyalah perubahan kecil.

Untuk mencapai hal ini, kita akan melakukan langkah-langkah berikut:
*   Modifikasi file tersebut. Dalam kasus ini, saya akan memodifikasi `botfile` untuk memasukkan kata yang sebelumnya saya lewatkan.
*   Selanjutnya, tambahkan file tersebut ke staging area dengan ```git add <namafile>```

Biasanya setelah menambahkan file ke staging area, hal selanjutnya yang kita lakukan adalah `git commit -m "pesan commit kita"`, bukan?
Namun karena yang ingin kita capai di sini adalah mengubah (amend) commit sebelumnya, kita akan menjalankan:

* ```git commit --amend```
 Ini kemudian akan memunculkan teks editor dan meminta Anda untuk mengedit pesannya. Anda dapat memutuskan untuk membiarkan pesan tersebut seperti sebelumnya atau mengubahnya.
* Keluar dari editor
* Push perubahan Anda dengan ```git push origin <nama-branch>```

Dengan cara tersebut, kedua perubahan akan berada dalam satu commit yang sama.

## Memodifikasi commit pada remote repository

Jika commit yang ingin Anda ubah sudah di-push ke remote, mengubah commit ini akan menyebabkan riwayat (history) lokal Anda berbeda dari remote (karena pada dasarnya Anda membuat commit baru dan menggantikan yang diubah). Karena Anda ingin mengubah commit pada remote, Anda perlu menimpa riwayat remote pada branch Anda. Untuk mencapainya, ikuti prosedur yang sama seperti yang dijelaskan di atas, tetapi gunakan *force push* saat melakukan push commit Anda ke remote.

> **Peringatan**  
> Melakukan *force push* ke remote akan menimpa (dan membuang) perubahan pada remote dan hanya menyimpan commit yang Anda push. Perubahan pada remote, yang mungkin dilakukan oleh anggota tim lain sementara itu, akan tertimpa juga.

Inilah cara Anda memodifikasi commit terbaru pada remote:

```bash
git add <file-yang-anda-ubah>
git commit --amend -m "diikuti dengan pesan commit baru Anda"
git push --force
```

> Menggunakan `--force-with-lease` adalah pilihan yang lebih aman daripada `--force` yang dapat menghindari tertimpanya perubahan dari orang lain di remote branch (jika Anda memang tidak bermaksud melakukannya).
