[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Sumbangan Pertama

Ia sukar. Ia sentiasa sukar buat kali pertama kamu melakukan sesuatu. Terutama apabila kamu berkolaborasi, membuat kesilapan bukan perkara yang selesa. Kami mahu menyederhanakan cara penyumbang sumber terbuka baru belajar & menyumbang buat kali pertama.

Membaca artikel & menonton tutorial boleh membantu, tetapi apa yang lebih baik daripada melakukan perkara dalam persekitaran yang praktikal? Projek ini bertujuan memberi bimbingan & memudahkan seseorang yang baru bermula untuk membuat sumbangan pertama mereka. Jika kamu ingin membuat sumbangan pertama kamu, ikuti langkah-langkah di bawah.

#### *Jika anda tidak selesa dengan 'command line', [sini adalah tutorial menggunakan alat GUI.](#Tutorial-Menggunakan-Alat-Lain)*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Jika anda tidak mempunyai git dalam mesin kamu, [pasang](https://help.github.com/articles/set-up-git/).

## Fork repositori ini

Fork repo ini dengan mengklik butang fork di atas halaman ini.
Ini akan membuat salinan repositori ini dalam akaun kamu.

## Klon repositori

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Sekarang klon repo yang bercabang ke mesin kamu. Pergi ke akaun GitHub anda, buka repo yang bercabang, klik pada butang klon dan kemudian klik ikon * copy to clipboard *.

Buka terminal dan jalankan arahan git berikut:

```
git clone "url anda baru disalin"
```
dimana "url anda baru disalin" (tanpa tanda petikan) adalah url ke repositori ini (fork projek anda). Lihat langkah-langkah sebelumnya untuk mendapatkan url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Contoh:
```
git clone https://github.com/this-is-you/first-contributions.git
```
dimana `this-is-you` adalah nama pengguna GitHub kamu. Di sini kamu menyalin kandungan repositori sumbangan pertama dalam GitHub ke komputer kamu.

## Membuat cawangan

Tukar ke direktori repositori pada komputer kamu (jika kamu belum berada disana):

```
cd first-contributions
```
Sekarang cipta cawangan menggunakan arahan `git checkout`:
```
git checkout -b <add-your-new-branch-name>
```

Contoh:
```
git checkout -b add-alonzo-church
```
(Nama cawangan tidak perlu mempunyai perkataan * add * di dalamnya, tetapi ia adalah perkara yang munasabah untuk disertakan kerana tujuan cawangan ini adalah untuk menambah nama anda ke senarai.)

## Buat perubahan yang diperlukan dan komit perubahan tersebut

Sekarang buka fail `Contributors.md` dalam editor teks, tambahkan nama anda kepadanya. Jangan tambahkannya pada awal atau akhir fail. Letakkan di mana sahaja di antara. Sekarang, simpan fail itu.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />


Jika anda pergi ke direktori projek dan laksanakan arahan `git status`, kamu akan melihat perubahanya.

Tambah perubahan tersebut ke cawangan yang baru kamu cipta menggunakan arahan `git add`:

```
git add Contributors.md
```

Sekarang komit perubahan tersebut menggunakan perintah `git commit`:
```
git commit -m "Add <your-name> to Contributors list"
```
menggantikan `<your-name>` dengan nama kamu.

## Push changes to GitHub

Tolak perubahan anda menggunakan arahan `push push`:
```
git push origin <add-your-branch-name>
```
menggantikan `<add-your-branch-name>` dengan nama cawangan yang kamu cipta sebelumnya.

## Hantar perubahan anda untuk semakan

Jika anda pergi ke repositori anda di GitHub, anda akan melihat butang `Compare & pull request`. Klik pada butang itu.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Sekarang hantar 'pull request' itu.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Tidak lama lagi saya akan menggabungkan semua perubahan anda ke cawangan 'master' projek ini. Anda akan mendapat e-mel pemberitahuan sebaik sahaja perubahan telah digabungkan.

## Ke mana pergi dari sini?

Tahniah! Anda baru saja selesai melaksanakan standard _fork -> clone -> edit -> PR_ aliran kerja yang sering kamu akan terserempak sebagai seorang penyumbang!

Raikan sumbangan kamu dan kongsi dengan rakan dan pengikut kamu dengan pergi ke [aplikasi web](https://roshanjossey.github.io/first-contributions/#social-share).

Anda boleh menyertai pasukan 'Slack' kami sekiranya anda memerlukan bantuan atau mempunyai sebarang soalan. [Sertai pasukan Slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Sekarang mari kita mulakan dengan menyumbang kepada projek lain. Kami telah menyusun senarai projek dengan isu mudah yang boleh anda mulakan. Semak [senarai projek dalam aplikasi web](https://roshanjossey.github.io/first-contributions/#project-list).

### [Bahan tambahan](../additional-material/git_workflow_scenarios/additional-material.md)


## Tutorial Menggunakan Alat Lain

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/Readme/gk-icon.png" width="100"></a>|<a href="../github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|
|---|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|[Visual Studio Code](../github-windows-vs-code-tutorial.md)|
