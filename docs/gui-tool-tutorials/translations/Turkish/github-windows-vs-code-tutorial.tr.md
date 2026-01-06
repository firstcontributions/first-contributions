[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# First Contributions

| <img alt="Visual Studio Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width="40"> | Visual Studio Code |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |


Zor gelir. Herhangi bir işi ilk kez yapmak daima zor gelir. Özellikle başkalarıyla ortak çalışıyorsanız, hata yapmak içinize sinmez. Ancak "Açık Kaynağın" temelinde işbirliği ve birlikte çalışma yatmakta. Biz, açık kaynak projelere ilk kez katkıda bulunacak kişilerin bu süreci öğrenmesini ve ilk katkılarını sunmalarını kolaylaştırmayı istiyoruz.

Makale okumak ve eğitim videoları izlemek yardımcı olabilir, fakat bir işi gerçekten yapmanın yerini ne tutabilir ki? Bu proje yeni başlayanların veya ilk defa katkıda bulunacakların işini kolaylaştırmak ve onlara rehberlik etmek amacındadır. Unutmayın ki ne kadar rahat olursanız o kadar rahat öğrenirsiniz. Eğer bir GitHub projesine ilk defa katkıda bulunacaksanız, aşağıda gösterilen basit adımları takip etmeniz yeterli olacaktır. Söz veriyoruz, eğlenceli olacak.

Eğer bilgisayarınızda Visual Studio Code kurulu değilse, [ yükleyin ](https://code.visualstudio.com/download).

**Not:** Bu öğretici Windows 10 üzerinde Visual Studio Code (Sürüm 1.27.2) kullanılarak hazırlanmıştır. Bu öğreticide bazı klavye kısayolları kullanacağız. Bunlar diğer işletim sistemlerinde (macOS/Linux) ve klavye düzenlerinde (UK, DE vb.) farklı olabilir. Kısayol listenizi Command Palette (Komut Paleti) içinde "shortcut" (kısayol) araması yaparak görebilirsiniz.

## Projeyi "forklama"

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="bu depoyu forklayın" />

Sayfanın sağ üst köşesinde bulunan "Fork" (Çatalla) düğmesine tıklayarak bu projeyi çatallayın. Bu işlem sizin hesabınız altında projenin bir kopyasını oluşturacaktır.

GitHub, deponuz ile çatalladığınız depo arasındaki ilişkiyi takip eder. Deponuzu bir çalışma kopyası olarak düşünebilirsiniz.

Diğer herhangi bir depodan çatallanmış olmayan (üst seviye) çoğu GitHub deposunun doğrudan değişiklik yapabilen küçük bir çekirdek ekibi vardır. Diğer tüm katkıda bulunanlar, depoyu çatallayıp değişiklikleri bu çatalda yapmalı ve değişikliklerin üst seviye depoya birleştirilmesini istemek için bir Pull Request (çekme isteği) oluşturmalıdır. Üst seviye depo yöneticisi değişiklikleri beğenirse birleştirilir ve anında şöhret ve servet kazanırsınız! Bunu nasıl yapacağınıza birazdan değineceğiz.

## Depoyu (Repository) klonlama

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="depoyu klonlayın" />

Sonraki adım, değişiklik yapmaya başlayabilmek için deponuzu bilgisayarınıza klonlamaktır. VS Code, deponuzun URL'sine ihtiyaç duyar; bu nedenle "Code" (Kod) düğmesine ve ardından "copy to clipboard" (Panoya kopyala) simgesine tıklayın.

**DİKKAT:** Yeni katkıda bulunanların sıkça yaptığı bir hata, çatalladıkları depoyu değil, orijinal depoyu klonlamaktır. Tarayıcınızın adres çubuğunu kontrol edin ve kendi deponuzu klonladığınızdan emin olun.

Şimdi Visual Studio Code'u açın. VS Code'un karşılama sayfası açılacaktır. Buradan `F1` tuşuna basarak aşağıdaki çubuğu açın. Metin alanında zaten bir `>` (büyüktür) işareti olduğunu fark edeceksiniz. Giriş alanına `CTRL-P` tuşlarına basarak da erişebilir ve ardından `>` karakterini yazabilirsiniz.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone.png" alt="Klon penceresi (Komut penceresi)" />

Aşağıda bazı karışık komutların listelendiğini görebilirsiniz. Bunlar daha önce kullanılan komutlardır. Bunları dikkate almayabilirsiniz.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone1.png" alt="Depoyu klonlayın" />

Şimdi `git clone`, yalnızca `git` ya da `clone` yazın (arama gibi çalışır).
`Git: Clone` (Git: Klonla) girdisini seçip `Enter` tuşuna basın.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone2.png" alt="Depo URL'sini yapıştırın" />

Depo URL'sini yapıştırın ve `Enter` tuşuna basın. Bu, Git deposunun kaydedileceği yeri seçebileceğiniz bir File Explorer (Dosya Gezgini) penceresi açacaktır.

**Önemli**: Çatalladığınız depo olduğundan ve orijinal depo olmadığından emin olun; aksi halde çalışmaz.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone3.png" alt="Durum penceresi" />

Visual Studio Code'un sağ alt kısmında bir durum bildirimi görmelisiniz. İşlem tamamlandığında, iletişim kutusundaki düğmeleri kullanarak klonlanan depoyu (artık bilgisayarınızdaki bir klasör) açabilirsiniz.

## Dal (Branch) oluşturma

`F1` tuşuna basarak Command Palette'i (Komut Paleti) tekrar açın. `branch` yazın ve `create branch` (dal oluştur) komutunu seçin. Bir sonraki adımda yeni dalınızın adını yazın; örneğin `ahmet-yilmaz-eklendi`. `Enter` tuşuna basın; dal oluşturulacaktır. Dal ayrıca otomatik olarak checkout (geçerli dal yapma) edilmiş olur. [Checkout ne demek?](https://www.git-scm.com/docs/git-checkout)

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-branch.png" alt="Dal Komut Paleti" />

## Gerekli değişiklikleri yapma

`Contributors.md` dosyasını açın ve dosyanın herhangi bir yerine isminizi ekleyin. Bu dosya, <a href="https://en.wikipedia.org/wiki/Markdown">markdown</a> söz diziminin tescilli bir çeşidi olan GFM (GitHub Flavored Markdown) içerir.

Diğer katkıda bulunanlardan birinin satırını kopyalayın ve söz dizimi doğru olacak şekilde kendi adınızla değiştirin. Dosyayı kaydedin.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-changes.png" alt="İsminizi ekleyin" />

## Değişiklikleri onaylama ve GitHub'a gönderme

VS Code'un sol tarafında 5 ikonlu bir menü bulunur. Sürüm kontrolü/Source Control (Kaynak Kontrol) ikonunu seçin.
(Kısayol: Ctrl + Shift + G)

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-commit.png" alt="Değişiklikleri onaylayın" />

File Explorer (Dosya Gezgini), son commit'ten sonra değişen tüm dosyaları gösterir. Dosyaların üzerine gelip `+` (artı) düğmesine tıklayarak dosyaları stage (sahneleme) edebilirsiniz.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-commit1.png" alt="Sahnelenen dosyalar">

Gezginin üst kısmındaki satıra bir commit mesajı yazın ve onay işaretine tıklayın. Değişiklikler artık yerel kopyanıza commit edilmiştir. Şimdi değişikliklerin GitHub'a gönderilmesi gerekir.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-push.png" alt="Sahnelenen dosyalar">

Üç nokta simgesiyle menüyü açıp `Publish Branch` (Dal Yayınla) seçeneğini seçin. Bu işlem, GitHub kimlik bilgilerinizin girileceği bir iletişim kutusu açacaktır.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-gh-auth.png" alt="Sahnelenen dosyalar">

## Değişikliklerinizi inceleme için gönderme

Bu noktada değişikliğinizi tamamlamış olacaksınız, ancak hâlâ sadece sizin deponuzda bulunur. Bu adım, üst seviye depo yöneticisinden değişikliğinizi birleştirmesini istemeyi gösterir.

GitHub'daki deponuzda, yeni dal bildiriminin yanında `Compare & pull request` (Karşılaştır ve çekme isteği) düğmesini göreceksiniz. Bu düğmeye tıklayın.

<img src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="çekme isteği oluşturun" />

Şimdi çekme isteğini (pull request) gönderin.

<img src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="çekme isteğini gönderin" />

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
