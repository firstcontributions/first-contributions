[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" src="https://firstcontributions.herokuapp.com/badge.svg">](https://firstcontributions.herokuapp.com)

# Kontribusi Pertama

Melakukan suatu hal untuk pertama kali akan selalu terasa sulit. Terutama apabila berkolaborasi dimana membuat kesalahan akan menimbulkan rasa tidak nyaman. Namun, sumber terbuka adalah tentang berkolaborasi dan kerja sama. Kami ingin menyederhanakan cara kontributor sumber terbuka yang baru untuk mulai belajar dan berkontribusi untuk pertama kali

Membaca artikel dan menonton tutorial memang dapat membantu, tetapi apa yang lebih baik dibandingkan dengan melakukannya langsung tanpa membuat kekacauan? Proyek ini bertujuan untuk menyediakan panduan dan menyederhanakan bagaimana para pemula dapat membuat kontribusi pertama mereka. Ingat: Semakin santai anda, maka semakin cepat anda belajar. Jika anda mencari cara untuk membuat kontribusi pertama maka cukup ikuti langkah-langkah berikut. Kami janji, ini akan menyenangkan.

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

*Read this in other languages: [English](../README.md), [Spanish](README.es.md), [Dutch](README.nl.md), [Hindi](README.hi.md), [Russian](README.ru.md), [Japanese](README.ja.md), [Vietnamese](README.vn.md), [Polish](README.pl.md), [Korean](README.ko.md), [German](README.de.md), [Simplified Chinese](README.chs.md), [Traditional Chinese](README.cht.md), [Greek](README.gr.md), [العربية](README.ar.md).*

Apabila belum memiliki git, [ install ]( https://help.github.com/articles/set-up-git/ ).

## Fork repositori ini

Fork repositori ini dengan cara menekan tombol fork yang ada di bagian atas layar.
Hal tersebut akan membuat salinan repositori ini di akun anda.

## Clone repositori

<img style="float: left;" width="300" src="../assets/clone.png" alt="clone this repository" />

Sekarang clone repositori ini ke komputer anda. Tekan tombol clone lalu tekan ikon "copy to clipboard".

Buka terminal dan eksekusi perintah git berikut:

```
git clone "url yang telah anda copy"
```
yang mana "url yang telah anda copy" (tanpa tanda petik) adalah url ke repositori ini. Lihat langkah sebelumnya untuk mendapatkan url.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

Contoh:
```
git clone https://github.com/username-anda/first-contributions.git
```
Dimana `username-anda` adalah username Github. Pada langkah ini anda menduplikasi konten dari repositori first-contributions di GitHub ke komputer anda.

## Membuat Branch

Ganti ke direktori repositori di komputer (jika belum ada di di sana):

```
cd first-contributions
```
Buat cabang dengan perintah `git checkout`:
```
git checkout -b <add-nama>
```

Contoh:
```
git checkout -b add-alonzo-church
```
(Nama cabang tidak perlu mengandung kata *add* namun layak untuk ditambahkan karena tujuan dari cabang ini adalah menambahkan nama anda ke dalam sebuah daftar.)

## Buat perubahan yang diperlukan lalu commit perubahan tersebut

Buka berkas `Contributors.md` menggunakan teks editor, tambahkan nama anda ke dalamnya lalu simpan berkas tersebut. Apabila anda masuk ke direktori dan mengeksekusi perintah `git status` maka anda dapat melihat bahwa telah ada perubahan. Tambahkan perubahan tersebut ke dalam cabang yang sebelumnya telah dibuat menggunakan perintah `git add`:
```
git add Contributors.md
```

Commit perubahan tersebut menggunakan perintah `git commit`:
```
git commit -m "Add <nama> to Contributors list"
```
ganti `<nama>` dengan nama anda.

## Push perubahan ke GitHub

Push perubahan menggunakan perintah `git push`:
```
git push origin <add-nama>
```
Ganti `<add-nama>` dengan nama cabang yang sebelumnya telah dibuat.

## Submit perubahan untuk diulas

Jika anda membuka repositori anda di GitHub, maka akan ada tombol `Compare & pull request`. Tekan tombol tersebut.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

Submit pull request.

<img style="float: right;" src="../assets/submit-pull.png" alt="submit pull request" />

Suatu saat nanti saya akan melakukan penggabungan terhadap semua perubahan anda ke master cabang proyek ini. Anda akan mendapatkan email notifikasi setelah perubahan tersebut selesai digabungkan.

Cabang master dari fork anda tidak akan memiliki perubahan-perubahan tersebut. Untuk membuat fork anda selaras dengan milik saya, ikuti langkah-langkah berikut.

## Membuat fork anda selaras dengan repositori ini

 Pertama, ganti posisi ke branch master.
 ```
 git checkout master
 ```
 Tambahkan url repo saya sebagai `upstream remote url`:
```
git remote add upstream https://github.com/Roshanjossey/first-contributions
```
Hal ini untuk memberitahu git bahwa ada versi lain dari proyek ini di url yang telah dispesifikasikan dan disebut sebagai `upstream`. Apabila perubahan telah digabungkan, ambil versi baru dari repositori saya:
```
git fetch upstream
```

Di sini kita melakukan penarikan terhadap semua perubahan di fork saya (upstream remote). Sekarang, anda perlu melakukan penggabungan terhadap revisi baru dari repositori saya ke dalam branch master milik anda.
```
git rebase upstream/master
```
Di sini anda menerapkan semua perubahan yang telah anda ambil ke cabang master. Jika anda dorong cabang master sekarang, fork anda juga akan memiliki perubahan:
```
git push origin master
```
Perhatikan bahwa di sini anda melakukan push ke remote bernama origin.

Pada titik ini saya telah melakukan penggabungan terhadap cabang anda `<add-nama>` ke dalam cabang master dan anda telah melakukan penggabungan terhadap cabang master saya ke dalam cabang master milik anda. Cabang milik anda sudah tidak dibutuhkan lagi sehingga bisa anda hapus:
```
git branch -d <add-nama>
```
dan anda dapat menghapus versi tersebut yang ada di repositori remote:
```
git push origin --delete <add-nama>
```
Hal ini sebenarnya tidak diperlukan namun nama dari branch ini menunjukan tujuan yang spesial. Masa hidupnya bisa dijadikan pendek

## Tutorial Menggunakan Tools Lain


|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.microsoft.com/net/images/vslogo.png" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|

## Ke mana lagi setelah dari sini?

Anda dapat bergabung dengan tim slack kami jika membutuhkan bantuan atau memiliki pertanyaan. [Bergabung dengan tim slack](https://firstcontributions.herokuapp.com)

Berikut adalah beberapa isu level pemula di repositori populer yang dapat anda kerjakan. Silahkan kunjungi repositori-repositori tersebut untuk belajar lebih lanjut.

|[![exercism](https://avatars2.githubusercontent.com/u/5624255?v=3&s=100)](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[![fun-retro](https://avatars3.githubusercontent.com/u/15913975?v=3&s=100)](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[<img width="100" src="https://cdn.worldvectorlogo.com/logos/react.svg">](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[![habitat](https://avatars1.githubusercontent.com/u/18171698?v=3&s=100)](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![scikit-learn](https://avatars0.githubusercontent.com/u/365630?v=3&s=100)](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[<img width="100" src="https://camo.githubusercontent.com/0f302c808c8457f6460913e33aed3478124612c2/687474703a2f2f6c65696e696e67656e2e6f72672f696d672f6c65696e696e67656e2e6a7067">](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[<img width="100" src="https://images.plot.ly/plotly-documentation/thumbnail/numpy-logo.jpg">](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[![elasticsearch](https://avatars2.githubusercontent.com/u/6764390?v=3&s=100)](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|---|---|---|---|---|---|---|---|
|[exercism](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[Fun Retros](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[react](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[habitat](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[scikit-learn](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[Leiningen](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[numpy](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[elasticsearch](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|[![homebrew](https://avatars2.githubusercontent.com/u/1503512?v=3&s=100)](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[![rust](https://avatars1.githubusercontent.com/u/5430905?v=3&s=100)](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[![vuejs](https://avatars1.githubusercontent.com/u/6128107?v=3&s=100)](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[![Suave](https://avatars2.githubusercontent.com/u/5822862?v=3&s=100)](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[![OpenRA](https://avatars3.githubusercontent.com/u/409046?v=3&s=100)](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![PowerShell](https://avatars0.githubusercontent.com/u/11524380?v=3&s=100)](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[![coala](https://avatars2.githubusercontent.com/u/10620750?v=3&s=100)](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[![moment](https://avatars2.githubusercontent.com/u/4129662?v=3&s=100)](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[homebrew](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[Rust](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[vuejs](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[Suave](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[OpenRA](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[PowerShell](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[coala](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[moment](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[![ava](https://avatars0.githubusercontent.com/u/8527916?v=3&s=100)](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[![freeCodeCamp](https://avatars0.githubusercontent.com/u/9892522?v=3&s=100)](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![webpack](https://avatars3.githubusercontent.com/u/2105791?v=3&s=100)](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[![hoodie](https://avatars1.githubusercontent.com/u/1888826?v=3&s=100)](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![pouchdb](https://avatars3.githubusercontent.com/u/3406112?v=3&s=100)](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[![neovim](https://avatars0.githubusercontent.com/u/6471485?v=3&s=100)](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[![babel](https://avatars2.githubusercontent.com/u/9637642?v=3&s=100)](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[<img width="100" src="https://github.com/adobe/brackets/blob/gh-pages/images/brackets_128.png?raw=true">](https://github.com/adobe/brackets/labels/Starter%20bug)|
|[ava](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[webpack](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[hoodie](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[pouchdb](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[neovim](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[babel](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[brackets](https://github.com/adobe/brackets/labels/Starter%20bug)|
| [![Node.js](https://avatars1.githubusercontent.com/u/9950313?v=3&s=100)](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|[<img width="100" src="https://github.com/Semantic-Org/Semantic-UI-React/raw/master/docs/app/logo.png">](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|
| [Node.js](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |[Semantic-UI-React](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |
