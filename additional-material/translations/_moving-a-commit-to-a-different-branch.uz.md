# Kommit'larni boshqa branch'ga o'tkazish
Agar siz majburiyatni o'z zimmangizga olgan bo'lsangiz va keyin noto'g'ri filialni o'zgartirganingizni tushunsangiz nima bo'ladi?
Bu xatoni qanday tuzatish mumkin? Bu savolga ushbu ko'rsatma javob beradi.

## So'nggi majburiyatlarni mavjud filialga o'tkazish
Buning uchun yozing:

```git reset HEAD~ --soft``` - Oxirgi majburiyatni bekor qiladi, lekin kiritilgan o'zgarishlarni saqlaydi.
```git stash``` - Katalog holatini saqlab qolish uchun.  

```git checkout <o'tiladigan branch nomi>``` - Boshqa branch'ga o'tish uchun.   
```git stash pop``` - Oxirgi saqlangan holatni qaytarish uchun.  
```git add .``` - Individual fayllarning barchasini qo'shish uchun.  
```git commit -m "ваш комментарий"``` - Saqlash va o'zgaritirishlarni kommit qilish uchun.  

O'zgaritirishlaringiz endi kerakli bo'limda.


### Oxirgi majburiyatlarni yangi filialga o'tkazish
Buning uchun quyidagilarni kiriting: 
```git branch newbranch``` -  Barcha kommitlarni saqlab qolgan holda yangi branch ochish uchun.   
```git reset --hard HEAD~[n]``` - Asosiy filialni qaytaradi n majburiyat. Shuni yodda tutingki, ushbu majburiyatlar tarkibidagi o'zgarishlar asosiy bo'limdan butunlay o'chiriladi.  
```git checkout newbranch``` - Siz yaratgan filialga o'tadi. Endi bu filial barcha majburiyatlarni o'z ichiga oladi.   

Esda tuting: majburiyatga kiritilmagan har qanday o'zgarishlar to'liq yo'qoladi.
