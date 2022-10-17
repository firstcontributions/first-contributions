# Memindahkan komit ke cabang yang berbeda
Bagaimana jika Anda melakukan perubahan, dan kemudian sadar bahwa Anda komit ke cabang yang berbeda?
Bagaimana Anda mau mengubah itu? Inilah yang dicakup oleh tutorial ini.

## Memindahkan komit terbaru ke cabang yang ada
Untuk melakukannya, ketik:

```git reset HEAD~ --soft``` - Membatalkan komit terakhir, tetapi membiarkan perubahan tetap ada.  
```git stash``` - Merekam status direktori.  

```git checkout name-of-the-correct-branch``` - Beralih ke cabang lain.
```git stash pop``` - Menghapus status simpanan terbaru.
```git add .``` - Atau coba tambahkan file individual.
```git commit -m "your message here"``` - Menyimpan dan komit perubahan.

Sekarang perubahan Anda ada di cabang yang benar


### Memindahkan komit terbaru ke Cabang baru
Untuk melakukannya, ketik:  
```git branch newbranch``` -  Membuat Cabang baru. Menyimpan semua Komit. 
```git reset --hard HEAD~#``` - Pindahkan master kembali dengan # komit. Ingat, komit ini akan hilang dari master
```git checkout newbranch``` - Pergi ke cabang yang Anda buat. Itu akan memiliki semua komit. 

Ingat: Setiap perubahan yang tidak dilakukan akan HILANG.
