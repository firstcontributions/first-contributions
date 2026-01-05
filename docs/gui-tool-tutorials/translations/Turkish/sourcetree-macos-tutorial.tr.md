[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# First Contributions

|<img alt="SourceTree" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-logo.png" width="200">|Atlassian Sourcetree|
|---|---|

Zor gelir. Herhangi bir işi ilk kez yapmak daima zor gelir. Özellikle başkalarıyla ortak çalışıyorsanız, hata yapmak içinize sinmez. Ancak "Açık Kaynağın" temelinde işbirliği ve birlikte çalışma yatmakta. Biz, açık kaynak projelere ilk kez katkıda bulunacak kişilerin bu süreci öğrenmesini ve ilk katkılarını sunmalarını kolaylaştırmayı istiyoruz.

Makale okumak ve eğitim videoları izlemek yardımcı olabilir, fakat bir işi gerçekten yapmanın yerini ne tutabilir ki? Bu proje yeni başlayanların veya ilk defa katkıda bulunacakların işini kolaylaştırmak ve onlara rehberlik etmek amacındadır. Unutmayın ki ne kadar rahat olursanız o kadar rahat öğrenirsiniz. Eğer bir GitHub projesine ilk defa katkıda bulunacaksanız, aşağıda gösterilen basit adımları takip etmeniz yeterli olacaktır. Söz veriyoruz, eğlenceli olacak.


## Sourcetree

Lütfen dikkat: Bu öğretici macOS içindir. Windows'taki Sourcetree'ye benzer, ancak bazı şeyler farklı görünebilir.
<!--
	****************************************
	*** Bu bölüm Windows öğreticisi      ***
	*** hazırlanana kadar yorumda       ***
	*** bırakılmıştır.                  ***
	****************************************
Lütfen dikkat: Bu öğretici macOS içindir. Sourcetree'yi Windows'ta kullanacaksanız [Windows Öğreticisi]() bağlantısına bakın.
-->

[Sourcetree](https://www.sourcetreeapp.com) uygulamasını indirin, kurun ve açın.

"Sourcetree" başlıklı bir açılır pencere görmelisiniz.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-1-main.png" alt="Sourcetree ana ekran" />

Buradan "Remote" (Uzak) düğmesine tıklayın. İlk kurulumsa GitHub hesabınızı henüz bağlamamış olabilirsiniz. "Connect" (Bağlan) düğmesine tıklayarak bağlayın.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-2-main-connect.png" alt="Sourcetree bağlanma" />

*Accounts* (Hesaplar) iletişim kutusu açılacaktır. Sol alt köşedeki "Add" (Ekle) düğmesine tıklayın. Ardından GitHub (ya da eklemek istediğiniz başka bir hesap) için uygun ayarları seçin. GitHub ayarlarınızı seçtikten sonra "Connect Account" (Hesabı Bağla) düğmesine tıklayın.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-4-accounts-add.png" alt="Sourcetree hesap ekleme" />

Bu işlem web tarayıcınızda bir sayfa açacaktır. Hesabınızı yetkilendirmek için verilen adımları takip edin.

## Projeyi "forklama"

Sayfanın üst kısmındaki "Fork" (Çatalla) düğmesine tıklayarak bu projeyi çatallayın.
<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/fork.png" alt="bu depoyu forklayın" />
Bu işlem sizin hesabınız altında projenin bir kopyasını oluşturacaktır.


## Depoyu (Repository) klonlama

Sourcetree'de "Remote" (Uzak) düğmesine tıklayın. Bu, GitHub'da listelenen tüm depolarınızı yükleyecektir.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-5-cloning.png" alt="depoyu klonlayın" />

"Clone" (Klonla) düğmesine tıkladığınızda, birkaç farklı ayarı tanımlayacağınız başka bir ekran açılacaktır.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-6-cloning-confirm.png" alt="depoyu klonlayın" />

1) **Source URL** (Kaynak URL): Bu alan otomatik olarak doldurulur ve değiştirmeniz gerekmez. GitHub projenizin bulunduğu URL'dir.

2) **Destination Path** (Hedef Yol): Bu proje dosyalarının bilgisayarınızda kaydedileceği konumdur.

3) **Name** (Ad): Sourcetree'nin projenizi referans göstereceği "Yer İmi"dir. Kısayol gibi düşünebilirsiniz.

*Not: Genellikle bu alanlarda varsayılan değerler uygundur.*

