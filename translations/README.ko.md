[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# 첫 기여

이 프로젝트는 초보자가 처음으로 오픈소스에 기여할 수 있도록 쉽게 안내하는 것을 목표로 합니다. 첫 번째 기여를 하고 싶다면, 아래의 설명을 따라주세요.

_만약 명령어 인터페이스에 익숙하지 않다면, [여기에서 GUI 도구 튜토리얼을 참고하세요.](#다른-도구들을-사용한-튜토리얼)._

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="이 저장소 포크하기" />

#### 만약, git이 설치되어있지 않다면 [설치하세요](https://docs.github.com/en/get-started/quickstart/set-up-git).

## 저장소 포크하기

이 저장소 페이지의 상단에 있는 Fork 버튼을 클릭해서 저장소를 포크하세요. 그러면 본인의 깃허브 계정에 이 저장소의 복사본이 생성됩니다.

## 저장소 클론하기

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="이 저장소 복제하기" />

이제 fork한 저장소를 자신의 기기에 클론하세요. 깃허브 계정의 fork한 저장소에 들어가서, Code 버튼을 클릭하고, _클립보드로 url 복사_ 아이콘을 클릭합니다.

터미널을 열고 다음 git 명령을 실행합니다:

```bash
git clone "방금 복사한 URL"
```

위에 (따옴표를 제외한) "방금 복사한 URL"은 이 저장소의 URL입니다. URL은 이전 단계에서 찾을 수 있습니다.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="URL을 클립보드로 복사" />

예시:

```bash
git clone git@github.com:this-is-you/first-contributions.git
```

`this-is-you`에 해당하는 부분을 본인의 깃허브 계정명으로 바꾸어주세요. 이 명령어는 깃허브의 first-contributions 저장소를 자신의 컴퓨터로 복사합니다.

## 브랜치 생성하기

(아직 저장소 디렉토리가 아니라면) 아래의 명령어를 입력해서 조금 전에 컴퓨터에 복사한 저장소 디렉토리로 이동합니다.

```bash
cd first-contributions
```

그리고 `git switch` 명령어를 입력해서 브랜치를 생성합니다.

```bash
git switch -c your-new-branch-name
```

예시:

```bash
git switch -c add-alonzo-church
```

## 필요한 부분을 변경하고 변경사항을 커밋하기

이제 텍스트 편집기에서 `Contributors.md` 파일을 열고 본인의 이름을 아래와 같이 추가해주세요. 파일의 시작 부분이나 마지막 부분에 추가해서는 안됩니다. 중간 부분의 마음에 드는 곳에 추가하면 됩니다. 그리고 파일을 저장하세요.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

프로젝트 디렉토리로 이동해서 `git status` 명령어를 실행하면 변경사항이 존재하는 것을 볼 수 있습니다.

변경사항을 `git add` 명령어를 사용해서 조금 전에 생성한 브랜치에 추가합니다.

```bash
git add Contributors.md
```

이제 `git commit` 명령어를 사용해서 변경사항을 커밋합니다.

```bash
git commit -m "Add your-name to Contributors list"
```

`your-name`을 본인 이름으로 변경하세요.

## 변경사항을 깃허브에 푸시하기

`git push` 명령어로 변경사항을 푸시합니다.

```bash
git push -u origin your-branch-name
```

`your-branch-name` 부분을 조금 전에 생성한 브랜치 이름으로 변경하세요.

<details>
<summary> <strong>푸시하는 중에 에러가 발생했다면, 여기를 클릭하세요:</strong> </summary>

- ### Authentication Error
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  [깃허브 튜토리얼](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)로 이동해서 본인의 계정에 SSH key 생성 및 설정에 대한 정보를 얻을 수 있습니다.

</details>

## 검토를 위해 변경사항을 제출하기

이제 본인의 깃허브 저장소로 이동하면 `Compare & pull request` 버튼을 볼 수 있습니다. 버튼을 클릭하세요.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="풀 요청
생성하기" />

이제 풀 요청(Pull Request)을 제출합니다.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="풀 요청 제출하기"
/>

이제 여러분의 변경사항을 담당자가 확인한 후에 main 브랜치에 병합 하게 되면 알림 메일을 받을 수 있습니다.

## 첫 기여, 그리고 그 후

축하합니다! 앞으로 기여자로서 자주 사용하게될 기본 워크플로우인 _포크(fork) -> 클론(clone) -> 수정(edit) -> 풀 요청(pull request)_, 를 완료했습니다!

첫 기여에 대한 소식을 친구들 및 팔로워에게 [웹 앱](https://firstcontributions.github.io/#social-share)을 통해 공유해보세요.

도움이 필요하거나 질문이 있다면 저희 slack 팀에 참여할 수 있습니다. → [slack 팀 참여하기](https://firstcontributors.slack.com/join/shared_invite/zt-29qhyr9lt-Bi7WLbgGIFqV7aCEG_grvg#/shared-invite/email)

이제 다른 프로젝트에도 기여해보세요! 지금 바로 시작할 수 있는 난이도가 낮은 이슈들로 가득찬 목록이 있습니다. [웹앱의 프로젝트 목록](https://firstcontributions.github.io/#project-list)에서 확인해보세요.

### [추가 자료](../additional-material/translations/Korean/additional-material.ko.md)

## 다른 도구들을 사용한 튜토리얼

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |

<p>This project is supported by:</p>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>
