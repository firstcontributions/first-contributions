[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

#### _อ่านหน้านี้ใน[ภาษาอื่น ๆ](Translations.md)_

# First Contributions

โปรเจกต์นี้มีเป้าหมายเพื่อช่วยผู้ที่เพิ่งเริ่มต้น (มือใหม่่) สามารถมีส่วนร่วมทำ Open Source ได้ง่ายขึ้น และช่วยแนะนำขั้นตอนต่าง ๆ ถ้านี่เป็นการมีส่วนร่วมพัฒนาโปรเจกต์ (Contributions) ครั้งแรก ให้ทำตามขั้นตอนด้านล่างนี้ได้เลย

_ถ้าคุณไม่ถนัดการใช้ command line, เรามีคำแนะนำสำหรับเครื่องมือแบบ GUI ให้[ที่นี่](#ฝึกการคอนทริบิ้วต์โดยใช้เครื่องมืออื่น-ๆ)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="แยกที่เก็บนี้" />

#### ถ้าหากยังไม่ได้ติดตั้ง git ลงบนเครื่องของคุณ ติดตั้งได้[ที่นี่](https://docs.github.com/en/get-started/quickstart/set-up-git)

## การ "Fork" โปรเจกต์นี้

เริ่มต้นด้วยการ Fork โปรเจกต์นี้ โดยคลิกที่ปุ่ม "Fork" ด้านขวาบนของหน้านี้
การทำเช่นนี้จะเป็นการสร้างสำเนา (Copy) ของโปรเจกต์นี้ไปไว้ในบัญชี GitHub ของคุณ

## การ "Clone" โปรเจกต์

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="โคลนที่เก็บนี้" />

ขั้นตอนต่อไปคือการ Clone Repository ที่คุณเพิ่ง Fork ไว้ลงมาที่เครื่องคอมพิวเตอร์ของคุณ ไปที่บัญชี GitHub ของคุณ เปิดหน้า Repository ที่ Fork มา จากนั้นคลิกที่ปุ่ม Code เลือกแท็บ SSH แล้วคลิกไอคอน _copy url to clipboard_

เปิดโปรแกรม Terminal แล้วรันคำสั่ง git ต่อไปนี้:

```bash
git clone "url ที่คุณเพิ่งคัดลอกมา"
```

โดย "url ที่คุณเพิ่งคัดลอกมา" (ไม่ต้องใส่เครื่องหมายคำพูด) คือ url ของ Repository ในบัญชีของคุณที่คุณเพิ่งคัดลอกมาจากขั้นตอนที่แล้ว (fork ของโปรเจกต์นี้ในบัญชีของคุณ)

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="คัดลอก URL ไปยังคลิปบอร์ด" />

ตัวอย่าง:

```bash
git clone git@github.com:this-is-you/first-contributions.git
```

โดย `this-is-you` คือชื่อผู้ใช้ (Username) GitHub ของคุณ ในขั้นตอนนี้ ระบบกำลังคัดลอกเนื้อหาทั้งหมดของ Repository `first-contributions` จาก GitHub ลงมาที่คอมพิวเตอร์ของคุณ

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

ตอนนี้ให้เปิดไฟล์ `Contributors.md` ในโปรแกรม text editor แล้วเพิ่มชื่อของคุณลงไป โดยแทรกไว้ตรงไหนก็ได้ระหว่างรายชื่ออื่นๆ (หลีกเลี่ยงการใส่ไว้บรรทัดแรกสุดหรือท้ายสุดของไฟล์) จากนั้นเซฟไฟล์

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

Push โค้ดที่คุณเพิ่งแก้ไขขึ้นไปยัง GitHub ด้วยคำสั่ง `git push`:

```bash
git push -u origin ชื่อ-branch-ของคุณ
```

โดยแทนที่ `ชื่อ-branch-ของคุณ` ด้วยชื่อ Branch ที่คุณสร้างไว้ในขั้นตอนก่อนหน้า

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

## ส่งผลงานของคุณเพื่อรอการรีวิว (Pull Request)

ถ้าคุณไปที่ repository ของคุณบน GitHub คุณจะเห็นปุ่ม `Compare & pull request` ให้คลิกปุ่มนั้น

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="เปรียบเทียบและสร้าง pull request" />

ตอนนี้ให้ส่ง pull request

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="ส่ง pull request" />

หลังจากนั้นไม่นาน ทีมงานจะทำการ Merge (รวม) โค้ดที่คุณแก้ไขเข้ามายัง Main Branch ของโปรเจกต์หลัก และคุณจะได้รับอีเมลแจ้งเตือนเมื่อกระบวนการนี้เสร็จสิ้น

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
