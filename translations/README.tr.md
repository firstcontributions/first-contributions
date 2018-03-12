[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" src="https://firstcontributions.herokuapp.com/badge.svg">](https://firstcontributions.herokuapp.com)

# İlk Katkılar

Zordur. Bir şeyi ilk defa yaptığında her zaman zor gelir. Özellikle birileriyle müşterek çalışıyorsan, hata yapmak rahatsız edici olabilir. Fakat açık kaynak tamamen işbirliği ve birlikle çalışmaktır. Açık kaynak projelere ilk defa katkıda bulunacak kişilerin bu işi öğrenmelerini ve katkıda bulunmalarını kolaylaştırmak istiyoruz.

Makale okumak ve eğitim videoları yardımcı olabilir fakat, özel bir alıştırma ortamında bu işi gerçekten yapmaktan daha iyi ne olabilir? Bu projenin amacı yeni başlayanların veya ilk defa katkıda bulunacakların işini kolyalaştırmak ve onlara rehberlik etmektir. Unutmayın; ne kadar rahat olursanız o kadar rahat öğrenirsiniz. Eğer ilk defa bir GitHub projesine katkıda bulunacaksınız, aşağıda gösterilen basit adımları izlemeniz yeterli olacaktır.

#### *Bunu [başka dillerde](Translations.md) okumak için.*

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

Eğer bilgisayarınızda git kurulu değil ise, [ yükleyin ]( https://help.github.com/articles/set-up-git/ ).

## Depoyu çatallama

Sayfanın sağ üst köşesinde bulunan "Fork" butonuna basarak bu projeyi çatallayın.
Bu işlem kendi hesabınız altında deponun bir kopyasını oluşturacaktır.

## Depoyu kopyalama

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

Şimdi bu depoyu bilgisayarınıza kopyalayın (clone). Bunun için 'clone' butonuna basıp ardından *copy to clipboard* ikonuna basın.

Daha sonra terminali açıp aşağıdaki git komut satırını yazmanız gerekiyor:

```
git clone "az önce kopyaladığınız-url"
```
"az önce kopyaladığınız-url" yerine (tırnak işaretleri olmadan) bu deponun GitHub sayfasından aldığınız bağlantıyı koplayın.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

Örneğin:
```
git clone https://github.com/kullanıcı-adi/first-contributions.git
```
Bu komutta `kullanıcı-adi` yerine sizin kendi GitHub kullanıcı adınız olacak. Burada GitHub üzerinde bulunan first-contributions deposunun içeriğini kendi bilgisayırınıza kopyalıyorsunuz.

## Dal (Branch) oluşturma

Eğer zaten depo klasörü içinde değilseniz terminal üzerinde depo klasörünün bulunduğu klasöre gidin:

```
cd first-contributions
```
`git checkout` komutunu kullanarak yeni bir dal oluşutrun:
```
git checkout -b <add-kendi-isminiz>
```

Örneğin:
```
git checkout -b add-aydin-cagri-dumlu
```
(Dal ismi içinde *add* kelimesinin olması zorunlu değildir. Fakat bu dalın amacı ismimizi katkıda bulunanlar listesine eklemek olduğu için *add* kelimesinin eklenmesi mantıklı olacaktır.)

## Gerekli değişikliklerin yapılarak commit işleminin gerçekleştirilmesi

Bir metin editörü ile `Contributors.md` dosyasını açın. Bunun için basit bir markup dili olan Markdown'a aşina olmanız gerekiyor. Markdown kullanımı hakkında bilgi veren şu [cheat-sheet'i](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) kullanabilirsiniz.

`Contributors.md` dosyasının en sonuna aşağıdaki satırı ekleyin:

```
- [Kendi adınız](https://github.com/GitHub-kullanıcı-adınız)
```

Örneğin:

```
- [John Doe](https://github.com/johndoe)
```

İki parantez arasında (`](`) boşluk olMAdığından emin olun. Dosyayı kaydedin ve kapatın.

Terminal üzerinden depo klasörüne gidip `git status` komutunu yazarsanız yapmış olduğunuz değişiklikleri göreceksiniz. Yapmış olduğunuz bu değişiklikleri aşağıdaki şekilde `git add` komutunu kullanarak oluşturmuş olduğunuz yeni dal içerisine ekleyin:

```
git add Contributors.md
```

Şimdi `git commit` komutunu kullanarak yaptığınız değişiklikleri uygulayın (commit):
```
git commit -m "Add <kendi-adınız> to Contributors list"
```
`<kendi-adınız>` ifadesi yerine kendi isminizi yazın.

## Değişiklikleri GitHub üzerine gönderme (Push)

`git push` komutunu kullanarak değişikliklerinizi GitHub'a yükleyin (push):
```
git push origin <add-kendi-isminiz>
```
Burada `<add-kendi-isminiz>` yerine yukarıda oluşturduğunuz dal (branch) ismini yazın.

## Yaptığınız değişiklikleri incelenmek üzere gönderin

GitHub üzerinde oluşturmuş olduğunuz depoya bakarsanız, `Compare & pull request` butonunu göreceksiniz. Bu butona basın.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

Şimdi bir "pull request" isteği gönderin.

<img style="float: right;" src="../assets/submit-pull.png" alt="submit pull request" />

Yapmış olduğunuz tüm değişiklikleri en kısa sürede bu projenin ana dalı (master branch) ile birleştireceğim. Birleştirme işlem tamamlandığı zaman bir bilgilendirme e-postası alacaksınız.

## Bundan sonra ne yapabilirim?

Yapmış olduğunuz katkıdan kutlama yapın ve [web uygulaması](https://roshanjossey.github.io/first-contributions/#social-share)na giderek bunu arkadaşlarınız ve takipçileriniz ile paylaşın.

Eğer yardım ihtiyacınız veya herhangi bir sorunuz olursa slack takımımıza katılabilirsiniz. [Slack takımına katılmak için](https://firstcontributions.herokuapp.com).

Şimdi de başka projelere katkıda bulunmaya başlayabilirsiniz. Sizin için, katkıda bulunmaya başlayabileceğiniz basit sorunlar içeren projelerin bir listesini oluşturduk. [Proje listesini web uygulamasında inceleyin](https://roshanjossey.github.io/first-contributions/#project-list).

### [İlave malzemeler](additional-material/git_workflow_senarios/additional-material.md)

## Diğer Araçlar İçin Eğitimler

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/../assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

## Kendi tanıtımım

Eğer bu projeyi sevdiyseniz [GitHub](https://github.com/Roshanjossey/first-contributions)'da yıldızlayın.
Eğer kendinizi özellikle yardımsever hissediyorsanız beni takip edin:
[Roshan](https://roshanjossey.github.io/), 
[Twitter](https://twitter.com/sudo__bangbang), 
[GitHub](https://github.com/roshanjossey).

<a href="http://saasgrids.com"> <img alt="http://saasgrids.com" src="assets/saasgrids-banner.png" width="500"></a>
