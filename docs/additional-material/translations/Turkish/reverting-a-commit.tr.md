# Taahhüdü geri al

Bir taahhüdü iptal etmek, tüm taahhütleri iptal eden tamamen yeni bir belge oluşturmak anlamına gelir.
Öncekine yapılan değişiklikler. Git'te ``CTRL + Z``` yapmak gibi bir şey.

Git'te dönüştürme işlemi daha kolay hale gelir çünkü uzak deponuza gönderdiğiniz her katkının SHA (Güvenli Karma Algoritması) olarak bilinen benzersiz bir alfanümerik anahtarı vardır.
Yani bu, SHA'nız olduğu sürece herhangi bir commit'i geri alabileceğiniz anlamına geliyor.
Ancak daha sonra depolama alanınızı bozmamak için sırayı dikkatli bir şekilde değiştirmeniz gerekiyor.

Geri almak istediğimiz belirli bir commit'in SHA'sını seçmek için, yaptığımız tüm commit'lerin bir kaydı kullanışlı olacaktır.
Bunu elde etmek için şu komutu çalıştıracağız:
`` `git log --oneline` ``
``git log`` komutunun tek bir çalıştırılması bize SHA'yı (uzun formda) da verecektir
Ancak `` --oneline `` bayrağını kullanmak, git'e kolay okunabilmesi için bunun özlü (tek satırlık) bir düzende görüntülenmesini istediğimizi söyler.

Bu komut çalıştırıldığında görüntülenen ilk 7 karaktere kısa commit hash'i denir.

Örneğin, bu depoda ``git log --oneline`` komutunu çalıştırdığımda şunu elde ediyorum:
```
389004d başlığa boşluk eklendi
c1b9fc1 'master' dalını öğreticilere birleştir
77eaafd bir commit'i geri almak için öğretici ekledi
```

Bu, ``git log --oneline`` komutunu kullanarak depoya yapılan tüm commit'lerin bir listesini, SHA'sının ilk 7 karakteriyle birlikte alabileceğimizi gösteriyor.

"Başlığa boşluk ekle" işlemini geri almak istediğimi varsayalım. İşte adımlar:

* Belgenin SHA'sını kopyalayın, bu durumda ``389004d``
* Daha sonra ```git revert 389004d``` komutunu çalıştırın

Bu, metin düzenleyicimi açacak ve benden commit mesajını düzenlememi isteyecek.
Varsayılan git mesajı olarak, `Revert` kelimesiyle başlayan commit mesajını bırakmaya karar verebilirsiniz.
Veya mesajı kendi zevkinize göre özelleştirmeye de karar verebilirsiniz.

* Daha sonra metin düzenleyiciyi kaydedip kapatacağım.
* Komut satırına geri dön.
* Geri alınan değişiklikleri Github'a göndermek için `` `git push origin <branch-name>` `` komutunu çalıştırın.

Ve işte bu kadar, yapılan değişiklikler geri alınacaktır. Bu durumda, depomuz ``c1b9fc1``'de göründüğü gibi değişecek