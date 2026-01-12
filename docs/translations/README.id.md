[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Kontribusi Pertama

Proyek ini bertujuan untuk menyederhanakan dan membimbing perjalanan seorang pemula berkontribusi di Github untuk pertama kali. Perhatikan langkah-langkah berikut untuk memulai:

#### _Jika Anda tidak terbiasa dengan baris perintah(command line), [di sini ada tutorial untuk menggunakan GUI(antarmuka bergrafis).](#Tutorial-Menggunakan-Alat-Lain)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork repositori ini" />

Apabila Anda belum menginstall git di komputer Anda, [install segera](https://help.github.com/articles/set-up-git/).

## _Fork_ Repositori Ini

Fork repositori ini dengan cara klik tombol _Fork_ yang ada di bagian atas kanan pada halaman ini. Hal Ini akan membuat sebuah salinan repositori di akun Anda.

## _Clone_ (Kloning) Repositori

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="klon repositori ini" />

Sekarang kloning repositori yang sudah Anda _fork_ ke komputer Anda. Pergi ke akun GitHub Anda, buka repositori yang sudah Anda _fork_, klik tombol _Code_ dan kemudian klik ikon salin ke papan klip.

Buka sebuah terminal dan jalankan perintah git berikut:

```
git clone "url yang telah Anda disalin"
```

bagian "url yang telah Anda disalin" (tanpa tanda petik) adalah url ke repositori ini (proyek yang telah Anda _fork_ ini). Lihat langkah sebelumnya untuk mendapatkan url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="salin URL ke papan klip" />

Contohnya:

```
git clone git@github.com:ini-adalah-anda/first-contributions.git
```

bagian `ini-adalah-anda` adalah nama pengguna GitHub Anda. Di sini Anda menyalin konten dari repositori first-contributions di GitHub ke komputer Anda.

## Membuat Sebuah _Branch_ (Cabang)

Pindah ke direktori repositori yang terdapat pada komputer Anda (jika Anda belum berada di sana):

```
cd first-contributions
```

Sekarang buatlah sebuah _branch_ menggunakan perintah `git checkout`:

```
git checkout -b <tambahkan-nama-branch-baru>
```

Contohnya:

```
git checkout -b add-alonzo-church
```

<details>
<summary> <strong>Jika kamu mendapatkan beberapa kesalahan menggunakan <i>git switch</i>, klik disini:</strong> </summary>

Jika pesan error: "Git: `switch` is not a git command. See `git –help`" muncul, kemungkinan besar Anda menggunakan versi git yang lama.

Dalam kasus ini, coba gunakan `git checkout` sebagai gantinya:

```bash
git checkout -b your-new-branch-name
```

</details>

## Buat Perubahan Yang Diperlukan Lalu _Commit_ (Simpan) Perubahan Tersebut

Sekarang buka berkas `Contributors.md` menggunakan teks editor, tambahkan nama Anda ke dalamnya. Jangan menambahkan pada awal atau akhir dari berkas. Simpan dimana saja di antaranya. Sekarang simpan berkasnya.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="status git" />

Jika Anda pergi ke direktori proyek dan mengeksekusi perintah `git status`, Anda akan melihat ada sebuah perubahan.

Tambahkan perubahan tersebut ke _branch_ yang baru saja Anda buat menggunakan perintah `git add`:

```
git add Contributors.md
```

Sekarang simpan perubahan tersebut menggunakan perintah `git commit`:

```
git commit -m "Add <nama-anda> to Contributors list"
```

Ubah bagian `<nama-anda>` dengan nama Anda.

## Dorong (Push) Perubahan Ke GitHub

_Push_ perubahan menggunakan perintah `git push`:

```
git push origin <tambahkan-nama-cabang-baru>
```

ganti bagian `<tambahkan-nama-cabang-baru>` dengan nama cabang yang sebelumnya Anda buat.

<details>
<summary> <strong>Jika Anda mendapatkan kesalahan saat melakukan <i>push</i>, klik disini:</strong> </summary>

- ### Kesalahan Autentikasi

       <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.

  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  Buka [tutorial GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) untuk menghasilkan dan mengkonfigurasi sebuah kunci SSH ke akun Anda.

  Jika kelihatannya seperti ini:

    <pre>origin	https://github.com/your-username/your_repo.git (fetch)
    origin	https://github.com/your-username/your_repo.git (push)</pre>

  Buat perubahan dengan perintah:

    <pre>git remote set-url origin git@github.com:your-username/your_repo.git</pre>

  Jika tidak, Anda akan tetap dimintai nama pengguna dan kata sandi serta mendapatkan kesalahan autentikasi.
  </details>

## Kirim Perubahan Untuk Diperiksa

Jika Anda membuka repositori Anda di GitHub, Anda akan melihat sebuah tombol `Compare & pull request`. Tekan tombol tersebut.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="buat pull request" />

Sekarang kirimkan _Pull Request_

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="kirim pull request" />

Saya (pengelola) akan segera menggabungkan semua perubahan Anda ke cabang utama (_main branch_) dari proyek ini. Anda akan mendapatkan email pemberitahuan setelah perubahan digabungkan.

## Ke Mana Lagi Setelah Dari Sini?

Selamat! Anda baru saja menyelesaikan standar _fork_ -> _clone_ -> _edit_ -> _pull request_ sebuah alur kerja yang akan sering Anda temui sebagai seorang kontributor!

Rayakan kontribusi Anda dan bagikan dengan teman-teman dan pengikut Anda dengan membuka [web app](https://firstcontributions.github.io/#social-share).

Jika Anda ingin lebih banyak latihan, lihat [kontribusi kode](https://github.com/roshanjossey/code-contributions).

Sekarang mari kita mulai dengan berkontribusi di proyek lain. Kami sudah menyusun daftar proyek dengan isu yang mudah dikerjakan sehingga Anda dapat segera memulai. Cek di [daftar proyek web app](https://firstcontributions.github.io/#project-list).

## [Materi tambahan](../additional-material/translations/additional-material.id.md)

## Tutorial Menggunakan Alat (tools) Lain

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="Aplikasi GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="Program GitKraken " src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="Editor VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Aplikasi Sourcetree" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="Program IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |

<p>Proyek ini didukung oleh:</p>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>
