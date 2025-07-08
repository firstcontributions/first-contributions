# Saklamak

Ya büyük bir kod parçası üzerinde çalışıyorsanız ve aniden üzerinde çalıştığınız dalı başka bir dala geçirmeniz gerekirse? Kod tamamlanmamış ve herhangi bir test yapılmamış olduğundan muhtemelen onu commit etmek istemezsiniz. Ama değişiklik yapmadan başka bir dala geçemezsiniz, Git bu akışı bozmanıza izin vermez. Peki ne yapacağız? Dallara atlayabilirken gereksiz commit'leri nasıl engelleriz? İşte bu eğitim tam da bunu anlatıyor.

## Çalışmayı Gizleme

Diyelim ki bir proje dalında çalışıyorsunuz ve bazı dosyaları değiştiriyorsunuz. Şimdi ``git status`` komutunu çalıştırırsanız dosyalardaki değişiklikleri görebilirsiniz.

```
$ git durumu
# Dal ana üzerinde
# Taahhüt edilecek değişiklikler:
# (sahnelemeyi kaldırmak için "git reset HEAD <dosya>..." komutunu kullanın)
#
# değiştirildi: index.html
#
# Değişiklikler commit için hazır değil:
# (ne taahhüt edileceğini güncellemek için "git add <dosya>..." kullanın)
#
# değiştirildi: lib/simplegit.rb
#
```

Şimdi dalınızı değiştirmek istiyorsunuz, ancak henüz herhangi bir değişiklik yapmak istemiyorsunuz; böylece değişikliklerinizi kaydedebilirsiniz.
Yığına yeni bir kaynak eklemek için ``git stash`` komutunu çalıştırın:

```
$ git saklama
Çalışma dizini ve dizin durumu kaydedildi \
 "Ana projedeki WIP: 049d078 dizin dosyasını ekledi"
HEAD artık 049d078'de, dizin dosyası eklendi
(Geri yüklemek için "git stash apply" yazın)
```

Artık çalışma dizininiz temiz, ```git status``` kullanın:

```
$ git durumu
# Dal ana üzerinde
taahhüt edilecek bir şey yok, çalışma dizini temiz
```

Artık istediğiniz sektöre girip işinizi yapabilirsiniz; Gizli değişiklikler bir yığın olarak saklanır. Yığınınızda hangi stash'leri sakladığınızı görmek için ``git stash list`` komutunu kullanabilirsiniz:

```
$ git stash listesi
stash@{0}: WIP on master: 049d078 dizin dosyasını ekledi
stash@{1}: Ana dosyada WIP: c264051 "dosya_boyutu eklendi" geri alındı
stash@{2}: WIP ana bilgisayarda: 21d80a5 günlüğe sayı eklendi
```

