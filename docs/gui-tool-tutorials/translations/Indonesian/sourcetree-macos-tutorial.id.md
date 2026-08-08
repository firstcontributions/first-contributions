[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Kontribusi Pertama (First Contributions)

|<img alt="SourceTree" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-logo.png" width="200">|Atlassian Sourcetree|
|---|---|

Memang sulit. Selalu terasa sulit, ketika Anda melakukan sesuatu untuk pertama kalinya. Terutama saat Anda berkolaborasi, melakukan kesalahan bukanlah hal yang nyaman. Namun open source adalah tentang kolaborasi & bekerja sama. Kami ingin menyederhanakan cara kontributor open-source baru untuk belajar & berkontribusi untuk pertama kalinya.

Membaca artikel & menonton tutorial dapat membantu, tetapi apa yang lebih baik daripada benar-benar melakukan hal tersebut tanpa mengacaukan apa pun. Proyek ini bertujuan untuk memberikan panduan & menyederhanakan cara pemula melakukan kontribusi pertama mereka. Ingatlah bahwa semakin santai Anda, semakin baik Anda belajar. Jika Anda mencari cara untuk melakukan kontribusi pertama Anda, ikuti saja langkah-langkah sederhana di bawah ini. Kami berjanji, ini akan menyenangkan.


## Sourcetree

Harap dicatat, tutorial ini ditujukan untuk MacOS. Tampilannya mirip dengan Sourcetree di Windows tetapi beberapa hal mungkin terlihat berbeda.
<!--
	****************************************
	*** This is commented out until      ***
	*** a Windows tutorial can be created***
	****************************************
Please note, this tutorial is for MacOS. Please refer to the [Windows Tutorial]() for Sourcetree if that is what you want to use.
-->

Unduh [Sourcetree](https://www.sourcetreeapp.com), Instal dan buka aplikasinya.

Anda akan melihat dialog modal "Sourcetree".

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-1-main.png" alt="SourceTree Main" />

Dari sini, Anda perlu mengklik tab *Remote*. Jika ini adalah instalasi pertama, maka kemungkinan Anda belum menghubungkan akun GitHub Anda. Lakukan hal tersebut dengan mengklik tombol "Connect".

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-2-main-connect.png" alt="SourceTree Connect" />

Dialog *Accounts* akan muncul. Klik "Add" di pojok kiri bawah. Kemudian pilih pengaturan yang sesuai untuk menambahkan GitHub (atau akun lain yang Anda inginkan) ke klien tersebut. Setelah Anda memilih pengaturan untuk GitHub, klik "Connect Account."

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-4-accounts-add.png" alt="SourceTree Connect Add" />

Ini akan membuka sebuah halaman di browser web Anda. Ikuti langkah-langkah yang diberikan untuk mengotorisasi akun Anda.

## Fork repository ini

Lakukan fork pada repo ini dengan mengklik tombol fork di bagian atas halaman ini.
<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/fork.png" alt="fork this repository" />
Ini akan membuat salinan (copy) dari repository ini di akun Anda.


## Clone repository tersebut

Di Sourcetree, klik pada tombol "Remote". Ini akan memuat semua repository GitHub Anda yang terdaftar di GitHub.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-5-cloning.png" alt="clone this repository" />

Setelah Anda mengklik tombol "Clone", Anda akan disajikan dengan tampilan lain untuk menentukan beberapa hal yang berbeda.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-6-cloning-confirm.png" alt="clone this repository" />

1) **Source URL:** Ini terisi secara otomatis dan Anda tidak perlu mengubahnya. Ini adalah URL dari mana proyek GitHub Anda berada.

2) **Destination Path:** Ini adalah lokasi fisik di komputer Anda di mana proyek ini akan disimpan.

3) **Name:** Ini adalah sebuah "Bookmark" untuk bagaimana Sourcetree akan mereferensikan proyek Anda. Anggap saja seperti sebuah *shortcut* (jalan pintas).

