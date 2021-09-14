# Kommit'ni ortga qaytarish

Majburiyatni qaytarish shunchaki hamma narsani bekor qiladigan yangi majburiyatni yaratishni anglatadi
avvalgisiga kiritilgan o'zgarishlar. Git -da ```CTRL + Z ``` ni bajarishga o'xshaydi.

Qaytish jarayoni osonlashadi, chunki masofaviy omborga o'tkaziladigan har bir majburiyat SHA (Secure Hash Algorithm) deb nomlangan noyob alfasayısal kalitga ega.
Bu shuni anglatadiki, agar sizda SHA bo'lsa, har qanday majburiyatni qaytarishingiz mumkin.
Ammo keyin, siz omborni chalkashtirib yubormaslik uchun tartibni teskari o'zgartirishga ehtiyot bo'lishingiz kerak.


Biz bekor qilmoqchi bo'lgan aniq majburiyatning SHA -ni tanlash uchun, hozirgacha qilgan barcha majburiyatlarimiz jurnali yordam beradi.
Buni olish uchun biz buyruqni bajaramiz:
```git log --oneline ```
Faqat ```git log``` buyrug'ini bajarish bizga SHA -larni ham beradi (uzun shaklda)
Biroq, ```--oneline ``` bayrog'i yordamida biz o'qishni osonlashtirish uchun uni qisqacha (bitta satrda) ko'rsatishni xohlayotganimizni bildiramiz.

Ushbu buyruqni bajarganingizda ko'rsatiladigan birinchi 7 ta belgiga qisqartirilgan majburlash xeshi deyiladi.

Masalan, ```git log --oneline ``` buyrug'ini kiritganimda, quyidagilar ekranda ko'rinadi.
```
389004d sarlavha yozuvida bo'sh joy qo'shildi
c1b9fc1 'master'ni tutorials branch'iga birlashtirish
77eaafd kommitni qaytarish bo'yicha qo'llanma qo'shildi
```

Bu shuni ko'rsatadiki, ```git log --oneline``` yordamida biz SHA ning dastlabki 7 ta belgisi bilan birgalikda omborda qilingan barcha majburiyatlar ro'yxatini olishimiz mumkin.

Keling, men "sarlavhaga bo'sh joy qo'shish" majburiyatini bekor qilmoqchiman, deb o'ylayman, bu erda men bajaradigan qadamlar:

*   Kommit'dagi SHA'dan nusxa oling, bizning holatda bu: ```389004d```
*   Shundan so'ng, ```git revert 389004d``` buyru'ini kiriting.

Bu matn tahrirlovchisini ochadi va xabarni tahrir qilishimni so'raydi.
Siz `Revert` so'zi bilan boshlangan xabarni standart xabar sifatida qoldirishga qaror qilishingiz mumkin
yoki siz ham o'z xohishingizga ko'ra xabarni sozlashga qaror qilishingiz mumkin.

*   Shundan so'ng, o'zgarishlarni saqlaymiz va matn muharriri oynasini yopamiz.
*   Buyruqlar qatoriga qayting.
*   Quyidagi ```git push origin <branch-name>``` buyrug'ini qaytarilgan o'zgarishlarni GitHub'ga yuklash uchun kiriting.

Va bu shunday, o'zgarish bekor qilinadi. Bunday holda, mening omborim qanday ko'rinishga qaytadi ```c1b9fc1```
