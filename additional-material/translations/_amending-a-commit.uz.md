# Kommit'ga o'zgartirishlar kiritish

Tasavvur qiling -a, siz masofaviy omborga majburiyat oldingiz, keyin siz topshiriq izohida xatoga yo'l qo'yganingizni angladingiz yoki oxirgi topshiriqqa satr qo'shishni unutdingiz. Bunday vaziyatda nima qilish kerak? Bu hujjat haqida bo'ladi.

## Github'ga jo'natib yuborilganidan (pushed) so'ng, yaqinda qilingan majburiyat haqidagi sharhni qanday o'zgartirish mumkin
Buni faylni tahrir qilish uchun ochmasdan qilish uchun,
*   quyidagilarni kiriting  ```git commit --amend -m "bu yerga yangi izoh matni kiritilishi kerak"```
*   shundan so'ng, Github'ga o'zgartirishlarni kiritish uchun quyidagi ```git push origin <branch-nomi>``` buyrug'ini kiriting. 

Eslatma: Agar faqat ```git commit --amend``` deb kiritinsangiz, matn muharriri ochiladi va kommit uchun izoh kiritishni taklif qiladi. ``-m`` tugmachasini ishlatish matn muharririning ishga tushib ketishining oldini oladi.

## O'zgartirishlarni birgina kommit orqali  kiritish

Agar biz faylga ozgina o'zgartirish kiritishni unutgan bo'lsak -chi, masalan, uzoqdan saqlanadigan omborga o'tkazilgan majburiyatdagi bitta so'zni almashtirish.

Misol uchun, mening majburiyatlar jurnali yozuvlari shunday ko'rinadi:
```
g56123f 'bot file' nomli fayl yaratildi
a2235d  'contributor.md'ga tuzatish kiritildi
a5da0d  'bot file'ga o'zgartirishlar kitildi
```
Aytaylik, 'bot file' kommitida bitta so'zni kiritishni unutib qoldirdim.

Buni tuzatishning ikki yo'li bor. Birinchisi, bu o'zgarishlarni o'z ichiga olgan yangi kommit yaratish, masalan:
```
g56123f 'bot file' nomli fayl yaratildi
a2235d  'contributor.md'ga tuzatish kiritildi
a5da0d  'bot file'ga o'zgartirishlar kitildi
b0ca8f  'bot file'ga bitta so'z kiritildi
```
Ikkinchi usul - a5da0d majburiyatini tuzatish, yo'qolgan so'zni qo'shish va bu o'zgarishlarni Github'ga birgina kommit orqali kiritiladi.
Ikkinchi usul afzalroq deb hisoblanadiladi, chunki o'zgartirishlar juda ham kamdir.

Bunga erishish uchun biz quyidagicha harakat qilamiz:
*   Faylni o'zgartiramiz. Bunday holda, men ilgari o'tkazib yuborgan so'zni qo'shish uchun botfilni o'zgartiraman.
*   Keyinchalik, biz ushbu faylni buyruq yordamida indekslaymiz ```git add <fayl-nomi>```

Odatdagidek, indeksatsiyadan so'ng, biz  majburiyatiga ```git commit -m "kiritiladigan kommit uchun izoh"``` sharhlarini beramiz, to'g'rimi? Ammo bu holda bizning vazifamiz oldingi majburiyatni tuzatish bo'lgani uchun, biz uning o'rniga quyidagi buyruqni bajaramiz:

* ```git commit --amend```
Natijada, matn tahrirlovchisi oynasi ochiladi, unda biz sharhga o'zgartirish kiritish imkoniyatiga egamiz. Biz haqiqatan ham sharhni tahrir qilishimiz yoki uni o'zgarishsiz qoldirishimiz mumkin.
* Tahrirlovchidan chiqamiz.
* Kiritgan o'zgartirishlarimizni ```git push origin <имя-ветки>``` buyrug'i orqali Github'ga jo'natamiz. (push qilamiz).

Shunday qilib, ikkala tuzatish ham bir xil kommit'da bo'lishiga erishladi.
