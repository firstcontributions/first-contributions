[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Kontribusi Pertama (First Contributions)

|<img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="200">|Edisi GitKraken|
|---|---|

Memang sulit. Selalu terasa sulit, ketika Anda melakukan sesuatu untuk pertama kalinya. Terutama saat Anda berkolaborasi, melakukan kesalahan bukanlah hal yang nyaman. Namun open source adalah tentang kolaborasi & bekerja sama. Kami ingin menyederhanakan cara kontributor open-source baru untuk belajar & berkontribusi untuk pertama kalinya.

Membaca artikel & menonton tutorial dapat membantu, tetapi apa yang lebih baik daripada benar-benar melakukan hal tersebut tanpa mengacaukan apa pun. Proyek ini bertujuan untuk memberikan panduan & menyederhanakan cara pemula melakukan kontribusi pertama mereka. Ingatlah bahwa semakin santai Anda, semakin baik Anda belajar. Jika Anda mencari cara untuk melakukan kontribusi pertama Anda, ikuti saja langkah-langkah sederhana di bawah ini. Kami berjanji, ini akan menyenangkan.


## GitKraken

Unduh [GitKraken](https://www.gitkraken.com), Instal dan buka aplikasinya.


Anda akan melihat dialog modal "Welcome to GitKraken" - Masuk (Sign in) menggunakan GitHub dan izinkan GitKraken mengakses akun GitHub Anda.


<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-login.png" alt="login to GitHub" />

(opsional) Pergi ke File -> Preferences dan atur *project directory* Anda ke *root* dari *local repositories* Anda.


## Fork repository ini

Lakukan fork pada repo ini dengan mengklik tombol fork di bagian atas halaman ini.
<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/fork.png" alt="fork this repository" />
Ini akan membuat salinan (copy) dari repository ini di akun Anda.


## Clone repository tersebut

Di GitKraken, pergi ke File -> Clone Repo.


<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-clone.png" alt="clone this repository" />


Pilih GitHub.com di panel kanan. Di bawah *username* Anda, Anda akan melihat `first-contributions`. Klik repository tersebut dan periksa letak direktori (*full path*) yang ditampilkan di bagian bawah panel ini.

Setelah Anda yakin dengan letak direktorinya (*path*), klik "Clone the repo!".


## Buat branch baru

Klik tombol branch pada toolbar.

Beri nama branch Anda "add-nama-anda", misalnya: "add-william-sutton"

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-branch.png" alt="name your branch" />


## Buat perubahan yang diperlukan dan commit perubahan tersebut

Sekarang buka file `Contributors.md` di sebuah editor teks dan tambahkan nama Anda ke dalamnya, lalu simpan file tersebut.

Jika Anda membuka repo di GitKraken, Anda akan melihat ada perubahan. Tinjau (review) dan tempatkan (*stage*) perubahan tersebut dengan memilih commit terbaru yang ditandai dengan "// WIP" beserta jumlah file yang diubah dan jenis perubahannya.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-edit.png" alt="edit some file(s)" />

Tinjau file yang telah diubah dan putuskan apa yang ingin Anda tempatkan (*stage*). Staging penting untuk memberitahu Git dengan tepat perubahan file apa saja yang ingin Anda kaitkan dengan commit ini.


<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-stage.png" alt="stage your changes" />


Setelah Anda memiliki pesan commit yang bagus ("Add <nama-anda> to Contributors list" terdengar bagus dan deskriptif) dan puas dengan perubahan yang Anda buat, Anda dapat menekan "Stage all changes" untuk men-*stage* semua file yang dimodifikasi, atau "Stage File" untuk men-*stage* file secara individu.


<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-commit.png" alt="clone this repository" />


Jika Anda berubah pikiran, Anda dapat membatalkan stage (unstage) dari perubahan tersebut, atau Anda dapat membuangnya (discard) sama sekali.
PERINGATAN: Sesuai dengan kata *discard* (membuang), ini adalah operasi yang merusak/menghapus secara permanen. Lakukan ini hanya jika Anda benar-benar tidak menginginkan perubahan apa pun dari repository mana pun tempat Anda berada.

Tekan commit.

Selamat, Anda telah melakukan commit pada semua perubahan ke salinan lokal branch Anda dari fork `first-contributions` milik Anda. Lanjutkan!


## Push perubahan ke GitHub

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-push.png" alt="push your changes" />

Klik tombol Push pada toolbar.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-origin.png" alt="origin or branch" />

Submit perubahan pada *origin branch* jika Anda ingin perubahan tersebut langsung terlihat di *master branch*, jika tidak, pilih branch yang sesuai yang ingin Anda push.


## Ajukan perubahan Anda untuk direview (Pull Request)

Jika Anda pergi ke repository Anda di github, Anda akan melihat tombol `Compare & pull request`. Klik tombol tersebut.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/compare-and-pull.png" alt="create a pull request" />

Sekarang kirimkan (submit) pull request tersebut.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/submit-pull-request.png" alt="submit pull request" />

Segera saya akan menggabungkan (merge) semua perubahan Anda ke dalam master branch proyek ini. Anda akan mendapatkan email pemberitahuan setelah perubahan digabungkan.

## Ke mana selanjutnya?

Selamat! Anda baru saja menyelesaikan alur kerja standar _fork -> clone -> edit -> PR_ yang akan sering Anda temui sebagai kontributor!

Rayakan kontribusi Anda dan bagikan dengan teman dan pengikut Anda dengan mengunjungi [web app](https://firstcontributions.github.io/#social-share).

### [Materi tambahan](../additional-material/git_workflow_scenarios/additional-material.md)


## Tutorial Menggunakan Alat Lain
[Kembali ke halaman utama](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