Az önce sakladığınız değişiklikleri tekrar uygulamak isterseniz ``git stash apply`` komutunu kullanabilirsiniz. Bu komutla son kaydedilen dosyayı tekrar uygulayabilirsiniz. Başka bir dosyayı yeniden uygulamak için, onu şu şekilde adlandırarak belirtebilirsiniz: ```git stash apply <stash-name>```, `` `<stash-name>`` yerine stash'in adını yazın ve yeniden göndermem gerekiyor.

```
$ git stash uygula
# Dal ana üzerinde
# Değişiklikler commit için hazır değil:
# (ne taahhüt edileceğini güncellemek için "git add <dosya>..." kullanın)
#
# değiştirildi: index.html
# değiştirildi: lib/simplegit.rb
#
```

Git'in, pozisyonu kaydettiğinizde sildiğiniz dosyayı yeniden düzenlediğini görebilirsiniz. Bu durumda, stash'i uygulamaya çalıştığınızda temiz bir çalışma dizininiz vardı ve stash'i, stash'i aldığınız aynı şubeye uygulamaya çalıştınız; Ancak kutuları başarılı bir şekilde kullanmak için temiz bir çalışma dizinine sahip olmak ve onu aynı dalda kullanmak gerekli değildir. Kutularınızı bir dala kaydedebilir, daha sonra başka bir dala geçebilir ve değişiklikleri yeni dala yeniden uygulayabilirsiniz. Stash'i uyguladığınızda çalışma dizininizde değiştirilmiş ve açılmamış dosyalar da olabilir, başka hiçbir şey temiz bir şekilde uygulanmazsa git birleştirme çakışmaları verir.

Dosyalarınızda yaptığınız değişiklikler yeniden uygulandı, ancak oluşturduğunuz dosya yeniden yüklenmedi. Bunu yapmak için, komuta aşamalı değişiklikleri yeniden uygulamasını söylemek üzere ``git stash apply`` komutunu ```--index``` ile çalıştırmanız gerekir. Bunu çalıştırırsanız, başlangıç ​​noktasına geri dönersiniz:

```
$ git stash uygula --index
# Dal ana üzerinde
# Taahhüt edilecek değişiklikler:
# (sahnelemeyi kaldırmak için "git reset HEAD <dosya>..." komutunu kullanın)
#
# değiştirildi: index.html
#
# Değişiklikler commit için hazır değil:
# (ne taahhüt edileceğini güncellemek için "git add <dosya>..." kullanın)
#
# değiştirildi: lib/simplegit.rb
#
```

Apply komutu yalnızca kapatılan işe uygulanır, ancak iş hala yığınınızdadır. Bunu kaldırmak için, kaldırılacak yığın adıyla ``git stash drop`` komutunu çalıştırabilirsiniz.

```
$ git stash listesi
stash@{0}: WIP on master: 049d078 dizin dosyasını ekledi
stash@{1}: Ana dosyada WIP: c264051 "dosya_boyutu eklendi" geri alındı
stash@{2}: WIP ana bilgisayarda: 21d80a5 günlüğe sayı eklendi
$ git stash stash@{0}'ı bırak
Stash@{0} (364e91f3f268f0900bc3ee613f9f733e82aaed43) düşürüldü
```

Son değişiklikleri yığınınızdan kaldırmak için ``git stash pop`` komutunu kullanabilirsiniz.

## Saklamayı geri al

Bazı durumlarda stash değişikliklerini uygulamak, bir miktar iş yapmak, ancak başlangıçta stash'ten gelen değişiklikleri uygulamak istersiniz. Git, ``git unapply`` gibi bir komut sağlamaz, ancak stash ile ilişkili yamayı alıp ters sırada uygulayarak bu etkiyi elde edebilirsiniz:

```$ git stash show -p stash@{0} | git uygula -R```

Tekrar ediyorum, eğer bir stash belirtmezseniz Git en son stash'i varsayar:

```$ git stash göster -p | git uygula -R```

Bir takma ad oluşturup ``stash-unapply`` komutunu Git'inize eklemek isteyebilirsiniz. Örneğin:

```
$ git config --global alias.stash-unapply '!git stash göster -p | git uygula -R'
$ git stash uygula
$ #... çalış çalış çalış
$ git stash-unapply
```

## Stash'tan bir dal oluşturma

Eğer yaptığınız bir çalışmayı kaydedip bir süre orada bıraktıktan sonra, gizlediğiniz dalda çalışmaya devam ederseniz, tekrar çalıştığınızda sorun yaşayabilirsiniz. Bir uygulama sizin daha önce değiştirdiğiniz bir dosyayı değiştirmeye çalışırsa, birleştirme çakışması oluşur ve bunu çözmeniz gerekir. Stash değişikliklerinizi daha basit bir şekilde test etmek istiyorsanız, sizin için yeni bir dal oluşturan, işinizi stash ettiğinizde yaptığınız commit'leri kontrol eden ve işinizi yeniden yerleştiren ``git stash branch`` komutunu çalıştırabilirsiniz. orada ve ardından başarıyla uygulandığında kutuyu sıfırlar:

```
$ git stash branch testchanges
"testchanges" adlı yeni bir dala geçildi
# Branch testchanges üzerinde
# Taahhüt edilecek değişiklikler:
# (sahnelemeyi kaldırmak için "git reset HEAD <dosya>..." komutunu kullanın)
#
# değiştirildi: index.html
#
# Değişiklikler commit için hazır değil:
# (ne taahhüt edileceğini güncellemek için "git add <dosya>..." kullanın)
#
# değiştirildi: lib/simplegit.rb
#
Refs/stash@{0} (f0dfc4d5dc332d1cee34a634182e168c4efc3359) düşürüldü
```

Bu, gizli çalışmayı kolayca geri yüklemek ve yeni bir dalda üzerinde çalışmak için iyi bir kısayoldur.