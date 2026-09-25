# Birleştirme çatışması nedir?

Mevcut çalışma dalınızla başka bir dalı birleştirmeye çalıştığınızda, farklı bir bağlamda değişiklikler yapıyor ve bunları mevcut dosyalarınızla birleştiriyorsunuz.
Aynı dosyadaki aynı satırlar iki kişi tarafından değiştirilirse veya bir kişi silmeye karar verirken diğeri değiştirmeye karar verirse Git hangi sürümün doğru olduğunu belirleyemeyecektir. Git daha sonra dosyayı bir çakışma olarak işaretleyecektir; çalışmaya devam etmek için bu çakışmayı çözmeniz gerekecektir.

# Birleşme ihtilafı nasıl çözülür?

Bir birleştirme çakışmasıyla karşılaşıldığında, git dosyadaki sorunlu alanı başlangıç işareti ve diğer dal adı ile işaretler.

İlk işaretleyiciden sonraki içerik mevcut dalınızdan gelir. Git, değişikliklerin nereden (hangi daldan) geldiğini söyler. Ayırıcı satır, çakışan iki değişikliği ayırır.
Bizim görevimiz bu satırları temizlemek: İşimiz bittiğinde dosya istediğimiz gibi görünmeli. Çelişkili değişiklikleri yazan takım arkadaşınıza danışarak hangi versiyonun nihai olacağına karar vermeniz önerilir. Ya sizin olabilir ya da ikisinin karışımı olabilir.

Örneğin:
```
# Mevcut dalın içeriği
Bu üçüncü satırım.

# Başka bir dalın içeriği
Eklediğim dördüncü satır bu.
```

`HEAD`: Birleştirme çakışması olan satırların başlangıcını belirtir. İlk satır kümesi, değişiklikleri birleştirmeye çalıştığınız dosyadaki satırlardır.
Ayırıcı satır: Karşılaştırma için kullanılan kesme noktasını belirtir. Kullanıcının yaptığı değişiklikleri (yukarıda) birleştirmeden kaynaklanan değişikliklerle (aşağıda) görsel olarak karşılaştırarak farkları görmenizi sağlar.
`branch-name`: Birleştirme çakışması olan satırların sonunu işaretler.

Çakışmayı dosyayı düzenleyip daha sonra manuel olarak birleştirerek çözebilirsiniz. Bir şeyin veya birinin iptali veya değiştirilmesi veya ikisinin bir kombinasyonu anlamına gelebilir. Ayrıca dosyadaki çakışma işaretleri satırlarını da silmeniz gerekir.

Çatışmayı çözdükten sonra `git add` komutunu çalıştırın. Çakışmayı çözdüğünüzden emin olmanız gerektiğinden testleri çalıştırmayı unutmayın.

Birleştirme çakışmalarını daha kolay çözebilmek için kullandığınız IDE'ye bağlı olarak farklı eklentiler de indirebilirsiniz.

# Birleştirme nasıl geri alınır?
Birleştirmeyi iptal etmek istiyorsanız `git merge --abort` komutunu kullanabilirsiniz