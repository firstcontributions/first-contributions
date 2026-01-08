[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Kontribusi pisanan

Proyek iki nduweni tujuan kanggo nyederhanakake lan nuntun cara para pamula nggawe kontribusi pisanan. Yen sampeyan pengin nggawe kontribusi pisanan, tindakake langkah ing ngisor iki.

_Yen sampeyan ora kepenak karo baris perintah, [iki tutorial nggunakake alat GUI.](#tutorials-using-other-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### Yen sampeyan ora duwe git ing mesin sampeyan, [instal](https://docs.github.com/en/get-started/quickstart/set-up-git).


## Garpu gudang iki

Garpu gudang iki kanthi ngeklik tombol garpu ing sisih ndhuwur kaca iki.
Iki bakal nggawe salinan repositori iki ing akun sampeyan.

## Kloning repositori

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Saiki tiron repositori garpu menyang mesin sampeyan. Pindhah menyang akun GitHub sampeyan, bukak gudang bercabang, klik tombol kode, banjur ing tab SSH banjur klik _copy url to clipboard_ icon.

Bukak terminal lan jalanake perintah git ing ngisor iki:

```bash
git clone "url you just copied"
```

ngendi "url sampeyan mung disalin" (tanpa tandha petik) punika url kanggo gudang iki (garpu proyek iki). Deleng langkah sadurunge kanggo njupuk url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Contone:

```bash
git clone git@github.com:this-is-you/first-contributions.git
```
ngendi `this-is-you` jeneng panganggo GitHub sampeyan. Ing kene sampeyan lagi nyalin isi repositori kontribusi pisanan ing GitHub menyang komputer.

## Nggawe cabang

Ganti menyang direktori repositori ing komputer (yen sampeyan durung ana):

```bash
cd first-contributions
```

Saiki gawe cabang nggunakake printah `git switch`:

```bash
git switch -c your-new-branch-name
```
Contone:

```bash
git switch -c your-new-branch-name
```

<detail>
<summary> <strong>Yen sampeyan nemu kesalahan nggunakake git switch, klik kene:</strong> </summary>

Yen pesen kesalahan "Git: `switch` dudu perintah git. Waca `git –help`" katon, kemungkinan amarga sampeyan nggunakake versi git sing lawas.

Ing kasus iki, coba gunakake `git checkout` tinimbang:

```bash
git checkout -b jeneng-cabang-anyar sampeyan
```

</detail>

## Gawe owah-owahan sing perlu lan tindakake owah-owahan kasebut

Saiki bukak file `Contributors.md` ing editor teks, tambahake jeneng sampeyan. Aja ditambahake ing wiwitan utawa pungkasan file. Sijine ing ngendi wae ing antarane. Saiki, simpen file kasebut.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="status git" />

Yen sampeyan pindhah menyang direktori proyek lan nglakokake perintah `git status`, sampeyan bakal weruh ana owah-owahan.

Tambahake owah-owahan kasebut menyang cabang sing lagi wae digawe nggunakake perintah `git add`:

```bash
git add Contributors.md
```

Saiki gawe owah-owahan kasebut nggunakake perintah `git commit`:

```bash
git commit -m "Add your-name to Contributors list"
```

ngganti `your-name` karo jeneng sampeyan.

## Push owah-owahan menyang GitHub

Push owahan sampeyan nggunakake printah `git push`:

```bash
git push -u origin your-branch-name
```

ngganti `your-branch-name` karo jeneng cabang sing digawe sadurunge.

<detail>
<summary> <strong>Yen ana kesalahan nalika meksa, klik kene:</strong> </summary>

- ### Kasalahan Authentication
     <pre>remote: Dhukungan kanggo otentikasi tembung sandhi wis dibusak tanggal 13 Agustus 2021. Mangga gunakake token akses pribadhi.
  remot: Mangga deleng https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ kanggo informasi luwih lengkap.
  fatal: Otentikasi gagal kanggo 'https://github.com/<your-username>/first-contributions.git/'</pre>
  Bukak [Github's Tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) kanggo nggawe lan ngatur kunci SSH menyang akun sampeyan.

  Uga, sampeyan bisa uga pengin mbukak 'git remote -v' kanggo mriksa alamat remot.
  
  Yen katon kaya iki:
  <pre>asal https://github.com/your-username/your_repo.git (fetch)
  origin https://github.com/your-username/your_repo.git (push)</pre>
  
  ngganti nggunakake printah iki:
  ```bash
  git remote set-url asal git@github.com:your-username/your_repo.git
  ```
  Yen ora, sampeyan isih bakal dijaluk jeneng pangguna lan sandhi lan entuk kesalahan otentikasi.
</detail>

## Kirim owahan kanggo ditinjau

Yen sampeyan pindhah menyang repositori ing GitHub, sampeyan bakal weruh tombol `Compare & pull request`. Klik tombol kasebut.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Saiki kirim panjalukan tarik.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Sakcepete aku bakal nggabungake kabeh owah-owahan sampeyan menyang cabang utama proyek iki. Sampeyan bakal entuk email kabar yen owah-owahan wis digabung.

## Saka ngendi arep lunga?

Sugeng! Sampeyan mung ngrampungake standar _fork -> clone -> edit -> pull request_ workflow sing bakal kerep ditemoni minangka kontributor!

Rayakan kontribusi sampeyan lan enggo bareng karo kanca lan pandherekipun kanthi pindhah menyang [web app](https://firstcontributions.github.io/#social-share).

Yen sampeyan pengin latihan liyane, priksa [code contribution](https://github.com/roshanjossey/code-contributions).

Saiki ayo miwiti kontribusi kanggo proyek liyane. Kita wis nyusun dhaptar proyek kanthi masalah sing gampang sampeyan bisa miwiti. Priksa [the list of projects in the web app](https://firstcontributions.github.io/#project-list).

### [Additional material](docs/additional-material/git_workflow_scenarios/additional-material.md)

## Tutorial Nggunakake Piranti Liyane

| <a href="docs/gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="docs/gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="docs/gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](docs/gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](docs/gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](docs/gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](docs/gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |

<p>Proyek iki didhukung dening:</p>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>
