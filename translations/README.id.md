[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Kontribusi Pertama

Melakukan suatu hal untuk pertama kali akan selalu terasa sulit. Terutama ketika berkolaborasi dan membuat kesalahan, akan menimbulkan rasa tidak nyaman. Namun, sumber terbuka adalah tentang berkolaborasi dan kerja sama. Kami ingin menyederhanakan cara kontributor sumber terbuka yang baru untuk mulai belajar dan berkontribusi untuk pertama kali.

Membaca artikel dan menonton tutorial memang dapat membantu, tetapi apa yang lebih baik dibandingkan dengan melakukannya langsung tanpa membuat kekacauan? Proyek ini bertujuan untuk menyediakan panduan dan menyederhanakan bagaimana para pemula dapat membuat kontribusi pertama mereka. Ingat: Semakin santai Anda, maka semakin cepat Anda belajar. Jika Anda mencari cara untuk membuat kontribusi pertama maka cukup ikuti langkah-langkah berikut. Kami janji, ini akan menyenangkan.

#### *Baca dalam [bahasa lainnya](../Translations.md)* 

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

Apabila belum memiliki git, [ install segera ]( https://help.github.com/articles/set-up-git/ ).

## Fork repositori ini

Fork repositori ini dengan cara menekan tombol fork yang ada di bagian atas layar.
Hal tersebut akan membuat salinan repositori ini di akun Anda.

## Klon repositori

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

Sekarang klon repositori ini ke komputer Anda. Tekan tombol clone lalu tekan ikon "copy to clipboard".

Buka terminal dan eksekusi perintah git berikut:

```
git clone "url yang telah Anda salin"
```
yang mana "url yang telah Anda salin" (tanpa tanda petik) adalah url ke repositori ini. Lihat langkah sebelumnya untuk mendapatkan url.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

Contoh:
```
git clone https://github.com/username-anda/first-contributions.git
```
Dimana `username-anda` adalah username Github Anda. Pada langkah ini Anda menduplikasi konten dari repositori first-contributions di GitHub ke komputer Anda.

## Membuat Cabang

Ganti ke direktori repositori di komputer (jika belum ada di sana):

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
(Nama cabang tidak perlu mengandung kata *add* namun layak untuk ditambahkan karena tujuan dari cabang ini adalah menambahkan nama Anda ke dalam sebuah daftar.)

## Buat perubahan yang diperlukan lalu commit perubahan tersebut

Buka berkas `Contributors.md` menggunakan teks editor, tambahkan nama Anda ke dalamnya lalu simpan berkas tersebut. Apabila Anda masuk ke direktori dan mengeksekusi perintah `git status` maka Anda dapat melihat bahwa telah ada perubahan. Tambahkan perubahan tersebut ke dalam cabang yang sebelumnya telah dibuat menggunakan perintah `git add`:
```
git add Contributors.md
```

Simpan perubahan tersebut menggunakan perintah `git commit`:
```
git commit -m "Add <nama> to Contributors list"
```
ganti `<nama>` dengan nama Anda.

## Dorong perubahan ke GitHub

Dorong perubahan menggunakan perintah `git push`:
```
git push origin <add-nama>
```
Ganti `<add-nama>` dengan nama cabang yang sebelumnya telah dibuat.

## Submit perubahan untuk diulas

Jika Anda membuka repositori Anda di GitHub, maka akan ada tombol `Compare & pull request`. Tekan tombol tersebut.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

Submit pull request.

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />

Suatu saat nanti saya akan melakukan penggabungan terhadap semua perubahan Anda ke cabang master proyek ini. Anda akan mendapatkan pemberitahuan melalui email setelah perubahan tersebut selesai digabungkan.

Cabang master dari fork Anda tidak akan memiliki perubahan-perubahan tersebut. Untuk membuat fork Anda selaras dengan milik saya, ikuti langkah-langkah berikut.

## Membuat fork Anda selaras dengan repositori ini

 Pertama, ganti posisi ke cabang master.
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

Di sini kita melakukan penarikan terhadap semua perubahan di fork saya (upstream remote). Sekarang, Anda perlu melakukan penggabungan terhadap revisi baru dari repositori saya ke dalam cabang master milik Anda.
```
git rebase upstream/master
```
Di sini Anda menerapkan semua perubahan yang telah Anda ambil ke cabang master. Jika Anda dorong cabang master sekarang, fork Anda juga akan memiliki perubahan:
```
git push origin master
```
Perhatikan bahwa di sini Anda melakukan push ke remote bernama origin.

Pada titik ini saya telah melakukan penggabungan terhadap cabang Anda `<add-nama>` ke dalam cabang master dan Anda telah melakukan penggabungan terhadap cabang master saya ke dalam cabang master milik Anda. Cabang milik Anda sudah tidak dibutuhkan lagi sehingga bisa Anda hapus:
```
git branch -d <add-nama>
```
dan Anda dapat menghapus versi tersebut yang ada di repositori remote:
```
git push origin --delete <add-nama>
```
Hal ini sebenarnya tidak diperlukan namun nama dari cabang ini menunjukkan tujuan yang spesial. Masa hidupnya bisa dijadikan lebih pendek.

## Tutorial Menggunakan Tools Lain

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|<a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|
|---|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|[Visual Studio Code](github-windows-vs-code-tutorial.md)|

## Ke mana lagi setelah dari sini?

Mari rayakan kontribusi Anda dan bagikan pengalaman tersebut bersama teman-teman dengan pergi ke [web app](https://roshanjossey.github.io/first-contributions/#social-share).

Anda dapat bergabung dengan tim slack kami jika membutuhkan bantuan atau memiliki pertanyaan. [Bergabung dengan tim slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Sekarang, mari mulai berkontribusi di proyek lain. Kami sudah mengumpulkan daftar proyek dengan isu yang mudah dikerjakan sehingga Anda dapat segera memulai. Cek di [daftar proyek web app] (https://roshanjossey.github.io/first-contributions/#project-list).

## [ Materi tambahan ](../additional-material/git_workflow_scenarios/additional-material.md)

## Tutorial menggunakan alat lain

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|<a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|
|---|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|[Visual Studio Code](github-windows-vs-code-tutorial.md)|

## Promosi

Jika Anda menyukai proyek ini, bintangi di [GitHub](https://github.com/Roshanjossey/first-contributions).
Jika Anda orang yang gemar bersosial, ikuti [Roshan](https://roshanjossey.github.io/) di
[Twitter](https://twitter.com/sudo__bangbang) dan
[GitHub](https://github.com/roshanjossey).
