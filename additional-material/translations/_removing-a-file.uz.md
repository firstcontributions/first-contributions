# GIT boshqaruv tizimidan faylni olib tashlash

Ba'zida faylni GIT boshqaruvidan olib tashlashingiz kerak bo'ladi, lekin uni kompyuteringizga saqlang. Bunga quyidagi buyruq yordamida erishish mumkin:

``git rm <файл> --cached``

## Nima sodir bo'ldi?

GIT endi masofaviy fayldagi o'zgarishlarni kuzatmaydi. GIT nuqtai nazaridan, bu fayl yo'q, lekin agar siz ushbu faylni fayl tizimida lokalizatsiya qilishga urinib ko'rsangiz, u hali ham joyida ekanligini ko'rasiz.

E'tibor bering, yuqoridagi buyruq `--cached`kalitidan foydalanadi. Agar biz bu kalitni qo'shmagan bo'lsak, GIT faylni nafaqat ombordan, balki fayl tizimidan ham yo'q qiladi.

Agar siz git `git commit -m "file1.js faylini o'chirish"` buyrug'ini bajargan bo'lsangiz va uni `git push origin master` buyrug'i bilan uzoqdagi omborga o'tkazsangiz, fayl ham masofaviy ombordan o'chiriladi.

## Дополнительная информация

-  Agar siz bir nechta faylni o'chirmoqchi bo'lsangiz, buni bitta buyruqdagi barcha fayllarni ro'yxatga olish orqali qilishingiz mumkin:

    `git rm file1.js file2.js file3.js --cached`

-   Fayllarni o'xshash nomlar bilan olib tashlash uchun siz (*) naqshidan foydalanishingiz mumkin, masalan, agar .txt fayllarini mahalliy ombordan olib tashlamoqchi bo'lsangiz, quyidagini kiriting: 

    `git rm *.txt --cached`
