# Keeping your fork synced with this repository

Birinchidan, to'liq sinxronizatsiya oqimini tushunish kerak, bu muhim. Ushbu sxemada 3 xil repo mavjud: Github'dagi ommaviy repoim `github.com/firstcontributions/first-contributions.git`, GitHub'dagi sizning `github.com/Your-Name/first-contributions/` vilkangiz. va siz ishlaydigan mahalliy mashinaning repo -si. Bunday hamkorlik ochiq manbali loyihalar uchun odatiy va `Triangle Workflows` deb nomlanadi.

<img style="float;" src="../../assets/triangle_workflow.png" alt="triangle workflow" />

Ikkala repo-ni ommaviy repo bilan yangilab turish uchun, avvalo, mahalliy mashinaning repo-si bilan ommaviy reponi olib kelishimiz kerak.
Bizning ikkinchi qadamimiz - mahalliy repo -ni GitHub vilkangizga surish. Siz ilgari ko'rganingizdek, faqat vilkangizdan "tortish iltimosini" so'rashingiz mumkin. Shunday qilib, sizning GitHub vilkasi - yangilangan oxirgi repo.

Keling, buni qanday qilishni ko'rib chiqaylik:

Birinchidan, siz o'zingizning ustaxonangizda bo'lishingiz kerak. Qaysi filialda ekanligingizni bilish uchun birinchi qatorni tekshiring:
```
git status
```
Agar hali master branch'ida bo'lmasangiz:
```
git checkout master
```

Keyin mening ommaviy repo -ni git -ga qo'shishingiz kerak `add upstream remote-url`:
```
git remote add upstream https://github.com/firstcontributions/first-contributions.git
```
Bu git -ga ushbu loyihaning boshqa versiyasi ko'rsatilgan urlda mavjudligini aytishning bir usuli va biz uni `upstream` deb ataymiz. Sizning git ismingiz bo'lganidan so'ng, ombor omborining so'nggi versiyasini olaylik:
```
git fetch upstream
```

Siz mening vilkaning so'nggi versiyasini oldingiz (`upstream` remote). Endi siz omborni asosiy filialingizga birlashtirishingiz kerak.
```
git rebase upstream/master
```
Bu yerda siz omborni asosiy filialingiz bilan birlashtirasiz. Mahalliy mashinangizning asosiy filiali hozirda yangilangan. Nihoyat, agar siz asosiy filialingizni vilkangizga sursangiz, GitHub vilkangizda ham o'zgarishlar bo'ladi:
```
git push origin master
```
E'tibor bering, siz nomlangan masofadan boshqarish pultiga o'tmoqdasiz `origin`.

Shunday qilib, hozir yoki hozirda sizning barcha omborlaringiz yangilangan. Juda qoyil! Buni qilish kerak, har safar sizning GitHub repoingiz sizga bir nechta majburiyatlar ortda qolayotganingizni aytadi.
