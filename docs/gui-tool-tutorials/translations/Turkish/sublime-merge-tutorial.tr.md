[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# First Contributions

|<img alt="Sublime Merge" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sublime-merge-tutorial/sublime-merge.png" width="200">|Sublime Merge Git Client|
|---|---|

Zor gelir. Herhangi bir işi ilk kez yapmak daima zor gelir. Özellikle başkalarıyla ortak çalışıyorsanız, hata yapmak içinize sinmez. Ancak "Açık Kaynağın" temelinde işbirliği ve birlikte çalışma yatmakta. Biz, açık kaynak projelere ilk kez katkıda bulunacak kişilerin bu süreci öğrenmesini ve ilk katkılarını sunmalarını kolaylaştırmayı istiyoruz.

Makale okumak ve eğitim videoları izlemek yardımcı olabilir, fakat bir işi gerçekten yapmanın yerini ne tutabilir ki? Bu proje yeni başlayanların veya ilk defa katkıda bulunacakların işini kolaylaştırmak ve onlara rehberlik etmek amacındadır. Unutmayın ki ne kadar rahat olursanız o kadar rahat öğrenirsiniz. Eğer bir GitHub projesine ilk defa katkıda bulunacaksanız, aşağıda gösterilen basit adımları takip etmeniz yeterli olacaktır. Söz veriyoruz, eğlenceli olacak.


## Sublime Merge

[Sublime Merge](https://www.sublimemerge.com/) uygulamasını indirin, kurun ve açın.

## Projeyi "forklama"

Sayfanın üst kısmındaki "Fork" (Çatalla) düğmesine tıklayarak bu projeyi çatallayın.
<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sublime-merge-tutorial/fork.png" alt="bu depoyu forklayın" />
Bu işlem sizin hesabınız altında projenin bir kopyasını oluşturacaktır.

<br>
<br>
<br>
<br>

## Depoyu (Repository) klonlama

<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sublime-merge-tutorial/clone.png" alt="depoyu klonlayın" />

Sublime Merge'de File -> Clone Repository (Dosya -> Depo Klonla) yoluna gidin.


<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sublime-merge-tutorial/sm-clone.png" alt="depoyu klonlayın" />

Depoyu klonlama adımı, değişiklik yapabilmek için deponuzu bilgisayarınıza kopyalamanızı sağlar. Sublime Merge, deponuzun URL'sine ihtiyaç duyar; bu nedenle "clone" (Klonla) düğmesine ve ardından "copy to clipboard" (Panoya kopyala) simgesine tıklayın.

**DİKKAT:** Yeni katkıda bulunanların sıkça yaptığı bir hata, çatalını aldıkları depoyu değil, orijinal depoyu klonlamaktır. Tarayıcınızın adres çubuğunu kontrol edin ve kendi deponuzu klonladığınızdan emin olun.


Sublime Merge'e depo URL'sini girin, bir depo adı verin (ya da boş bırakın) ve deponun kaydedileceği dizini seçin.

Yoldan emin olduğunuzda "Clone" (Klonla) düğmesine tıklayın.


## Dal (Branch) oluşturma

Branches -> Create Branch (Dallar -> Dal Oluştur) seçeneğine sağ tıklayın
veya
Repository -> Create Branch (Depo -> Dal Oluştur) yolunu izleyin.

Dalınıza <isminiz-eklendi> gibi bir isim verin. Örneğin: "ahmet-yilmaz-eklendi"

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sublime-merge-tutorial/sm-branch.png" alt="dalınıza isim verin" />


## Gerekli değişiklikleri yapma ve değişiklikleri onaylama

Şimdi `Contributors.md` dosyasını bir metin düzenleyicide açın, isminizi ekleyin ve dosyayı kaydedin.

Depo Sublime Merge'de açıksa değişiklikler olduğunu göreceksiniz.
Üstteki en yeni commit'i seçin; bu öğe "x unstaged files" (x sahnelenmemiş dosya) olarak görünür.
Değişen dosyaları gözden geçirip hangilerini stage (sahneleme) etmek istediğinize karar verin.
Commit mesajı girin ("Add <isminiz> to Contributors list" açıklayıcı bir mesajdır).
Değişikliklerden memnunsanız dosyaları tek tek sahneleyerek ya da "stage all" (hepsini sahnele) seçeneğini kullanarak stage edin. Staging (sahneleme), bu commit ile ilişkilendirmek istediğiniz dosya değişikliklerini Git'e net şekilde söylemek için önemlidir.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sublime-merge-tutorial/sm-stage.png" alt="değişiklikleri sahneleyin" />

Fikrinizi değiştirirseniz bu değişiklikleri unstage (sahnelemeden çıkar) edebilir ya da tamamen discard (sil) edebilirsiniz.
UYARI: discard (sil) ifadesinin de ima ettiği gibi bu işlem geri alınamaz. Sadece bulunduğunuz depodaki değişiklikleri istemiyorsanız uygulayın.

"Commit" (Onayla) düğmesine tıklayın, kullanıcı adınızı ve e-posta adresinizi girip "Update" (Güncelle) düğmesine basın.

"Commit" (Onayla) düğmesine tekrar tıklayın.

Tebrikler, first-contributions çatallarınızdaki dalın yerel kopyasına tüm değişiklikleri onayladınız. Şimdi sırada sonraki adımlar var!


## Değişiklikleri GitHub'a gönderme

Repository -> Push (Depo -> Gönder) yolunu izleyin
veya
sağ üst köşedeki yukarı yönlü küçük oka tıklayın.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sublime-merge-tutorial/sm-login.png" alt="giriş yapın" />

GitHub hesabınıza kullanıcı adınız ve parolanızla giriş yapın.

Değişikliklerin master (ana) dalda doğrudan görünmesini istiyorsanız origin (uzak depo) dalını seçin; aksi halde göndermek istediğiniz uygun dalı seçin.


## Değişikliklerinizi inceleme için gönderme

GitHub'daki deponuza giderseniz `Compare & pull request` (Karşılaştır ve çekme isteği) düğmesini göreceksiniz. Bu düğmeye tıklayın.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sublime-merge-tutorial/compare-and-pull.png" alt="çekme isteği oluşturun" />

Şimdi çekme isteğini (pull request) gönderin.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sublime-merge-tutorial/submit-pull-request.png" alt="çekme isteğini gönderin" />

Yakında tüm değişikliklerinizi bu projenin master (ana) dalıyla birleştireceğim. Değişiklikler birleştirildiğinde bir bildirim e-postası alacaksınız.

## Bundan sonra ne yapabilirim?

Tebrikler! Katkıda bulunan biri olarak sıkça karşılaşacağınız standart _fork -> clone -> edit -> PR_ iş akışını tamamladınız!

Katkınızı kutlayın ve [web uygulamasına](https://firstcontributions.github.io#social-share) giderek bunu arkadaşlarınız ve takipçilerinizle paylaşın.

### [Ek bilgi](../additional-material/git_workflow_senarios/additional-material.md)


## Diğer araçlarla ilgili eğitimler

| <a href="github-desktop-tutorial.tr.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="github-windows-vs2017-tutorial.tr.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gitkraken-tutorial.tr.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="github-windows-vs-code-tutorial.tr.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="sourcetree-macos-tutorial.tr.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="github-windows-intellij-tutorial.tr.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](github-desktop-tutorial.tr.md)                                                                                                                 | [Visual Studio 2017](github-windows-vs2017-tutorial.tr.md)                                                                                                                                            | [GitKraken](gitkraken-tutorial.tr.md)                                                                                                                                                           | [Visual Studio Code](github-windows-vs-code-tutorial.tr.md)                                                                                                                                      | [Atlassian Sourcetree](sourcetree-macos-tutorial.tr.md)                                                                                                                                          | [IntelliJ IDEA](github-windows-intellij-tutorial.tr.md)                                                                                                                                           |

[Ana sayfaya dön](../../../translations/README.tr.md#diğer-araçlarla-ilgili-eğitimler)
