[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" src="https://firstcontributions.herokuapp.com/badge.svg">](https://firstcontributions.herokuapp.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)


# 첫 기여


힘이 듭니다. 처음으로 뭔가를하는 것은 언제나 어렵습니다. 특히 공동 작업 할 때 실수를 저지르는 것은 쉬운 일이 아닙니다. 그러나 오픈 소스는 협업과 협력에 관한 모든 것입니다. 우리는 새로운 오픈 소스 제공자가 처음 배우고 기여하는 방식을 단순화하고자했습니다.

기사를 읽고 자습서를 보는 것이 도움이 될 수 있습니다. 그냥 덤벼들었다가 망쳐 놓는 것 보다는 낫겠죠. 이 프로젝트는 초보자가 첫 번째로 기여하는 방법을 안내하고 단순화하는 것을 목표로합니다. 기억하십시오 : 당신이 편안함을 느낄수록 배우는 것이 좋습니다. 첫 번째 기여를 하려면 아래의 간단한 단계를 따르십시오. 재미있을 것이라 약속드립니다.
#### *이 분서를 [다른 언어로 보기](../Translations.md)* 

<img align="right" width="300" src="../assets/fork.png" alt="이 저장소 포크하기" />

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

## 이제 어디로 가나요?

여러분의 첫 기여를 축하합니다. 이제 [웹 앱](https://roshanjossey.github.io/first-contributions/#social-share)으로 이동하여 친구 및 팔로워와 공유하십시오.

도움이 필요하거나 질문이있을 경우, 우리의 slack 팀에 합류 할 수 있습니다. [slack 팀 가입하기](https://firstcontributions.herokuapp.com).

이제 다른 프로젝트에 기여해보십시오. 시작하기 쉬운 문제가있는 프로젝트 목록을 작성했습니다. [웹 앱에 있는 프로젝트 목록](https://roshanjossey.github.io/first-contributions/#project-list)을 확인하세요.



### [ 추가 정보 ](../additional-material/translations/additional-material.ko.md)

## 자습서 다른 도구 사용

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.microsoft.com/net/images/vslogo.png" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

## Self-Promotion

본 프로젝트가 마음에 드신다면, [GitHub](https://github.com/Roshanjossey/first-contributions)를 star버튼을 눌러주세요.

특히 도움이 되고자하신다면 [Twitter](https://twitter.com/sudo__bangbang) 와 [GitHub](https://github.com/roshanjossey)의 [Roshan](https://roshanjossey.github.io/)을 follow해주세요.
