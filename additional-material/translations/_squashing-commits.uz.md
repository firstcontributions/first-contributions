# Kommit'larni o'zaro siqish nima?

Git -da, squashing sizning qilgan ishlaringiz tarixini qayta yozishni anglatadi, shuning uchun siz bajarilgan o'zgarishlarning tavsifi bilan bitta majburiyat bilan yakunlanasiz.
Bu odatda ochiq manbali loyihalarda amalga oshiriladi, chunki ochiq manbali loyihalardagi filialning ko'p tarixi faqat uni yaratgan ishlab chiqaruvchiga tegishli va bu kiritilgan o'zgarishlarni tasvirlashning oddiy usulini va kerak bo'lganda ularni qaytarishni ta'minlaydi.

# Qanday qilib o'zingizni majbur qilasiz?

Birinchidan, joriy filialingizda birlashtirmoqchi bo'lgan majburiyatlarni ko'rib chiqish uchun git jurnalini bajaring.

```
git log
```

Siz bir qator kommit'larni ko'rishingiz mumkin:

```
commit blablabla
Author: bekroz
Date:   10/10/20
    Commit message 1

commit blablabla2
Author: bekroz
Date:   10/10/20
    Commit message 2
```

Shunday qilib, endi siz birlashmoqchi bo'lgan majburiyatlarni ko'rsangiz, biz buni ```git rebase``` bilan davom ettira olamiz. Agar siz allaqachon ```git rebase``` bilan tanish bo'lsangiz, biz git rebase interaktiv rejimida o'z vazifalarini bajarishni boshlashimiz mumkin:

```
git rebase -i
```

Endi, interaktiv qayta hisoblash bilan siz qancha orqaga ketishni xohlayotganingizning boshlanishi va tugash nuqtasini belgilashingiz mumkin:

```
git rebase -i HEAD~2
```

Ushbu buyruqni bajarish sizga quyidagilarni ko'rsatadi:

```
pick blablabla Changing test01.txt file
pick blablabla2 Adding dummy01.txt file

#
# Commands:
#  p, pick = kommit'dan foydalanish
#  r, reword = majburiyatdan foydalaning, lekin majburiyat xabarini tahrir qiling
#  e, edit = kommit'dan foydalanish, lekin o'zgartirish uchun to'xtatish uchun.
#  s, squash = kommit'dan foydalanish, lekin oldingi kommit'ga qo'shiling
#  f, fixup = "squash" kabi, lekin bu majburiyatning jurnal xabarini bekor qiling
#  x, exec = qobiq yordamida buyruqni (qatorning qolgan qismini) ishga tushiring
#
# Bu qatorlarni qayta buyurtma qilish mumkin; ular yuqoridan pastgacha bajariladi.
#
# Agar bu yerdagi qatorni olib tashlasangiz, BU KOMMIT BUTUNLAY YO'QOLADI.
#
# Ammo, agar hamma narsani olib tashlasangiz, qayta tiklash bekor qilinadi.
#
# E'tibor bering, bo'sh kommitlarga izoh berib o'tilgan.
```

Agar siz ```blablabla2``` ni ```blablablabla``` ga aylantirmoqchi bo'lsangiz, quyidagilarni o'zgartirasiz:

```
pick blablabla Changing test01.txt file
squash blablabla2 Adding dummy01.txt file

```

Agar hammasi ko'ngildagidek bo'lsa, quyidagi natija xabari aks etadi:

```
# This is a combination of 2 commits.
# The first commit's message is:
commit message 1

# This is the 2nd commit message:

commit message 2
```

Bu o'zgarishlarni saqlash uchun muharrirdan chiqishga qaror qilishdan oldin, siz erkin o'zgarishingiz mumkin.

Git jurnalini qayta ishga tushirish ekranda chiqishdan oldin kiritgan majburiyat xabarini ko'rsatishi kerak.
