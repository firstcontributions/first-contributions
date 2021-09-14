# Mahalliy kommit'larni bekor qilish

Mahalliy kommit'ni bekor qilish uchun siz faqat qilishingiz kerak
```
git reset
```
Bu buyruq sizning sahna maydonini oxirgi bajarilgan vazifangizga qaytaradi, lekin ishchi katalogingizga kiritgan o'zgarishlar o'zgarmaydi. Shunday qilib, siz o'zgartirgan narsangizni yana bajarishingiz mumkin.
Yoki, agar siz oldingi majburiyatingizdan faqat bitta faylni olib tashlamoqchi bo'lsangiz. Keyin quyidagi buyruqni bajarishingiz mumkin
```
git reset <file>
```
Buyruq faqat belgilangan faylni sahna maydonidan olib tashlaydi, lekin faylga kiritilgan o'zgartirishlar saqlanib qoladi.

Quyida ```git reset``` buyrug'idan foydalanishga oid misol berilgan:
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

Aytaylik, agar siz mahalliy omborni buzgan bo'lsangiz va uni oxirgi majburiyatingizga qaytarishni xohlasangiz.
Keyin quyidagi buyruqni bajarishingiz mumkin.
```
git reset --hard
```
Buyruq nafaqat sizning sahna maydonini qayta o'rnatibgina qolmay, balki fayllardagi barcha o'zgarishlarni oxirgi bajarishga qaytaradi.
```--hard``` rejimi Gitga ishchi katalogdagi barcha o'zgarishlarni bekor qilishni aytadi.
Siz buni butun mahalliy rivojlanishingizni tashlab yuborganingizga ishonchingiz komil bo'lganda bajarishingiz kerak.

Quyida ```git reset --hard``` buyrug'idan foydalanishga oid misol berilgan:
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
```
```git reset --hard HEAD~2```  joriy filialni 2 ta majburiy punktga orqaga siljitadi, shu bilan birga siz kiritgan barcha o'zgarishlarni qaytaradi va biz yaratgan 2 ta rasmni loyiha tarixidan o'chirib tashlaydi.

P.s. Hech qachon ```git reset --hard``` ni bajarmang, agar siz o'z majburiyatlaringizni umumiy omborga o'tkazgan bo'lsangiz, chunki bu omborda hamma uchun muammo tug'diradi.
