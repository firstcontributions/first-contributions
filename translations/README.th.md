[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" src="https://firstcontributions.herokuapp.com/badge.svg">](https://firstcontributions.herokuapp.com)

# "Contribute" ผลงานใน Github กับผู้อื่นครั้งแรกใช่ไหม?

ครั้งแรกของทุกอย่างมันมักจะยากเสมอ โดยเฉพาะการทำงานร่วมกับผู้อื่น เมื่อเราทำอะไรผิดพลาดเรามักรู้สึกไม่สบายใจ แต่ Opensource คือโลกของการทำงานร่วมกัน! เราจึงอยากให้ผู้ที่เข้ามาใหม่ได้เรียนรู้วิธีการ "คอนทริบิ้วต์" ผลงานร่วมกับผู้อื่นใน Github แบบง่ายๆ

การอ่านบทความและการทำตามตัวอย่างต่างๆ ก็อาจช่วยได้ แต่จะมีอะไรดีไปกว่าการที่เราได้ลงมือทำสิ่งนั้นๆ ด้วยตัวเองล่ะ! โปรเจ็คนี้จะสอนให้มือใหม่ส่ง "คอนทริบิ้วชั่นครั้งแรก" ได้อย่างง่ายๆ

จำเอาไว้ว่า: ทำใจให้สบาย ยิ่งคุณผ่อนคลายมากเท่าไหร่ คุณก็ยิ่งเรียนรู้ได้ดีมากขึ้นเท่านั้น!

ถ้าคุณอยากร่วมส่งคอนทริบิ้วชั่นครั้งแรกของคุณ เพียงแค่ทำตามขั้นตอนง่ายๆด้านล่าง เราบอกเลยว่า มันจะสนุกแน่นอน

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

*อ่านบทความนี้ในภาษาอื่นๆ: [English](../README.md), [Myanmar Unicode](translations/README.mm_unicode.md), [Indonesian](translations/README.id.md), [French](translations/README.fr.md), [Spanish](translations/README.es.md), [Dutch](translations/README.nl.md), [Hindi](translations/README.hi.md), [Russian](translations/README.ru.md), [Japanese](translations/README.ja.md), [Vietnamese](translations/README.vn.md), [Polish](translations/README.pl.md), [Korean](translations/README.ko.md), [German](translations/README.de.md), [Simplified Chinese](translations/README.chs.md), [Traditional Chinese](translations/README.cht.md), [Greek](translations/README.gr.md), [العربية](translations/README.ar.md), [Ukrainian](translations/README.ua.md), [Português/Brasil](translations/README.pt_br.md), [Italian](translations/README.it.md) และ [Galician](translations/README.gl.md).*

ถ้าหากคุณยังไม่ได้ติดตั้ง git ลงบนเครื่องของคุณ คุณสามารถ[ติดตั้งได้ที่นี่]( https://help.github.com/articles/set-up-git/ )

## กด "Fork" โปรเจ็คนี้

โปรเจ็คหลักนี้ จะเรียกว่า โปรเจ็คต้นน้ำ คุณสามารถแยกโปรเจ็คต้นน้ำออกไปทำที่แอคเคาน์ส่วนตัวของคุณได้ โดยการกดปุ่ม "Fork" ที่ด้านบนของหน้านี้

แล้วโปรเจ็คต้นน้ำจะถูกคัดลอกนำไปใส่ไว้ในแอคเคาน์ของคุณ

## กด "Clone" โปรเจ็คนี้

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

เอาล่ะ ตอนนี้ก็ Clone โปรเจ็คนี้ลงบนเครื่องคอมพิวเตอร์ของคุณ โดยการคลิ๊กที่ปุ่ม "Clone" แล้วเลือก *copy to clipboard* (คำสั่งคัดลอก)

เปิดโปรแกรมเทอร์มินอลในเครื่อง (เช่น Terminal ใน MacOS หรือ cmd ใน Windows) แล้วรันคำสั่ง git ต่อไปนี้:

```
git clone "url ที่คัดลอกไว้"
```
"url ที่คัดลอกไว้" (ไม่ต้องใส่ " ") คือ url ของโปรเจ็คของคุณ คุณสามารถเลื่อนกลับไปดูวิธีคัดลอก url ได้จากหัวข้อก่อนหน้านี้

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

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

ในโปรแกรมเทอร์มินอล ถ้าคุณอยู่ที่ directory ของโปรเจ็ค ให้ลองพิมพ์คำสั่ง `git status` จะเห็นว่าคุณได้ทำการเปลี่ยนอะไรไปบ้าง

เพิ่มการเปลี่ยนแปลงนั้นๆเข้าไปใน branch ที่เพิ่งสร้าง ด้วยคำสั่ง `git add`:
```
git add Contributors.md
```

ตอนนี้ "Commit" การเปลี่ยนแปลงนั้นๆ ด้วยคำสั่ง `git commit`:
```
git commit -m "Add <ชื่อของคุณ> to Contributors list"
```
แทนที่ `<ชื่อของคุณ>` ด้วยชื่อจริงๆของคุณ.

## "Push" โค้ดที่เปลี่ยนไปขึ้นบน Github

"Push" ผลงานที่คุณทำเมื่อกี้นี้ขึ้น Github ด้วยคำสั่ง `git push`:
```
git push origin <ชื่อ branch ของคุณ>
```
แทนที่ `<ชื่อ branch ของคุณ>` ด้วยชื่อของ branch ของคุณที่เพิ่งสร้างไปเมื่อหัวข้อที่แล้วๆ (add-ชื่อ-ของ-คุณ)

## ส่งผลงานของคุณและรอรีวิวจากเจ้าของโปรเจ็ค

ไปที่ repository ของคุณบน Github คลิ๊กที่ `Compare & pull request`

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

ตอนนี้ก็ส่ง Pull Request ไปที่โปรเจ็คต้นน้ำได้เลย

<img style="float: right;" src="../assets/submit-pull.png" alt="submit pull request" />

แล้วเดี๋ยวเราจะ "Merge" หรือรวมผลงานที่คุณได้เปลี่ยนแปลงโค้ดมาที่ master branch ของโปรเจ็คนี้ คุณจะได้รับอีเมลล์ เมื่อเราได้ทำการ Merge ผลงานของคุณเรียบร้อยแล้ว

### [ข้อมูลอื่นๆเพิ่มเติม](additional-material/additional-material.md)

## ทัวเทอร์เรียลสำหรับการใช้ Github ร่วมกับ Tools อื่นๆ


|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.microsoft.com/net/images/vslogo.png" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

## ทำอะไรต่อดีหลังจากนี้?

คุณจะลองมาเข้าร่วมทีมของเราใน Slack ก็ได้นะ! ถ้าคุณมีข้อสงสัยอะไรเพิ่มเติม สามารถเข้ามาถามได้เลย [เข้าร่วม](https://firstcontributions.herokuapp.com)

ข้างล่างนี่คือ repo สำหรับมือใหม่ ที่จะช่วยให้คุณใช้งาน Tools ต่างๆสำหรับโค้ดดิ้งได้ง่ายขึ้น ลองเข้าไปดูกันนะ :)

|[![exercism](https://avatars2.githubusercontent.com/u/5624255?v=3&s=100)](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[![fun-retro](https://avatars3.githubusercontent.com/u/15913975?v=3&s=100)](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[<img width="100" src="https://cdn.worldvectorlogo.com/logos/react.svg">](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[![habitat](https://avatars1.githubusercontent.com/u/18171698?v=3&s=100)](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![scikit-learn](https://avatars0.githubusercontent.com/u/365630?v=3&s=100)](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[<img width="100" src="https://camo.githubusercontent.com/0f302c808c8457f6460913e33aed3478124612c2/687474703a2f2f6c65696e696e67656e2e6f72672f696d672f6c65696e696e67656e2e6a7067">](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[<img width="100" src="https://images.plot.ly/plotly-documentation/thumbnail/numpy-logo.jpg">](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[![elasticsearch](https://avatars2.githubusercontent.com/u/6764390?v=3&s=100)](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|---|---|---|---|---|---|---|---|
|[exercism](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[Fun Retros](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[react](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[habitat](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[scikit-learn](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[Leiningen](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[numpy](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[elasticsearch](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|[![homebrew](https://avatars2.githubusercontent.com/u/1503512?v=3&s=100)](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[![rust](https://avatars1.githubusercontent.com/u/5430905?v=3&s=100)](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[![vuejs](https://avatars1.githubusercontent.com/u/6128107?v=3&s=100)](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[![Suave](https://avatars2.githubusercontent.com/u/5822862?v=3&s=100)](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[![OpenRA](https://avatars3.githubusercontent.com/u/409046?v=3&s=100)](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![PowerShell](https://avatars0.githubusercontent.com/u/11524380?v=3&s=100)](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[![coala](https://avatars2.githubusercontent.com/u/10620750?v=3&s=100)](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[![moment](https://avatars2.githubusercontent.com/u/4129662?v=3&s=100)](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[homebrew](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[Rust](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[vuejs](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[Suave](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[OpenRA](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[PowerShell](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[coala](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[moment](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[![ava](https://avatars0.githubusercontent.com/u/8527916?v=3&s=100)](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[![freeCodeCamp](https://avatars0.githubusercontent.com/u/9892522?v=3&s=100)](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![webpack](https://avatars3.githubusercontent.com/u/2105791?v=3&s=100)](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[![hoodie](https://avatars1.githubusercontent.com/u/1888826?v=3&s=100)](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![pouchdb](https://avatars3.githubusercontent.com/u/3406112?v=3&s=100)](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[![neovim](https://avatars0.githubusercontent.com/u/6471485?v=3&s=100)](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[![babel](https://avatars2.githubusercontent.com/u/9637642?v=3&s=100)](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[<img width="100" src="https://github.com/adobe/brackets/blob/gh-pages/images/brackets_128.png?raw=true">](https://github.com/adobe/brackets/labels/Starter%20bug)|
|[ava](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[webpack](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[hoodie](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[pouchdb](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[neovim](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[babel](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[brackets](https://github.com/adobe/brackets/labels/Starter%20bug)|
| [![Node.js](https://avatars1.githubusercontent.com/u/9950313?v=3&s=100)](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|[<img width="100" src="https://github.com/Semantic-Org/Semantic-UI-React/raw/master/docs/app/logo.png">](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|
| [Node.js](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |[Semantic-UI-React](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |
