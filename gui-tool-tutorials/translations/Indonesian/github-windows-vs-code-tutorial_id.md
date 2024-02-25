[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Kontribusi Pertama

| <img alt="Visual Studio Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width="40"> | Visual Studio Code |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |

Sulit. Memang selalu sulit melakukan sesuatu untuk pertama kali. Khususnya ketika kamu berkolaborasi, membuat sebuah masalah bukanlah hal yang mengenakkan. Tetapi proyek terbuka
berarti kolaborasi dan kerjasama. Kami ingin menyederhanakan cara belajar bagi kontributor dan cara berkontribusi untuk pertama kali.

Membaca artikel & menonton tutorial bisa membantu, tetapi lebih baik praktek langsung tanpa membuat masalah apapun pada proyek. Laman ini bertujuan untuk memberikan panduan & menyederhanakan cara bagi pemula untuk membuat kontribusi pertama. Ingat semakin santai kamu, maka semakin baik kamu belajar. Jika kamu ingin membuat kontribusi pertama, cukup ikuti langkah-langkah sederhana di bawah ini. Kami janji, ini akan menyenangkan kok.

Jika kamu belum punya Visual Studio Code pada perangkat mu, [install disini](https://code.visualstudio.com/download).


**Perlu Diingat:** Tutorial ini dibuat menggunakan Visual Studio Code (Versi 1.27.2) pada Windows 10. Nanti dalam tutorial ini kita akan menggunakan beberapa shortcut keyboard. Ini mungkin berbeda pada sistem operasi lain (macOS/Linux) serta bahasa keyboard (UK, DE, dll). Kamu dapat menelusuri daftar pintasan mu dengan mencari "shortcut" di Palet Perintah.

## Fork repositori ini

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Fork repo ini dengan mengklik tombol fork di kanan atas halaman ini. Ini akan membuat salinan repositori ini di akun GitHub Anda.

GitHub selalu menjaga repo mu dan sumber repo yang sudah kamu fork supaya tetap pada jalurnya. Kamu bisa menganggap repo mu sebagai salinan pekerjaan.

Sebagian besar repo GitHub tingkat atas (yaitu yang tidak di-copy dari repo lain mana pun) mempunyai tim inti yang terdiri dari orang-orang yang dapat langsung melakukan perubahan. Semua kontributor lain harus melakukan fork repo dan membuat perubahan pada fork, lalu membuat Pull Request untuk meminta perubahan mereka digabungkan kembali ke repo tingkat atas. Jika administrator repo tingkat atas menyukai perubahan, mereka akan menggabungkan perubahan mu dan kamu bisa mendapatkan reputasi dan nasib baik! Lebih lanjut tentang cara melakukannya akan dibahas nanti.

## Klon Repositori mu

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Langkah selanjutnya adalah mengkloning repo mu ke perangkat mu sehingga bisa segera mulai membuat perubahan. VS Code membutuhkan URL repo mu agar terhubung, jadi klik tombol "clone" dan kemudian klik ikon "copy to clipboard".

**HATI-HATI:** Satu kesalahan yang sering dilakukan oleh kontributor baru adalah mengkloning repo utama yang kamu fork _sumbernya_ daripada mengkloning repo mu sendiri. Periksa alamat browser mu dan pastikan kamu mengkloning repo mu sendiri.

Sekarang buka Visual Studio Code. Halaman selamat datang dari VS Code akan muncul. Dari sana tekan `F1` untuk membuka bar yang ditunjukkan di bawah ini. Perhatikan bahwa sudah ada tanda `>` (lebih besar dari) di kolom teks. Anda juga dapat membuka input prompt dengan menekan `CTRL-P` lalu ketik `>`.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone.png" alt="Clone Popup (Command Popup)" />

Anda mungkin memperhatikan bahwa sudah ada beberapa perintah tidak jelas yang tercantum di bawah ini. Itu adalah perintah yang digunakan baru-baru ini. Jadi, hiraukan saja.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone1.png" alt="Clone repo" />

Sekarang ketik `git clone`, hanya `git` atau `clone` (berfungsi seperti melakukan pencarian).
Pilih Entri `Git: Clone` dan tekan `Enter`

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone2.png" alt="Paste Repository URL in" />

Tempelkan URL repositori kamu dan tekan `Enter`. Ini akan membuka File Explorer di mana kamu dapat memilih di mana repositori Git harus disimpan

**Penting**: Pastikan itu adalah repositori yang kamu fork dan bukan yang asli, jika tidak maka tidak akan berfungsi

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone3.png" alt="Status popup" />

Kamu akan melihat status popup di kanan bawah Visual Studio Code. Setelah selesai, kamu dapat membuka repositori kloning (di folder yang sudah kamu pilih) menggunakan tombol di dialog.

## Membuat Cabang (Branch)

Buka kembali palet perintah dengan menekan `F1`. Ketik `branch` dan pilih perintah `create branch` dari sana. Pada langkah berikutnya ketik nama cabang baru kamu, misalnya `add-david-kroell`. Tekan enter dan cabang akan dibuat. Cabang juga sudah siap dipakai. [Apa artinya checkout?](https://www.git-scm.com/docs/git-checkout)

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-branch.png" alt="Branches Command Palette" />

## Buat Perubahan yang diperlukan

Buka `Contributors.md` dan tambahkan nama kamu di mana saja di file. File ini berisi GFM (GitHub Flavoured Markdown) yang merupakan ciri khas sintaks <a href="https://en.wikipedia.org/wiki/Markdown">markdown</a>.

Salin salah satu kontributor lain&apos; baris dan modifikasi dengan nama mu untuk memastikan kamu menggunakan sintaks yang benar - itu bisa pilih-pilih

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-changes.png" alt="Add your name" />

## Commit & Push perubahan ke GitHub

Di sisi kiri VS Code adalah menu dengan 5 ikon yang ditampilkan. Pilih ikon versi kontrol/Sumber Kontrol.
(Pintasan: Ctrl + Shift + G)

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-commit.png" alt="Commit changes" />

File explorer menampilkan semua file yang diubah setelah komit terakhir. Dengan mengarahkan penunjuk pada file dan mengklik `+` (plus) file akan disiapkan.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-commit1.png" alt="Stashed Files">

Ketik sesuatu pada baris di atas explorer dan tekan tanda centang. Perubahan telah tersimpan pada salinan lokal kamu. Sekarang perubahan harus di _push_ kembali ke GitHub.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-push.png" alt="Stashed Files">

Gunakan ikon titik tiga untuk membuka menu tempat kamu akan memilih opsi `Publish Branch`. Ini akan membuka dialog untuk memasukkan kredensial GitHub kamu.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-gh-auth.png" alt="Stashed Files">

## Submit perubahan mu untuk diperiksa

Dititik ini kamu telah menyelesaikan perubahan mu tetapi masih berada di repo mu sendiri. Langkah ini akan menunjukkan bagaimana cara mengirimkan permintaan ke administrator repo tingkat atas untuk menggabungkan perubahan

Pada repo mu di GitHub, kamu akan melihat tombol `Compare & pull request` di sebelah pemberitahuan cabang baru. Klik tombol itu.

<img src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Sekarang kirimkan permintaan _pull_.

<img src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Segera saya akan menggabungkan semua perubahan mu ke dalam cabang utama proyek ini. Kamu akan mendapatkan email pemberitahuan setelah perubahan digabungkan.

## Kemana lagi setelah ini?

Selamat! kamu baru saja menyelesaikan alur kerja _fork -> clone -> edit -> PR_ standar yang akan sering kamu temui sebagai kontributor!

Rayakan kontribusi mu dan bagikan dengan teman dan pengikut kamu dengan membuka [web app](https://firstcontributions.github.io#social-share).

Kamu dapat bergabung dengan tim slack kami jika memerlukan bantuan atau memiliki pertanyaan. [Bergabung dengan tim Slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).


### [ Materi tambahan ](../../additional-material/translations/additional-material.id.md)



## Tutorial menggunakan Alat lain
[Kembali ke halaman utama](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
