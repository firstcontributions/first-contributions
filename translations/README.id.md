[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Kontribusi Pertama

Sulit. Selalu sulit saat pertama kali Anda melakukan sesuatu. Terutama ketika Anda berkolaborasi, membuat kesalahan bukanlah hal yang nyaman. Kami ingin menyederhanakan cara kontributor *open-source* baru belajar dan berkontribusi untuk pertama kalinya.

Membaca artikel dan menonton tutorial dapat membantu, tetapi apa yang lebih baik daripada langsung mempraktikan hal-hal tersebut? Proyek ini bertujuan untuk memberikan panduan dan menyederhanakan cara memberikan kontribusi pertama bagi pemula. Jika Anda ingin memberikan kontribusi untuk pertama kalinya, ikuti langkah-langkah di bawah ini.

#### _Jika Anda tidak nyaman dengan baris perintah, [di sini ada tutorial menggunakan GUI.](#tutorial-menggunakan-alat-lain)_

#### _Baca ini dalam [bahasa lain](translations/Translations.md)._

[🇮🇳](translations/Translations.md)
[🇲🇲](translations/README.mm_unicode.md)
[🇮🇩](translations/README.id.md)
[🇫🇷](translations/README.fr.md)
[🇪🇸](translations/README.es.md)
[<img src="../assets/catalan1.png" width="22">](translations/README.ca.md)
[🇳🇱](translations/README.nl.md)
[🇱🇹](translations/README.lt.md)
[🇷🇺](translations/README.ru.md)
[🇧🇬](translations/README.bg.md)
[:slovakia:](translations/README.slk.md)
[🇯🇵](translations/README.ja.md)
[🇻🇳](translations/README.vn.md)
[🇵🇱](translations/README.pl.md)
[🇮🇷](translations/README.fa.md)
[🇮🇷](translations/README.fa.en.md)
[🇰🇷 🇰🇵](translations/README.ko.md)
[🇩🇪](translations/README.de.md)
[🇩🇰](translations/README.da.md)
[🇨🇳](translations/README.chs.md)
[🇹🇼](translations/README.cht.md)
[🇬🇷](translations/README.gr.md)
[🇪🇬](translations/README.eg.md)
[🇸🇦](translations/README.ar.md)
[🇺🇦](translations/README.ua.md)
[🇧🇷](translations/README.pt_br.md)
[🇵🇹](translations/README.pt-pt.md)
[🇮🇹](translations/README.it.md)
[🇹🇭](translations/README.th.md)
[🏴](translations/README.gl.md)
[🇳🇵](translations/README.np.md)
[🇵🇰](translations/README.ur.md)
[:bangladesh:](translations/README.bn.md)
[🇲🇩 🇷🇴](translations/README.ro.md)
[🇹🇷](translations/README.tr.md)
[🇸🇪](translations/README.se.md)
[🇲🇾](translations/README.my.md)
[:slovenia:](translations/README.sl.md)
[🇮🇱](translations/README.hb.md)
[🇨🇿](translations/README.cs.md)
[<img src="../assets/pirate.png" width="22">](translations/README.en-pirate.md)
[🇲🇽](translations/README.mx.md)
[🇵🇭](translations/README.tl.md)
[🇿🇦](translations/README.zul.md)
[🇿🇦](translations/README.afk.md)
[🇰🇪](translations/README.kws.md)
[🇳🇬](translations/README.igb.md)
[🇷🇸](translations/README.sr.md)


<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

Apabila belum memiliki git, [ install segera ](https://help.github.com/articles/set-up-git/).

## Fork Repositori Ini

Fork repositori ini dengan cara menekan tombol *fork* yang ada di bagian kanan atas layar.
Hal tersebut akan membuat salinan repositori ini di akun anda.

## Klon Repositori

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

Sekarang klon repositori ini ke komputer anda. Tekan tombol *clone* lalu tekan ikon "copy to clipboard".

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

`username-anda` adalah *username* Github Anda. Pada langkah ini, Anda menyalin konten dari repositori first-contributions di GitHub ke komputer anda.

## Membuat Cabang (Branch)

Pindah ke direktori repositori Anda yang baru saja disalin (jika belum ada di sana):

```
cd first-contributions
```

Buat cabang dengan perintah `git checkout`:

```
git checkout -b <add-nama-cabang-baru>
```

Contoh:

```
git checkout -b add-alonzo-church
```

(Nama cabang tidak perlu mengandung kata _add_ namun layak untuk ditambahkan karena tujuan dari cabang ini adalah menambahkan nama Anda ke dalam sebuah daftar.)

## Buat Perubahan yang Diperlukan Lalu Commit Perubahan Tersebut

Buka berkas `Contributors.md` menggunakan teks editor, tambahkan nama Anda ke dalamnya lalu simpan berkas tersebut. Apabila Anda masuk ke direktori dan mengeksekusi perintah `git status` maka Anda dapat melihat bahwa telah ada perubahan. Tambahkan perubahan tersebut ke dalam cabang yang sebelumnya telah dibuat menggunakan perintah `git add`:

```
git add Contributors.md
```

Simpan perubahan tersebut menggunakan perintah `git commit`:

```
git commit -m "Add <nama> to Contributors list"
```

ganti `<nama>` dengan nama anda.

## Dorong (Push) Perubahan ke GitHub

Dorong perubahan menggunakan perintah `git push`:

```
git push origin <add-nama-cabang-baru>
```

Ganti `<add-nama-cabang-baru>` dengan nama cabang yang sebelumnya telah dibuat.

## Submit Perubahan untuk Diperiksa

Jika Anda membuka repositori Anda di GitHub, maka akan ada tombol `Compare & pull request`. Tekan tombol tersebut.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

Kirimkan *Pull Request* (PR)

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />

Segera Saya (pengelola) akan menggabungkan semua perubahan Anda ke cabang utama dari proyek ini. Anda akan mendapatkan email notifikasi setelah perubahan digabungkan.

## Ke Mana Lagi Setelah dari Sini?

Selamat! Anda baru saja menyelesaikan *fork* -> klon -> ubah -> alur kerja *Pull Request* yang akan sering Anda temui sebagai kontributor!

Mari rayakan kontribusi Anda dan bagikan pengalaman tersebut bersama teman-teman dengan pergi ke [web app](https://roshanjossey.github.io/first-contributions/#social-share).

Anda dapat bergabung dengan tim slack kami jika membutuhkan bantuan atau memiliki pertanyaan. [Bergabung dengan tim slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Sekarang, mari mulai berkontribusi di proyek lain. Kami sudah mengumpulkan daftar proyek dengan isu yang mudah dikerjakan sehingga Anda dapat segera memulai. Cek di [daftar proyek web app](https://roshanjossey.github.io/first-contributions/#project-list).

## [ Materi tambahan ](../additional-material/git_workflow_scenarios/additional-material.md)

## Tutorial Menggunakan Alat Lain

| <a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a> | <a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> |
| ---------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gitkraken-tutorial.md)                                                              | [Visual Studio Code](github-windows-vs-code-tutorial.md)                                                                                                                  |
|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|<a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|
|---|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|[Visual Studio Code](github-windows-vs-code-tutorial.md)|
