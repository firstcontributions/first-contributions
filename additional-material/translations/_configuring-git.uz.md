# GIT'ni sozlash

Siz birinchi marta harakat qilmoqchi bo'lganingizda, siz shunday xabarni ko'rishingiz mumkin:

```bash
$ git commit
*** Please tell me who you are. [Iltimos, kimligingizni ayting.]

Quyidagi buyruqlarni bajaring:

git config --global user.email "you@example.com"
git config --global user.name "Your Name"

ushbu hisob uchun standart foydalanuvchini aniqlash.
Agar foydalanuvchini faqat shu ombor uchun kŏrsatmoqchi bŏlsangiz -global kalitini ŏtkazib yubormang.  
```

Majburiyat yaratish uchun GIT muallif kimligini bilishi kerak. Birgalikda ishlayotganda, siz loyihaning ayrim qismlari kim tomonidan va qachon o'zgartirilganligini bilishingiz kerak, shuning uchun GIT har bir majburiyat foydalanuvchining ismi va elektron pochta manzili bilan bog'liqligini ta'minlaydi.

Sizning elektron pochta manzilingiz va ismingiz bilan `git commit` buyrug'ini bog'lashning bir necha yo'li mavjud va biz ulardan ba'zilarini bu erda sanab o'tamiz.

### Global konfiguratsiya

Global konfiguratsiya qismi sifatida saqlangan ma'lumotlar butun tizim uchun amal qiladi, ya'ni. siz ishlaydigan barcha repolarga. Bu afzal qilingan usul va ko'p hollarda foydalanish uchun javob beradi.     

Ma'lumotni global konfiguratsiyada saqlash uchun quyidagi formatda `config` buyrug'idan foydalaning:

`$ git config --global <o'zgaruvchi nomi> <o'zgaruvchi qiymati>`

Foydalanuvchi ma'lumotlariga qo'llanilganda biz quyidagi buyruqlarni bajaramiz:

```
$ git config --global user.email "pochtamanzilingiz@example.com"
$ git config --global user.name "Sizning ismingiz"
```

### Repozitoriya konfiguratsiyasi

Sarlavhadan ko'rinib turibdiki, bunday konfiguratsiya ma'lum bir omborda ishlaydi. Agar siz ma'lum bir omborga, masalan, sizning kompaniyangizning elektron pochtasidan foydalangan holda o'z biznesingizga tegishli loyihani o'z ichiga olmoqchi bo'lsangiz, siz ushbu konfiguratsiya usulidan foydalanishingiz mumkin.

Konfiguratsiyani ombor darajasida o'zgartirish uchun  `config`  buyrug'idagi `--global`kalitini quyidagicha qoldiring:

`$ git config <o'zgaruvchi nomi> <o'zgaruvchi qiymati>`

Foydalanuvchi ma'lumotlariga nisbatan quyidagicha ko'rinadi:

```
$ git config user.email "boshqapochtamanzilingiz@alternate.com"
$ git config user.name "Sizning ismingiz"
```

### Buyruqlar qatori konfiguratsiyasi

Ushbu konfiguratsiya usuli faqat shu buyruq uchun amal qiladi. Barcha GIT buyruqlari konfiguratsiya parametrlarini vaqtincha o'rnatish uchun buyruqni aniqlaydigan fe'ldan oldin `-c` kalitidan foydalanishga ruxsat beradi.

Faqatgina ushbu buyruq uchun qo'llaniladigan konfiguratsiya parametrlarini o'zgartirish uchun quyidagi GIT buyruq formatidan foydalaning:

`$ git -c <ŏzgaruvchi-1>=<ŏzgaruvchi-qiymati-1> -c <ŏzgaruvchi-2>=<ŏzgaruvchi-qiymati-2> <buyruq>`

Bizning holatlarimizda, buyruq buyrug'i quyidagicha bo'ladi:

`git -c user.name='Sizning ismingiz' -c user.email='pochtangiz@example.com' commit -m "Kommit uchun izohingiz"`

### Ustuvorlik haqida eslatma

Yuqorida sanab ŏtilgan uchta konfiguratsiya buyruğining ustunlik tartibi `buyruqlar qatori konfiguratsiyasi > repozitoriya konfiguratsiyasi > global konfiguratsiya` deb ta'riflanadi. Bu shuni anglatadiki, agar global konfiguratsiyada ham, buyruq satrida ham har qanday o'zgaruvchi aniqlansa, buyruq satrida berilgan qiymat ishlatiladi.

## Faqat foydalanuvchi ma'lumotlari emas

Hozircha biz GIT konfiguratsiyasini muhokama qilishda faqat foydalanuvchi ma'lumotlari haqida gaplashdik. Biroq, GIT sizga yana bir nechta parametrlarni sozlash imkonini beradi. Mana ulardan ba'zilari:

1.  `core.editor` - tahrir qilinadigan tahrirlovchining nomini, majburiyat uchun sharhni va boshqalarni belgilaydi,
2.  `commit.template` - kommit uchun dastlabki shablonni o'z ichiga olgan faylni bildiradi, 
3.  `color.ui` - GIT terminalidagi xabarlarda rangli shriftlardan foydalanish kerakligini ko'rsatuvchi boolean o'zgaruvchi.

Oddiylik uchun biz ba'zi tafsilotlarni ŏtkazib yubordik. Batafsil ma'lumot uchun quyidagi havolaga ŏting:  [git-scm.com](https://git-scm.com/book/ru/v1/Введение-Первоначальная-настройка-Git).