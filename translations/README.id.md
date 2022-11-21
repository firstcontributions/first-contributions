[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Kontribusi Pertama 

Proyek ini memiliki tujuan yaitu untuk menyederhanakan dan membimbing pemula untuk membuat kontribusi pertamanya di Github. Jika Anda ingin membuat kontribusi pertama mu, ikuti langkah-langkah berikut.


#### _Jika Anda tidak terbiasa dengan baris perintah, [di sini ada tutorial untuk menggunakan GUI.](#Tutorial-Menggunakan-Alat-Lain)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Apabila Anda belum menginstall git di komputer anda, [ install segera ](https://help.github.com/articles/set-up-git/).

## *Fork* Repositori Ini

Fork repositori ini dengan cara klik tombol *fork* yang ada di bagian atas kanan pada halaman ini.
Dan repository ini akan disalin ke akun anda.

## *Clone* Repositori

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Sekarang klon repositori yang sudah Anda *fork* di akun Github anda ke komputer anda. Buka akun GitHub Anda, buka repository yang sudah di *fork*, Klik tombol *Code* dan kemudian klik ikon salin ke papan klip.

Buka terminal dan jalankan perintah git berikut:

```
git clone "url yang telah disalin"
```

bagian "url yang telah disalin" (tanpa tanda petik) adalah url ke repositori ini (proyek yang telah anda *fork* ini). Lihat langkah sebelumnya untuk mendapatkan url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Contoh:

```
git clone https://github.com/ini-adalah-anda/first-contributions.git
```

bagian `ini-adalah-anda` adalah *username* GitHub Anda. Disini Anda menyalin konten dari repositori first-contributions di GitHub ke komputer Anda.

## Membuat Cabang (Branch)

Pindah ke direktori repositori yang terdapat pada komputer Anda (jika Anda belum ada di sana):

```
cd first-contributions
```

Sekarang buat cabang dengan menggunakan perintah `git checkout`:

```
git checkout -b <add-nama-cabang-baru>
```

Contohnya:

```
git checkout -b add-alonzo-church
```


## Buat Perubahan yang Diperlukan Lalu Commit Perubahan Tersebut

Sekarang buka Folder `Contributors.md` menggunakan teks editor, tambahkan nama Anda ke dalamnya. Jangan menambahkan pada awal atau akhir dari file. Simpan dimana saja di antaranya. Sekarang simpan filenya.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Jika Anda pergi ke direktori proyek dan mengeksekusi perintah `git status`, Anda akan melihat ada perubahan.

Tambahkan perubahan tersebut ke cabang yang baru saja Anda buat menggunakan perintah `git add`:

```
git add Contributors.md
```

Sekarang simpan perubahan tersebut menggunakan perintah `git commit`:

```
git commit -m "Add <nama-Anda> to Contributors list"
```

Ubah bagian `<nama-Anda>` dengan nama anda.

## Dorong (Push) Perubahan ke GitHub

*Push* perubahan menggunakan perintah `git push`:

```
git push origin <add-nama-cabang-baru>
```

ganti bagian `<add-nama-cabang-baru>` dengan nama cabang yang sebelumnya Anda buat.

<details>
<summary> <strong>Jika Anda mendapatkan kesalahan saat melakukan <i>push</i>, klik disini:</strong> </summary>

- ### Kesalahan otentikasi
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  Buka [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) untuk menghasilkan dan mengonfigurasi kunci SSH ke akun Anda.

</details>

## Kirim Perubahan untuk Diperiksa

Jika Anda membuka repositori Anda di GitHub, Anda akan melihat sebuat tombol `Compare & pull request`. Tekan tombol tersebut.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Sekarang kirimkan *Pull Request* (PR)

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Saya (pengelola) akan segera menggabungkan semua perubahan Anda ke cabang utama dari proyek ini. Anda akan mendapatkan email pemberitahuan setelah perubahan digabungkan.

## Ke Mana Lagi Setelah dari Sini?

Selamat! Anda baru saja menyelesaikan standar *fork* -> *clone* -> ubah -> *Pull Request* sebuah alur kerja yang akan sering Anda temui sebagai kontributor!

Rayakan kontribusi Anda dan bagikan dengan teman dan pengikut Anda dengan membuka [web app](https://roshanjossey.github.io/first-contributions/#social-share).

Anda dapat bergabung dengan tim slack kami jika membutuhkan bantuan atau memiliki pertanyaan. [Bergabung dengan tim slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Sekarang, mari kita mulai dengan berkontribusi di proyek lain. Kami sudah menyusun daftar proyek dengan isu yang mudah dikerjakan sehingga Anda dapat segera memulai. Cek di [daftar proyek web app](https://roshanjossey.github.io/first-contributions/#project-list).

## [ Materi tambahan ](../additional-material/translations/additional-material.id.md)

## Tutorial Menggunakan Alat Lain


| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
