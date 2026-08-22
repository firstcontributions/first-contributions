# Rebase vs Merge

Saat berkontribusi pada proyek open-source, penting untuk memahami cara mengintegrasikan perubahan Anda dengan bersih.  
Dua cara umum untuk membawa pembaruan dari satu branch ke branch lain adalah **merge** dan **rebase**.


## Apa Itu Rebase?

**Rebasing** memainkan ulang (replays) commit Anda dari satu branch di atas branch yang lain — yang secara efektif memindahkan pekerjaan Anda untuk dimulai dari ujung branch yang lain.  
Hal ini menciptakan **riwayat commit yang linier dan bersih** tanpa adanya merge commit.

### Contoh

```bash
# Beralih ke feature branch Anda
git switch feature_branch

# Lakukan Rebase pada feature branch Anda di atas main
git rebase main
```

Atau, 
```bash
git checkout <branch-anda> 
git rebase <branch-yang-ingin-anda-salin-perubahannya>
```
> `git switch <branch>` dan `git checkout <branch>` keduanya beralih antar branch, tetapi `switch` lebih baru dan lebih mudah digunakan (user-friendly).

---
Baik merge maupun rebase digunakan untuk mengintegrasikan perubahan dari satu branch ke branch lainnya. 

**Merging** menggabungkan riwayat (history) dari dua branch dengan membuat sebuah **merge commit** baru. Ini **mempertahankan urutan kejadian yang sebenarnya**, menunjukkan dengan tepat bagaimana dan kapan branch tersebut menyimpang (diverged) dan bergabung kembali (rejoined). 

```bash
*   b576e33 (HEAD -> main) Merge branch 'feature' into main
|\
| * 22c5476 C4
| * b1a9c33 C3
* | f2a4d33 C2 (branch - 'feature')
|/
* c9f0a10 C1 (main)
```

Di sisi lain, **Rebasing**, **menerapkan kembali commit Anda** di atas status terbaru dari branch lain. Hal ini secara efektif **menjaga agar riwayat commit tetap linier dan bersih**, seolah-olah semua pekerjaan Anda terjadi secara berurutan setelah commit-commit pada branch target. 

```bash
* e4d2b3c (HEAD -> feature) C4
* 3f68a71 C3 (branch - 'feature')
* f2a4d33 C2
* c9f0a10 C1 (main)
```

``` bash
# Perintah ini akan menampilkan grafik commit bergaya ASCII langsung di terminal Anda.
# Ini menunjukkan riwayat commit dalam struktur seperti pohon (tree-like structure).
git log --graph --oneline --all
```

## Merge vs Rebase

| **Fitur**        | **Merge**                                      | **Rebase**                                  |
|------------------|------------------------------------------------|---------------------------------------------|
| **Riwayat**      | Mempertahankan riwayat kronologis yang sebenarnya| Menciptakan riwayat yang linier               |
| **Commit Ekstra**| Menambahkan satu ekstra merge commit            | Tidak ada commit ekstra                       |
| **Keterbacaan**  | Dapat menjadi berantakan dengan merge commit    | Lebih mudah dibaca dan diikuti                |
| **Penggunaan**   | Ideal untuk branch publik (misal, `main`)       | Ideal untuk branch personal atau feature      |


## Aturan Penting
**Jangan pernah melakukan rebase pada branch publik/bersama (seperti main).**
Rebasing menulis ulang riwayat commit, yang dapat menyebabkan masalah bagi kolaborator yang telah mendasarkan pekerjaannya pada commit-commit tersebut.
Selalu lakukan rebase branch personal atau feature Anda **ke main (onto main)**, bukan sebaliknya.

> Jika branch tersebut dibagikan (shared) — gunakan merge.
> Jika branch tersebut personal — gunakan rebase.


## Opsi Konfigurasi Git
Anda dapat memberitahu Git apakah harus melakukan merge atau rebase saat menarik (pulling) pembaruan:

```bash
# Selalu merge (perilaku default)
git config pull.rebase false

# Selalu rebase secara default (direkomendasikan untuk riwayat linier)
git config --global pull.rebase true
```

**CATATAN: Mengatur opsi global memastikan branch lokal Anda tetap bersih dan linier tanpa merge commit yang tidak diperlukan.**
