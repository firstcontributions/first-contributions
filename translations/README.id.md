[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Kontribusi Pertama

Selalu sulit saat pertama kali Anda melakukan sesuatu. Terutama ketika Anda berkolaborasi, membuat kesalahan bukanlah hal yang nyaman. Kami ingin menyederhanakan cara kontributor *open-source* baru belajar dan berkontribusi untuk pertama kalinya.

Membaca artikel dan menonton tutorial dapat membantu, tetapi apa yang lebih baik daripada langsung mempraktikan hal-hal tersebut? Proyek ini bertujuan untuk memberikan panduan dan menyederhanakan cara memberikan kontribusi pertama bagi pemula. Jika Anda ingin memberikan kontribusi untuk pertama kalinya, ikuti langkah-langkah di bawah ini.

#### _Jika Anda tidak nyaman dengan command line, [di sini ada tutorial menggunakan GUI.](#Tutorial-Menggunakan-Alat-Lain)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Apabila belum memiliki git, [install segera](https://help.github.com/articles/set-up-git/).

## Fork Repositori Ini

Fork repositori ini dengan cara menekan tombol *fork* yang ada di bagian kanan atas layar.
Ini akan membuat salinan repositori di akun Anda.

## Clone Repositori

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Sekarang clone repositori ini ke komputer Anda. Buka laman github Anda, buka repositori yang telah di fork, klik tombol *code*, lalu tekan ikon "copy to clipboard".

Buka terminal dan eksekusi perintah git berikut:

```
git clone "url yang telah Anda salin"
```

"url yang telah Anda salin" (tanpa tanda petik) adalah url ke repositori ini. Lihat langkah sebelumnya untuk mendapatkan url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Contoh:

```
git clone https://github.com/username-anda/first-contributions.git
```

`username-anda` adalah *username* Github Anda. Pada langkah ini, Anda menyalin konten dari repositori first-contributions di GitHub ke komputer Anda.

## Membuat Cabang (Branch)

Pindah ke direktori repositori Anda yang baru saja disalin:

```
cd first-contributions
```

Buat cabang dengan perintah `git switch`:

```
git switch -c <add-nama-cabang-baru>
```

Contoh:

```
git switch -c add-alonzo-church
```

(Nama cabang tidak perlu mengandung kata _add_ namun lebih baik untuk ditambahkan karena tujuan dari cabang ini adalah menambahkan nama Anda ke dalam sebuah daftar.)

## Buat Perubahan yang Diperlukan Lalu Commit Perubahan Tersebut

Buka `Contributors.md` menggunakan teks editor, tambahkan nama Anda ke dalamnya. Jangan letakkan di awal atau di akhir file, letakkan saja di tengah-tengah atau di antara nama-nama yang ada. Lalu simpan berkas tersebut.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Apabila Anda masuk ke direktori dan mengeksekusi perintah `git status`, maka Anda dapat melihat bahwa telah ada perubahan. 

Tambahkan perubahan tersebut pada cabang yang sebelumnya telah dibuat menggunakan perintah `git add`:

```
git add Contributors.md
```

Simpan perubahan tersebut menggunakan perintah `git commit`:

```
git commit -m "Add <nama> to Contributors list"
```

Ubah `<nama>` dengan nama anda.

## Dorong (Push) Perubahan ke GitHub

Dorong perubahan menggunakan perintah `git push`:

```
git push origin <add-nama-cabang-baru>
```

Ubah `<add-nama-cabang-baru>` dengan nama cabang yang sebelumnya telah dibuat.

## Submit Perubahan untuk Di-review

Jika Anda membuka repositori Anda di GitHub, maka akan ada tombol `Compare & pull request`. Tekan tombol tersebut.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Kirimkan *Pull Request* (PR)

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Segera, Saya (pengelola repositori ini), akan menggabungkan semua perubahan Anda ke cabang utama dari proyek ini. Anda akan mendapatkan email notifikasi setelah perubahan digabungkan.

## Ke Mana Lagi Setelah dari Sini?

Selamat! Anda baru saja menyelesaikan *fork* -> *clone* -> ubah -> *Pull Request* sebuah alur kerja yang akan sering Anda temui sebagai kontributor!

Mari rayakan kontribusi Anda dan bagikan pengalaman tersebut bersama teman-teman dengan pergi ke [web app](https://roshanjossey.github.io/first-contributions/#social-share).

Anda dapat bergabung dengan tim slack kami jika membutuhkan bantuan atau memiliki pertanyaan. [Bergabung dengan tim slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Sekarang, mari mulai berkontribusi di proyek lain. Kami sudah mengumpulkan daftar proyek dengan isu yang mudah dikerjakan sehingga Anda dapat segera memulai. Cek di [daftar proyek web app](https://roshanjossey.github.io/first-contributions/#project-list).

## [ Materi tambahan ](../additional-material/git_workflow_scenarios/additional-material.md)

## Tutorial Menggunakan Alat Lain


| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> |
| ---------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                               | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                   |                                                                                                                |
