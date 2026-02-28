[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# First Contributions

|<img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Visual_Studio_2017_logo_and_wordmark.svg/2000px-Visual_Studio_2017_logo_and_wordmark.svg.png" width="200">|Visual Studio 2017 Edition|
|---|---|

Zor gelir. Herhangi bir işi ilk kez yapmak daima zor gelir. Özellikle başkalarıyla ortak çalışıyorsanız, hata yapmak içinize sinmez. Ancak "Açık Kaynağın" temelinde işbirliği ve birlikte çalışma yatmakta. Biz, açık kaynak projelere ilk kez katkıda bulunacak kişilerin bu süreci öğrenmesini ve ilk katkılarını sunmalarını kolaylaştırmayı istiyoruz.

Makale okumak ve eğitim videoları izlemek yardımcı olabilir, fakat bir işi gerçekten yapmanın yerini ne tutabilir ki? Bu proje yeni başlayanların veya ilk defa katkıda bulunacakların işini kolaylaştırmak ve onlara rehberlik etmek amacındadır. Unutmayın ki ne kadar rahat olursanız o kadar rahat öğrenirsiniz. Eğer bir GitHub projesine ilk defa katkıda bulunacaksanız, aşağıda gösterilen basit adımları takip etmeniz yeterli olacaktır. Söz veriyoruz, eğlenceli olacak.

Eğer bilgisayarınızda Visual Studio 2017 kurulu değilse, [ yükleyin ](https://www.visualstudio.com/downloads/).

## Projeyi "forklama"

<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/fork.png" alt="bu depoyu forklayın" />

Sayfanın üst kısmındaki "Fork" (Çatalla) düğmesine tıklayarak bu projeyi çatallayın. Bu işlem GitHub hesabınızda bu deponun bir kopyasını oluşturacaktır.

GitHub, deponuz ile çatalladığınız depo arasındaki ilişkiyi takip eder. Deponuzu bir çalışma kopyası olarak düşünebilirsiniz.

Diğer herhangi bir depodan çatallanmış olmayan (üst seviye) çoğu GitHub deposunun doğrudan değişiklik yapabilen küçük bir çekirdek ekibi vardır. Diğer tüm katkıda bulunanlar, depoyu çatallayıp değişiklikleri bu çatalda yapmalı ve değişikliklerin üst seviye depoya birleştirilmesini istemek için bir Pull Request (çekme isteği) oluşturmalıdır. Üst seviye depo yöneticisi değişiklikleri beğenirse birleştirilir ve anında şöhret ve servet kazanırsınız! Bunu nasıl yapacağınıza birazdan değineceğiz.

## Depoyu (Repository) klonlama

<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/clone.png" alt="depoyu klonlayın" />

Sonraki adım, değişiklik yapmaya başlayabilmek için deponuzu bilgisayarınıza klonlamaktır. Visual Studio deponuzun URL'sine ihtiyaç duyar; bu nedenle "clone" (klonla) düğmesine ve ardından "copy to clipboard" (Panoya kopyala) simgesine tıklayın.

**DİKKAT:** Yeni katkıda bulunanların sıkça yaptığı bir hata, çatalladıkları depoyu değil, orijinal depoyu klonlamaktır. Tarayıcınızın adres çubuğunu kontrol edin ve kendi deponuzu klonladığınızdan emin olun.

Artık Visual Studio 2017'ye geçme zamanı! Bu öğretici boyunca çoğunlukla Team Explorer (Takım Gezgini) sekmesinde çalışacaksınız. Varsayılan olarak açık değilse `View > Team Explorer` (Görünüm > Team Explorer) yoluna tıklayarak açın.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-01-clone1.png" alt="Team Explorer (Takım Gezgini)" />

Team Explorer (Takım Gezgini) birden fazla görünüm sunar ve farklı alanlara geçişi kolaylaştırmak için üst kısımda gezinme düğmeleri bulunur. Bir depoyu klonlamak için Connect (Bağlan) görünümünde olmanız gerekir; bu görünüm varsayılan olarak gelmelidir. "clone" (klonla) düğmesini görmüyorsanız, üstteki yeşil fiş simgesine tıklayın.

**Local Git Repositories** (Yerel Git Depoları) altında `Clone` (Klonla) seçeneğine tıklayın ve deponuzun URL'sini metin kutusuna yapıştırın. Bu, az önce GitHub'dan panonuza kopyaladığınız URL olmalıdır.

İşlemi başlatmak için `Clone` (Klonla) düğmesine tıklayın.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-02-clone2.png" alt="Depoyu klonlayın" />

İşlem tamamlandığında Solution Explorer (Çözüm Gezgini) sekmesine geçersiniz ve deponuzun içeriğini görebilirsiniz. Sizdeki görünüm aşağıdaki ekran görüntüsünden farklı olabilir; bu gayet normal.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-03-clone3.png" alt="Solution Explorer (Çözüm Gezgini)" />

## Dal (Branch) oluşturma

Tekrar Team Explorer (Takım Gezgini) sekmesine tıklayın ve ana gezinme açılır menüsünden Branches (Dallar) görünümünü açın.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-04-branch1.png" alt="Branches görünümü" />

**first-contributions** deposunu ve varsayılan dal olan `master` (ana) dalını görmelisiniz. `master` (ana) dalı üzerine sağ tıklayın ve `New Local Branch From...` (Yeni Yerel Dal Oluştur...) seçeneğini seçin.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-05-branch2.png" alt="Yeni dal" />

Dalınıza `isminiz-eklendi` gibi bir isim verin. Örneğin: `ahmet-yilmaz-eklendi`.

`Checkout branch` (Dalı checkout et) kutusunu işaretli bırakın ve `Create Branch` (Dal Oluştur) düğmesine tıklayın.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-06-branch3.png" alt="Dal oluşturun" />

Yeni dalınızı listede görmelisiniz.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-07-branch4.png" alt="Yeni dalı görün" />

## Gerekli değişiklikleri yapma

`Contributors.md` dosyasını açın ve listenin sonuna adınızı ekleyin. Bu dosya, <a href="https://en.wikipedia.org/wiki/Markdown">markdown</a> söz diziminin tescilli bir çeşidi olan GFM (GitHub Flavored Markdown) içerir.

Söz dizimi doğru olsun diye diğer katkıda bulunanlardan birinin satırını kopyalayıp kendi adınızla değiştirin; bu konuda hassas olabilir.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-08-change1.png" alt="İsminizi ekleyin" />

## Değişiklikleri onaylama ve GitHub'a gönderme

Team Explorer (Takım Gezgini) sekmesine geri dönün ve Changes (Değişiklikler) görünümüne geçin.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-09-commit1.png" alt="Değişiklikler" />

Commit ile göndermek istediğiniz bilgileri girin ve `Save` (Kaydet) düğmesine tıklayın. Visual Studio bunu gelecekteki commit'ler için hatırlayacaktır.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-10-commit2.png" alt="Git kullanıcı bilgileri" />

**Not:** Visual Studio, kişisel ayar ve tercihlerinizi saklamak için `.vs` adlı gizli bir klasör kullanır. Bu klasörün içeriği **Git'e kaydedilmemelidir**.
Bu klasör daha önce göz ardı edilmediyse, Git'e bu klasörü yok saymasını söylemeniz gerekebilir.

Bu klasör bu depoda zaten yok sayılıyor; dolayısıyla bu adımı uygulamanıza gerek yoktur. Bu bilgi sadece gelecekteki projeleriniz için bir nottur.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-11-commit3.png" alt="vs klasörünü yok say" />

Artık değişen dosyaların listesini ve bir commit yorumu yazabileceğiniz bir metin kutusunu görmelisiniz. Yorumlar kısa ama açıklayıcı olmalıdır. Şunu görmekten daha kötüsü yoktur: "I updated some stuff". Birkaç saniye ayırıp commit'inizi özetleyin. Ekibiniz size teşekkür edecektir, hatta siz bile kendinize teşekkür edebilirsiniz!

Yerel commit oluşturup değişikliklerinizi deponuza tek adımda göndermek için `Commit All and Push` (Hepsini Onayla ve Gönder) düğmesine tıklayın.

**Not:** Commit, Push işleminden ayrı yapılabilir. Burada kolaylık olması için ikisini birden yapıyoruz. Commit değişiklikleri yerelde kaydeder, ancak Push yapana kadar GitHub deponuzda görünmez.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-12-commit4.png" alt="Onayla ve gönder" />

İlk kez GitHub'a Push yaptığınızda Visual Studio sizden GitHub kimlik bilgilerinizi isteyecektir. Bu bilgiler önbelleğe alınır; bu nedenle bu ekranı sık görmezsiniz.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-13-commit5.png" alt="Giriş" />

Push işlemi tamamlandıktan sonra deponuzu GitHub'da açın; yakın zamanda gönderilmiş bir dalı belirten bir mesaj görmelisiniz.

`Branch: master` (Dal: master) açılır menüsünü açıp yeni dalınızı seçerek değişikliklerinizi görüntüleyebilirsiniz. Tebrikler, dal URL'sini paylaşarak ilerlemenizi dünyaya gösterebilirsiniz!

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-14-commit6.png" alt="GitHub'da gönderilen dalı görün" />

## Değişikliklerinizi inceleme için gönderme

Bu noktada değişikliğinizi tamamlamış olacaksınız, ancak hâlâ sadece sizin deponuzda bulunur. Bu adım, üst seviye depo yöneticisinden değişikliğinizi birleştirmesini istemeyi gösterir.

GitHub'daki deponuzda, yeni dal bildiriminin yanında `Compare & pull request` (Karşılaştır ve çekme isteği) düğmesini göreceksiniz. Bu düğmeye tıklayın.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/compare-and-pull.png" alt="çekme isteği oluşturun" />

Şimdi çekme isteğini (pull request) gönderin.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/submit-pull-request.png" alt="çekme isteğini gönderin" />

Yakında tüm değişikliklerinizi bu projenin master (ana) dalıyla birleştireceğim. Değişiklikler birleştirildiğinde bir bildirim e-postası alacaksınız.

## Bundan sonra ne yapabilirim?

Tebrikler! Katkıda bulunan biri olarak sıkça karşılaşacağınız standart _fork -> clone -> edit -> PR_ iş akışını tamamladınız!

Katkınızı kutlayın ve [web uygulamasına](https://firstcontributions.github.io#social-share) giderek bunu arkadaşlarınız ve takipçilerinizle paylaşın.

### [Ek bilgi](../additional-material/git_workflow_scenarios/additional-material.md)

## Diğer araçlarla ilgili eğitimler

| <a href="github-desktop-tutorial.tr.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="github-windows-vs2017-tutorial.tr.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gitkraken-tutorial.tr.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="github-windows-vs-code-tutorial.tr.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="sourcetree-macos-tutorial.tr.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="github-windows-intellij-tutorial.tr.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](github-desktop-tutorial.tr.md)                                                                                                                 | [Visual Studio 2017](github-windows-vs2017-tutorial.tr.md)                                                                                                                                            | [GitKraken](gitkraken-tutorial.tr.md)                                                                                                                                                           | [Visual Studio Code](github-windows-vs-code-tutorial.tr.md)                                                                                                                                      | [Atlassian Sourcetree](sourcetree-macos-tutorial.tr.md)                                                                                                                                          | [IntelliJ IDEA](github-windows-intellij-tutorial.tr.md)                                                                                                                                           |

[Ana sayfaya dön](../../../translations/README.tr.md#diğer-araçlarla-ilgili-eğitimler)
