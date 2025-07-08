# Programcı Olmayan Birinin Yapabileceği Şeyler  

## Dinlemeye Başlayın  

Açık kaynak dünyasında her şey diğer insanlarla ilgilidir.  
Bir ekibe katılmak istiyorsunuz, bu da topluluğu ve nasıl çalıştığını anlamanız gerektiği anlamına gelir.  
Bir projeye girip *"Merhaba, bu projenin böyle olması gerektiğini düşünüyorum."* demek genellikle iyi bir yaklaşım olarak görülmez.  
Bazı projeler bu tür bir yaklaşımı kabul edebilir, ancak proje uzun süredir devam ediyorsa bu tavrın benimsenme ihtimali düşüktür.  
**Dinlemek, projenin neye ihtiyacı olduğunu anlamanın en iyi yoludur.**  

### 1. **Bir e-posta listesine katılın**  
Birçok proje için e-posta listesi, proje gelişimi hakkında ana iletişim kanalıdır.  
Özellikle büyük projelerde birden fazla e-posta listesi bulunabilir.  
Örneğin, *PostgreSQL* projesinin kullanıcı odaklı en az 12 ve geliştiricilere yönelik 6 farklı e-posta listesi vardır.  
Başlangıç olarak, ana kullanıcı listesi ve ana geliştirici listesine abone olmanızı öneririm.  

### 2. **Bir blog takip edin**  
Ana geliştiriciler tarafından tutulan bloglar, gelecekteki sürümler ve gereksinimler hakkında bilgi verir.  
Bazı projeler için *planet sitesi* (örneğin, `planet.gnome.org` veya `planet.mysql.com`) tüm güncellemeleri bir araya getirir.  
Google'da `"planet <proje adı>"` şeklinde arama yaparak başlayabilirsiniz.  

### 3. **Bir IRC kanalına katılın**  
Birçok açık kaynak projesinin geliştiriciler ve kullanıcılar için özel IRC kanalları vardır.  
Projenin web sitesini ziyaret ederek kanal adı ve bulunduğu IRC ağı hakkında bilgi edinebilirsiniz.  

---

## Ticket (Hata Bildirimi) ile Çalışmak  

Kod, her açık kaynak projesinin kalbidir, ancak kod yazmak tek katkı yolu değildir.  
Projelerde yeni özellikler eklemeye ve hataları düzeltmeye odaklanılırken, sistemlerin bakımına yeterince zaman ayrılmayabilir.  
Bu alanlara katkıda bulunarak bir projeye dahil olabilirsiniz.  

### 4. **Bir hatayı teşhis edin**  
Hatalar çoğu zaman eksik rapor edilir.  
Bir hatayı analiz etmek ve sınıflandırmak, geliştiricilere zaman kazandırır.  
Bir kullanıcı *"Yazılım X yaptığımda çalışmıyor"* dediyse, şu sorulara cevap arayarak sorunu detaylandırabilirsiniz:  

- Hata tekrar edilebilir mi?  
- Aynı hatayı oluşturmak için belirli adımlar var mı?  
- Belirli bir tarayıcıda veya işletim sisteminde mi ortaya çıkıyor?  

Bulduğunuz her şeyi hata raporuna ekleyerek projenin ilerlemesine yardımcı olabilirsiniz.  

### 5. **Çözülen hataları kapatın**  
Birçok hata raporu çözüldükten sonra sistemde açık olarak kalır.  
Bunları temizlemek zaman alıcı olabilir, ancak proje için çok değerlidir.  

- Eski hata raporlarını (1 yıl veya daha eski) gözden geçirin.  
- Projenin sürüm notlarını kontrol ederek hatanın çözülüp çözülmediğini belirleyin.  
- Hatayı yeni sürümde test edin, eğer hata artık yoksa raporu kapatın.  

---

## Kod ile Çalışmak  

Her seviyeden programcı, bir projeye katkıda bulunabilir.  
Bir projede kod yazmak istiyorsanız, projeye nasıl katkı sağlandığını öğrenin.  
Bazı projeler değişiklikleri doğrudan kabul ederken, bazıları kodun önce bir inceleme sürecinden geçmesini ister.  

### 6. **Beta veya aday sürümü test edin**  
Çoklu platform desteği olan projelerde, yeni sürümlerin test edilmesi büyük önem taşır.  
Sürüm yöneticileri, beta sürümünü farklı platformlarda test etmek isteyen kullanıcılara ihtiyaç duyar.  
Yapmanız gereken:  

- Yazılımın son sürümünü indirip derlemek  
- Farklı donanım ve işletim sistemlerinde çalışıp çalışmadığını kontrol etmek  
- Test sonuçlarını geliştiricilere bildirmek  

### 7. **Bir hatayı düzeltin**  
Geliştiricilerin genellikle başladığı nokta burasıdır.  

- Bir hata bularak çözmeye çalışın  
- Çözümünüzü kod içinde belgeleyin  
- Gerekirse bir test ekleyin  
- Eğer hatayı çözemezseniz bile bulgularınızı hata kaydına ekleyin  

### 8. **Bir test yazın**  
Projelerin test sistemleri genellikle eksik olabilir.  
*gcov* (C için) veya *Devel::Cover* (Perl için) gibi test kapsamı araçlarını kullanarak eksik alanları tespit edin.  
Ardından bu alanları kapsayan testler yazın.  

### 9. **Derleyici uyarılarını giderin**  
Özellikle *C tabanlı projelerde*, derleyiciler bazen uyarılar verir.  
Bunlar gerçek bir hataya işaret etmese bile, fazla uyarı almak kodun daha karışık görünmesine sebep olabilir.  
Uyarıyı analiz edin ve gerçekten bir hata olup olmadığını belirleyin.  

### 10. **Yorum ekleyin**  
Eğer bir kod parçasını anlamakta zorlandıysanız, başkaları da zorlanabilir.  
Kod içindeki kafa karıştırıcı bölgelere açıklayıcı yorumlar ekleyerek projeye katkıda bulunabilirsiniz.  

---

## Dokümantasyon ile Çalışmak  

Dokümantasyon genellikle projelerin ihmal edilen kısmıdır.  
Projeyi uzun süredir geliştirenler, yeni gelenlerin nelere ihtiyacı olabileceğini gözden kaçırabilir.  

### 11. **Bir örnek oluşturun**  
Kodun veya aracın nasıl çalıştığını gösteren iyi örnekler, en az teknik belgeler kadar önemlidir.  

- API veya kütüphane kullanımı için örnek kodlar yazın  
- Komut satırı araçları için gerçek hayattan kullanım senaryoları oluşturun  
- Arayüzlü uygulamalar için ekran görüntüleri ile açıklamalar ekleyin  

---

## Topluluk ile Çalışmak  

Açık kaynak sadece koddan ibaret değildir, topluluk da büyük önem taşır.  

### 12. **Bir soruya cevap verin**  
Birine yardımcı olmak, projenin büyümesine katkıda bulunmanın en iyi yollarından biridir.  
Özellikle yeni başlayanlara karşı sabırlı olun ve onlara yol gösterin.  

### 13. **Bir blog yazısı yazın**  
Projeyle ilgili deneyimlerinizi paylaşarak iki şekilde yardımcı olabilirsiniz:  

1. Projeye olan ilgiyi artırabilirsiniz.  
2. Karşılaştığınız sorunlara çözümler sunarak başkalarına rehber olabilirsiniz.  

### 14. **Bir web sitesini geliştirin**  
Eğer web tasarımı konusunda bilginiz varsa, projenin web sitesini geliştirebilirsiniz.  
Grafik tasarım ve logo gibi görsel öğeler konusunda da destek sağlayabilirsiniz.  

### 15. **Teknik dokümantasyon yazın**  
Bir yazılımın nasıl çalıştığını açıklamak için teknik dokümanlar oluşturabilirsiniz.  
Özellikle açık kaynak projeler, güncellenmiş ve anlaşılır dokümanlara her zaman ihtiyaç duyar.  

### 16. **Öğretin ve başkalarına yardımcı olun**  
Bir konuyu öğretmek, onu öğrenmenin en iyi yoludur.  
Açık kaynak projelerine katılan insanlara rehberlik ederek hem kendinizi geliştirir hem de topluluğa katkıda bulunmuş olursunuz.  
Paylaşılan bilgi, daha fazla kişinin açık kaynak ekosistemine katkıda bulunmasını sağlar.  

---
