[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# First Contributions

| <img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/9/9c/IntelliJ_IDEA_Icon.svg" width="40"> | Intellij IDEA |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |


Zor gelir. Herhangi bir işi ilk kez yapmak daima zor gelir. Özellikle başkalarıyla ortak çalışıyorsanız, hata yapmak içinize sinmez. Ancak "Açık Kaynağın" temelinde işbirliği ve birlikte çalışma yatmakta. Biz, açık kaynak projelere ilk kez katkıda bulunacak kişilerin bu süreci öğrenmesini ve ilk katkılarını sunmalarını kolaylaştırmayı istiyoruz.

Makale okumak ve eğitim videoları izlemek yardımcı olabilir, fakat bir işi gerçekten yapmanın yerini ne tutabilir ki? Bu proje yeni başlayanların veya ilk defa katkıda bulunacakların işini kolaylaştırmak ve onlara rehberlik etmek amacındadır. Unutmayın ki ne kadar rahat olursanız o kadar rahat öğrenirsiniz. Eğer bir GitHub projesine ilk defa katkıda bulunacaksanız, aşağıda gösterilen basit adımları takip etmeniz yeterli olacaktır. Söz veriyoruz, eğlenceli olacak.

Eğer bilgisayarınızda IntelliJ IDEA kurulu değilse, [ yükleyin ](https://www.jetbrains.com/idea/download/#section=windows).

**Not:** Bu öğretici Windows 10 üzerinde IntelliJ IDEA (Sürüm 2019.3.2) kullanılarak hazırlanmıştır. Bu öğreticide bazı klavye kısayolları kullanacağız. Bunlar diğer işletim sistemlerinde (macOS/Linux) farklı olabilir.

## Projeyi "forklama"

<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/fork.png" alt="bu depoyu forklayın" />

Sayfanın sağ üst köşesinde bulunan "Fork" (Çatalla) düğmesine tıklayarak bu projeyi çatallayın. Bu işlem sizin hesabınız altında projenin bir kopyasını oluşturacaktır.

GitHub, deponuz ile çatalladığınız depo arasındaki ilişkiyi takip eder. Deponuzu bir çalışma kopyası olarak düşünebilirsiniz.

Diğer herhangi bir depodan çatallanmış olmayan (üst seviye) çoğu GitHub deposunun doğrudan değişiklik yapabilen küçük bir çekirdek ekibi vardır. Diğer tüm katkıda bulunanlar, depoyu çatallayıp değişiklikleri bu çatalda yapmalı ve değişikliklerin üst seviye depoya birleştirilmesini istemek için bir Pull Request (çekme isteği) oluşturmalıdır. Üst seviye depo yöneticisi değişiklikleri onaylarsa birleştirilir ve anında şöhret ve servet kazanırsınız! Bunu nasıl yapacağınıza birazdan değineceğiz.

## Depoyu (Repository) klonlama

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="depoyu klonlayın" />

Sonraki adım, değişiklik yapmaya başlayabilmek için deponuzu bilgisayarınıza klonlamaktır. IntelliJ IDEA deponuzun URL'sine ihtiyaç duyar; bu nedenle "clone" (klonla) düğmesine ve ardından "copy to clipboard" (Panoya kopyala) simgesine tıklayın.

**DİKKAT:** Yeni katkıda bulunanların sıkça yaptığı bir hata, çatalladıkları depoyu değil, orijinal depoyu klonlamaktır. Tarayıcınızın adres çubuğunu kontrol edin ve kendi deponuzu klonladığınızdan emin olun.

Şimdi IntelliJ IDEA'yı açın.

IntelliJ IDEA mevcut bir depoyu check out (Git'te klonlamak) etmenize ve indirdiğiniz verilerle yeni bir proje oluşturmanıza olanak tanır.

Ana menüden `VCS | Get from Version Control` (VCS | Sürüm Kontrolden Al) seçeneğini seçin veya hiç proje açık değilse hoş geldiniz ekranındaki Get from Version Control (Sürüm Kontrolden Al) seçeneğine tıklayın.

Get from Version Control (Sürüm Kontrolden Al) penceresinde klonlamak istediğiniz uzak deponun URL'sini belirtin ("Test" (Test) düğmesine tıklayarak bağlantının sağlandığından emin olabilirsiniz) ya da soldaki VCS barındırma hizmetlerinden birini seçin. Seçtiğiniz hizmette zaten oturum açtıysanız, otomatik tamamlama klonlayabileceğiniz depoların listesini önerir.

"Clone" (Klonla) düğmesine tıklayın. Klonladığınız kaynaklardan bir IntelliJ IDEA projesi oluşturmak istiyorsanız onay penceresinde "Yes" (Evet) seçeneğini seçin. Git root mapping (Git kök eşlemesi) otomatik olarak proje kök dizinine ayarlanacaktır.

Projenizde submodule'lar varsa, bunlar da klonlanır ve otomatik olarak proje kökleri olarak kaydedilir.

**Önemli**: Çatalladığınız depo olduğundan ve orijinal depo olmadığından emin olun; aksi halde çalışmaz.

## Dal (Branch) oluşturma

Git'te branching (dallanma), ana geliştirme hattından ayrılmanızı sağlayan güçlü bir mekanizmadır. Örneğin bir özellik üzerinde çalışmanız gerektiğinde veya bir sürüm için kod tabanının belirli bir durumunu dondurmak istediğinizde kullanılır.

IntelliJ IDEA'da dallarla ilgili tüm işlemler Git Branches (Git Dalları) açılır penceresinde yapılır. Bu pencereyi açmak için Status bar (Durum çubuğu) üzerindeki Git widget'ına tıklayın veya Ctrl+Shift+` tuşlarına basın.

Şu anda checkout edilmiş dalın adı Status bar (Durum çubuğu) üzerindeki Git widget'ında görünür.

Açılan Branches (Dallar) penceresinde New Branch (Yeni Dal) seçeneğini seçin.

Açılan pencerede dal adını belirtin; örneğin "ahmet-yilmaz-eklendi". Bu dala geçmek istiyorsanız Checkout branch (Dalı checkout et) seçeneğinin işaretli olduğundan emin olun.

Yeni dal, mevcut HEAD'den başlatılır. Mevcut dalın HEAD'i yerine önceki bir commit'ten başlamak isterseniz, Version Control (Sürüm Kontrol) araç penceresinin Log (Günlük) sekmesinde (Alt+9) bu commit'i seçin ve içerik menüsünden New Branch (Yeni Dal) seçeneğini seçin.

## Gerekli değişiklikleri yapma

`Contributors.md` dosyasını açın ve dosyanın herhangi bir yerine isminizi ekleyin. Bu dosya, <a href="https://en.wikipedia.org/wiki/Markdown">markdown</a> söz diziminin tescilli bir çeşidi olan GFM (GitHub Flavored Markdown) içerir.

Söz dizimi doğru olsun diye diğer katkıda bulunanlardan birinin satırını kopyalayıp kendi adınızla değiştirin; bu konuda hassas olabilir.

## Değişiklikleri onaylama ve GitHub'a gönderme

Version Control (Sürüm Kontrol) araç penceresindeki Local Changes (Yerel Değişiklikler) sekmesinde commit etmek istediğiniz dosyaları veya tüm bir değişiklik listesini seçin ve Ctrl+K tuşlarına basın ya da araç çubuğundaki Commit (Onayla) düğmesine tıklayın.

Açılan Commit Changes (Değişiklikleri Onayla) penceresi, son commit'ten bu yana değiştirilen tüm dosyaları ve yeni eklenen, sürüm kontrolüne alınmamış dosyaları listeler.

Anlamlı bir commit mesajı girin.

Son commit mesajları arasından seçim yapmak için Commit Message history (Commit Mesajı Geçmişi) düğmesine tıklayabilir veya Ctrl+M tuşlarına basabilirsiniz.

Commit'i göndermeden önce commit mesajını daha sonra da düzenleyebilirsiniz.

Ctrl+Shift+K tuşlarına basın veya ana menüden `VCS | Git | Push` (VCS | Git | Gönder) yolunu izleyin. Push Commits (Commit'leri Gönder) penceresi açılır; bu pencere tüm Git depolarını (çoklu depo projeleri için) gösterir ve her depoda son push işleminden bu yana mevcut dalda yapılan commit'leri listeler.

## Değişikliklerinizi inceleme için gönderme

Bu noktada değişikliğinizi tamamlamış olacaksınız, ancak hâlâ sadece sizin deponuzda bulunur. Bu adım, üst seviye depo yöneticisinden değişikliğinizi birleştirmesini istemeyi gösterir.

GitHub'daki deponuzda, yeni dal bildiriminin yanında `Compare & pull request` (Karşılaştır ve çekme isteği) düğmesini göreceksiniz. Bu düğmeye tıklayın.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/compare-and-pull.png" alt="çekme isteği oluşturun" />

Şimdi çekme isteğini (pull request) gönderin.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/submit-pull-request.png" alt="çekme isteğini gönderin" />

Yakında tüm değişikliklerinizi bu projenin master (ana) dalıyla birleştireceğim. Değişiklikler birleştirildiğinde bir bildirim e-postası alacaksınız.

## Bundan sonra ne yapabilirim?

Tebrikler! Katkıda bulunan biri olarak sıkça karşılaşacağınız standart _fork -> clone -> edit -> PR_ iş akışını tamamladınız!

Katkınızı kutlayın ve [web uygulamasına](https://firstcontributions.github.io#social-share) giderek bunu arkadaşlarınız ve takipçilerinizle paylaşın.


### [Ek bilgi](../additional-material/git_workflow_scenarios/additional-material.md)

## Diğer araçlarla ilgili eğitimler
[Ana sayfaya dön](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
