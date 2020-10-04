[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-hfcq788y-QaXzXT5clBBWukXQyBhH4w)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# İlk katkılar

Zordur. Bir işi ilk kez yapmak her zaman zordur. Özellikle birileriyle işbirliği içindeyseniz, hata yapmak içinize sinmez. Fakat açık kaynağın temelinde işbirliği ve birlikte çalışma yatar. Biz açık kaynak projelere ilk kez katkıda bulunacak kişilerin süreci öğrenmesini ve ilk katkılarını sunmalarını kolaylaştırmak istiyoruz.

Makale okumak ve eğitim videoları izlemek yardımcı olabilir, fakat bir işi gerçekten yapmanın yerini ne tutabilir ki? Bu proje yeni başlayanların veya ilk defa katkıda bulunacakların işini kolaylaştırmayı ve onlara rehberlik etmeyi amaçlıyor. İlk katkınızı yapmak istiyorsanız, aşağıdaki adımları takip edin.

#### _Eğer komut satırı kullanmak konusunda pek rahat değilseniz, [GUI araçlarla ilgili eğitimler burada..](#diğer-araçlarla-ilgili-eğitimler)_


<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="bu depoyu çatallandırın" />

#### Eğer bilgisayarınızda git yoksa, [yükleyin](https://help.github.com/articles/set-up-git/).

## Bu depoyu çatallandırın (Fork)

Sayfanın sağ üst köşesinde bulunan "Fork" butonuna basıp bu depoyu çatallandırın.
Bu işlem sizin hesabınız altında bu deponun bir kopyasını oluşturacaktır.

## Depoyu klonlayın (Clone)

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="bu depoyu klonlayın" />

Şimdi çatalladığınız depoyu bilgisayarınıza klonlayın. GitHub hesabınıza gidin, çatalladığınız depoyu açın, Bunun için code butonuna basıp ardından _copy to clipboard_ ikonuna basın.

Bir komut istemi açın ve aşağıdaki git komutunu girin:

```
git clone "kopyaladığınız-url"
```

"kopyaladığınız-url" (tırnak işaretleri olmadan) bu deponun url adresidir (bu projenin sizin çatalladığınız hali). URL'yi elde etmek için önceki adımlara bakın.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="URL adresini kopyalayın" />

Örneğin:

```
git clone https://github.com/bu-sizsiniz/first-contributions.git
```

`bu-sizsiniz` sizin GitHub kullanıcı adınız. Burada GitHub üzerinde bulunan first-contributions deposunun içeriğini bilgisayarınıza kopyalıyorsunuz.

## Bir dal oluşturun (Branch)

Bilgisayarınızda deponun klasörüne geçin (eğer zaten orada değilseniz):

```
cd first-contributions
```

Şimdi de `git checkout` komutunu kullanarak yeni bir dal(branch) oluşturun:

```
git checkout -b yeni-dalinizin-ismi
```

Örneğin:

```
git checkout -b ekle-aydin-cagri-dumlu
```

(Dal ismi içinde *ekle* kelimesinin geçme zorunluluğu yok, fakat bu dal isminizi katkı sunanlar listesine ekleme amacıyla oluşturulduğundan, ekle yazmak mantıklı olacaktır.)

## Gerekli değişiklikleri yapın ve bu değişiklikleri işleyin (Commit)

Şimdi bir metin editöründe `Contributors.md` dosyasını açın, adınızı bu dosyaya ekleyin. Dosyanın başına veya sonuna eklemeyin. Aradaki herhangi bir yere koyun. Şimdi, dosyayı kaydedin.

<img align="right" width="450" src="../assets/git-status.png" alt="git status" />

Komut istemi üzerinde proje klasörüne gidip `git status` komutunu çalıştırdığınızda yaptığınız değişiklikleri göreceksiniz.

`git add` komutu ile bu değişiklikleri oluşturduğunuz dal içine ekleyin:

```
git add Contributors.md
```

Şimdi `git commit` komutunu kullanarak değişikliklerinizi işleyin (commit):

```
git commit -m "<sizin-isminiz> katkıda bulunanlar listesine eklendi"
```

`<sizin-isminiz>` yerine kendi isminizi yazın.

> *Çevirmen Notu:* Açık kaynak dünyasında, dünyanın farklı yerlerinden insanlarla birlikte çalışacağınız için, onay mesajını İngilizce de yazabilirsiniz.

## Değişiklikleri GitHub'a itin (Push)

`git push` komutu ile değişikliklerinizi itin:

```
git push origin <yeni-dalinizin-ismi>
```

`<yeni-dalinizin-ismi>` yerine daha önce oluşturduğunuz dalın ismini girin.

## Değişikliklerinizi incelenmesi için gönderin

Oluşturduğunuz deponun Github sayfasında `Compare & pull request` butonunu göreceksiniz. Bu butona basın.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="çekme isteği oluşturun" />

Şimdi çekme isteğini (pull request) gönderin.

<img style="float: right;" src="../assets/submit-pull-request.png" alt="çekme isteğini gönderin" />

En kısa zamanda yaptığınız tüm değişiklikleri bu projenin "master" dalı ile birleştireceğim. Değişiklikleriniz birleştirildiği zaman bir bilgilendirme e-postası alacaksınız.

## Bundan sonra ne yapabilirim?

Tebrikler! Katkıda bulunurken sıklıkla karşılaşacağınız standart _fork -> clone -> edit -> pull request_ iş akışını az önce tamamladınız!

Sunduğunuz katkının coşkusunu yaşayın ve [web uygulamamızı](https://roshanjossey.github.io/first-contributions/#social-share) kullanarak arkadaşlarınız ve takipçilerinizle de paylaşın

Bir sorunuz veya yardıma ihtiyacınız olursa Slack takımımıza katılabilirsiniz. [Slack takımına katıl](https://firstcontributions.herokuapp.com).

Artık diğer projelere katkı sunmaya hazırsınız. Çözmeye başlayabileceğiniz giriş seviyesindeki sorunlara (issue) sahip projeleri [sizin için derledik](https://roshanjossey.github.io/first-contributions/#project-list).

### [Ek materyal](../additional-material/git_workflow_scenarios/additional-material.md)

## Diğer araçlarla ilgili eğitimler

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="../assets/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/IntelliJ_IDEA_Logo.svg" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                               | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                   |
