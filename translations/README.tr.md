[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" src="https://firstcontributions.herokuapp.com/badge.svg">](https://firstcontributions.herokuapp.com)

# İlk defa katkıda bulunma

Zor. Herhangi yaptığın bir iş ilk seferinde her zaman zor gelir. Özellikle birileriyle işbirliği içindeysen, hata yapmak rahatsız edici olabilir. Fakat açık kaynak tamamen işbirliği ve birlikle çalışmaktır. Biz ilk defa açık kaynak projelere katkıda bulunacak kişilerin öğrenme ve katkıda bulunmasını kolaylaştırmak istiyoruz.

Makale okumak ve eğitim videoları yardımcı olabilir fakat, o işi gerçekten senin yapman yapmandan daha iyi ne olabilir? Bu proje yeni başlayanların veya ilk defa katkıda bulunacakların işini kolyalaştırmak ve onlara rehberlik etmek amacındadır. Unutmayın ki; ne kadar rahat olursanız o kadar rahat öğrenirsiniz. Eğer ilk defa bir GitHub projesine katkıda bulunacaksınız, aşağıda gösterilen basit adımları izlemeniz yeterli olacaktır. Söz veriyoruz, eğlenceli olucak.

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

Eğer bilgisayarınızda git kurulu değil ise, [ yükleyin ]( https://help.github.com/articles/set-up-git/ ).

## Projeyi kopyalama

Sayfanın sağ üst köşesinde bulunan "Fork" butonuna basıp bu projeyi forklayın.
Bu işlem sizin hesabınız altında projenin bir kopyasını oluşturacaktır.

## Depoyu (Repository) klonlama

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

Şimdi bu repoyu bilgisayarınıza klonlayın. Bunun için 'clone' butonuna basıp ardından *copy to clipboard* ikonuna basın.

Daha sonra terminali açıp aşağıda ki git komut satırını girmemiz gerekiyor:

```
git clone "kopyaladığınız-url"
```
"kopyaladığınız-url" (tırnak işaretleri olmadan) yerine bu deponun GitHub sayfasından aldığınız linki koplayın.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

Örneğin:
```
git clone https://github.com/kullanıcı-adi/first-contributions.git
```
`kullanıcı-adi` sizin GitHub kullanıcı adınız. Burada GitHub üzerinde bulunan first-contributions reposunun içeriğini bilgisayırınıza kopyalıyorsunuz.

## Dal (Branch) oluşturma

Eğer zaten klasör içinde değilseniz terminal üzerinde repo klasörünün bulunduğu konuma gidin:

```
cd first-contributions
```
`git checkout` komutunu kullanarak yeni bir branch oluşutrun:
```
git checkout -b <ekle-sizin-isminiz>
```

Örneğin:
```
git checkout -b ekle-aydin-cagri-dumlu
```
(Branch ismi içinde *ekle* kelimesinin zorunluluğu bulunmamakta, fakat bu branch ismimizi contributor listesine eklemek için oluşturduğundan ekle kelimesinin konulması mantıklı olacaktır.)

## Gerekli değişiklikleri yapıp commit işlemini gerçekleştrimek

Text editor ile `Contributors.md` dosyasını açıp, içinde ismininizi yazdıktan sonra dosyayı kaydedin. Terminal üzerinden projen klasörüne gidip `git status` komutunu yazdığınızda yaptığınız değişiklikleri göreceksiniz. Daha sonra `git add` komutu ile bu değişiklikleri oluşturduğunuz branch içine ekleyin.

```
git add Contributors.md
```

Şimdi `git commit` komutunu kullanarak dosyalarınızı commit edin:
```
git commit -m "Contributors listesine <isminiz> ekle"
```
`<isminiz>` yerine kendi isminizi yazın.

## Değişiklikleri GitHub üzerine gönderme (Push)

`git push` komutu ile değişiklikleriniz pushlayın:
```
git push origin <ekle-kendi-isminiz>
```
`<ekle-kendi-isminiz>` yerine daha önce oluşturduğunuz branch ismini girin.

## Değişikliklerinizi inceleme için gönderin

GitHub üzerinde oluşturmuş olduğunuz repoya baktığınız zaman `Compare & pull request` butonunu göreceksiniz. Bu butona basın.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

Şimdi bir pull request isteği gönderin.

<img style="float: right;" src="../assets/submit-pull.png" alt="submit pull request" />

En kısa zamanda yaptığınız değişiklikler master branch ile birleştirilecek. Bu işlem tamamlandı zaman bilgilendirme maili alıcaksınız.

### [ Sonraki adımlar ](additional-material)

## Diğer araçlar için eğitimler


|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.microsoft.com/net/images/vslogo.png" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/../assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

## Bundan sonra ne yapabilirim?

Bir sorunuz veya yardıma ihtiyacınız olma durumunda slack takımıza katılabilirsiniz. [Slack takımına katıl](https://firstcontributions.herokuapp.com)

Popüler repolarda ki başlangıç seviyesinde çözebileceğiniz konulara ait linkler aşağıda yer almaktadır. İnceleyin ve daha fazla bilgiye sahip olun

|[![exercism](https://avatars2.githubusercontent.com/u/5624255?v=3&s=100)](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[![fun-retro](https://avatars3.githubusercontent.com/u/15913975?v=3&s=100)](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[<img width="100" src="https://cdn.worldvectorlogo.com/logos/react.svg">](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[![habitat](https://avatars1.githubusercontent.com/u/18171698?v=3&s=100)](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![scikit-learn](https://avatars0.githubusercontent.com/u/365630?v=3&s=100)](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[<img width="100" src="https://camo.githubusercontent.com/0f302c808c8457f6460913e33aed3478124612c2/687474703a2f2f6c65696e696e67656e2e6f72672f696d672f6c65696e696e67656e2e6a7067">](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[<img width="100" src="https://images.plot.ly/plotly-documentation/thumbnail/numpy-logo.jpg">](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[![elasticsearch](https://avatars2.githubusercontent.com/u/6764390?v=3&s=100)](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|---|---|---|---|---|---|---|---|
|[exercism](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[Fun Retros](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[react](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[habitat](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[scikit-learn](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[Leiningen](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[numpy](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[elasticsearch](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|[![homebrew](https://avatars2.githubusercontent.com/u/1503512?v=3&s=100)](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[![rust](https://avatars1.githubusercontent.com/u/5430905?v=3&s=100)](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[![vuejs](https://avatars1.githubusercontent.com/u/6128107?v=3&s=100)](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[![Suave](https://avatars2.githubusercontent.com/u/5822862?v=3&s=100)](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[![OpenRA](https://avatars3.githubusercontent.com/u/409046?v=3&s=100)](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![PowerShell](https://avatars0.githubusercontent.com/u/11524380?v=3&s=100)](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[![coala](https://avatars2.githubusercontent.com/u/10620750?v=3&s=100)](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[![moment](https://avatars2.githubusercontent.com/u/4129662?v=3&s=100)](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[homebrew](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[Rust](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[vuejs](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[Suave](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[OpenRA](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[PowerShell](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[coala](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[moment](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[![ava](https://avatars0.githubusercontent.com/u/8527916?v=3&s=100)](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[![freeCodeCamp](https://avatars0.githubusercontent.com/u/9892522?v=3&s=100)](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![webpack](https://avatars3.githubusercontent.com/u/2105791?v=3&s=100)](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[![hoodie](https://avatars1.githubusercontent.com/u/1888826?v=3&s=100)](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![pouchdb](https://avatars3.githubusercontent.com/u/3406112?v=3&s=100)](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[![neovim](https://avatars0.githubusercontent.com/u/6471485?v=3&s=100)](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[![babel](https://avatars2.githubusercontent.com/u/9637642?v=3&s=100)](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[<img width="100" src="https://github.com/adobe/brackets/blob/gh-pages/images/brackets_128.png?raw=true">](https://github.com/adobe/brackets/labels/Starter%20bug)|
|[ava](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[webpack](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[hoodie](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[pouchdb](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[neovim](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[babel](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[brackets](https://github.com/adobe/brackets/labels/Starter%20bug)|
| [![Node.js](https://avatars1.githubusercontent.com/u/9950313?v=3&s=100)](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|[<img width="100" src="https://github.com/Semantic-Org/Semantic-UI-React/raw/master/docs/app/logo.png">](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|
| [Node.js](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |[Semantic-UI-React](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |
