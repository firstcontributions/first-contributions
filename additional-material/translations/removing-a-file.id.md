# Menghapus file dari Git

Terkadang, kamu mau menghapus sebuah file dari Git tanpa menghapusnya dari komputermu. Kamu dapat melakukannya dengan menggunakan perintah berikut:

``git rm <file> --cached``

## Apa yang terjadi ?

Git tidak akan lagi melacak perubahan pada file yang telah di hapus. Sejauh yang Git tau, seolah-olah kamu sudah menghapus file tersebut. Jika kamu ingin mengetahui lokasi file tersebut di sistem file kamu, kamu akan menyadari bahwa file tersebut masih ada disana.

Perhatikan pada contoh diatas, opsi `--cached` digunakan. Jika kamu tidak menambahkan opsi ini, Git akan menghapus file tersebut, tidak hanya pada repository kamu, tapi file yang berada di sistem file kamu juga akan terhapus.

Jika kamu melakukan commit perubahan dengan `git commit -m "Remove file1.js"` dan melakukan push ke remote repository menggunakan `git push origin master`, remote repository akan menghapus filenya.

## Fitur tambahan

- Jika kamu mau menghapus lebih dari satu file, kamu dapat menggabungkan semua file tersebut dalam satu perintah:

    `git rm file1.js file2.js file3.js --cached`

- Kamu dapat menggunakan sebuah wildcard (*) untuk menghapus file yang mirip. Contohnya, jika kamu ingin menghapus semua file .txt dari local repository:

    `git rm *.txt --cached`
