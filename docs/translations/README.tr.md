[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# İlk katkı

Zor gelir... Herhangi bir işi ilk kez yapmak daima zor gelir. Özellikle başkalarıyla ortak çalışıyorsanız, hata yapmak içinize sinmez. Ancak "Açık Kaynakın" temelinde işbirliği ve birlikte çalışma yatmakta. Biz, açık kaynak projelere ilk kez katkıda bulunacak kişilerin bu süreci öğrenmesini ve ilk katkılarını sunmalarını kolaylaştırmayı istiyoruz.

Makale okumak ve eğitim videoları izlemek yardımcı olabilir, fakat bir işi gerçekten yapmanın yerini ne tutabilir ki? Bu proje yeni başlayanların veya ilk defa katkıda bulunacakların işini kolaylaştırmak ve onlara rehberlik etmek amacındadır. Unutmayın ki ne kadar rahat olursanız o kadar rahat öğrenirsiniz. Eğer bir GitHub projesine ilk defa katkıda bulunacaksanız, aşağıda gösterilen basit adımları takip etmeniz yeterli olacaktır. Söz veriyoruz, eğlenceli olacak.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Eğer bilgisayarınızda git kurulu değil ise, [ yükleyin ]( https://help.github.com/articles/set-up-git/ ).

## Projeyi "forklama"

Sayfanın sağ üst köşesinde bulunan "Fork" butonuna basıp bu projeyi çatallayın.
Bu işlem sizin hesabınız altında projenin bir kopyasını oluşturacaktır.

## Depoyu (Repository) klonlama

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Şimdi bu depoyu bilgisayarınıza klonlayın. GitHub hesabınıza gidin, çatalladığınız depoyu açın, 'clone' butonuna basıp ardından *copy to clipboard* simgesine basın.

Daha sonra komut istemini açıp aşağıdaki git komutunu çalıştırın:

```bash
git clone "kopyaladığınız-url"
```
"kopyaladığınız-url" (tırnak işaretleri olmadan) yerine bu deponun GitHub sayfasından aldığınız linki kopyalayın.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Örneğin:
```bash
git clone https://github.com/kullanıcı-adi/first-contributions.git
```
`kullanıcı-adi` sizin GitHub kullanıcı adınız. Burada GitHub üzerinde bulunan first-contributions reposunun içeriğini bilgisayarınıza kopyalıyorsunuz.

## Dal (Branch) oluşturma

Eğer henüz klasör içerisinde değilseniz komut isteminde ana klasörünün konumuna gidin:

```bash
cd first-contributions
```
`git checkout` komutunu kullanarak yeni bir dal(branch) oluşturun:
```bash
git checkout -b <sizin-yeni-dal-isminiz>
```

Örneğin:
```bash
git checkout -b ekle-aydin-cagri-dumlu
```
(Dal ismi içinde *ekle* kelimesinin geçme zorunluluğu yok, fakat bu dal isminizi katkı sunanlar listesine ekleme amacıyla oluşturulduğundan, ekle yazmak mantıklı olacaktır.)

## Gerekli değişiklikleri yapma ve değişiklikleri onaylama

Şimdi, bir metin editöründe `Contributors.md` dosyasını açın. Basit bir işaretleme dili olan Markdown'a alışkın olmanız gerekmektedir. Nasıl kullanacağınızı öğrenmek için bu [kopya kağıdına](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) göz atabilirsiniz.

`Contributors.md` dosyasının sonuna bu satırı ekleyin:

```markdown
- [İsminiz](https://github.com/kullanici-adiniz)
```

Örneğin:

```markdown
- [Ahmet Yılmaz](https://github.com/ahmet-yilmaz)
```

`](` arasında boşluk olmadığından emin olun. Dosyayı kaydedin ve kapatın.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Komut istemi üzerinde proje klasörüne gidip `git status` komutunu yazdığınızda yaptığınız değişiklikleri göreceksiniz.

`git add` komutu ile bu değişiklikleri oluşturduğunuz dal içerisine ekleyin.

```bash
git add Contributors.md
```

Şimdi `git commit` komutunu kullanarak değişikliklerinizi onaylayın (commit):
```bash
git commit -m "<isminiz> katkıda bulunanlar listesine eklendi"
```
`<isminiz>` yerine kendi isminizi yazın.

(Ç.N: Açık kaynak dünyasında dünyanın farklı yerlerinden insanlarla birlikte çalışacağınız için onay mesajını İngilizce yazabilirsiniz.)

## Değişiklikleri GitHub üzerine "itme" (Push)

`git push` komutu ile değişikliklerinizi ittirin:
```bash
git push origin <ekle-sizin-dal-isminiz>
```
`<ekle-sizin-dal-isminiz>` yerine daha önce oluşturduğunuz dalın ismini girin.

## Değişikliklerinizi inceleme için gönderin

Oluşturduğunuz deponun Github sayfasında `Compare & pull request` butonunu göreceksiniz. Bu butona basın.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Şimdi çekme isteğini (pull request) gönderin.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Yaptığınız değişiklikleri en kısa zamanda projenin "master" dalı ile birleştireceğiz. Bu işlem tamamlandığı zaman bir bilgilendirme e-postası alacaksınız.

## Bundan sonra ne yapabilirim?

Tebrikler! Katkıda bulunan kişi olarak sıklıkla karşılaşacağınız standart _çatal -> klon -> düzenle -> çekme isteği_ iş akışını tamamladınız!

Sunduğunuz katkının coşkusunu yaşamak ve bunu arkadaşlarınız ve takipçilerinizle paylaşmak için [bu bağlantıdaki](https://firstcontributions.github.io/#social-share) uygulamamızı kullanabilirsiniz.

Bir sorunuz veya yardıma ihtiyacınız olursa Slack takımımıza katılabilirsiniz. [Slack takımına katıl](https://firstcontributions.herokuapp.com)

Artık diğer projelere katkı sunmaya hazırsınız. Çözmeye başlayabileceğiniz giriş seviyesindeki konulara (issue) sahip projeleri [sizin için derledik](https://firstcontributions.github.io/#project-list).

### [Ek bilgi](../additional-material/git_workflow_scenarios/additional-material.md)

## Diğer araçlarla ilgili eğitimler


| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
