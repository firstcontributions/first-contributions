[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Kontribusi Pertama

Proyek ini bertujuan untuk membantu dan membimbing kontributor pemula untuk melakukan kontribusi pertamanya. Jika anda ingin melakukan kontribusi pertama anda, ikutilah langkah-langkah berikut.

#### _Jika anda tidak nyaman dengan command line, anda bisa menggunakan GUI dengan tutorial [berikut](#Tutorial-Menggunakan-Alat-Lain)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Untuk melakukan tutorial ini anda diperlukan untuk [menginstall git](https://help.github.com/articles/set-up-git/).

## Fork Repositori Ini

Fork repositori ini dengan cara menekan tombol *fork* yang ada di bagian kanan atas layar.
Tombol ini akan membuat salinan repositori first-contribution di akun anda.

## Clone Repositori

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Setelah anda melakukan langkah diatas, repository akan muncul di akun Github anda. Tekan tombol *clone* lalu tekan ikon "copy to clipboard".

Buka terminal dan eksekusi perintah git berikut:

```
git clone "url yang telah anda salin"
```

"url yang telah anda salin" (tanpa tanda petik) adalah url ke repositori ini. Lihat langkah sebelumnya untuk mendapatkan url repositori.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Contoh:

```
git clone https://github.com/username-anda/first-contributions.git
```

`username-anda` adalah *username* Github anda. Dengan menjalankan perintah ini, anda telah menyalin repositori first-contributions dari GitHub ke komputer anda.

## Membuat Cabang (Branch)

Jika anda belum berada di direktori repositori `first-contribution` di komputer anda, anda dapat menjalankan perintah:

```
cd first-contributions
```

Kemudian buatlah cabang dengan perintah `git checkout`:

```
git checkout -b <add-nama-cabang-baru>
```

Contoh:

```
git checkout -b add-alonzo-church
```

(Nama cabang tidak perlu mengandung kata _add_ namun lebih baik untuk ditambahkan karena tujuan dari cabang ini adalah menambahkan nama anda ke dalam sebuah daftar.)

## Buat Perubahan yang Diperlukan Lalu Commit Perubahan Tersebut

Buka berkas `Contributors.md` menggunakan teks editor, tambahkan nama anda ke dalamnya lalu simpan berkas tersebut. Anda dapat melihat perubahan yang telah anda buat dengan menjalankan perintah `git status` pada direktori repositori. Anda dapat menambahkan perubahan yang telah anda buat dengan menjalankan perintah `git add`:

```
git add Contributors.md
```

Kemudian simpan perubahan tersebut menggunakan perintah `git commit`:

```
git commit -m "Add <nama> to Contributors list"
```

Ubah `<nama>` dengan nama anda.

## Dorong (Push) Perubahan ke GitHub

Push perubahan menggunakan perintah `git push`:

```
git push origin <add-nama-cabang-baru>
```

Ubah `<add-nama-cabang-baru>` dengan nama cabang yang sebelumnya telah dibuat.

## Submit Perubahan untuk Diperiksa

Bukalah repositori ini di akun Github anda dan tekanlah tombol
`Compare & pull request`. 

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Kirimkan *Pull Request* (PR)

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Setelah PR anda dikirim, pengelola repositori akan segera menggabungkan semua perubahan anda kirim ke cabang utama dari proyek ini. anda akan mendapatkan email notifikasi setelah perubahan digabungkan.

## Ke Mana Lagi Setelah ini?

Selamat! Anda baru saja menyelesaikan *fork* -> *clone* -> ubah -> *Pull Request*, sebuah alur kerja yang akan sering anda temui sebagai kontributor!

Rayakan kontribusi anda dan bagikan pengalaman tersebut bersama teman-teman anda melalui [web app](https://roshanjossey.github.io/first-contributions/#social-share).

Anda dapat bergabung dengan tim slack kami jika membutuhkan bantuan atau memiliki pertanyaan. [Bergabung dengan tim slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Sekarang, mari mulai berkontribusi di proyek lain. Kami telah mengumpulkan daftar proyek dengan isu yang mudah dikerjakan sehingga anda dapat segera memulai. Cek di [daftar proyek web app](https://roshanjossey.github.io/first-contributions/#project-list).

## [ Materi tambahan ](../additional-material/git_workflow_scenarios/additional-material.md)

## Tutorial Menggunakan Tools Lain

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> |
| ---------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                              | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  |
