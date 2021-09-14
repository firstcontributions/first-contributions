# .gitignore

.gitignore fayli - bu loyihada qaysi fayllar yoki papkalarni e'tiborsiz qoldirishni Gitga bildiradigan matnli fayl.

Mahalliy .gitignore fayli odatda loyihaning bosh katalogiga joylashtiriladi. Shuningdek, global .gitignore faylini ham yaratishingiz mumkin va bu fayldagi barcha yozuvlar barcha Git repozitoriyangizda e'tiborga olinmaydi, ya'ni GitHub'ga jo'natilmaydi (push qilinmaydi).

## Nima uchun .gitignore

Endi nima uchun ba'zi fayllar va papkalar e'tiborsiz qoldirilishi kerak degan savol tug'ilishi tabiiy. Buning sababi, siz qurish fayllari, kesh fayllari, tugun modullari, kompilyatsiya fayllari, IDE yaratadigan vaqtinchalik fayllar va boshqalar kabi boshqa mahalliy konfiguratsiya fayllari git tomonidan kuzatilishini xohlamaysiz. Odatda bu sizning ishchi katalogingizdan boshqa hamkorlar uchun foydali bo'lmagan vaqtinchalik fayllarni o'tkazmaslik uchun ishlatiladi.

## Ishni boshlash uchun

Mahalliy .gitignore faylini yaratish uchun matnli fayl yarating va unga .gitignore deb nom bering (. Boshida qo'shishni unutmang). Keyin kerakli faylni tahrir qiling. Har bir yangi satrda Git e'tibor bermasligi kerak bo'lgan qo'shimcha fayl yoki papka ko'rsatilishi kerak.

Bu fayldagi yozuvlar ham mos keladigan naqshga amal qilishi mumkin.

```
* joker o'yin sifatida ishlatiladi
/ .gitignore fayliga nisbatan yo'l nomlarini e'tiborsiz qoldirish uchun ishlatiladi
# .gitignore fayliga izoh kiritish uchun ishlatiladi.

Bu .gitignore fayli qanday ko'rinishi mumkinligi misoli:

# Mac tizimidagi fayllarni e'tiborsiz qoldirish
.DS_store

# Node_modules katalogini e'tiborsiz qoldirish
node_modules

# Barcha matnli fayllarni e'tiborsiz qoldirish
*.txt

# API kalitlari bilan bog'liq barcha fayllarni e'tiborsiz qoldirish
.env

# SASS konfiguratsiya fayllarini e'tiborsiz qoldirish
.sass-cache

```

Global .gitignore faylini qo'shish yoki o'zgartirish uchun quyidagi buyruqni bajaring:

```
git config --global core.excludesfile ~/.gitignore_global

```

Bu ~/.gitignore_global faylini yaratadi. Endi siz bu faylni mahalliy .gitignore faylidagi kabi tahrir qilishingiz mumkin. Barcha Git omborlari global .gitignore faylida sanab o'tilgan fayl va papkalarni e'tiborsiz qoldiradi.

## Gitignore'da ilgari qilingan fayllarni qanday olib tashlash mumkin

Bitta faylni kuzatib borish uchun, ya'ni faylni kuzatishni to'xtating, lekin uni tizimdan o'chirmang:

```
git rm --cached filename
```

.Gitignore -dagi har bir faylni kuzatib borish uchun:

Birinchidan, har qanday ajoyib kod o'zgarishlarini bajaring va keyin ishga tushiring:

```
git rm -r --cached
```

Bu o'zgartirilgan fayllarni indeksdan (sahnalash maydoni) olib tashlaydi, so'ngra ishga tushiring:

```
git add .
```

Kommit qiling:

```
git commit -m ".gitignore faylini qo'shdim"
```

Bekor qilish qilish uchun `git rm --cached filename` buyrug'idan so'ng, `git add filename` buyrug'ini kiriting.'
