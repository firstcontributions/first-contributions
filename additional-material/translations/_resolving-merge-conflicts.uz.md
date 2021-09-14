# Birlashtirishdagi ziddiyat (merge konflikti) nima?

Agar siz boshqa filialni joriy ishchi bo'limingizga qo'shmoqchi bo'lsangiz, siz boshqa kontekstdan o'zgarishlarni qabul qilasiz va ularni joriy ishchi fayllaringiz bilan birlashtirasiz.
Agar bitta faylda ikki kishi bir xil satrlarni o'zgartirgan bo'lsa yoki bir kishi uni o'chirishga qaror qilgan bo'lsa, ikkinchisi uni o'zgartirishga qaror qilgan bo'lsa, Git qaysi versiya to'g'ri ekanligini aniqlay olmaydi. Git keyin faylni ziddiyatli deb belgilaydi - bu ishni davom ettirishdan oldin hal qilish kerak.

# Birlashtirishdagi ziddiyatni qanday hal qilish mumkin?

Birlashish ziddiyatiga duch kelganda, git fayldagi muammoli maydonni "<<<<<<<< HEAD" va ">>>>>>>>>> [boshqa filial nomi]" bilan belgilab qo'yadi.

Birinchi markerdan keyingi tarkib hozirgi ishchi bo'limingizdan olingan. Burchak qavsidan keyin Git bizga o'zgarishlar qayerdan (qaysi filialdan) kelganini aytadi. "=======" yozuvi ikkita qarama -qarshi o'zgarishlarni ajratib turadi.
Bizning vazifamiz endi bu satrlarni tozalashdir: ishimiz tugagach, fayl biz xohlagandek ko'rinishi kerak. Qaysi versiya yakuniy bo'lishi kerakligini hal qilish uchun qarama -qarshi o'zgarishlarni yozgan jamoadoshi bilan maslahatlashish tavsiya etiladi. Bu sizniki bo'lishi mumkin - yoki ikkalasining aralashmasi.

e.g. :
```
 <<<<<<< HEAD:mergetest
 Bu men qo'shgan uchinchi qator
 =======
 Bu men qo'shayotgan to'rtinchi qator
 >>>>>>> 4e2b407f501b68f8588aa645acafffa0224b9b78:mergetest
```

`<<<<<<<`: Birlashma ziddiyatli qatorlarning boshlanishini ko'rsatadi. Birinchi qatorlar - bu o'zgarishlarni birlashtirishga harakat qilayotgan faylning satrlari. 
`=======`: Taqqoslash uchun ishlatiladigan uzilish nuqtasini ko'rsatadi. Farqlarni vizual tarzda ko'rish uchun foydalanuvchi birlashtirishdan (pastdan) keladigan o'zgarishlarni (yuqorida) o'zgartirgan.  
`>>>>>>>`: Birlashtirilgan ziddiyatli satrlarning oxirini bildiradi.  

Siz ziddiyatni faylni tahrir qilish orqali hal qilasiz va keyin faylni qismlarini qo'lda birlashtirishda muammoga duch kelasiz. Bu sizning yoki boshqa birovning o'zgarishlarini bekor qilishni yoki ikkalasini aralashtirib yuborishni anglatishi mumkin. Shuningdek, fayldagi '<<<<<<<', '=======' va '>>>>>>>' ni o'chirib tashlashingiz kerak bo'ladi.


Mojaroni hal qilganingizdan so'ng, `git add` ni bajaring. Sinovlarni o'tkazishni unutmang, chunki siz nizoni hal qilganingizga ishonch hosil qilishingiz kerak.

Birlashtirishdagi ziddiyatlarni hal qilishning oson yo'li uchun o'zingiz foydalanayotgan IDE ga qarab turli xil plaginlarni yuklab olishingiz mumkin.


# Birlashtirishni qanday bekor qilish mumkin?
Agar siz birlashtirishni bekor qilmoqchi bo'lsangiz, buni qila olasiz `git merge —abort`
