# Repozitoriyadan branch'ni olib tashlash uchun

Agar siz qo'llanmani hozirgacha kuzatgan bo'lsangiz, bizning `<add-your-name>` bo'limi o'z maqsadini tugatdi, uni mahalliy kompyuterning reposidan o'chirish vaqti keldi. Bu kerak emas, lekin bu filialning nomi uning o'ziga xos maqsadini ko'rsatadi. Uning umri mos ravishda qisqa bo'lishi mumkin.

Birinchi navbatda, ustaxonangizga `<add-your-name>` ni qo'shamiz, shunda sizning asosiy bo'limingizga o'ting:
```
git checkout master
```

Mahalliy kompyuteringizdagi `<add-your-name>` repozitoriyasini master branch'iga birlashtirish uchun:
```
git merge <add-your-name> master
```

Mahalliy kompyuteringizdagi repozitoriyadan `<add-your-name>` brach'ini o'chirib tashlash uchun:
```
git branch -d <add-your-name>
```

Hozir mahalliy mashinangizning `<add-your-name>` bo'limini o'chirib tashladingiz va hamma narsa toza va tartibli ko'rinishga keldi.
GitHub vilkasida siz hali ham `<add-your-name>`bo'limiga ega bo'lishingiz kerak. Ammo, buni o'chirishdan oldin, esda tutingki, siz mening uzoqdagi filialimdan "repo so'rovini" yuborgansiz. Agar men uni birlashtirmagan bo'lsam, bu filialni o'chirmang.

Ammo, agar men sizning filialingizni birlashtirgan bo'lsam va siz uzoqdagi filialni o'chirmoqchi bo'lsangiz, quyidagilarni ishlating:
```
git push origin --delete <add-your-name>
```

Now, you know how to tidy your branches.
With time, many commits will be added to my public repo. And the master branches of your local machine and of your GitHub fork won't be up-to-date. So in order to keep your repositories synchronized with mine, follow the steps below.

#### [Vilkani ombor bilan sinxronlashtirish](keeping-your-fork-synced-with-this-repository.md)
