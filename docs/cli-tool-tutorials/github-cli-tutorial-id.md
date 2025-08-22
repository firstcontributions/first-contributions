[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Kontribusi Pertama

| <img alt="GitHub Desktop" src="https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png" width="200"> | GitHub Command Line Interface (CLI) |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |

Ini merupakan panduan untuk seseorang yang ingin melakukan semuanya lewat terminal. Hal ini dapat kita lakukan berkat adanya [Github-CLI](https://cli.github.com/), sehingga kontribusi pertamamu menjadi lebih menyenangkan dan memotivasi kamu untuk terus berkontribusi.

Panduan ini sedikit lebih menantang karena kita tidak menggunakan GUI sama sekali, namun tentunya tetap seru dan bisa kamu ikuti dengan mudah.

Prasyarat pertama, kamu harus:

- Memastikan Git sudah terinstall (cara install [git](https://git-scm.com/downloads)))
- Mempunyai akun Github

Selanjutnya, kita perlu menginstall `github-cli` di sistem kita dengan mengikuti langkah-langkah pada [dokumentasi resmi](https://github.com/cli/cli#installation)

Setelah itu, kita harus login ke CLI dengan menjalankan perintah:

```bash
gh auth login
```

Ikuti instruksinya sampai kamu berhasil login.

# Fork repositori ini

Caranya sangat mudah, dengan menjalankan perintah:
```bash
gh repo fork firstcontributions/first-contributions
```

**Penting: Pilih opsi "yes" ketika muncul pertanyaan untuk mengkloning (clone) repositorinya.**

# Buat branch baru

Kita dapat melakukannya menggunakan git. Caranya dengan menjalankan perintah ini. Nama branch dapat kamu ganti sesuai dengan yang kamu mau, contohnya:

```bash
git switch -c add-john-doe
```

# Lakukan perubahan yang diperlukan, kemudian Commit perubahan tersebut

Sekarang, kamu bisa buka file `Contributors.md` menggunakan teks editor pilihanmu, dan menambahkan namamu. Jangan lupa untuk save file nya.

Pada direktori proyek ini, jalankan perintah `git status`, kamu bisa melihat perubahan yang telah dilakukan.
<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Tambahkan perubahan tersebut ke branch yang sudah kamu buat menggunakan perintah `git add`:
`git add Contributors.md`

Kemudian commit perubahan tersebut menggunakan perintah `git commit`:
`git commit -m "Add your-name to Contributors list`
ganti `your-name` menggunakan namamu.

# Push perubahan ke Github

Push perubahan yang kamu lakukan dengan perintah `git push`:

```
git push origin -u your-branch-name
```

ubah `your-branch-name` dengan nama branch yang kamu buat sebelumnya.

<details>
<summary> <strong>Kalo ada error saat melakukan push, klik di sini:<strong> </summary>

- ### Authentication Error
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  Buka [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) tentang mengenerate dan menkonfigurasi SSH key untuk akunmu.

</details>

# Submit perubahanmu untuk direview

Jalankan perintah berikut untuk membuat pull request supaya perubahanmu bisa direview:

```bash
gh pr create --repo firstcontributions/first-contributions
```

Setelah itu, submit pull requestnya.

Kamu bisa menjalankan perintah `gh status` untuk melihan pull request yang kamu ajukan.

## Selanjutnya apa?

Selamat, kamu telah menyelesaikan langkah _fork -> clone -> edit -> pull request_ yang pasti akan kamu lakukan saat menjadi kontributor.

Rayakan kontribusimu dan bagikan ke kawan-kawan mu dengan cara pergi ke [web app](https://firstcontributions.github.io/#social-share).

Kamu juga bisa join ke slack team kami jika kamu butuh bantuan atau punya pertanyaan. [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA).

Sekarang, kamu bisa mulai berkontribusi ke proyek-proyek lain. Kami telah mengumpulkan beberapa proyek dengan issues yang mudah diselesaikan untuk kamu. Cek [list nya di web app](https://firstcontributions.github.io/#project-list))

### [Materi tambahan](additional-material/git_workflow_scenarios/additional-material.md)

## Tutorials Menggunakan Tools Lainnya

[Kembali ke halaman utama](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
