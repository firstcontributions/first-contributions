[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Kontribusi Pertama

Melakukan suatu hal untuk pertama kali akan selalu terasa sulit. Terutama ketika berkolaborasi dan membuat kesalahan, akan menimbulkan rasa tidak nyaman. Namun, sumber terbuka adalah tentang berkolaborasi dan kerja sama. Kami ingin menyederhanakan cara kontributor sumber terbuka yang baru untuk mulai belajar dan berkontribusi untuk pertama kali.

Membaca artikel dan menonton tutorial memang dapat membantu, tetapi apa yang lebih baik dibandingkan dengan melakukannya langsung tanpa membuat kekacauan? Proyek ini bertujuan untuk menyediakan panduan dan menyederhanakan bagaimana para pemula dapat membuat kontribusi pertama mereka. Ingat: Semakin santai anda, maka semakin cepat anda belajar. Jika anda mencari cara untuk membuat kontribusi pertama maka cukup ikuti langkah-langkah berikut. Kami janji, ini akan menyenangkan.

#### *Jika anda belum terbiasa dengan command line, [berikut merupakan tutorial menggunakan aplikasi lainnya.]( #tutorial-menggunakan-aplikasi-lainnya )*

#### *Baca tutorial ini [dalam bahasa lain](translations/Translations.md).*

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

Jika komputer anda belum terpasang git, [ install segera ]( https://help.github.com/articles/set-up-git/ ).

## Fork repositori ini

Fork repositori ini dengan cara menekan tombol fork yang ada di bagian atas layar.
Hal tersebut akan membuat salinan repositori ini di akun anda.

## Clone repositori ini

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

Sekarang klon repositori ini ke komputer anda. Tekan tombol clone lalu tekan ikon "copy to clipboard".

Buka terminal dan eksekusi perintah git berikut:

```
git clone "url yang telah anda salin"
```
yang mana "url yang telah anda salin" (tanpa tanda petik) adalah url ke repositori ini. Lihat langkah sebelumnya untuk mendapatkan url.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

Contoh:
```
git clone https://github.com/username-anda/first-contributions.git
```
Dimana `username-anda` adalah username Github anda. Pada langkah ini anda menduplikasi konten dari repositori first-contributions di GitHub ke komputer anda.

## Membuat Cabang

Pindah ke direktori repositori di komputer (jika belum ada di sana):

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

Buka berkas `Contributors.md` menggunakan teks editor, tambahkan nama anda ke dalamnya lalu simpan berkas tersebut. Jangan tambahkan nama anda pada awal atau akhir dari berkas yang anda edit, tambahkan di manapun selain pada awal dan akhir berkas.
Kemudian, simpan berkas yang telah diedit.

<img align="right" width="450" src="assets/git-status.png" alt="git status" />

Apabila anda masuk ke direktori dan mengeksekusi perintah `git status` maka anda dapat melihat bahwa telah ada perubahan.

Tambahkan perubahan tersebut ke dalam cabang yang sebelumnya telah dibuat menggunakan perintah `git add`:
```
git add Contributors.md
```

Simpan perubahan tersebut menggunakan perintah `git commit`:
```
git commit -m "Add <nama-anda> to Contributors list"
```
ganti `<nama-anda>` dengan nama anda.

## Dorong perubahan ke GitHub

Dorong perubahan menggunakan perintah `git push`:
```
git push origin <add-nama>
```
Ganti `<add-nama>` dengan nama cabang yang sebelumnya telah dibuat sebelumnya.

## Submit perubahan untuk diulas

Jika anda membuka repositori anda di GitHub, maka akan ada tombol `Compare & pull request`. Tekan tombol tersebut.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

Submit pull request.

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />

Kemudian saya akan melakukan penggabungan terhadap semua perubahan anda ke cabang master proyek ini. Anda akan mendapatkan pemberitahuan melalui email setelah perubahan tersebut selesai digabungkan.

## Apa yang anda lakukan setelah ini?

Selamat! Anda telah menyelesaikan alur kerja _fork -> clone -> edit -> PR_ yang akan anda lakukan sebagai seorang kontributor!

Mari rayakan kontribusi anda dan bagikan pengalaman tersebut bersama teman-teman dengan pergi ke [web app](https://firstcontributions.github.io/#social-share).

Anda dapat bergabung dengan tim slack kami jika membutuhkan bantuan atau memiliki pertanyaan. [Bergabung dengan tim slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM).

Sekarang, mari mulai berkontribusi di proyek lain. Kami sudah mengumpulkan daftar proyek dengan isu yang mudah dikerjakan sehingga anda dapat segera mulai berkontribusi. Cek di [daftar proyek web app](https://firstcontributions.github.io/#project-list).

## [ Materi tambahan ](../additional-material/git_workflow_scenarios/additional-material.md)

## Tutorial menggunakan aplikasi lain

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|<a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|<a href="sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a>|
|---|---|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|[Visual Studio Code](github-windows-vs-code-tutorial.md)|[Atlassian Sourcetree](sourcetree-macos-tutorial.md)|

