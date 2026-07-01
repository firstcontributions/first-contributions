# Apa itu squashing?

Dalam git, squashing mengacu pada penulisan ulang riwayat (history) commit Anda, sehingga Anda berakhir dengan satu commit dengan deskripsi perubahan yang telah dilakukan.
Hal ini biasanya dilakukan dalam proyek open source karena banyak riwayat dari suatu branch di proyek open source hanya relevan bagi developer yang membuatnya, dan ini memberikan cara yang lebih sederhana untuk mendeskripsikan perubahan yang dibuat dan juga membatalkannya (revert) jika diperlukan.

# Bagaimana cara men-squash commit?

Pertama, lakukan `git log` untuk meninjau commit yang ingin Anda gabungkan (merge) di branch Anda saat ini.

```bash
git log
```

Anda akan melihat serangkaian commit Anda seperti ini:

```
commit blablabla
Author: omguhh
Date:   10/10/20
    Commit message 1

commit blablabla2
Author: omguhh
Date:   10/10/20
    Commit message 2
```

Jadi sekarang setelah Anda melihat commit yang ingin Anda gabungkan menjadi satu, kita dapat melanjutkannya dengan ```git rebase```. Dengan asumsi Anda sudah familiar dengan ```git rebase```, kita dapat mulai men-squash commit dalam mode interaktif git rebase yang dapat Anda aktifkan seperti ini:

```bash
git rebase -i
```

Sekarang, dengan interactive rebasing Anda dapat menentukan titik awal dan akhir seberapa jauh Anda ingin mundur pada commit seperti ini:

```bash
git rebase -i HEAD~2
```

Menjalankan perintah ini akan menunjukkan kepada Anda sesuatu seperti berikut:

```
pick blablabla Changing test01.txt file
pick blablabla2 Adding dummy01.txt file

#
# Commands:
#  p, pick = use commit
#  r, reword = use commit, but edit the commit message
#  e, edit = use commit, but stop for amending
#  s, squash = use commit, but meld into previous commit
#  f, fixup = like "squash", but discard this commit's log message
#  x, exec = run command (the rest of the line) using shell
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
#
# However, if you remove everything, the rebase will be aborted.
#
# Note that empty commits are commented out
```

Jadi jika Anda ingin men-squash ```blablabla2``` ke dalam ```blablablabla```, Anda akan mengubah hal berikut:

```
pick blablabla Changing test01.txt file
squash blablabla2 Adding dummy01.txt file

```

Jika semuanya berjalan lancar, Anda akan mendapatkan hasil yang terlihat seperti ini:

```
# This is a combination of 2 commits.
# The first commit's message is:
commit message 1

# This is the 2nd commit message:

commit message 2
```

Anda dapat dengan bebas mengubahnya sebelum memutuskan untuk keluar dari editor guna menyimpan perubahan ini.

Menjalankan `git log` lagi akan menunjukkan kepada Anda pesan commit yang Anda masukkan sebelum keluar dari layar dengan commit yang sudah digabungkan menjadi satu.