*Catatan: Biasanya nilai default di kolom-kolom ini sudah cukup baik.*

**Setelah Anda merasa pas, klik "Clone"**

Ini akan memunculkan *main repo browser* untuk repository Anda!

## Buat branch baru

Klik tombol branch pada toolbar.

Beri nama branch Anda "add-nama-anda-to-contribution", misalnya: "add-sally-to-contribution".

Untuk melakukan ini, klik **Branch (1)** yang akan meluncurkan dialog penamaan. Kemudian **Tambahkan nama Anda (2)** seperti yang baru saja dijelaskan. Terakhir klik **Create Branch**. Ini akan membuat branch yang baru saja Anda beri nama.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-7-branching.png" alt="name your branch" />


## Buat perubahan yang diperlukan dan commit perubahan tersebut

Sekarang buka file `Contributors.md` di sebuah editor teks dan tambahkan nama Anda ke dalamnya, beserta link URL Github Anda, lalu simpan file tersebut.

Anda seharusnya dapat melihat dan meninjau file yang telah diubah dan memutuskan apa yang ingin Anda tempatkan (*stage*). Staging penting untuk memberitahu Git dengan tepat perubahan file apa saja yang ingin Anda kaitkan dengan commit ini.

*Catatan: Jika Anda tidak melihat perbedaan (*diff*) file tersebut, klik **Uncommitted Files** di bagian atas dialog Anda*

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-8-viewing-changed-files.png" alt="edit some file(s)" />

Selanjutnya klik tombol **Commit** di kiri atas dialog. Ini akan menunjukkan area *staging* Anda.

Klik *Checkbox* untuk **menambahkan (add)** file tersebut ke staging area. Kemudian masukkan pesan commit.

*Catatan: Anda juga dapat memilih file (baik di area staging maupun unstaged) dan menambah/menghapus file dari masing-masing area dengan menggunakan tombol spasi*

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-9-committing.png" alt="stage your changes" />


Setelah Anda menambahkan perubahan Anda dan menambahkan pesan commit, Anda dapat menekan tombol **Commit** untuk akhirnya melakukan commit.

Selamat, Anda telah melakukan commit pada semua perubahan ke salinan lokal branch Anda dari fork `first-contributions` milik Anda. Lanjutkan!


## Push perubahan ke GitHub

Sekarang Anda siap untuk me-push (mendorong) perubahan Anda ke github. Ini akan di-push ke salinan proyek (fork) Anda sendiri. Ikuti langkah-langkah ini untuk me-push branch Anda ke atas. Pertama, klik **Push (1)**, ini akan menampilkan dialog remote/push. **Klik (2)** checkbox dari branch yang ingin Anda push. Pilih **OK (3)** dan ini akan me-push commit Anda ke Github.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-10-pushing.png" alt="origin or branch" />

## Ajukan perubahan Anda untuk direview (Pull Request)

Jika Anda pergi ke repository Anda di github, Anda akan melihat tombol `Compare & pull request`. Klik tombol tersebut.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/compare-and-pull.png" alt="create a pull request" />

Sekarang kirimkan (submit) pull request tersebut.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/submit-pull-request.png" alt="submit pull request" />

Segera saya akan menggabungkan (merge) semua perubahan Anda ke dalam master branch proyek ini. Anda akan mendapatkan email pemberitahuan setelah perubahan digabungkan.

## Ke mana selanjutnya?

Selamat! Anda baru saja menyelesaikan alur kerja standar _fork -> clone -> edit -> PR_ yang akan sering Anda temui sebagai kontributor!

Rayakan kontribusi Anda dan bagikan dengan teman dan pengikut Anda dengan mengunjungi [web app](https://firstcontributions.github.io/#social-share).

### [Materi tambahan](../additional-material/git_workflow_scenarios/additional-material.md)


## Tutorial Menggunakan Alat Lain
[Kembali ke halaman utama](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
