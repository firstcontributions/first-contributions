[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# First Contributions

|<img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="200">|GitKraken Edition|
|---|---|

Zor gelir. Herhangi bir işi ilk kez yapmak daima zor gelir. Özellikle başkalarıyla ortak çalışıyorsanız, hata yapmak içinize sinmez. Ancak "Açık Kaynağın" temelinde işbirliği ve birlikte çalışma yatmakta. Biz, açık kaynak projelere ilk kez katkıda bulunacak kişilerin bu süreci öğrenmesini ve ilk katkılarını sunmalarını kolaylaştırmayı istiyoruz.

Makale okumak ve eğitim videoları izlemek yardımcı olabilir, fakat bir işi gerçekten yapmanın yerini ne tutabilir ki? Bu proje yeni başlayanların veya ilk defa katkıda bulunacakların işini kolaylaştırmak ve onlara rehberlik etmek amacındadır. Unutmayın ki ne kadar rahat olursanız o kadar rahat öğrenirsiniz. Eğer bir GitHub projesine ilk defa katkıda bulunacaksanız, aşağıda gösterilen basit adımları takip etmeniz yeterli olacaktır. Söz veriyoruz, eğlenceli olacak.


## GitKraken

[GitKraken](https://www.gitkraken.com) uygulamasını indirin, kurun ve açın.

"Welcome to GitKraken" (GitKraken'e hoş geldiniz) başlıklı bir açılır pencere görmelisiniz. "Sign in with GitHub" (GitHub ile oturum aç) seçeneğiyle giriş yapın ve GitKraken'in GitHub hesabınıza erişmesine izin verin.


<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-login.png" alt="GitHub'a giriş yapın" />

(İsteğe bağlı) File -> Preferences (Dosya -> Tercihler) yoluna gidip proje dizininizi yerel depolarınızın kök dizini olarak ayarlayın.


## Projeyi "forklama"

Sayfanın üst kısmındaki "Fork" (Çatalla) düğmesine tıklayarak bu projeyi çatallayın.
<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/fork.png" alt="bu depoyu forklayın" />
Bu işlem sizin hesabınız altında projenin bir kopyasını oluşturacaktır.


## Depoyu (Repository) klonlama

GitKraken'de File -> Clone Repo (Dosya -> Depo Klonla) yoluna gidin.


<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-clone.png" alt="depoyu klonlayın" />


Sağ panelde "GitHub.com" seçeneğini seçin. Kullanıcı adınızın altında first-contributions deposunu görmelisiniz. Bu depoya tıklayın ve panelin alt kısmında görünen tam yolu kontrol edin.

Yol bilgisinden emin olduğunuzda "Clone the repo!" (Depoyu klonla!) düğmesine tıklayın.


## Dal (Branch) oluşturma

Araç çubuğundaki "Branch" (Dal) düğmesine tıklayın.

Dalınıza <isminiz-eklendi> gibi bir isim verin. Örneğin: "ahmet-yilmaz-eklendi"

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-branch.png" alt="dalınıza isim verin" />


## Gerekli değişiklikleri yapma ve değişiklikleri onaylama

Şimdi `Contributors.md` dosyasını bir metin düzenleyicide açın, isminizi ekleyin ve dosyayı kaydedin.

Depo GitKraken'de açıksa değişiklikler olduğunu göreceksiniz. "// WIP" etiketiyle işaretlenmiş en yeni kaydı seçip değişen dosya sayısını ve değişiklik türünü kontrol ederek değişiklikleri gözden geçirin ve stage (sahneleme) işlemini yapın.

Değişen dosyaları inceleyip hangilerini stage (sahneleme) etmek istediğinize karar verin. Staging (sahneleme), bu commit ile ilişkilendirmek istediğiniz dosya değişikliklerini Git'e net şekilde söylemek için önemlidir.


<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-edit.png" alt="dosyaları düzenleyin" />


<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-stage.png" alt="değişiklikleri sahneleyin" />

Uygun bir commit mesajı seçtikten sonra ("Add <isminiz> to Contributors list" açıklayıcı bir mesajdır) ve değişikliklerinizden memnunsanız, tüm değişiklikleri sahnelemek için "Stage all changes" (Tüm değişiklikleri sahnele) ya da tek bir dosyayı sahnelemek için "Stage File" (Dosyayı sahnele) seçeneğine tıklayın.


<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-commit.png" alt="değişiklikleri onaylayın" />


Fikrinizi değiştirirseniz bu değişiklikleri unstage (sahnelemeden çıkar) edebilir ya da tamamen discard (sil) edebilirsiniz.
UYARI: discard (sil) ifadesinin de ima ettiği gibi bu işlem geri alınamaz. Sadece bulunduğunuz depodaki değişiklikleri istemiyorsanız uygulayın.

"Commit" (Onayla) düğmesine tıklayın.

Tebrikler, first-contributions çatallarınızdaki dalın yerel kopyasına tüm değişiklikleri onayladınız. Şimdi sırada sonraki adımlar var!


## Değişiklikleri GitHub'a gönderme

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-push.png" alt="değişikliklerinizi gönderin" />

Araç çubuğundaki "Push" (Gönder) düğmesine tıklayın.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-origin.png" alt="origin ya da dal" />

Değişikliklerin master (ana) dalda doğrudan görünmesini istiyorsanız origin (uzak depo) dalını seçin; aksi halde göndermek istediğiniz uygun dalı seçin.


## Değişikliklerinizi inceleme için gönderme

GitHub'daki deponuza giderseniz `Compare & pull request` (Karşılaştır ve çekme isteği) düğmesini göreceksiniz. Bu düğmeye tıklayın.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/compare-and-pull.png" alt="çekme isteği oluşturun" />

Şimdi çekme isteğini (pull request) gönderin.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/submit-pull-request.png" alt="çekme isteğini gönderin" />

Yakında tüm değişikliklerinizi bu projenin master (ana) dalıyla birleştireceğim. Değişiklikler birleştirildiğinde bir bildirim e-postası alacaksınız.

## Bundan sonra ne yapabilirim?

Tebrikler! Katkıda bulunan biri olarak sıkça karşılaşacağınız standart _fork -> clone -> edit -> PR_ iş akışını tamamladınız!

Katkınızı kutlayın ve [web uygulamasına](https://firstcontributions.github.io/#social-share) giderek bunu arkadaşlarınız ve takipçilerinizle paylaşın.

### [Ek bilgi](../additional-material/git_workflow_scenarios/additional-material.md)


## Diğer araçlarla ilgili eğitimler

| <a href="github-desktop-tutorial.tr.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="github-windows-vs2017-tutorial.tr.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gitkraken-tutorial.tr.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="github-windows-vs-code-tutorial.tr.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="sourcetree-macos-tutorial.tr.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="github-windows-intellij-tutorial.tr.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](github-desktop-tutorial.tr.md)                                                                                                                 | [Visual Studio 2017](github-windows-vs2017-tutorial.tr.md)                                                                                                                                            | [GitKraken](gitkraken-tutorial.tr.md)                                                                                                                                                           | [Visual Studio Code](github-windows-vs-code-tutorial.tr.md)                                                                                                                                      | [Atlassian Sourcetree](sourcetree-macos-tutorial.tr.md)                                                                                                                                          | [IntelliJ IDEA](github-windows-intellij-tutorial.tr.md)                                                                                                                                           |

[Ana sayfaya dön](../../../translations/README.tr.md#diğer-araçlarla-ilgili-eğitimler)
