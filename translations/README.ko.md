[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# 첫 기여

무엇을 하든 누구나 처음에는 어렵게 느껴집니다. 특히 협업을 할 때 실수를 하기라도 하면 마음이 편치 않습니다. 그래서 저희는 새로운 오픈소스 기여자들이 첫 기여를 하고 그것을 익히는 과정을 단순화하고자 했습니다.

물론 관련 글을 읽거나 튜토리얼을 보는 것도 도움이 되지만, 연습공간에서 직접 해보는 것보다 나은 방법이 있을까요? 이 프로젝트의 목표는 초보자도 첫 오픈소스 기여를 할 수 있도록 단순한 방식으로 안내하는 것입니다. 첫 기여를 하고 싶으시다면 아래의 설명을 따라주세요.

만약 명령줄을 이용하는 것이 익숙하지 않다면, GUI 도구 튜토리얼을 참고하세요.

커맨드 라인 사용에 익숙치 않으시다면 [이곳](#다른-도구들에-관한-튜토리얼)에서 GUI 툴에 대한 튜토리얼을 확인할 수 있습니다.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="이 저장소 포크하기" />

가장 먼저, Git이 없으시다면  [설치](https://help.github.com/articles/set-up-git/)해주세요.

## 저장소 포크하기

이 페이지의 상단에 있는 Fork 버튼을 클릭하여 이 저장소를 포크하세요. 그러면 본인의 GitHub 계정에 이 저장소의 복제본이 생성될 것입니다.

## 저장소 클론하기

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="이 저장소 복제하기" />

이제 이 저장소를 자신의 기기에 클론합니다. GitHub 계정으로 가서, fork된 저장소를 열고, Code 버튼을 눌러 클립보드로 복사 아이콘을 클릭합니다.

터미널을 열고 다음 Git 명령을 실행합니다:

```
git clone "방금 복사한 URL"
```

위에 (따옴표를 제외한) "방금 복사한 URL"은 이 저장소의 URL입니다. URL은 이전 단계에서 찾을 수 있습니다.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="URL 을 클립보드로 복사" />

예시:

```
git clone https://github.com/this-is-you/first-contributions.git
```

예시의 `this-is-you`는 본인의 GitHub 계정으로 바꾸어주세요. 이 명령어는
깃헙의 first-contributions 저장소의 내용을 로컬 컴퓨터에 복사합니다.

## 브랜치 생성하기

(아직 저장소 디렉토리에 있지 않다면) 아래의 명령어를 입력하여 조금 전에 로컬 컴퓨터에 복사한 저장소 디렉토리로 이동합니다.

```
cd first-contributions
```

그리고 `git checkout` 명령어을 입력하여 브랜치를 생성합니다.

```
git checkout -b your-new-branch-name
```

예시:

```
git checkout -b add-alonzo-church
```

(브랜치의 이름에 꼭 *add*가 들어가지 않아도 됩니다. 하지만 이 브랜치의 목적은 당신의 이름을 리스트에 추가하는 것이기 때문에 이름에 *add*를 포함하는 것이 합리적입니다.)

## 필요한 변경사항을 작성하고 커밋하기

이제 텍스트 편집기에서 `Contributors.md` 파일을 열고, 본인의 이름을 아래와 같이 추가해주세요. 이때 맨 처음이나 맨 끝을 제외한 중간에 마음에 드는 곳에 추가하시면 됩니다. 그리고 파일을 저장하세요.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />  

프로젝트 디렉터리에서 `git status` 명령을 실행하면 변경사항을 볼 수 있습니다. 

변경사항을 `git add` 명령어를 입력하여 추가합니다.

```
git add Contributors.md
```

이제 `git commit` 명령어로 변경사항을 커밋합니다.

```
git commit -m "Add <your-name> to Contributors list"
```

`<your-name>`을 본인 이름으로 바꾸세요.

## 변경사항을 깃헙에 푸시하기

`git push` 명령어로 변경사항을 푸시합니다.

```
git push origin <add-your-branch-name>
```

`<add-your-branch-name>`을 조금 전에 생성한 브랜치 이름으로 바꾸세요.

## 검토를 위해 변경사항을 제출하기

이제 본인의 GitHub 저장소로 이동하면 `Compare & pull request` 버튼이 보일 것 입니다. 버튼을 클릭하세요.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="풀 요청
생성하기" />

이제 풀 요청(Pull Request)을 제출합니다.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="풀 요청 제출하기"
/>

이제 여러분의 변경사항을 담당자가 확인한 후에 마스터 브랜치에 머지하게 되면 알림 메일을 받으실 것입니다.

## 첫 기여, 그리고 그 후

축하합니다! 앞으로 기여자로서 자주 사용하게 될 기본 워크플로우, _포크(fork) -> 클론(clone) -> 수정(edit) -> 풀 요청(pull request)_, 를 완수하셨습니다!

첫 기여에 대한 소식을 친구들 및 팔로워에게 [웹 앱](https://roshanjossey.github.io/first-contributions/#social-share)을 통해 공유해보세요.

그리고 도움이 필요하거나 질문이 있다면 저희의 slack 에서 요청해보세요. → [slack 팀 가입하기](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)

이제 다른 프로젝트에도 기여해보세요! 지금 바로 시작할 수 있는 난이도가 낮은 이슈들로 가득찬 목록이 있습니다. [웹앱의 프로젝트 목록](https://roshanjossey.github.io/first-contributions/#project-list)에서 확인해보세요.


### [추가 정보](../additional-material/translations/additional-material.ko.md)

## 다른 도구들에 관한 튜토리얼

| <a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/Readme/gk-icon.png" width="100"></a> | <a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [GitHub Desktop](../github-desktop-tutorial.md)              | [Visual Studio 2017](../github-windows-vs2017-tutorial.md)   | [GitKraken](../gitkraken-tutorial.md)                        | [Visual Studio Code](../github-windows-vs-code-tutorial.md)  | [Atlassian Sourcetree](../sourcetree-macos-tutorial.md)      | [IntelliJ IDEA](../github-windows-intellij-tutorial.md)      |
