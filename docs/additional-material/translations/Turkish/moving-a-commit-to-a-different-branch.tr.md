# Taahhütleri başka bir dala taşıma
Peki ya bir değişiklik yapıp daha sonra başka bir dala geçtiğinizi fark ederseniz?
Bunu nasıl değiştirebilirsiniz? İşte bu eğitim tam da bunu anlatıyor.

## Son yapılan commit'leri mevcut bir dala taşıma
Böyle bir hareket için şunu yazın:

`` `git reset HEAD ~ --soft` `` - Son commit'i geri alır, ancak değişiklikleri kullanılabilir bırakır.
`` `git stash` `` - Bir dizinin durumunu kaydeder.

`` `git checkout <geçerli dal adı>` `` - Başka bir dala geçiş yapar.
`` `git stash pop` `` - Son kaydedilen durumu döndürür.
`` `git add .` `` - Tek tek dosyaları ekler.
`` `git commit -m "mesajınızı buraya yazın"``` - Değişiklikleri kaydeder ve onaylar.

Değişiklikleriniz artık doğru dalda.


### Son yapılan commit'leri yeni bir dala taşıma
Böyle bir hareket için şunu yazın:
`` `git branch newbranch` `` - Tüm commit'leri koruyarak yeni bir dal oluşturur.
`` `git reset --hard HEAD ~ [n]` `` - Ana dalı n adet commit'e geri döndürür. Bu commitlerde yer alan değişikliklerin master dalından tamamen silineceğini aklınızda bulundurun.
`` `git checkout newbranch` `` - Oluşturduğunuz dala geçiş yapar. Bu dal artık tüm commitleri içeriyor.

Unutmayın: Commit'e dahil edilmeyen tüm değişiklikler tamamen kaybolacaktır.