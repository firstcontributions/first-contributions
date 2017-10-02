[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" src="https://firstcontributions.herokuapp.com/badge.svg">](https://firstcontributions.herokuapp.com)

# İlk defa katkıda bulunma

Zor. Herhangi yaptığın bir iş ilk seferinde her zaman zor gelir. Özellikle birileriyle işbirliği içindeysen, hata yapmak rahatsız edici olabilir. Fakat açık kaynak tamamen işbirliği ve birlikle çalışmaktır. Biz ilk defa açık kaynak projelere katkıda bulunacak kişilerin öğrenme ve katkıda bulunmasını kolaylaştırmak istiyoruz.

Makale okumak ve eğitim videoları yardımcı olabilir fakat, o işi gerçekten senin yapman yapmandan daha iyi ne olabilir? Bu proje yeni başlayanların veya ilk defa katkıda bulunacakların işini kolyalaştırmak ve onlara rehberlik etmek amacındadır. Unutmayın ki; ne kadar rahat olursanız o kadar rahat öğrenirsiniz. Eğer ilk defa bir GitHub projesine katkıda bulunacaksınız, aşağıda gösterilen basit adımları izlemeniz yeterli olacaktır. Söz veriyoruz, eğlenceli olucak.


<img align="right" width="300" src="assets/fork.png" alt="fork this repository" />


Eğer bilgisayarınızda git kurulu değil ise, [ yükleyin ]( https://help.github.com/articles/set-up-git/ ).

## Projeyi kopyalama

Sayfanın sağ üst köşesinde bulunan "Fork" butonuna basıp bu projeyi forklayın.
Bu işlem sizin hesabınız altında projenin bir kopyasını oluşturacaktır.

## Depoyu (Repository) klonlama

<img align="right" width="300" src="assets/clone.png" alt="clone this repository" />

Şimdi bu repoyu bilgisayarınıza klonlayın. Bunun için 'clone' butonuna basıp ardından *copy to clipboard* ikonuna basın.

Daha sonra terminali açıp aşağıda ki git komut satırını girmemiz gerekiyor:

```
git clone "kopyaladığınız-url"
```
"kopyaladığınız-url" (tırnak işaretleri olmadan) bu deponun linki oluyor. 

<img align="right" width="300" src="assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

Örneğin:
```
git clone https://github.com/this-is-you/first-contributions.git
```
`this-is-you` sizin GitHub kullanıcı adınız. Burada GitHub üzerinde bulunan first-contributions reposunun içeriğini bilgisayırınıza kopyalıyorsunuz. 

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