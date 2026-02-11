[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Kontribusi Pisanan

Pancen angel. Mesthi angel nalika pisanan nglakoni sawijining perkara. Utamane nalika sampeyan kolaborasi, nggawe kesalahan iku ora nyenengake. Kita pengin nyederhanakake cara para kontributor open-source anyar sinau lan menehi kontribusi kanggo pisanan.

Maca artikel lan nonton tutorial bisa mbantu, nanging apa sing luwih apik tinimbang langsung nglakoni ing lingkungan latihan? Proyek iki tujuane nyedhiyakake pandhuan lan nyederhanakake cara para pemula nggawe kontribusi pisanan. Yen sampeyan pengin nggawe kontribusi pisanan, tindakna langkah-langkah ing ngisor iki.

#### *Yen sampeyan ora kepenak nggunakake command line, [iki ana tutorial nggunakake piranti GUI.](#Tutorial-Nggunakake-Piranti-Liyane)*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork repositori iki" />

Yen sampeyan durung duwe git ing komputer, [pasang dhisik](https://help.github.com/articles/set-up-git/).

## Fork repositori iki

Fork repositori iki kanthi ngeklik tombol fork ing sisih ndhuwur kaca iki.
Iki bakal nggawe salinan repositori iki ing akun sampeyan.

## Clone repositori

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone repositori iki" />

Saiki clone repositori iki menyang komputer sampeyan. Bukak akun GitHub sampeyan, klik tombol clone banjur klik ikon *copy to clipboard*.

Bukak terminal lan jalanake perintah git iki:

```bash
git clone "url sing mau disalin"
```

ing kono "url sing mau disalin" (tanpa tanda kutip) iku url menyang repositori iki (fork sampeyan saka proyek iki). Deleng langkah-langkah sadurunge kanggo entuk url kasebut.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="salin URL menyang clipboard" />

Tuladha:

```bash
git clone https://github.com/jeneng-sampeyan/first-contributions.git
```

ing kono `jeneng-sampeyan` iku jeneng pangguna GitHub sampeyan. Ing kene sampeyan nyalin isi repositori first-contributions ing GitHub menyang komputer sampeyan.

## Gawe branch

Pindhah menyang direktori repositori ing komputer sampeyan (yen durung ana ing kono):

```bash
cd first-contributions
```

Saiki gawe branch nggunakake perintah `git checkout`:

```bash
git checkout -b <tambah-jeneng-branch-anyar>
```

Tuladha:

```bash
git checkout -b add-budi-santoso
```

(Jeneng branch ora kudu nganggo tembung *add* ing kono, nanging pancen wajar yen kalebu merga tujuan branch iki yaiku nambahake jeneng sampeyan menyang dhaptar.)

## Gawe owah-owahan sing dibutuhake lan commit owah-owahan kasebut

Saiki bukak file `Contributors.md` ing editor teks, tambahake jeneng sampeyan. Aja ditambahake ing wiwitan utawa pungkasan file. Lebokna ing ngendi wae ing tengah. Saiki, simpen file kasebut.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="cek status git" />

Yen sampeyan menyang direktori proyek lan nglakokake perintah `git status`, sampeyan bakal weruh ana owah-owahan.

Tambahake owah-owahan kasebut menyang branch sing mau digawe nggunakake perintah `git add`:

```bash
git add Contributors.md
```

Saiki commit owah-owahan kasebut nggunakake perintah `git commit`:

```bash
git commit -m "Add <jeneng-sampeyan> to Contributors list"
```

ganti `<jeneng-sampeyan>` nganggo jeneng sampeyan.

## Push owah-owahan menyang GitHub

Push owah-owahan sampeyan nggunakake perintah `git push`:

```bash
git push origin <tambah-jeneng-branch-sampeyan>
```

ganti `<tambah-jeneng-branch-sampeyan>` karo jeneng branch sing digawe sadurunge.

## Kirimake owah-owahan sampeyan kanggo ditinjau

Yen sampeyan menyang repositori sampeyan ing GitHub, sampeyan bakal weruh tombol `Compare & pull request`. Klik tombol kasebut.

<function_calls>
<invoke name="str_replace">
<parameter name="description">Continue the Javanese translation from the pull request section onwards