[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" src="https://firstcontributions.herokuapp.com/badge.svg">](https://firstcontributions.herokuapp.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)


# 첫 기여하기

늘 처음은 어렵습니다. 잦은 실수를 하기도 하고요. 특히 다른 사람들과 함께 일할 때 실수를 하는 건 굉장히 불편한 일이죠.
하지만 오픈소스는 끊임없는 협력과 협업의 과정입니다. 우리는 사람들이 오픈소스에 대해 배우고, 처음으로 기여하는 일을 쉽게 만들어 보려고 했습니다.

글을 읽고 튜토리얼 비디오를 보는 건 물론 도움이 되지만, 직접 한 번 해 보는 것만큼 좋은 건 없겠죠.
이 프로젝트는 오픈소스 초보자가 처음으로 프로젝트에 기여하는 방법을 안내하고 쉽게 만들어 주는 걸 목표로 합니다.
긴장하지 않고 편안할 때 우리는 더 잘 배웁니다.
오픈소스 프로젝트에 처음으로 기여해 보고 싶다면, 아래의 설명을 따라 차근차근 진행해 보세요. 재밌을 거에요.

#### *이 문서를 [다른 언어로 보기](../LANGUAGES.md)* 

<img align="right" width="300" src="../assets/fork.png" alt="이 저장소 포크하기" />

지금 컴퓨터에 Git이 설치되어 있지 않으면, 먼저 [설치](https://help.github.com/articles/set-up-git/)하세요.

## 저장소 포크하기

지금 보는 페이지의 오른쪽 위에 있는 포크(fork) 버튼을 클릭하여 이 저장소를 포크하세요.
저장소를 포크하면, 여러분의 개인 계정에 저장소의 복사본이 저장됩니다.

## 저장소 복제하기

<img align="right" width="300" src="../assets/clone.png" alt="이 저장소 복제하기" />

이제 이 저장소를 여러분의 기기에 복제합니다. 복제 버튼을 클릭하고 *클립보드로 복사* 아이콘을 클릭합니다.

터미널을 열고 다음의 Git 명령을 실행합니다:

```
git clone "방금 복사한 주소"
```
따옴표를 제외한 "방금 복사한 주소"는 이 저장소의 주소입니다. 위에서 클립보드로 복사한 주소를 붙여 넣으면 됩니다.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="URL을 클립보드로 복사" />

예시:
```
git clone https://github.com/this-is-you/first-contributions.git
```
`this-is-you`는 여러분의 GitHub 계정입니다. 이 명령은 GitHub에 있는 first-contributions 저장소의 내용을 컴퓨터에 복사합니다.

## 브랜치 생성하기

아직 저장소 디렉토리에 있지 않다면 `cd` 명령어를 이용해 디렉토리 안으로 들어갑니다.
```
cd first-contributions
```

이제 `git checkout` 명령을 사용하여 브랜치를 생성합니다.
```
git checkout -b <add-your-name>
```

예시:
```
git checkout -b add-kildong-hong
```
(브랜치의 이름에 *add* 같은 단어가 꼭 들어갈 필요는 없습니다. 하지만 여러분의 이름을 추가한다는 브랜치의 목적에 맞춰 브랜치의 이름을 붙여 주는 게 좋습니다.)

## 필요한 변경 사항을 작성하고 커밋하기

이제 텍스트 편집기에서 `Contributors.md` 파일을 열고, 당신의 이름을 추가한 뒤에 저장합니다.
프로젝트 디렉토리에서 `git status` 명령을 실행하면 변경사항을 볼 수 있습니다. `git add` 명령으로 변경 사항을 추가합니다.

```
git add Contributors.md
```

이제 아래 `git commit` 명령으로 변경 사항을 커밋합니다.
```
git commit -m "Add <your-name> to Contributors list"
```
`<your-name>` 을 당신의 이름으로 바꾸세요.

## 변경사항을 GitHub에 푸시하기

`git push` 명령으로 변경사항을 푸시합니다.

```
git push origin <add-your-name>
```

`<add-your-name>` 을 위에서 생성한 브랜치 이름으로 바꾸세요.

## 커밋 검토 받기

GitHub에서 여러분이 포크한 개인 저장소에 들어가면, `Compare & pull request` 버튼을 볼 수 있습니다. 그 버튼을 클릭하세요.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="풀 요청 생성하기" />

이제 풀 요청을 제출합니다.

<img style="float: right;" src="../assets/submit-pull.png" alt="풀 요청 제출하기" />

여러분의 변경사항을 제가 확인한 후에, master 브랜치에 병합하게되면 알림 메일을 받으실 수 있습니다.

## 이제 뭘 하면 되나요?

여러분의 첫 기여를 축하합니다. 이제 [웹 앱](https://roshanjossey.github.io/first-contributions/#social-share)으로 이동하여 친구 및 팔로워에게 자랑하세요!

도움이 필요하거나 질문이 있을 경우, 저희의 slack 팀에 가입할 수 있습니다. [slack 팀 가입하기](https://firstcontributions.herokuapp.com).

이제 다른 프로젝트에 기여해 보세요. 여러분이 손 대기 쉬운 프로젝트 목록을 작성했습니다. [프로젝트 목록](https://roshanjossey.github.io/first-contributions/#project-list)을 확인하세요.

### [ 추가 정보 ](../additional-material/translations/additional-material.ko.md)

## 다른 툴을 사용한 튜토리얼

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.microsoft.com/net/images/vslogo.png" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

## Self-Promotion

본 프로젝트가 마음에 드신다면, [GitHub](https://github.com/Roshanjossey/first-contributions)에서 Star 버튼을 눌러주세요.

조금 더 도움을 주고 싶으시다면, 
[트위터](https://twitter.com/sudo__bangbang)와
[GitHub](https://github.com/roshanjossey)에서
[Roshan](https://roshanjossey.github.io/)을 팔로우해주세요.