**Her şey tamamsa "Clone" (Klonla) düğmesine tıklayın.**

Bu işlem, deponuz için ana tarayıcı ekranını açacaktır.

## Dal (Branch) oluşturma

Araç çubuğundaki "Branch" (Dal) düğmesine tıklayın.

Dalınıza <isminiz-eklendi> gibi bir isim verin. Örneğin: "ahmet-yilmaz-eklendi".

Bunu yapmak için adlandırma penceresini açan **Branch (1)** (Dal) seçeneğine tıklayın. Ardından yukarıda anlatıldığı gibi **Add your name (2)** (İsminizi ekleyin) alanını doldurun. Son olarak **Create Branch** (Dal Oluştur) düğmesine tıklayın. Bu işlem, az önce adını verdiğiniz dalı oluşturacaktır.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-7-branching.png" alt="dalınıza isim verin" />


## Gerekli değişiklikleri yapma ve değişiklikleri onaylama

Şimdi `Contributors.md` dosyasını bir metin düzenleyicide açın, GitHub URL bağlantınızla birlikte isminizi ekleyin ve dosyayı kaydedin.

Değişen dosyaları görüp inceleyebilmeli ve hangilerini stage (sahneleme) etmek istediğinize karar verebilmelisiniz. Staging (sahneleme), bu commit ile ilişkilendirmek istediğiniz dosya değişikliklerini Git'e net şekilde söylemek için önemlidir.

*Not: Dosyanın farklarını göremiyorsanız, pencerenizin üst kısmındaki **Uncommitted Files** (Onaylanmamış Dosyalar) seçeneğine tıklayın.*

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-8-viewing-changed-files.png" alt="dosyaları düzenleyin" />

Şimdi pencerenin sol üstündeki **Commit** (Onayla) düğmesine tıklayın. Bu, sahneleme alanınızı gösterecektir.

Dosyayı sahneleme alanına **add** (ekle) etmek için *Checkbox* (işaret kutusu) üzerine tıklayın. Ardından bir commit mesajı girin.

*Not: Staging ve unstaged alanlarında dosyaları seçip boşluk (space) tuşunu kullanarak ilgili alanlara dosya ekleyip kaldırabilirsiniz.*

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-9-committing.png" alt="değişiklikleri sahneleyin" />

Değişikliklerinizi ekleyip commit mesajını girdikten sonra, işlemi tamamlamak için **Commit** (Onayla) düğmesine tıklayın.

Tebrikler, first-contributions çatallarınızdaki dalın yerel kopyasına tüm değişiklikleri onayladınız. Şimdi sırada sonraki adımlar var!


## Değişiklikleri GitHub'a gönderme

Artık değişikliklerinizi GitHub'a göndermeye hazırsınız. Bu işlem, projenin size ait çatallanmış kopyasına yapılacaktır. Dalınızı göndermek için adımları takip edin. Önce **Push (1)** (Gönder) düğmesine tıklayın; bu, uzak/push penceresini açar. Göndermek istediğiniz dalın onay kutusunu (2) numaralı adımda işaretleyin. Ardından **OK (3)** (Tamam) seçeneğini seçin; bu işlem commit'inizi GitHub'a gönderir.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-10-pushing.png" alt="origin ya da dal" />

## Değişikliklerinizi inceleme için gönderme

GitHub'daki deponuza giderseniz `Compare & pull request` (Karşılaştır ve çekme isteği) düğmesini göreceksiniz. Bu düğmeye tıklayın.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/compare-and-pull.png" alt="çekme isteği oluşturun" />

Şimdi çekme isteğini (pull request) gönderin.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/submit-pull-request.png" alt="çekme isteğini gönderin" />

Yakında tüm değişikliklerinizi bu projenin master (ana) dalıyla birleştireceğim. Değişiklikler birleştirildiğinde bir bildirim e-postası alacaksınız.

## Bundan sonra ne yapabilirim?

Tebrikler! Katkıda bulunan biri olarak sıkça karşılaşacağınız standart _fork -> clone -> edit -> PR_ iş akışını tamamladınız!

Katkınızı kutlayın ve [web uygulamasına](https://firstcontributions.github.io/#social-share) giderek bunu arkadaşlarınız ve takipçilerinizle paylaşın.

### [Ek bilgi](../additional-material/git_workflow_scenarios/additional-material.md)


## Diğer araçlarla ilgili eğitimler
[Ana sayfaya dön](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
