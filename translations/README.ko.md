# 첫 기여

<img align="right" width="300" src="../assets/fork.png" alt="이 저장소 포크하기" />

*Read this in other languages: [English](../README.md), [Spanish](README.es.md),
[Dutch](README.nl.md), [Hindi](README.hi.md), [Russian](README.ru.md),
[Japanese](README.ja.md), [Vietnamese](README.vn.md), [Polish](README.pl.md),
[Korean](README.ko.md), [Greek](README.gr.md).*

지금 Git 이 없으면 [설치](https://help.github.com/articles/set-up-git/)하세요.

## 저장소 포크하기

포크 버튼을 클릭하여 이 저장소를 포크하세요.

## 저장소 복제하기

<img align="right" width="300" src="../assets/clone.png" alt="이 저장소 복제하기"
/>

이제 이 저장소를 자신의 기기에 복제합니다. 복제 버튼을 클릭하고 클립보드로 복사
아이콘을 클릭합니다.

터미널을 열고 다음 Git 명령을 실행합니다:

```
git clone "방금 복사한 주소"
```

(따옴표를 제외한) "방금 복사한 주소"는 이 저장소의 주소입니다. 주소를 얻으려면
이전 단계를 참조하세요.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="URL 을
클립보드로 복사" />

예시:

```
git clone https://github.com/this-is-you/first-contributions.git
```

'this-is-you' 는 당신의 깃허브 계정입니다. 여기서 깃허브에 있는
first-contributions 저장소의 내용을 컴퓨터에 복사합니다.

## 브랜치 생성하기

아직 저장소 디렉토리에 있지 않다면 그곳으로 변경합니다.

```
cd first-contributions
```

이제 `git checkout` 명령을 사용하여 브랜치를 생성합니다.

```
git checkout -b <add-your-name>
```

예시:

```
git checkout -b add-alonzo-church
```

## 필요한 변경사항을 작성하고 커밋하기

이제 텍스트 편집기에서 `Contributors.md` 파일을 열고 당신의 이름을 추가하고
저장합니다. 프로젝트 디렉토리에서 `git status` 명령을 실행하면 변경사항을 볼 수
있습니다. 변경사항을 아래 `git add` 명령으로 추가합니다.

```
git add Contributors.md
```

이제 아래 `git commit` 명령으로 변경사항을 커밋합니다.

```
git commit -m "Add <your-name> to Contributors list"
```

`<your-name>` 을 당신의 이름으로 바꾸세요.

## 변경사항을 깃허브에 푸시하기

`git push` 명령으로 변경사항을 푸시합니다.

```
git push origin <add-your-name>
```

`<add-your-name>` 을 이전에 생성한 브랜치 이름으로 바꾸세요.

## 검토를 위해 변경사항을 제출하기

깃허브의 당신의 저장소에 가면, `Compare & pull request` 버튼을 볼 수 있습니다.
그 버튼을 클릭하세요.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="풀 요청
생성하기" />

이제 풀 요청을 제출합니다.

<img style="float: right;" src="../assets/submit-pull.png" alt="풀 요청 제출하기"
/>

이제 여러분의 변경사항을 제가 확인 후에  마스터 브랜치에 머지하게되면 알림메일을 받으실 수 있습니다.

## 포크한 저장소와 이 저장소 동기화하기

이제 나는 이 프로젝트의 마스터 브랜치에 모든 변경사항을 병합할 것 입니다. 당신의
포크는 그러한 변경사항을 가지고 있지 않습니다. 당신의 포크를 나의 것과 동기화
하기 위해서, 내 저장소의 주소를 `upstream remote url` 로 추가하세요.

```
git remote add upstream https://github.com/multunus/first-contributions
```

이것은 명시된 주소에 이 프로젝트의 또 다른 버전이 존재한다는 점을 Git 에
알려줍니다. 우리는 이것을 업스트림이라고 부릅니다. 변경사항이 병합되면 내
저장소의 새 버전을 가지고 오세요.

```
git fetch upstream
```

이거로 내 저장소(업스트림 원격)의 모든 변경사항을 가지고 옵니다. 이제, 내
저장소의 새 개정판을 당신의 마스터 브랜치에 병합해야 합니다.

```
git rebase upstream/master
```

여기서 당신이 가져온 모든 변경사항을 마스터 브랜치에 적용됩니다. 마스터 브랜치를
푸시하면, 당신의 포크도 역시 변경사항을 가질 것 입니다.

```
git push origin master
```

origin 이라 명명된 원격으로 푸시하고 있는 것에 주목하세요.


### [ 추가 정보 ](../additional-material/translations/additional-material.ko.md)

## 자습서 다른 도구 사용

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.microsoft.com/net/images/vslogo.png" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|


## 이제 어디로 가나요?

이곳의 인기있는 저장소에 당신이 해결할 수 있는 초보자 수준의 문제들이 있습니다.
더 자세히 알아보기 위해 해당 저장소를 방문해보세요.

|[![exercism](https://avatars2.githubusercontent.com/u/5624255?v=3&s=100)](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[![fun-retro](https://avatars3.githubusercontent.com/u/15913975?v=3&s=100)](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[<img width="100" src="https://cdn.worldvectorlogo.com/logos/react.svg">](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[![habitat](https://avatars1.githubusercontent.com/u/18171698?v=3&s=100)](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![scikit-learn](https://avatars0.githubusercontent.com/u/365630?v=3&s=100)](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[<img width="100" src="https://camo.githubusercontent.com/0f302c808c8457f6460913e33aed3478124612c2/687474703a2f2f6c65696e696e67656e2e6f72672f696d672f6c65696e696e67656e2e6a7067">](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[<img width="100" src="https://images.plot.ly/plotly-documentation/thumbnail/numpy-logo.jpg">](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[![elasticsearch](https://avatars2.githubusercontent.com/u/6764390?v=3&s=100)](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|---|---|---|---|---|---|---|---|
|[exercism](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[Fun Retros](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[react](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[habitat](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[scikit-learn](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[Leiningen](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[numpy](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[elasticsearch](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|[![homebrew](https://avatars2.githubusercontent.com/u/1503512?v=3&s=100)](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[![rust](https://avatars1.githubusercontent.com/u/5430905?v=3&s=100)](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[![vuejs](https://avatars1.githubusercontent.com/u/6128107?v=3&s=100)](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[![Suave](https://avatars2.githubusercontent.com/u/5822862?v=3&s=100)](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[![OpenRA](https://avatars3.githubusercontent.com/u/409046?v=3&s=100)](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![PowerShell](https://avatars0.githubusercontent.com/u/11524380?v=3&s=100)](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[![coala](https://avatars2.githubusercontent.com/u/10620750?v=3&s=100)](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[![moment](https://avatars2.githubusercontent.com/u/4129662?v=3&s=100)](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[homebrew](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[Rust](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[vuejs](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[Suave](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[OpenRA](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[PowerShell](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[coala](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[moment](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[![ava](https://avatars0.githubusercontent.com/u/8527916?v=3&s=100)](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[![freeCodeCamp](https://avatars0.githubusercontent.com/u/9892522?v=3&s=100)](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![webpack](https://avatars3.githubusercontent.com/u/2105791?v=3&s=100)](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[![hoodie](https://avatars1.githubusercontent.com/u/1888826?v=3&s=100)](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![pouchdb](https://avatars3.githubusercontent.com/u/3406112?v=3&s=100)](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[![neovim](https://avatars0.githubusercontent.com/u/6471485?v=3&s=100)](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[![babel](https://avatars2.githubusercontent.com/u/9637642?v=3&s=100)](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[<img width="100" src="https://github.com/adobe/brackets/blob/gh-pages/images/brackets_128.png?raw=true">](https://github.com/adobe/brackets/labels/Starter%20bug)|
|[ava](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[webpack](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[hoodie](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[pouchdb](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[neovim](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[babel](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[brackets](https://github.com/adobe/brackets/labels/Starter%20bug)|
| [![Node.js](https://avatars1.githubusercontent.com/u/9950313?v=3&s=100)](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|[<img width="100" src="https://github.com/Semantic-Org/Semantic-UI-React/raw/master/docs/app/logo.png">](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|
| [Node.js](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |[Semantic-UI-React](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |
