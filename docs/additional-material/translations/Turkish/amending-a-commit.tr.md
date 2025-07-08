# Commit Düzeltmeleri

Uzak bir depoya bir commit gönderdiğinizi ve daha sonra commit mesajında bir yazım hatası yaptığınızı veya bu son commite bir satır eklemeyi unuttuğunuzu fark ettiğinizi hayal edin. Bu durumda ne yapmalısınız? İşte bu belgede tam olarak bundan bahsedeceğiz.

## Github'a Gönderilmiş (Push Edilmiş) Son Commit'in Mesajını Nasıl Değiştirirsiniz?

Bunu bir dosyayı düzenlemeye açmadan yapmak için:
* ```git commit --amend -m "yeni commit mesajınız"``` komutunu girin.
* Ardından değişiklikleri Github'a göndermek için ```git push origin <branch-name>``` komutunu çalıştırın.

Not: Eğer sadece ```git commit --amend``` yazarsanız, bir metin editörü açılır ve commit mesajını düzenlemenizi önerir. 
``-m`` anahtarını kullanmak editörün açılmasını engeller.

## Bir Committe Nasıl Değişiklik Yapılır?

Eğer bir dosyada küçük bir değişiklik yapmayı unuttuysak, örneğin bir kelimeyi değiştirmeyi unuttuysak ve bu commit zaten uzak depoya gönderildiyse ne yapmalıyız?

Örneğin, commit geçmişim şu şekilde olsun:
`` `
g56123f create file bot file
a2235d updated contributor.md
a5da0d modified bot file
`` `

Diyelim ki bot file dosyasına bir kelime eklemeyi unuttum.

Bunu düzeltmek için iki yol var. İlk yol, bu değişikliği içeren yeni bir commit oluşturmaktır, örneğin:
`` `
g56123f create file botfile
a2235d updated contributor.md
a5da0d modified botfile
b0ca8f added single word to botfile
`` `
İkinci yol ise a5da0d commit'ini düzeltmek, bu eksik kelimeyi eklemek ve bu değişiklikleri Github'a tek bir commit olarak göndermektir.
İkinci yol tercih edilir çünkü bu sadece küçük bir değişiklikle ilgilidir.

Bunu başarmak için şu adımları izleyeceğiz:
* Dosyayı değiştirin. Bu durumda, botfile dosyasını değiştirip daha önce unuttuğum kelimeyi ekleyeceğim.
* Ardından, bu dosyayı ```git add <dosya-adı>``` komutuyla indeksleyin.

Normalde indekslemeden hemen sonra `` `git commit -m" commit mesajımız "` `` yaparız, değil mi? Ancak bu durumda amacımız önceki commit'i düzeltmek olduğu için bunun yerine şu komutu çalıştıracağız:

* ```git commit --amend```
 Bu, bir metin editörü penceresi açacak ve commit mesajında değişiklik yapma imkanı sunacaktır. Mesajı gerçekten düzenleyebilir veya olduğu gibi bırakabiliriz.
* Editörden çıkın.
* Değişikliklerimizi ```git push origin <branch-name>``` komutuyla gönderin.

Böylece, her iki düzeltme de tek bir commit'te birleştirilmiş olacaktır.