[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Sumbangan Pertama

Ia sukar. Ianya sememangnya sukar setiap kali anda melakukan sesuatu buat kali yang pertama. Terutamanya apabila anda berkolaborasi, membuat kesilapan bukan suatu perkara yang enak. Kami mahu membantu anda yang baru belajar untuk menyumbang kepada sumber terbuka buat kali yang pertama dengan menunjukkan cara mudah untuk berbuat demikian.

Membaca artikel & menonton tutorial tentunya dapat membantu, tetapi lebih baik kita bersama-sama melakukan perkara tersebut dalam persekitaran yang praktikal. Projek ini bertujuan memberi bimbingan & memudahkan seseorang yang baru bermula untuk membuat sumbangan pertama mereka. Jika anda ingin membuat sumbangan pertama anda, ikuti langkah-langkah di bawah.

#### *Jika anda tidak selesa dengan 'command line', [sini adalah tutorial menggunakan alat GUI.](#Tutorial-Menggunakan-Alat-Lain)*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Jika anda tidak mempunyai git dalam komputer anda, [muat turun](https://help.github.com/articles/set-up-git/).

## Fork repositori ini

Fork repo ini dengan menekan butang fork yang berada di atas halaman ini.
Ini akan membuat salinan repositori ini dalam akaun anda.

## Klon repositori

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Sekarang, klon repo yang telah di-fork ke dalam mesin anda. Pergi ke akaun GitHub anda, buka repo telah di-fork sebentar tadi, klik pada butang klon dan kemudian klik ikon * copy to clipboard *.

Buka terminal dan jalankan arahan git berikut:

```
git clone "url yang anda baru salin"
```
dimana "url yang anda baru salin" (tanpa tanda pembuka dan penutup kata) adalah url ke repositori ini (fork anda untuk projek ini). Lihat langkah-langkah sebelum ini untuk mendapatkan url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Contoh:
```
git clone https://github.com/this-is-you/first-contributions.git
```
dimana `this-is-you` adalah nama pengguna GitHub anda. Di sini, anda sedang menyalin kandungan repositori ini dari GitHub ke dalam komputer anda.

## Membuat cawangan

Tukar ke direktori repositori pada komputer anda (jika belum berada disana):

```
cd first-contributions
```
Sekarang cipta cabang menggunakan arahan `git switch`:
```
git switch -c <add-your-new-branch-name>
```

Contoh:
```
git switch -c add-alonzo-church
```
(Nama cabang tidak perlu mengandungi perkataan * add * di dalamnya, tetapi ia adalah perkara yang munasabah untuk disertakan kerana tujuan cabang ini adalah untuk menambah nama anda ke senarai.)

## Buat perubahan yang diperlukan dan komit perubahan tersebut

Sekarang buka fail `Contributors.md` dalam editor teks, tambahkan nama anda ke dalam senarai itu. Jangan tambahkan pada awal atau akhir fail. Letakkan di tengah-tengah dokumen. Sekarang, simpan fail tersebut.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />


Jika anda pergi ke direktori projek dan jalankan arahan `git status`, anda akan melihat perubahanya.

Tambah perubahan tersebut ke cabang yang baru anda cipta menggunakan arahan `git add`:

```
git add Contributors.md
```

Sekarang komit perubahan tersebut menggunakan perintah `git commit`:
```
git commit -m "Add <your-name> to Contributors list"
```
menggantikan `<your-name>` dengan nama anda.

## Push perubahan ke dalam GitHub

Push perubahan anda menggunakan arahan `git push`:
```
git push -u origin <add-your-branch-name>
```
menggantikan `<add-your-branch-name>` dengan nama cabang yang baru sahaja anda cipta sebentar tadi.

## Hantar perubahan anda untuk semakan

Jika anda pergi ke repositori anda di GitHub, anda akan melihat butang `Compare & pull request`. Klik pada butang tersebut.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Sekarang, hantar 'pull request' itu.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Tidak lama lagi saya akan menggabungkan semua perubahan anda ke cabang 'master' projek ini. Anda akan mendapat satu e-mel pemberitahuan sebaik sahaja perubahan telah digabungkan.

## Pergi ke mana selepas ini?

Tahniah! Anda baru saja selesai melaksanakan standard _fork -> clone -> edit -> PR_ aliran kerja yang sering anda akan lalui sebagai seorang penyumbang!

Raikan sumbangan anda dan kongsi dengan rakan dan pengikut anda dengan pergi ke [aplikasi web](https://firstcontributions.github.io/#social-share).

Anda boleh menyertai pasukan 'Slack' kami sekiranya anda memerlukan bantuan atau mempunyai sebarang soalan. [Sertai pasukan Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Sekarang mari kita mulakan dengan menyumbang kepada projek lain. Kami telah menyusun senarai projek dengan isu mudah yang boleh anda mulakan. Semak [senarai projek dalam aplikasi web](https://firstcontributions.github.io/#project-list).

### [Bahan tambahan](../additional-material/git_workflow_scenarios/additional-material.md)


## Tutorial Menggunakan Alat Lain

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
