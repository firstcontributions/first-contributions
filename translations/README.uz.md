[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Birinchi hissalar 

Ushbu loyiha yangi boshlanuvchilarning birinchi hissasini qo'shish usullarini soddalashtirish va yo'naltirishga qaratilgan. Agar siz birinchi hissangizni qo'shmoqchi bo'lsangiz, quyidagi amallarni bajaring.   

_Agar buyruq satri sizga mos bo'lmasa, [Bu erda GUI vositalaridan foydalanib amalga oshirishga oid darsliklari mavjud](#boshqa-vositalardan-foydalanish-uchun-qollanmalar)_


<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="repositoryni fork qiling" />

#### Agar kompyuteringizda git mavjud bo'lmasa, [buni o'rnating](https://help.github.com/articles/set-up-git/).

## Bu repositoryni fork qilib oling

Bu repositoryni ushbu sahifaning yuqorisidagi fork tugmasini bosish orqali fork qilib oling.
Bu akkountingizda ushbu repositoryning nusxasini yaratadi.

## Bu repositoryni klon qilib oling

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="bu repositoryni klon qilib oling" />

Endi fork qilingan repositoryni kompyuteringizga klon qiling. Github akkountingizga kirib, fork qilingan repositoryni oching, code tugmasi ustiga bosing va keyin _copy to clipboard_ belgisi (icon) ustiga bosing.

Terminalni oching va quyidagi git buyruqlarini yurg'izing:

```bash
git clone "siz horizgina ko'chirib olgan url"
```

bu yerda "siz horizgina ko'chirib olgan url" (qo'shtirnoqlarsiz) ushbu repositoryning (siz fork qilingan proyekt) 'URL'idir. URLni olish uchun oldingi bosqichlarni ko'ring.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="urlni klipboardga ko'chiring" />

Misol uchun:

```bash
git clone https://github.com/bu-siz/first-contributions.git
```

bu yerdagi `bu-siz` sizning Github akkount nomingiz (username). Bu yerda Githubdagi  first-contributions repositorysining kontentlarini kompyuteringizga
ko'chiryapsiz. 

## Branch yaratish

Kompyuteringizda repository papkasiga kiring (agar u yerda bo'lmasangiz)

```bash
cd first-contributions
```

Endi `git switch` buyrug'i orqali branch yarating:

```bash
git switch -c yangi-branch-nomingiz
```

Misol uchun:

```bash
git switch -c add-aliml92
```

## Kerakli o'zgarishlarni qiling va bu o'zgarishlarni commit qiling

Endi matn muharririda `Contributors.md` faylini oching, unga ismingizni qo'shing. Uni faylning boshiga yoki oxiriga qo'shmang. Uni istalgan o'rta qismga  qo'shing. Endi faylni saqlang. 

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Agar proyekt papkasiga o'tsangiz va `git status` buyrug'ini yurg'izsangiz, o'zgarishlar borligini ko'rasiz.

`git add` buyrug'i yordamida hosil qilgan branchingizga o'zgarishlarni qo'shing:

```bash
git add Contributors.md
```

Endi `git commit` buyrug'i yordamida bu o'zgarishlarni commit qiling: 

```bash
git commit -m "Contributors royxatiga ismingiz-ni kiritish"
```
`ismingiz-` ni o'rniga o'zingizni ismingizni yozing.

## O'zgarishlarni Githubga push qilish

`git push` buyrug'i bilan o'zgartishlaringizni push qiling:

```bash
git push origin -u yangi-branch-nomingiz
```

albatta, `yangi-branch-nomingiz` ni biroz oldin yaratgan branch nomiga almashtirgan holda.

<details>
<summary> <strong>Push qilish vaqtida biror xatolarni ko'rsangiz, bu yerni bosing</strong> </summary>

- ### Autentifikatsiya Xatoligi
<pre>
  remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'
</pre>

Akkountingizga SSH kalit yaratish va konfiguratsiya qilish uchun [GitHub qo'llanma](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) ga o'ting.

</details>

## O'zgartirishlaringizni ko'rib chiqilishi uchun topshirish

Agar Githubdagi repositoryingizga o'tsangiz, `Compare & pull request` tugmasini ko'rasiz. O'sha tugmani bosing.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="pull request hosil qilish" />

Endi pull requestni submit qiling.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="pull request submit qilish" />

Tez orada men sizning barcha o'zgarishlaringizni ushbu proyektning main branchiga birlashtiraman. O'zgarishlar birlashtirilgandan so'ng sizga elektron pochta xabarnomasi keladi.

## Bu yerdan qayerga borish?

Tabriklayman! Siz horizgina contributor sifatida tez-tez uchraydigan standard ish ketma-ketligi ya'ni _fork -> clone -> edit -> pull request_ ni tamonladingiz. 

Hissangizni nishonlang va [web app](https://firstcontributions.github.io/#social-share)ga o'tish orqali do'stlaringizga va ergashuvchilaringizga ulashing. 


Agar sizga yordam kerak bo'lsa yoki savollaringiz bo'lsa, bizning slack jamoamizga qo'shilishingiz mumkin.[Slack jamoasiga qo'shiling](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Endi boshqa proyektlarga hissa qo‘shishni boshlaylik. Siz boshlashingiz mumkin bo'lgan oson masalalar bilan proyektlar ro'yxatini tuzdik. Ko'zdan kechiring [web appdagi proyektlar ro'yxati](https://firstcontributions.github.io/#project-list).

### [Qo'shimcha materiallar](additional-material/git_workflow_scenarios/additional-material.md)

## Boshqa Vositalardan Foydalanish Uchun Qollanmalar

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |
