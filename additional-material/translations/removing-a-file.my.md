# Mengalih keluar fail dari Git

Kadangkala, kamu mungkin mahu mengeluarkan fail dari Git tetapi tidak mahu memadamkannya dari komputer kamu. Kamu boleh mencapai ini dengan menggunakan arahan berikut:

``git rm <file> --cached``

## Jadi apa yang berlaku?

Git tidak lagi akan menjejaki perubahan dalam fail yang dibuang. Sejauh yang diketahui oleh Git, seolah-olah anda telah memadam fail itu. Jika kamu mencari fail dalam sistem fail kamu, kamu akan melihat bahawa ia masih ada.

Perhatikan bahawa dalam contoh di atas, bendera `--cached` digunakan. Jika kami tidak menambah bendera ini, Git akan mengeluarkan failnya bukan hanya dari repo, tetapi juga dari sistem fail kamu.

Jika kamu melakukan perubahan dengan `git commit -m "Alih keluar file1.js"` dan menghantar ke repositori jauh menggunakan `git push origin master ', repository jauh akan mengeluarkan fail tersebut.
## Ciri-ciri tambahan

-  Sekiranya kamu mahu mengeluarkan lebih daripada satu fail, kamu boleh memasukkan kesemuanya dalam arahan yang sama:

    `git rm file1.js file2.js file3.js --cached`

-   Kamu boleh menggunakan wildcard (*) untuk mengalih keluar fail yang serupa. Sebagai contoh, jika anda ingin mengalih keluar semua fail .txt dari repositori setempat kamu:

    `git rm *.txt --cached`
