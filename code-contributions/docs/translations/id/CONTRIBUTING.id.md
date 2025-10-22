# Langkah-langkah untuk berkontribusi

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork repositori ini" />

## Fork repositori ini dengan mengklik tombol fork

## Kloning fork Anda dari repositori ini.

Pada fork repositori ini, klik tombol kode. Pilih tab SSH dan kemudian klik tombol `copy to clipboard`.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />
Buka terminal dan jalankan perintah `git clone`

```bash
git clone “url yang kamu salin”
```

> [!IMPORTANT]
> Pada langkah-langkah berikut, ketika Anda melihat `<your-github-id>`, Anda harus menggantinya dengan ID GitHub Anda.  
> Misalnya, jika ID GitHub Anda adalah `aaronsw`,  
> `git switch -c add-<your-github-id>` menjadi `git switch -c add-aaronsw`  
> `contributors/<github-id-<your-github-id>.html` menjadi `contributors/aaronsw.html`

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="salin URL ke clipboard" />

## Membuat sebuah cabang

Buka direktori repositori jika Anda belum berada di sana

```bash
cd kontribusi-kode
```

Membuat cabang dengan perintah `git switch`

```bash
git switch -c add-<github-id Anda>''
```

## Membuat kartu Anda

Anda dapat menambahkan kartu Anda sebagai berkas HTML di direktori kontributor. Buat sebuah berkas dengan nama pengguna Anda di direktori kontributor. Anda dapat menyalin templat berikut untuk memulai.

`contributors/<your-github-id>.html`
```html
<article>
  <h3>nama pengguna Anda</h3>
  <p>Biografi singkat tentang Anda (opsional)</p>
  <h4>Bahasa pemrograman yang saya gunakan</h4>
  <section class="container">
    <div class="badge" style="background-color: #3874a4; color: white">
      Python
    </div>
    <div class="badge" style="background-color: #f7df1e; color: black;">
      JavaScript
    </div>
  </section>

  <h4>alat yang saya gunakan</h4>
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

## Tambahkan kartu Anda ke daftar kontributor

Tambahkan nama berkas yang Anda buat ke berkas `scripts/contributors.js`.

`scripts/contributors.js`
```js
const contributorFiles = [
  "<your-github-id>.html", // tambahkan nama file Anda di sini
  "roshanjossey.html",
  "gokultp.html",
];
```

## Melihat perubahan Anda di browser web

Anda dapat melihat perubahan Anda dengan membuka `index.html` di browser web. Anda seharusnya dapat melihat kartu baru yang Anda tambahkan pada langkah sebelumnya.

Anda dapat melanjutkan membuat perubahan pada kartu Anda dan menyegarkan tab browser web untuk melihat perubahan tersebut.

## Komit perubahan Anda

Pertama-tama, lakukan perubahan Anda dengan perintah `git add`

```bash
git tambahkan kontributor/<your-github-id>.html
```

Sekarang komit perubahan kamu dengan perintah `git commit`

```bash
git commit -m “tambahkan <your-github-id>”
```

## Dorong perubahan Anda ke GitHub

```bash
git push -u asal add-<your-github-id>
```

## Kirimkan perubahan Anda untuk ditinjau

Jika Anda membuka repositori Anda di GitHub, Anda akan melihat tombol `Bandingkan & tarik permintaan`. Klik tombol tersebut.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="buat permintaan penarikan" />

Sekarang kirimkan permintaan penarikan.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="kirimkan pull request" />

Anda akan mendapatkan email notifikasi setelah perubahan telah digabungkan.