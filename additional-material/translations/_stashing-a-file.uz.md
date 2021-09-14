# Muzlatish (stashing)

Agar siz katta kod ustida ishlayotgan bo'lsangiz va kutilmaganda siz hozirda ishlayotgan filialni boshqa filialga o'tkazishingiz kerak bo'lsa. Kod to'liq emas va hech qanday sinovsiz, ehtimol siz uni bajarishni xohlamaysiz. Ammo siz o'zgarishsiz boshqa filialga o'tolmaysiz, Git sizga bu oqimni buzishga ruxsat bermaydi. Keyin nima qilamiz? Shoxlardan sakrashga qodir bo'lgan holda, keraksiz majburiyatni qanday oldini olamiz? Bu darslik nimani qamrab oladi.

## Ishlarni muzlatib qo'yish

Aytaylik, siz ba'zi fayllarni o'zgartirgan loyihaning filialida ishlayapsiz. Agar siz ```git status``` ni ishlatsangiz, fayllardagi o'zgarishlarni ko'rishingiz mumkin.

```
$ git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#      modified:   index.html
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#
#      modified:   lib/simplegit.rb
#
```

Endi siz o'z filialingizni o'zgartirmoqchisiz, lekin hali o'zgarishlarni xohlamaysiz; shuning uchun siz o'zgarishlarni saqlaysiz.
Stack -ga yangi zaxirani kiritish uchun ushbu  ```git stash``` buyrug'ini kiriting:

```
$ git stash
Saved working directory and index state \
  "WIP on master: 049d078 added the index file"
HEAD is now at 049d078 added the index file
(To restore them type "git stash apply")
```

Endi sizning ishchi katalogingiz toza,```git status``` buyrug'idan foydalaning:

```
$ git status
# On branch master
nothing to commit, working directory clean
```

Endi siz istalgan filialga o'tishingiz va o'z ishingizni qilishingiz mumkin; sizning saqlangan o'zgarishlar to'plam shaklida saqlanadi. Qaysi omborlarda saqlanganligini ko'rish uchun ```git stash list``` buyrug'idan foydalanishingiz mumkin:

```
$ git stash list
stash@{0}: WIP on master: 049d078 added the index file
stash@{1}: WIP on master: c264051 Revert "added file_size"
stash@{2}: WIP on master: 21d80a5 added number to log
```

Agar siz saqlagan o'zgarishlarni qayta qo'llamoqchi bo'lsangiz, ```git stash apply``` buyrug'idan foydalanishingiz mumkin. Ushbu buyruq yordamida siz oxirgi saqlangan faylni qayta qo'llashingiz mumkin. Boshqa faylni qayta qo'llash uchun uni shunday nomlash orqali belgilashingiz mumkin: ```git stash apply <stash-name>```, ```<stash-name>``` o'rniga pulni qayta topshirishingiz kerak.

```
$ git stash apply
# On branch master
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#
#      modified:   index.html
#      modified:   lib/simplegit.rb
#
```

Siz ko'rishingiz mumkinki, git zaxirani saqlaganingizda bajarilmagan faylni qayta o'zgartiradi. Bunday holda, siz zaxirani qo'llaganingizda toza ishchi katalogga ega bo'ldingiz va siz uni saqlagan o'sha filialga qo'llashga harakat qildingiz; zaxirani muvaffaqiyatli qo'llash uchun toza ishchi katalogga ega bo'lish va uni o'sha filialda qo'llash shart emas. Siz zaxirani bitta filialga saqlashingiz, keyin boshqa filialga o'tishingiz va yangi filialdagi o'zgarishlarni qayta qo'llashingiz mumkin. Agar siz zaxirani qo'llaganingizda, ishchi katalogingizda o'zgartirilgan va bajarilmagan fayllarga ega bo'lishingiz mumkin, agar biror narsa endi to'g'ri qo'llanilmasa, git birlashma ziddiyatlarini beradi.

Fayllaringizga kiritilgan o'zgartirishlar qayta qo'llaniladi, lekin siz o'rnatgan fayl qayta tiklanmagan. Buni amalga oshirish uchun ```git stash apply``` with a ```--index``` bilan ishga tushirish kerak, bu buyruqni bosqichli o'zgarishlarni qayta qo'llashni buyuradi. Agar siz uning o'rniga ishlagan bo'lsangiz, siz asl holatiga qaytgan bo'lar edingiz:

```
$ git stash apply --index
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#      modified:   index.html
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#
#      modified:   lib/simplegit.rb
#
```

Qo'llash buyrug'i faqat saqlangan ishni qo'llaydi, lekin siz hali ham uni to'plamingizda saqlaysiz. O'chirish uchun, ```git stash drop``` ni olib tashlash uchun zaxiraning nomi bilan ishga tushirishingiz mumkin.

```
$ git stash list
stash@{0}: WIP on master: 049d078 added the index file
stash@{1}: WIP on master: c264051 Revert "added file_size"
stash@{2}: WIP on master: 21d80a5 added number to log
$ git stash drop stash@{0}
Dropped stash@{0} (364e91f3f268f0900bc3ee613f9f733e82aaed43)
```

Oxirgi o'zgarishlarni zaxirangizdan olib tashlash uchun ```git stash pop``` dan foydalanishingiz mumkin.

## Muzlatish voz kechish

Ba'zi hollarda, saqlangan o'zgarishlarni qo'llashni xohlaysiz, biroz ish qiling, lekin zaxiradan kelib chiqqan o'zgarishlarni amalda qo'llang. Git ```git unapply``` kabi buyruq bermaydi, lekin zaxiraga biriktirilgan yamoqni qaytarib olish va uni teskari qo'llash orqali bunga erishish mumkin:

```$ git stash show -p stash@{0} | git apply -R```

Agar zaxirani aniqlamagan bo'lsangiz, Git eng yangi zaxirani oladi:

```$ git stash show -p | git apply -R```

Siz taxallus yaratib, Git-ga ```stash-unapply``` buyrug'ini samarali qo'shishni xohlashingiz mumkin. Masalan:

```
$ git config --global alias.stash-unapply '!git stash show -p | git apply -R'
$ git stash apply
$ #... work work work
$ git stash-unapply
```

## Stash -dan filial yaratish

Agar siz biron bir ishni zaxiralab qo'ygan bo'lsangiz, uni bir muddat shu erda qoldiring va asarni saqlagan joyingizda davom etsangiz, ishni qayta qo'llashda muammo bo'lishi mumkin. Agar dastur siz o'zgartirgan faylni o'zgartirishga harakat qilsa, siz birlashma ziddiyatiga duch kelasiz va uni hal qilishingiz kerak bo'ladi. Agar siz saqlangan o'zgarishlarni qayta sinab ko'rishni osonroq usulini xohlasangiz, ```git stash branch``` ni ishga tushirishingiz mumkin, bu siz uchun yangi filial yaratadi, ishingizni zaxiraga olganingizda bajargan majburiyatingizni tekshiradi va ishingizni qayta qo'llaydi. u erda, va agar u muvaffaqiyatli qo'llanilsa, zaxirani tushiradi:

```
$ git stash branch testchanges
Switched to a new branch "testchanges"
# On branch testchanges
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#      modified:   index.html
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#
#      modified:   lib/simplegit.rb
#
Dropped refs/stash@{0} (f0dfc4d5dc332d1cee34a634182e168c4efc3359)
```

Bu zaxiradagi ishni osonlikcha tiklash va yangi filialda ishlash uchun yaxshi yorliq.