[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# İlk katkılar

Zor gelir. Bir işi ilk kez yapmak her zaman zor gelir. Özellikle birileriyle işbirliği içindeyseniz, hata yapmak içinize sinmez. Fakat açık kaynağın temelinde işbirliği ve birlikte çalışma yatar. Biz açık kaynak projelere ilk kez katkıda bulunacak kişilerin süreci öğrenmesini ve ilk katkılarını sunmalarını kolaylaştırmak istiyoruz.

Makale okumak ve eğitim videoları izlemek yardımcı olabilir, fakat bir işi gerçekten yapmanın yerini ne tutabilir ki? Bu proje yeni başlayanların veya ilk defa katkıda bulunacakların işini kolaylaştırmak ve onlara rehberlik etmek amacındadır. Unutmayın ki ne kadar rahat olursanız o kadar rahat öğrenirsiniz. Eğer bir GitHub projesine ilk defa katkıda bulunacaksanız, aşağıda gösterilen basit adımları izlemeniz yeterli olacaktır. Söz veriyoruz, eğlenceli olacak.

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

Eğer bilgisayarınızda git kurulu değil ise, [ yükleyin ]( https://help.github.com/articles/set-up-git/ ).

## Projeyi "çatallandırma"

Sayfanın sağ üst köşesinde bulunan "Fork" butonuna basıp bu projeyi çatallandırın.
Bu işlem sizin hesabınız altında projenin bir kopyasını oluşturacaktır.

## Depoyu (Repository) klonlama

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

Şimdi bu depoyu bilgisayarınıza klonlayın. Bunun için 'clone' butonuna basıp ardından *copy to clipboard* ikonuna basın.

Daha sonra komut istemini açıp aşağıdaki git komutunu girmemiz gerekiyor:

```
git clone "kopyaladığınız-url"
```
"kopyaladığınız-url" (tırnak işaretleri olmadan) yerine bu deponun GitHub sayfasından aldığınız linki koplayın.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

Örneğin:
```
git clone https://github.com/kullanıcı-adi/first-contributions.git
```
`kullanıcı-adi` sizin GitHub kullanıcı adınız. Burada GitHub üzerinde bulunan first-contributions reposunun içeriğini bilgisayarınıza kopyalıyorsunuz.

## Dal (Branch) oluşturma

Eğer henüz klasör içinde değilseniz komut isteminde ana klasörünün konumuna gidin:

```
cd first-contributions
```
`git checkout` komutunu kullanarak yeni bir dal(branch) oluşturun:
```
git checkout -b <ekle-sizin-isminiz>
```

Örneğin:
```
git checkout -b ekle-aydin-cagri-dumlu
```
(Dal ismi içinde *ekle* kelimesinin geçme zorunluluğu yok, fakat bu dal isminizi katkı sunanlar listesine ekleme amacıyla oluşturulduğundan, ekle yazmak mantıklı olacaktır.)

## Gerekli değişiklikleri yapıp bu değişiklikleri onaylama

Şimdi, bir metin editöründe `Contributors.md` dosyasını açın. Hafif bir işaretleme dili olan Markdown'a alışkın olmanız gerekmektedir. Nasıl kullanacağınızı öğrenmek için bu [kopya kağıdına](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) göz atabilirsiniz.

`Contributors.md` dosyasının sonuna bu satırı ekleyin:

```
- [İsminiz](https://github.com/kullanici-adiniz)
```

Örneğin:

```
- [Ahmet Yılmaz](https://github.com/ahmet-yilmaz)
```

`](` arasında boşluk olmadığından emin olun. Dosyayı kaydedin ve kapatın.

Komut istemi üzerinde proje klasörüne gidip `git status` komutunu yazdığınızda yaptığınız değişiklikleri göreceksiniz. `git add` komutu ile bu değişiklikleri oluşturduğunuz dal içine ekleyin.

```
git add Contributors.md
```

Şimdi `git commit` komutunu kullanarak değişikliklerinizi onaylayın (commit):
```
git commit -m "<isminiz> katkıda bulunanlar listesine eklendi"
```
`<isminiz>` yerine kendi isminizi yazın.

(Ç.N: Açık kaynak dünyasında dünyanın farklı yerlerinden insanlarla birlikte çalışacağınız için onay mesajını İngilizce yazabilirsiniz.)

## Değişiklikleri GitHub üzerine "itme" (Push)

`git push` komutu ile değişikliklerinizi ittirin:
```
git push origin <ekle-kendi-isminiz>
```
`<ekle-kendi-isminiz>` yerine daha önce oluşturduğunuz dalın ismini girin.

## Değişikliklerinizi inceleme için gönderin

Oluşturduğunuz deponun Github sayfasında `Compare & pull request` butonunu göreceksiniz. Bu butona basın.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

Şimdi çekme isteğini (pull request) gönderin.

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />

Yaptığınız değişiklikleri en kısa zamanda projenin "master" dalı ile birleştireceğiz. Bu işlem tamamlandığı zaman bir bilgilendirme postası alacaksınız.

### [Sonraki adımlar](../additional-material/git_workflow_scenarios/additional-material.md)

## Bundan sonra ne yapabilirim?

Sunduğunuz katkının coşkusunu yaşamak ve bunu arkadaşlarınız ve takipçilerinizle paylaşmak için [bu bağlantıdaki](https://roshanjossey.github.io/first-contributions/#social-share) uygulamamızı kullanabilirsiniz.

Bir sorunuz veya yardıma ihtiyacınız olursa Slack takımımıza katılabilirsiniz. [Slack takımına katıl](https://firstcontributions.herokuapp.com)

Artık diğer projelere katkı sunmaya hazırsınız. Çözmeye başlayabileceğiniz giriş seviyesindeki konulara (issue) sahip projeleri [sizin için derledik](https://roshanjossey.github.io/first-contributions/#project-list).

## Diğer araçlarla ilgili eğitimler


|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="../assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

