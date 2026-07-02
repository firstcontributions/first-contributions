[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

#### _อ่านหน้านี้ใน[ภาษาอื่น ๆ](Translations.md)_

# First Contributions

โปรเจกต์นี้มีเป้าหมายเพื่อทำให้การมีส่วนร่วมครั้งแรกของผู้เริ่มต้นง่ายขึ้น และช่วยแนะนำขั้นตอนต่าง ๆ หากคุณกำลังจะมีส่วนร่วมเป็นครั้งแรก ให้ทำตามขั้นตอนด้านล่างนี้

_ถ้าคุณไม่ถนัดการใช้ command line, [เรามีบทแนะนำสำหรับเครื่องมือแบบ GUI ให้ที่นี่](#ฝึกการคอนทริบิ้วต์โดยใช้เครื่องมืออื่น-ๆ)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="แยกที่เก็บนี้" />

#### ถ้าหากคุณยังไม่ได้ติดตั้ง git ลงบนเครื่องของคุณ [ติดตั้งได้ที่นี่](https://docs.github.com/en/get-started/quickstart/set-up-git)

## การ "Fork" โปรเจกต์นี้

Fork โปรเจกต์นี้โดยคลิกปุ่ม "Fork" ที่ด้านบนของหน้านี้
ซึ่งจะสร้างสำเนาของโปรเจกต์นี้ไว้ในบัญชีของคุณ

## การ "Clone" โปรเจกต์

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="โคลนที่เก็บนี้" />

ตอนนี้ให้ clone repository ที่คุณ fork ไว้ลงมาที่เครื่องของคุณ ไปที่บัญชี GitHub ของคุณ เปิด repository ที่ fork ไว้ คลิกปุ่ม Code จากนั้นเลือกแท็บ SSH แล้วคลิกไอคอน _copy url to clipboard_

เปิดโปรแกรมเทอร์มินอล แล้วรันคำสั่ง git ต่อไปนี้:

```bash
git clone "url ที่คุณเพิ่งคัดลอกมา"
```

โดย "url ที่คุณเพิ่งคัดลอกมา" (ไม่ต้องใส่เครื่องหมายคำพูด) คือ url ของ repository นี้ (fork ของโปรเจกต์นี้ในบัญชีของคุณ) ดูขั้นตอนก่อนหน้าเพื่อคัดลอก url

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="คัดลอก URL ไปยังคลิปบอร์ด" />

ตัวอย่าง:

```bash
git clone git@github.com:this-is-you/first-contributions.git
```

โดย `this-is-you` คือชื่อผู้ใช้ GitHub ของคุณ ในขั้นตอนนี้คุณกำลังคัดลอกเนื้อหาของ repository first-contributions บน GitHub ลงมาที่คอมพิวเตอร์ของคุณ

## การสร้าง branch

เปลี่ยนไปยัง directory ของ repository บนคอมพิวเตอร์ของคุณ (หากคุณยังไม่ได้อยู่ในนั้น):

```bash
cd first-contributions
```

ตอนนี้ให้สร้าง branch ด้วยคำสั่ง `git switch`:

```bash
git switch -c ชื่อ-branch-ใหม่ของคุณ
```

ตัวอย่าง:

```bash
git switch -c add-alonzo-church
```

<details>
<summary> <strong>หากคุณพบข้อผิดพลาดขณะใช้ git switch, คลิกที่นี่:</strong> </summary>

ถ้าข้อความผิดพลาด "Git: `switch` is not a git command. See `git –help`" แสดงขึ้นมา อาจเป็นเพราะคุณใช้ git เวอร์ชันเก่า

ในกรณีนี้ ให้ลองใช้ `git checkout` แทน:

```bash
git checkout -b ชื่อ-branch-ใหม่ของคุณ
```

</details>

## แก้ไขสิ่งที่จำเป็นและ commit การเปลี่ยนแปลงเหล่านั้น

ตอนนี้ให้เปิดไฟล์ `Contributors.md` ในโปรแกรม text editor แล้วเพิ่มชื่อของคุณลงไป อย่าเพิ่มไว้ที่จุดเริ่มต้นหรือท้ายไฟล์ ให้ใส่ไว้ตรงไหนก็ได้ระหว่างนั้น จากนั้นเซฟไฟล์

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="สถานะ git" />

ถ้าคุณไปที่ directory ของโปรเจกต์และรันคำสั่ง `git status` คุณจะเห็นว่ามีการเปลี่ยนแปลงเกิดขึ้น

เพิ่มการเปลี่ยนแปลงเหล่านั้นเข้าไปใน branch ที่คุณเพิ่งสร้าง ด้วยคำสั่ง `git add`:

```bash
git add Contributors.md
```

ตอนนี้ commit การเปลี่ยนแปลงเหล่านั้นด้วยคำสั่ง `git commit`:

```bash
git commit -m "Add your-name to Contributors list"
```

โดยแทนที่ `your-name` ด้วยชื่อของคุณ

## "Push" การเปลี่ยนแปลงขึ้น GitHub

Push การเปลี่ยนแปลงของคุณด้วยคำสั่ง `git push`:

```bash
git push -u origin ชื่อ-branch-ของคุณ
```

โดยแทนที่ `ชื่อ-branch-ของคุณ` ด้วยชื่อ branch ที่คุณสร้างไว้ก่อนหน้านี้

<details>
<summary> <strong>หากคุณพบข้อผิดพลาดขณะ push, คลิกที่นี่:</strong> </summary>

- ### ข้อผิดพลาดเกี่ยวกับการยืนยันตัวตน
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/&lt;your-username&gt;/first-contributions.git/'</pre>
  ไปที่[บทแนะนำของ GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) เกี่ยวกับการสร้างและตั้งค่า SSH key ให้กับบัญชีของคุณ

  นอกจากนี้ คุณอาจต้องรันคำสั่ง 'git remote -v' เพื่อตรวจสอบ remote address ของคุณ

  ถ้ามันมีลักษณะประมาณนี้:
  <pre>origin	https://github.com/your-username/your_repo.git (fetch)
  origin	https://github.com/your-username/your_repo.git (push)</pre>

  ให้เปลี่ยนด้วยคำสั่งนี้:
  ```bash
  git remote set-url origin git@github.com:your-username/your_repo.git
  ```
  ไม่อย่างนั้นคุณจะยังถูกถาม username และ password และเจอข้อผิดพลาดเกี่ยวกับการยืนยันตัวตนอยู่
</details>

## ส่งผลงานของคุณเพื่อรอการรีวิว

ถ้าคุณไปที่ repository ของคุณบน GitHub คุณจะเห็นปุ่ม `Compare & pull request` ให้คลิกปุ่มนั้น

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="เปรียบเทียบและสร้าง pull request" />

ตอนนี้ให้ส่ง pull request

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="ส่ง pull request" />

อีกไม่นานผมจะ merge การเปลี่ยนแปลงทั้งหมดของคุณเข้าสู่ main branch ของโปรเจกต์นี้ คุณจะได้รับอีเมลแจ้งเตือนเมื่อการเปลี่ยนแปลงถูก merge แล้ว

## เสร็จแล้วทำยังไงต่อดี

ยินดีด้วย คุณเพิ่งทำ workflow มาตรฐานของการมีส่วนร่วมแบบ _fork -> clone -> edit -> pull request_ เสร็จเรียบร้อยแล้ว ซึ่งเป็นขั้นตอนที่คุณมักจะพบในฐานะ contributor

ฉลองการมีส่วนร่วมของคุณและแบ่งปันให้เพื่อน ๆ หรือผู้ติดตามของคุณ โดยไปที่ [web app](https://firstcontributions.github.io/#social-share)

หากคุณต้องการฝึกเพิ่มเติม ลองดู [code contributions](https://github.com/roshanjossey/code-contributions)

ตอนนี้มาเริ่มต้นมีส่วนร่วมกับโปรเจกต์อื่น ๆ กัน เราได้รวบรวมรายชื่อโปรเจกต์ที่มี issue ง่าย ๆ ให้คุณเริ่มต้นได้ ลองดู[รายชื่อโปรเจกต์ใน web app](https://firstcontributions.github.io/#project-list)

### [ข้อมูลอื่น ๆ เพิ่มเติม](../additional-material/git_workflow_scenarios/additional-material.md)

## ฝึกการคอนทริบิ้วต์โดยใช้เครื่องมืออื่น ๆ

| <a href="../gui-tool-tutorials/translations/github-desktop-tutorial.th.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/960px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/translations/github-desktop-tutorial.th.md)                                                                                           | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                       | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                     | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                               | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                    | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                |
