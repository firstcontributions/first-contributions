[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# "Contribute" ผลงานใน GitHub กับผู้อื่นเป็นครั้งแรกใช่ไหม?

มันเป็นเรื่องยาก, ครั้งแรกของทุกอย่างมันมักจะยากเสมอแหละ โดยเฉพาะการทำงานร่วมกับผู้อื่น เมื่อเราทำอะไรผิดพลาดเรามักจะรู้สึกไม่สบายใจ แต่โอเพนซอร์ส (open source) คือโลกของการทำงานร่วมกัน ! เราจึงอยากให้ผู้ที่เข้ามาใหม่ได้เรียนรู้วิธีการ "คอนทริบิ้วต์" ผลงานร่วมกับผู้อื่นใน GitHub แบบง่าย ๆ

การอ่านบทความและการทำตามตัวอย่างต่าง ๆ ก็อาจจะช่วยได้  แต่จะมีอะไรดีไปกว่าการที่เราได้ลงมือทำสิ่งนั้น ๆ ด้วยตัวเองล่ะ ! โปรเจ็คนี้จะสอนให้มือใหม่ส่ง "คอนทริบิ้วชั่นครั้งแรก" ได้อย่างง่าย ๆ

จำเอาไว้ว่า: ทำใจให้สบาย ยิ่งคุณผ่อนคลายมากเท่าไหร่ คุณก็ยิ่งเรียนรู้ได้ดีมากขึ้นเท่านั้น !

ถ้าคุณอยากร่วมส่งคอนทริบิ้วชั่นครั้งแรกของคุณ เพียงแค่ทำตามขั้นตอนง่าย ๆ ด้านล่าง เราบอกเลยว่า มันจะสนุกแน่นอน

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

_ถ้าคุณยังใช้ git command line ยังไม่คล่องเท่าไหร่ , [นี้คือตัวอย่างการใช้ผ่านเครื่องมือ GUI](#tutorials-using-other-tools)_

ถ้าหากคุณยังไม่ได้ติดตั้ง git ลงบนเครื่องของคุณ คุณสามารถ[ติดตั้งได้ที่นี่]( https://help.github.com/articles/set-up-git/ )

## กด "Fork" โปรเจ็คนี้

โปรเจ็คหลักนี้ จะเรียกว่า โปรเจ็คต้นน้ำ คุณสามารถแยกโปรเจ็คต้นทางออกไปทำที่แอคเคาน์ส่วนตัวของคุณได้ โดยการกดปุ่ม "Fork" ที่ด้านบนของหน้านี้

แล้วโปรเจ็คต้นทางจะถูกคัดลอกนำไปใส่ไว้ในแอคเคาน์ของคุณ

## กด "Clone" โปรเจ็คนี้

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

เอาล่ะ ตอนนี้ก็ Clone โปรเจ็คนี้ลงบนเครื่องคอมพิวเตอร์ของคุณ โดยการคลิ๊กที่ปุ่ม "Clone" แล้วเลือก *Copy to clipboard* (คำสั่งคัดลอก)

เปิดโปรแกรมเทอร์มินอลในเครื่อง (เช่น Terminal ใน MacOS หรือ cmd ใน Windows) แล้วรันคำสั่ง git ต่อไปนี้:

```
git clone "url ที่คัดลอกไว้"
```
"url ที่คัดลอกไว้" (ไม่ต้องใส่ " ") คือ url ของโปรเจ็คบน git ของคุณ คุณสามารถเลื่อนกลับไปดูวิธีการคัดลอก url ได้จากหัวข้อก่อนหน้านี้

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

ตัวอย่าง:
```
git clone https://github.com/this-is-you/first-contributions.git
```
`this-is-you` คือชื่อ username ของคุณบน GitHub ถึงตรงนี้คุณได้ "Clone" โปรเจ็ค first-contributions ไปไว้ที่คอมพิวเตอร์ของคุณแล้ว

## สร้าง branch

ในโปรแกรมเทอร์มินอล เปลี่ยน directory ไปยังที่ที่คุณได้ Clone โปรเจ็คไว้:

```
cd first-contributions
```
ตรงนี้ให้สร้าง branch (แตกกิ่งการทำงานใหม่) ด้วยคำสั่ง `git checkout`:
```
git checkout -b <ชื่อ branch>
```

ตัวอย่าง:
```
git checkout -b add-alonzo-church
```
(ปกติชื่อของ branch ไม่จำเป็นต้องมีคำว่า *add* แต่ในโปรเจ็คนี้อยากให้ใช้ add-ชื่อ-ของ-คุณ เพราะชื่อของคุณจะไปแสดงอยู่ในรายชื่อ Contributors (ผู้เข้าร่วม) ของโปรเจ็คนี้

## เพิ่มหรือลดโค้ดลงไปเลย แล้วอย่าลืม "Commit" บอกว่าคุณได้เปลี่ยนอะไรไปบ้างล่ะ

ตอนนี้ให้เปิดไฟล์ `Contributors.md` ในโปรแกรม text editor เพิ่มชื่อของคุณลงไป จากนั้นเซฟไฟล์

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

ในโปรแกรมเทอร์มินอล ถ้าคุณอยู่ที่ directory ของโปรเจ็ค ให้ลองพิมพ์คำสั่ง `git status` จะเห็นว่าคุณได้ทำการเปลี่ยนอะไรไปบ้าง

เพิ่มการเปลี่ยนแปลงนั้น ๆ เข้าไปใน branch ที่เพิ่งสร้าง ด้วยคำสั่ง `git add`:
```
git add Contributors.md
```

ตอนนี้ "Commit" การเปลี่ยนแปลงนั้น ๆ ด้วยคำสั่ง `git commit`:
```
git commit -m "Add <ชื่อของคุณ> to Contributors list"
```
แทนที่ `<ชื่อของคุณ>` ด้วยชื่อจริง ๆ ของคุณ.

## "Push" โค้ดที่เปลี่ยนไปขึ้นบน GitHub

"Push" ผลงานที่คุณทำเมื่อกี้นี้ขึ้น GitHub ด้วยคำสั่ง `git push`:
```
git push origin <ชื่อ branch ของคุณ>
```
แทนที่ `<ชื่อ branch ของคุณ>` ด้วยชื่อของ branch ของคุณที่เพิ่งสร้างไปเมื่อหัวข้อที่แล้ว ๆ (add-ชื่อ-ของ-คุณ)

## ส่งผลงานของคุณและรอรีวิวจากเจ้าของโปรเจ็ค

ไปที่ repository ของคุณบน GitHub คลิ๊กที่ `Compare & pull request`

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

ตอนนี้ก็ส่ง Pull Request ไปที่โปรเจ็คต้นน้ำได้เลย

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

แล้วเดี๋ยวเราจะ "Merge" หรือรวมผลงานที่คุณได้เปลี่ยนแปลงโค้ดมาที่ master branch ของโปรเจ็คนี้ คุณจะได้รับอีเมลล์ เมื่อเราได้ทำการ Merge ผลงานของคุณเรียบร้อยแล้ว

## ไปไหนต่อดีหลังจากนี้?
ยินดีด้วย คุณเพิ่งทำวัฏจักรพื้นฐานของการทำ contribute คือ fork -> clone -> edit -> pull request ซึ่งสิ่งเหล่านี้คุณจะพบเจอเป็นปกติเมื่อเป็น contributor
ฉลองการมีส่วนร่วมของคุณ จากนั้นก็แบ่งปันให้เพื่อน ๆ ได้ทราบ โดยการไปที่ [หน้าเว็บนี้](https://roshanjossey.github.io/first-contributions/#social-share)

หรือจะมาร่วมสนทนากับเราผ่าน Slack ในกรณีที่คุณต้องการความช่วยเหลือ หรือมีข้อสงสัยใด ๆ [เข้าร่วม slack กับเรา](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)

จากนี้คุณสามารถคอนทริบิ้วต์ให้กับโครงการอื่น ๆ ได้ โดยเราได้สร้างรายการบางส่วน เพื่อให้ง่ายต่อการเริ่มต้น [รายชื่อโครงการที่น่าสนใจ](https://roshanjossey.github.io/first-contributions/#project-list)

### [ข้อมูลอื่น ๆ เพิ่มเติม](../additional-material/git_workflow_scenarios/additional-material.md)

## ฝึกการคอนทริบิ้วต์โดยใช้เครื่องมืออื่น ๆ

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/Readme/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

