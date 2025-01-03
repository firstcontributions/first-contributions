[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Sumbangan Pertama

Projek ini bertujuan untuk memberikan panduan dan memudahkan individu yang baru mula belajar membuat sumbangan pertama mereka. 
Jika anda ingin membuat sumbangan pertama anda, sila ikuti arahan yang disediakan di bawah.

#### *Sekiranya anda tidak selesa dengan menggunakan antara muka baris perintah (CLI), anda boleh mengikuti [panduan untuk menggunakan alat GUI di sini.](#Tutorial-Menggunakan-Alat-Lain)*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Jika git belum dipasang di mesin anda, sila memasangnya [di sini](https://help.github.com/articles/set-up-git/).

## Fork repositori ini

Fork repositori ini dengan menekankan butang 'Fork' yang terletak di bahagian atas halaman ini.
Tindakan tersebut akan menghasilkan salinan repositori ini ke dalam akaun GitHub anda.

## Klon repositori ini

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Klon repositori yang anda telah fork ke mesin anda. Selepas itu, layari akaun GitHub anda, buka repositori yang baru dicabang, klik butang Clone, dan kemudian klik ikon *Copy url to clipboard*.

Buka terminal dan jalankan arahan git berikut:

```
git clone "URL anda baru disalin"
```
di mana "URL anda baru disalin" (tanpa tanda petikan) adalah URL ke repositori ini (fork anda bagi projek ini). Rujuk langkah-langkah sebelumnya untuk mendapatkan URL tersebut.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Contoh:
```
git clone https://github.com/<this-is-you>/first-contributions.git
```
di mana `this-is-you` adalah nama pengguna GitHub anda. Di sini, anda menyalinkan kandungan repositori GitHub 'first-contributions' ke komputer anda.

## Membuat branch

Tukar ke direktori repositori pada komputer anda (jika lokasi CLI belum berada di sana):

```
cd first-contributions
```
Sila buat branch menggunakan arahan `git switch`:
```
git switch -c add-your-name
```

Contoh:
```
git switch -c add-emma-maembong
```

## Buat perubahan yang diperlukan dan komit perubahan tersebut

Sekarang, buka fail `Contributors.md` dalam sebuah editor teks, dan tambahkan nama anda ke dalam fail itu. Jangan tambahkan pada awal atau akhir fail. Letakkan di mana-mana bahagian di antara kedua-duanya. Kemudian, simpan fail tersebut.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />


Jika anda pergi ke direktori projek dan laksanakan arahan `git status`, anda akan melihat perubahan tersebut.

Tambahkan perubahan itu ke branch yang baru anda cipta menggunakan arahan `git add`:

```
git add Contributors.md
```

Selepas itu, komit perubahan tersebut menggunakan arahan `git commit`:
```
git commit -m "Add <your-name> to Contributors list"
```
menggantikan `<your-name>` dengan nama anda.

## Push perubahan ke dalam GitHub

Tolak perubahan anda menggunakan arahan `git push`:
```
git push -u origin <add-your-name>
```
menggantikan `<add-your-name>` dengan nama branch yang kamu cipta sebelumnya.

## Hantar perubahan anda untuk semakan

Jika anda pergi ke repositori anda di GitHub, anda akan melihat butang `Compare & pull request`. Klik butang tersebut.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Hantar 'pull request' tersebut.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Tidak lama lagi, saya akan menggabungkan semua perubahan anda ke dalam branch 'main' projek ini. Anda akan menerima e-mel pemberitahuan sebaik sahaja perubahan telah digabungkan.

## Pergi ke mana selepas ini?

Tahniah! Anda baru saja selesai melaksanakan aliran kerja standard _fork -> clone -> edit -> pull request_ yang sering anda akan temui sebagai seorang penyumbang!

Raikan sumbangan anda dan kongsi dengan rakan-rakan serta pengikut melalui [aplikasi web](https://firstcontributions.github.io/#social-share).

Anda boleh menyertai pasukan 'Slack' kami sekiranya anda memerlukan bantuan atau mempunyai sebarang pertanyaan. [Sertai pasukan Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Mari kita mulakan dengan menyumbang kepada projek lain. Kami telah menyediakan senarai projek dengan isu-isu mudah yang boleh anda mula sumbangkan. Sila rujuk [senarai projek dalam aplikasi web](https://firstcontributions.github.io/#project-list).

### [Bahan tambahan](../additional-material/git_workflow_scenarios/additional-material.md)


## Tutorial Menggunakan Alat Lain

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
