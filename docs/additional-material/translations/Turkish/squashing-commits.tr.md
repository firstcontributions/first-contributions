# Squashing nedir?

Git'te squashing, eylemlerinizin geçmişini yeniden yazmak anlamına gelir, böylece yaptığınız değişikliklerin bir açıklamasıyla karşılaşırsınız.
Bu, açık kaynaklı projelerde sıklıkla yapılır çünkü açık kaynaklı projelerdeki birçok dal geçmişi yalnızca onları oluşturan geliştiriciyle ilgilidir ve yapılan değişiklikleri tanımlamanın ve gerekirse geri almanın daha kolay bir yolunu sağlar.

# Commit'leri nasıl ezersiniz?

Öncelikle, mevcut dalınıza birleştirmek istediğiniz commit'leri analiz etmek için bir git günlüğü çalıştırın.

```
git günlüğü
```

Taahhütlerinizin bir kısmını şu şekilde görmelisiniz:

```
bla bla bla yapmak
Yazar: omguhh
Tarih: 10/10/20
 Mesaj 1'i kaydet

blablabla2'yi taahhüt et
Yazar: omguhh
Tarih: 10/10/20
 Mesaj 2'yi kaydet
```

Şimdi, birleştirmek istediğimiz commitleri gördüğümüzde ``git rebase`` ile oraya gidebiliriz. ``git rebase`` ile zaten aşina olduğunuzu varsayarak, etkileşimli git rebase modunda commit'leri ezmeye başlayabiliriz; bu şu şekilde etkinleştirilebilir:

```
git rebase -i
```

Artık etkileşimli yeniden temellendirme ile şu şekilde hareketlerle ne kadar ileri gitmek istediğinizin başlangıç ​​ve bitiş noktalarını tanımlayabilirsiniz:

```
git rebase -i HEAD~2
```

Bu komutu çalıştırdığınızda aşağıdakine benzer bir şey göreceksiniz:

```
pick blablabla test01.txt dosyasını değiştirme
blablabla2'yi seçin dummy01.txt dosyası ekleniyor

#
# Komutlar:
# p, seç = kullan commit
# r, reword = commit'i kullan, ancak commit mesajını düzenle
# e, edit = commit kullan, ancak değişiklik yapmak için durdur
# s, squash = commit'i kullan, ancak önceki commit'e birleştir
# f, fixup = "squash" gibi, ancak bu commit'in günlük mesajını at
# x, exec = komutu (satırın geri kalanını) kabuk kullanarak çalıştır
#
# Bu satırlar yeniden sıralanabilir; yukarıdan aşağıya doğru infaz edilirler.
#
# Buradaki bir satırı silerseniz O COMMIT KAYBOLACAĞIZ.
#
# Ancak her şeyi kaldırırsanız, yeniden temellendirme işlemi iptal edilecektir.
#
# Boş commit'lerin yorum satırına alındığını unutmayın
```

Yani, ```blablabla2```'yi ```blablablabla```'ya sıkıştırmak istiyorsanız, aşağıdakileri değiştirmeniz gerekir:

```
pick blablabla test01.txt dosyasını değiştirme
squash blablabla2 dummy01.txt dosyası ekleniyor

```

Her şey yolunda giderse şu sonucu elde edeceksiniz:

```
# Bu 2 commit'in birleşimidir.
# İlk commit'in mesajı şu şekilde:
mesaj 1'i kaydet

# Bu 2. commit mesajıdır:

mesaj 2'yi gönder
```

Değişiklikleri kaydetmek için editörden çıkmadan önce bunları özgürce değiştirebilirsiniz.

Git log'u çalıştırdığınızda, çıkmadan önce girdiğiniz commit mesajı, commit'ler birleştirilerek tek bir commit'te gösterilmelidir.