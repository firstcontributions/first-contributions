[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Sumbangan Pertama

Projek ini bertujuan untuk memberikan panduan dan memudahkan individu yang baru mula belajar membuat sumbangan pertama mereka.
Jika anda ingin membuat sumbangan pertama anda, sila ikuti arahan yang disediakan di bawah.

#### *Sekiranya anda tidak selesa dengan menggunakan antara muka baris perintah (CLI), anda boleh mengikuti [panduan untuk menggunakan alat GUI di sini.](#Tutorial-Menggunakan-Alat-Lain)*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="Fork repositori ini" />

Jika git belum dipasang di mesin anda, sila memasangnya, [rujuk di sini](https://help.github.com/articles/set-up-git/).

## Fork repositori ini

Langkah pertama, fork repositori ini dengan menekan butang **Fork** yang terletak di bahagian atas halaman ini.
Tindakan ini akan membuat salinan repositori ini ke dalam akaun GitHub anda.

## Klon repositori ini

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="Klon repositori ini" />

Klon repositori yang telah anda *fork* ke komputer anda. Pergi ke akaun GitHub anda, buka repositori yang baru dicabang, klik butang **Code**, dan kemudian tekan ikon *Copy URL to clipboard*.

Buka terminal dan jalankan arahan git berikut:

```bash
git clone "URL anda baru disalin"
```
di mana "URL anda baru disalin" (tanpa tanda petikan) adalah URL ke repositori fork anda bagi projek ini. Rujuk langkah-langkah sebelumnya untuk mendapatkan URL tersebut.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="Salin URL ke papan keratan" />

Contoh:
```bash
git clone https://github.com/<this-is-you>/first-contributions.git
```
di mana `this-is-you` adalah nama pengguna GitHub anda. Arahan ini akan menyalin kandungan repositori anda tadi 'first-contributions' ke komputer anda.

## Membuat branch

Tukar ke direktori repositori di komputer anda (jika terminal anda belum berada di dalamnya):

```bash
cd first-contributions
```
Cipta branch menggunakan arahan `git switch`:
```bash
git switch -c add-your-name
```

Contoh:
```bash
git switch -c add-emma-maembong
```

<details>
<summary> <strong>Jika anda mendapati sebarang kesalahan menggunakan git switch, klik di sini:</strong> </summary>

Jika mesej ralat "Git: `switch` is not a git command. See `git –help`" muncul, kemungkinan kerana anda menggunakan versi git yang lebih lama.

Untuk kes ini, cuba gunakan `git checkout` sebagai ganti:

```bash
git checkout -b your-new-branch-name
```

</details>

## Buat perubahan yang diperlukan dan komit perubahan tersebut

Sekarang, buka fail `Contributors.md` dalam sebuah penyunting teks, dan tambahkan nama anda ke dalam fail itu. Jangan tambahkan pada awal atau paling bawah fail. Letakkan di mana-mana bahagian di antaranya. Kemudian, simpan fail tersebut.

> [!IMPORTANT]
> Untuk membuat keseragaman, sila ikut format yang sama seperti:
> ```bash
> - [Nama Anda](https://github.com/nama-pengguna-github-anda)
> atau
> - [Nama Anda]
> ```
> Elakkan menambah perkataan yang tidak perlu seperti "Ini adalah sumbangan pertama saya" atau sebagainya.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Jika anda pergi ke direktori projek dan melaksanakan arahan `git status`, anda akan melihat perubahan yang telah dibuat.

Tambahkan perubahan itu ke branch yang baru anda cipta menggunakan arahan `git add`:

```bash
git add Contributors.md
```

Kemudian, komit perubahan tersebut menggunakan arahan `git commit`:
```bash
git commit -m "Add <your-name> to Contributors list"
```
Gantikan `<your-name>` dengan nama anda.

## Muatnaik (Push) perubahan ke dalam GitHub

Muatnaik perubahan anda menggunakan arahan `git push`:
```bash
git push -u origin <your-name>
```
Gantikan `<your-name>` dengan nama branch yang kamu cipta.

<details>
<summary> <strong>Jika anda mendapati sebarang ralat semasa menghantar (push), klik di sini:</strong> </summary>

Anda mungkin mendapat mesej ralat seperti ini:
```bash
fatal: 'origin' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

Anda mungkin perlu menambah repositori asal sebagai 'remote' untuk repositori anda. Jalankan arahan berikut:
```bash
git remote add origin <URL repositori fork anda>
```

</details>

## Hantar perubahan anda untuk semakan

Jika anda pergi ke repositori anda di GitHub, anda akan melihat butang `Compare & pull request`. Klik pada butang tersebut.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="Cipta pull request" />

Hantar 'pull request' tersebut.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="Hantar pull request" />

Tidak lama lagi, saya akan menggabungkan semua perubahan anda ke dalam branch 'main' projek ini. Anda akan menerima e-mel pemberitahuan sebaik sahaja perubahan telah digabungkan.

## Pergi ke mana selepas ini?

Tahniah! Anda baru saja selesai melaksanakan aliran kerja standard _fork -> clone -> edit -> pull request_ yang sering anda akan temui sebagai seorang penyumbang!

Raikan sumbangan anda dan kongsi dengan rakan-rakan serta pengikut melalui [aplikasi web](https://firstcontributions.github.io/#social-share).

Mari kita mulakan dengan menyumbang kepada projek lain. Kami telah menyediakan senarai projek dengan isu-isu mudah yang boleh anda mula sumbangkan. Sila rujuk [senarai projek dalam aplikasi web](https://firstcontributions.github.io/#project-list).

### [Bahan tambahan](../additional-material/git_workflow_scenarios/additional-material.md)


## Tutorial Menggunakan Alat Lain

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
