[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# อยากเริ่ม Contribute โปรเจคใน GitHub ของผู้อื่นเป็นครั้งแรกใช่ไหม?

แน่นอนว่ามันอาจฟังดูเป็นเรื่องยาก, เพราะครั้งแรกของทุกอย่างมันมักจะยากเสมอแหละ โดยเฉพาะการทำงานร่วมกับผู้อื่น เพราะเมื่อเราทำอะไรผิดพลาดเรามักจะรู้สึกไม่สบายใจ
แต่สำหรับโลกของโอเพนซอร์ส(open source) มันคือโลกของการทำงานร่วมกัน! ดังนั้นไม่ต้องกลัว เราจะสอนให้คุณรู้วิธีในการ contribute ผลงานร่วมกับผู้อื่นใน GitHub แบบง่ายๆ เลยล่ะ

การอ่านบทความและการทำตามตัวอย่างต่างๆ ก็อาจจะช่วยได้ แต่จะมีอะไรดีไปกว่าการที่เราได้ลงมือทำสิ่งนั้นๆ ด้วยตัวเองล่ะ! สำหรับโปรเจ็คนี้จะช่วยสอนให้มือใหม่ส่ง contribute กับโปรเจคต่างๆได้อย่างง่ายๆเลย เพียงทำตามขั้นตอนต่อไปนี้

โปรดทำใจให้สบาย ยิ่งคุณผ่อนคลายมากเท่าไหร่ คุณก็ยิ่งเรียนรู้ได้ดีมากขึ้นเท่านั้น!

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

ถ้าหากคุณยังไม่ได้ติดตั้ง git ลงบนเครื่องของคุณ คุณสามารถ[ติดตั้งได้ที่นี่]( https://help.github.com/articles/set-up-git/)

ก่อนอื่นเลย หาโปรเจคที่คุณอยากจะร่วม contribute ก่อนเลย เมื่อคุณเจอโปรเจคที่สนใจแล้วมาเริ่มทำตามขั้นตอนต่อไปนี้กัน
(ต่อไปนี้เราจะขอเรียกโปรเจคต้นทางว่า "โปรเจ็คต้นน้ำ" (Source-project\Upstream-project))

## การ "Fork" โปรเจ็ค
เพื่อให้คุณสามารถคัดลอกเพื่อแยกโปรเจ็คต้นน้ำออกไปทำที่แอคเคาน์ส่วนตัวของคุณได้ โดยการกดปุ่ม "Fork" ที่ด้านบนของหน้านี้

แล้วโปรเจ็คต้นน้ำจะถูกคัดลอกนำไปใส่ไว้ในแอคเคาน์ของคุณ

## การ "Clone" โปรเจ็ค

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

การ clone โปรเจคนั้น เป็นการ download sourcecode จาก GtiHub repository นั้นๆ มาลงคอมพิวเตอร์ของคุณ
โดยการคลิ๊กที่ปุ่ม "Clone" แล้วเลือก *Copy to clipboard* (คำสั่งคัดลอก)

เปิดโปรแกรมเทอร์มินอลในเครื่อง (เช่น Terminal ใน MacOS หรือ cmd ใน Windows) แล้วรันคำสั่ง git ต่อไปนี้:

```bash
git clone "url ที่คัดลอกไว้"
```
"url ที่คัดลอกไว้" (ไม่ต้องใส่ " ") คือ url ของโปรเจ็คของคุณ คุณสามารถเลื่อนกลับไปดูวิธีการคัดลอก url ได้จากหัวข้อก่อนหน้านี้

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

ตัวอย่าง:
```bash
git clone https://github.com/this-is-you/first-contributions.git
```
`this-is-you` คือชื่อ username ของคุณบน GitHub ถึงตรงนี้คุณได้ "Clone" โปรเจ็ค first-contributions ไปไว้ที่คอมพิวเตอร์ของคุณแล้ว

## การสร้าง branch

ในโปรแกรมเทอร์มินอล เปลี่ยน directory ไปยังที่ที่คุณได้ Clone โปรเจ็คไว้:

```bash
cd first-contributions
```
ตรงนี้ให้สร้าง branch (แตกกิ่งการทำงานใหม่) ด้วยคำสั่ง `git checkout`:
```bash
git checkout -b <ชื่อ branch>
```

ตัวอย่าง:
```bash
git checkout -b add-alonzo-church
```
(ปกติชื่อของ branch ไม่จำเป็นต้องมีคำว่า *add* แต่ในโปรเจ็คนี้อยากให้ใช้ add-ชื่อ-ของ-คุณ เพราะชื่อของคุณจะไปแสดงอยู่ในรายชื่อ Contributors (ผู้เข้าร่วม) ของโปรเจ็คนี้

## เพิ่มหรือลดโค้ดลงไปเลย แล้วอย่าลืม "Commit" บอกว่าคุณได้เปลี่ยนอะไรไปบ้างล่ะ

ตอนนี้ให้เปิดไฟล์ `Contributors.md` ในโปรแกรม text editor เพิ่มชื่อของคุณลงไป จากนั้นเซฟไฟล์

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

ในโปรแกรมเทอร์มินอล ถ้าคุณอยู่ที่ directory ของโปรเจ็ค ให้ลองพิมพ์คำสั่ง `git status` จะเห็นว่าคุณได้ทำการเปลี่ยนอะไรไปบ้าง

เพิ่มการเปลี่ยนแปลงนั้น ๆ เข้าไปใน branch ที่เพิ่งสร้าง ด้วยคำสั่ง `git add`:
```bash
git add Contributors.md
```

ตอนนี้ "Commit" การเปลี่ยนแปลงนั้น ๆ ด้วยคำสั่ง `git commit`:
```bash
git commit -m "Add <ชื่อของคุณ> to Contributors list"
```
แทนที่ `<ชื่อของคุณ>` ด้วยชื่อจริง ๆ ของคุณ.

## "Push" โค้ดที่เปลี่ยนไปขึ้นบน GitHub

"Push" ผลงานที่คุณทำเมื่อกี้นี้ขึ้น GitHub ด้วยคำสั่ง `git push`:
```bash
git push origin <ชื่อ branch ของคุณ>
```
แทนที่ `<ชื่อ branch ของคุณ>` ด้วยชื่อของ branch ของคุณที่เพิ่งสร้างไปเมื่อหัวข้อที่แล้ว ๆ (add-ชื่อ-ของ-คุณ)

## ส่งผลงานของคุณและรอรีวิวจากเจ้าของโปรเจ็ค

ไปที่ repository ของคุณบน GitHub คลิ๊กที่ `Compare & pull request`

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

ตอนนี้ก็ส่ง Pull Request ไปที่โปรเจ็คต้นน้ำได้เลย

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

แล้วเดี๋ยวเราจะ "Merge" หรือรวมผลงานที่คุณได้เปลี่ยนแปลงโค้ดมาที่ master branch ของโปรเจ็คนี้ คุณจะได้รับอีเมล เมื่อเราได้ทำการ Merge ผลงานของคุณเรียบร้อยแล้ว

## เสร็จแล้วทำยังไงต่อดี
ยินดีด้วย คุณเพิ่งทำวัฏจักรพื้นฐานของการทำ contribute คือ fork -> clone -> edit -> pull request ซึ่งสิ่งเหล่านี้คุณจะพบเจอเป็นปกติเมื่อเป็น contributor
ฉลองการมีส่วนร่วมของคุณ จากนั้นก็แบ่งปันให้เพื่อน ๆ ได้ทราบ โดยการไปที่ [หน้าเว็บนี้](https://firstcontributions.github.io/#social-share)

หรือจะมาร่วมสนทนากับเราผ่าน Slack ในกรณีที่คุณต้องการความช่วยเหลือ หรือมีข้อสงสัยใด ๆ [เข้าร่วม slack กับเรา](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)

จากนี้คุณสามารถคอนทริบิ้วต์ให้กับโครงการอื่น ๆ ได้ โดยเราได้สร้างรายการบางส่วน เพื่อให้ง่ายต่อการเริ่มต้น [รายชื่อโครงการที่น่าสนใจ](https://firstcontributions.github.io/#project-list)

### [ข้อมูลอื่น ๆ เพิ่มเติม](../additional-material/git_workflow_scenarios/additional-material.md)

## ฝึกการคอนทริบิ้วต์โดยใช้เครื่องมืออื่น ๆ

| <a href="../gui-tool-tutorials/translations/github-desktop-tutorial.th.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/translations/github-desktop-tutorial.th.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
