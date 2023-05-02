# Menghapus file

Terkadang Anda ingin menghapus file dari Git, tetapi Anda tidak ingin menghapusnya dari komputer Anda. Anda dapat melakukan ini dengan menggunakan perintah berikut:

`git rm <file> --cached`

## Apa yang terjadi?

Git tidak akan lagi melacak perubahan pada file yang dihapus. Adapun Git, file ini sudah tidak ada lagi. Jika Anda mencari file di disk Anda, Anda melihat bahwa file itu masih ada.

Pada contoh di atas, kita menggunakan flag `--cached`. Jika kita tidak menggunakannya, Git juga akan menghapus file dari disk kita.

Jika sekarang kita membuat komit dengan `git commit -m "Hapus file1.js"` dan kirimkan ke repositori jarak jauh dengan perintah `git push origin master`, file tersebut juga akan dihapus dari repositori jarak jauh.

## Opsi tambahan

- Jika Anda ingin menghapus banyak file, Anda dapat memasukkan semuanya dalam satu perintah:

  `git rm file1.js file2.js file3.js --cached`

- Anda dapat menggunakan wildcard (\*) untuk menghapus file serupa. Misalnya, untuk menghapus semua file .txt dari repositori Anda, gunakan perintah:

  `git rm *.txt --cached`
