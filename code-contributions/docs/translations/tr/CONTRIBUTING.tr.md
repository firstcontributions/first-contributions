# Katkıda Bulunma Adımları

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="bu depoyu çatalla" />

## Bu depoyu fork butonuna tıklayarak çatallayın (fork).

## Çatalladığınız depoyu klonlayın.

Çatalladığınız depoda code butonuna tıklayın. SSH sekmesini seçin ve ardından `panoya kopyala` butonuna basın.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="bu depoyu klonla" />
Bir terminal açın ve `git clone` komutunu çalıştırın

```bash
git clone "kopyaladığınız-url"
```

> [!ÖNEMLİ]
> Sonraki adımlarda `<github-idniz>` gördüğünüz yerlerde kendi GitHub ID’nizi kullanmalısınız.  
> Örneğin, GitHub ID’niz `aaronsw` ise,  
> `git switch -c add-<github-idniz>` → `git switch -c add-aaronsw` olur  
> `contributors/<github-idniz>.html` → `contributors/aaronsw.html` olur

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="URL'yi panoya kopyala" />

## Yeni bir dal (branch) oluşturun

Depo dizinine gidin (zaten orada değilseniz)

```bash
cd code-contributions
```

`git switch` komutu ile yeni bir dal oluşturun

```bash
git switch -c add-<github-idniz>
```


## Kartınızı oluşturun

Katkıda bulunanlar klasörüne kendi kartınızı bir HTML dosyası olarak ekleyebilirsiniz. Katkıda bulunanlar klasöründe kullanıcı adınızla bir dosya oluşturun. Başlamak için aşağıdaki şablonu kopyalayabilirsiniz.

`contributors/<github-idniz>.html`
```html
<article>
  <h3>Kullanıcı adınız</h3>
  <p>Hakkınızda kısa bir biyografi (isteğe bağlı)</p>
  <h4>Kullandığım programlama dilleri</h4>
  <section class="container">
    <div class="badge" style="background-color: #3874a4; color: white">
      Python
    </div>
    <div class="badge" style="background-color: #f7df1e; color: black;">
      JavaScript
    </div>
  </section>

  <h4>Kullandığım araçlar</h4>
  <section class="container">
    <img
      class="icon"
      src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/bash/bash-original.svg"
    />
    <img
      class="icon"
      src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linux/linux-original.svg"
    />
  </section>
</article>
<style>
  body {
    font-family: sans-serif;
  }
  .container {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
  }
  .badge {
    padding: 0.5rem;
    border-radius: 0.25rem;
  }
  .icon {
    width: 2rem;
  }
</style>

```
## Kartınızı katkıda bulunanlar listesine ekleyin

Oluşturduğunuz dosyanın adını `scripts/contributors.js` dosyasına ekleyin.

`scripts/contributors.js`
```js
const contributorFiles = [
  "<github-idniz>.html", // dosya adınızı buraya ekleyin
  "roshanjossey.html",
  "gokultp.html",
];
```

## Değişikliklerinizi tarayıcıda görün

`index.html` dosyasını bir tarayıcıda açarak değişikliklerinizi görebilirsiniz. Önceki adımlarda eklediğiniz yeni kartı görmelisiniz.

Kartınızda değişiklik yapmaya devam edebilir ve tarayıcı sekmesini yenileyerek güncellemeleri görebilirsiniz.

## Değişikliklerinizi onaylayın (commit)

Önce değişikliklerinizi `git add` komutu ile hazırlayın

```bash
git add contributors/<github-idniz>.html
```

Sonra değişikliklerinizi `git commit` komutu ile kaydedin

```bash
git commit -m "add <github-idniz>"
```

## Değişikliklerinizi GitHub’a gönderin (push)

```bash
git push -u origin add-<github-idniz>
```

## Değişikliklerinizi inceleme için gönderin (Pull Request)

GitHub’daki deponuza gittiğinizde `Compare & pull request` butonunu göreceksiniz. Ona tıklayın.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Şimdi pull request oluşturup gönderin

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Değişiklikler birleştirildiğinde size bildirim e-postası gelecektir.