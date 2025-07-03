# Yerel onayları geri al

Yerel onayları geri almak için yapmanız gereken tek şey
```
git sıfırlama
```

Bu komut, staging alanını son commit'e sıfırlayacaktır, ancak çalışma dizininizde yapılan değişiklikler değişmeyecektir. Bu şekilde, yaptığınız değişiklikleri tekrar uygulayabilirsiniz.
Veya, önceki bir commit'ten sadece bir dosyayı kaldırmak istiyorsanız. Daha sonra aşağıdaki komutu uygulayabilirsiniz

```
git reset <dosya>
```
Komut yalnızca belirtilen dosyayı hazırlama alanından kaldıracaktır, ancak dosyada yapılan değişiklikler yine de kalacaktır.

```git reset``` kullanımına örnek
```
# index.php ve tutorial.php'de değişiklikler yapın
# Dosyaları sahneleme alanına ekleyin
$ git add .
# Her iki dosyanın da ayrı ayrı commit edilmesi gerektiğini unutmayın
# Unstage öğreticisi.php
$ git sıfırlama öğreticisi.php
# Önce index.php'yi işleyin
$ git commit -m "index.php değiştirildi"
# Şimdi tutorial.php'yi gönder
$ git add öğretici.php
$ git commit -m "tutorial.php değiştirildi"
```

Diyelim ki yerel depolama alanınızı bozdunuz ve onu sadece son commit'e sıfırlamak istiyorsunuz.
Daha sonra aşağıdaki komutu çalıştırabilirsiniz.
```
git reset --hard
```

Komut sadece hazırlama alanınızı sıfırlamakla kalmayacak, aynı zamanda dosyalardaki tüm değişikliklerinizi son commit'inize geri döndürecektir.
``--hard`` modu Git'e çalışma dizinindeki tüm değişiklikleri geri almasını söyler.
Bunu yalnızca tüm yerel geliştirmeyi çöpe atacağınızdan gerçekten eminseniz çalıştırmalısınız.

```git reset --hard``` kullanım örneği
```
# Çılgın bir deney başlatmaya karar verdim
# Yeni bir 'crazy.php' dosyası oluşturun ve içine biraz kod ekleyin
# crazy.php'yi yükle
$ git add crazy.php
$ git commit -m "Çılgın bir geliştirme başlatıldı"
# crazy.php dosyasını tekrar düzenleyin ve diğer birçok dosyayı değiştirin
# Takip edilen tüm dosyaları kaydet
$ git add .
$ git commit -m "Devam eden geliştirme"
# Test edildi ve işler kontrolden çıktı
# Her şeyi kaldırmaya karar verdim
$ git reset --hard HEAD~2
```

```git reset --hard HEAD~2``` geçerli dalı her seferinde 2 commit geriye taşır, yaptığınız tüm değişiklikleri geri alır ve az önce oluşturduğumuz 2 anlık görüntüyü proje geçmişinden kaldırır.

Not: Eğer commit'lerinizi paylaşımlı bir depoya taşıdıysanız asla ``git reset --hard`` komutunu çalıştırmayın, çünkü bu tüm depolarla sorunlara yol açacaktır.