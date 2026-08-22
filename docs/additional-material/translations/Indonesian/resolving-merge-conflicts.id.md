# Apa itu merge conflict?

Merge conflict terjadi ketika perubahan dari branch yang berbeda saling berbenturan dan Git tidak dapat menggabungkannya secara otomatis. Skenario umumnya meliputi:

- Dua kontributor mengedit baris yang sama di suatu file.
- Satu kontributor menghapus file yang telah dimodifikasi oleh kontributor lain.
- Mengganti nama (rename) suatu file menjadi nama yang berbeda di branch yang terpisah secara bersamaan.

Dalam kasus seperti itu, Git akan menghentikan proses merge dan menandai file yang berkonflik untuk diselesaikan secara manual. Ada alat bantu yang membantu pengguna menyelesaikan konflik ini, tetapi dalam panduan ini, kita akan fokus pada baris perintah (command line) git.

## Bagaimana cara menyelesaikan merge conflict?

1. **Identifikasi File yang Berkonflik**
   Setelah mencoba melakukan merge, Git akan memberi tahu Anda tentang adanya konflik. Gunakan perintah berikut untuk mencantumkannya:

```bash
git status
```

Cari file yang terdaftar di bawah "Unmerged paths."

2. **Buka dan Periksa File yang Berkonflik**
   Buka setiap file yang berkonflik di editor teks pilihan Anda. Git menetapkan batas-batas untuk konflik menggunakan penanda (markers) berikut:

```plaintext
<<<<<<< HEAD
Perubahan Anda
=======
Perubahan yang masuk
>>>>>>> nama-branch
```

- `<<<<<<< HEAD` mewakili perubahan dari branch Anda saat ini.

- `=======` memisahkan perubahan yang berkonflik.

- `>>>>>>> nama-branch` menunjukkan perubahan yang masuk dari branch lain.

3. **Selesaikan Konflik**

Putuskan bagaimana Anda akan mengintegrasikan perubahan tersebut:

- Simpan perubahan Anda.
- Terima perubahan yang masuk.
- Gabungkan kedua perubahan dengan cara yang koheren/masuk akal.

Setelah membuat penyesuaian yang diperlukan, hapus penanda konflik (`<<<<<<<`, `=======`, `>>>>>>>`).

4. **Tandai Konflik sebagai Terselesaikan**
   Setelah Anda menyelesaikan konflik dalam sebuah file:

```bash
git add <namafile>
```

**Ulangi langkah ini untuk setiap file yang berkonflik.**

5. **Commit hasil Merge**
   Setelah men-stage (add) semua file yang diselesaikan:

```bash
git commit -m "Resolved merge conflicts"
```

🎉Ini menyelesaikan proses merge.🎉

---

# Informasi Tambahan

## Alat untuk Membantu Resolusi Konflik

- Git Merge Tool: Meluncurkan visual merge tool untuk membantu menyelesaikan konflik.

```bash
git mergetool
```

> Catatan: Pastikan Anda memiliki alat penggabungan yang diinstal (misal, Meld, KDiff3, Beyond Compare).

- Membatalkan Merge: Jika Anda ingin membatalkan proses merge:

```bash
  git merge --abort
```

## Praktik Terbaik untuk Menghindari Konflik

Tarik Perubahan Secara Teratur: Sering-seringlah menarik (pull) perubahan dari branch `main` untuk tetap *up-to-date*.

```bash
git pull origin main
```

Bekerja pada Feature Branches: Buat branch terpisah untuk setiap fitur atau perbaikan.

```bash
git checkout -b feature-branch
```

## Sumber Daya Tambahan

- [GitHub: Resolving Merge Conflicts via Command Line](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line)

- [Atlassian: Git Merge Conflicts Tutorial](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts)

- [FreeCodeCamp: Practical Guide to Merge Conflicts](https://www.freecodecamp.org/news/resolve-merge-conflicts-in-git-a-practical-guide/)

Dengan mengikuti panduan ini, Anda akan diperlengkapi dengan baik untuk menangani merge conflict dengan percaya diri, memastikan proses kontribusi yang lebih lancar untuk proyek open source mana pun!
