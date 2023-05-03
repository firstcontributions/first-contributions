[![오픈 소스 Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# First Contributions

|<img alt="SourceTree" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-logo.png" width="200">|Atlassian 소스트리|
|---|---|

힘들어요. 무언가를 처음 할 때는 항상 어렵습니다. 특히 협업할 때 실수를 하는 것은 편한 일이 아닙니다. 하지만 오픈소스는 협업과 공동 작업에 관한 것입니다. 저희는 새로운 오픈소스 기여자가 처음으로 배우고 기여하는 방식을 단순화하고자 했습니다.

기사를 읽고 튜토리얼을 보는 것도 도움이 될 수 있지만, 아무것도 엉망으로 만들지 않고 실제로 해보는 것보다 더 좋은 것은 없습니다. 이 프로젝트는 초보자가 처음 기여하는 방법을 안내하고 간소화하는 것을 목표로 합니다. 편안할수록 더 잘 배울 수 있다는 것을 기억하세요. 첫 번째 기여를 하고 싶으시다면 아래의 간단한 단계를 따르세요. 재미있을 거라고 약속드립니다.


## 소스 트리

이 튜토리얼은 MacOS용입니다. Windows의 Sourcetree와 비슷하지만 몇 가지가 다르게 보일 수 있습니다.
<!--
	****************************************
	*** 이것은 ***까지 주석 처리됩니다.
	*** Windows 튜토리얼을 만들 수 있습니다***
	****************************************
이 튜토리얼은 MacOS용입니다. 사용하고자 하는 경우 소스트리에 대한 [Windows 튜토리얼]()을 참조하세요.
-->

소스트리] 다운로드(https://www.sourcetreeapp.com), 설치하고 엽니다.

"소스 트리" 모달 대화 상자가 표시될 것입니다.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-1-main.png" alt="SourceTree Main" />

여기에서 Remote를 클릭합니다. 처음 설치하는 경우 아직 GitHub 계정을 연결하지 않았을 가능성이 높습니다. "연결 버튼"을 클릭하여 연결하세요.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-2-main-connect.png" alt="SourceTree Connect" />

계정* 대화 상자가 나타납니다. 왼쪽 하단의 "추가"를 클릭합니다. 그런 다음 적절한 설정을 선택하여 클라이언트에 GitHub(또는 원하는 다른 계정)를 추가합니다. GitHub에 대한 설정을 선택한 후 "계정 연결"을 클릭합니다.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-4-accounts-add.png" alt="SourceTree Connect Add" />

그러면 웹 브라우저에 페이지가 열립니다. 안내된 단계에 따라 계정을 인증합니다.

## 이 리포지토리 포크

이 페이지 상단의 포크 버튼을 클릭하여 이 리포지토리를 포크합니다.
<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/fork.png" alt="fork this repository" />
T그는 귀하의 계정에 이 저장소의 복사본을 생성할 것입니다.


## 리포지토리 복제

소스트리에서 "원격" 버튼을 클릭합니다. 그러면 GitHub에 나열된 모든 GitHub 리포지토리가 로드됩니다.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-5-cloning.png" alt="clone this repository" />

"복제" 버튼을 클릭하면 여러 가지를 정의할 수 있는 다른 보기가 표시됩니다.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-6-cloning-confirm.png" alt="clone this repository" />

1) **소스 URL: **이 값은 자동으로 입력되며 변경할 필요가 없습니다. GitHub 프로젝트가 있는 곳의 URL입니다.

2) **대상 경로:** 이 프로젝트가 저장될 컴퓨터의 실제 위치입니다.

3) **이름:** 소스트리가 프로젝트를 참조하는 방법에 대한 "북마크"입니다. 바로 가기라고 생각하세요.

*참고: 일반적으로 이 필드의 기본값은 괜찮습니다.

**만족스러우면 "복제"**를 클릭합니다.

그러면 리포지토리의 메인 리포지토리 브라우저가 나타납니다!

## 브랜치 만들기

도구 모음에서 브랜치 버튼을 클릭합니다.

예를 들어 브랜치 이름을 "기여에 이름 추가"로 지정합니다: "add-sally-to-contribution".

이렇게 하려면 **브랜치(1)**를 클릭하여 이름 지정 대화 상자를 시작합니다. 그런 다음 방금 설명한 대로 **이름 추가(2)**를 클릭합니다. 마지막으로 **브랜치 만들기**를 클릭합니다. 그러면 방금 이름을 지정한 브랜치가 생성됩니다.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-7-branching.png" alt="name your branch" />


## 필요한 변경을 하고 해당 변경 사항을 커밋합니다.

이제 텍스트 편집기에서 `Contributors.md` 파일을 열고 Github URL 링크와 함께 이름을 추가한 다음 파일을 저장합니다.

변경된 파일을 보고 검토하여 스테이징할 항목을 결정할 수 있어야 합니다.  스테이징은 이 커밋과 관련된 파일 변경 사항을 정확히 git에 알려주는 데 중요합니다.

*참고: 파일의 Diff가 보이지 않으면 대화 상자 상단의 **커밋되지 않은 파일**을 클릭하세요*.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-8-viewing-changed-files.png" alt="edit some file(s)" />

다음으로 대화 상자의 왼쪽 상단에 있는 **커밋** 버튼을 클릭합니다. 그러면 스테이징 영역이 표시됩니다.

체크박스*를 클릭하여 파일을 스테이징 영역에 **추가**합니다. 그런 다음 커밋 메시지를 입력합니다.

*참고: 스페이스바*를 사용하여 준비 영역과 준비되지 않은 영역 모두에서 파일을 선택하고 해당 영역에서 파일을 추가/제거할 수도 있습니다.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-9-committing.png" alt="stage your changes" />


변경사항을 추가하고 커밋 메시지를 추가했으면 **Commit** 버튼을 눌러 최종적으로 커밋할 수 있습니다.

축하합니다, 첫 번째 기여 포크 브랜치의 로컬 복사본에 모든 변경 사항을 커밋했습니다.  계속 진행하세요!


## GitHub에 변경 사항 푸시

이제 변경 사항을 Github에 푸시할 준비가 되었습니다. 이렇게 하면 프로젝트의 포크된 자신의 브랜치에 푸시됩니다. 다음 단계에 따라 브랜치를 푸시하세요. 먼저 **Push (1)**를 클릭하면 원격/푸시 대화 상자가 표시됩니다. 푸시하려는 브랜치의 체크박스를 **클릭(2)**합니다. 확인 (3)**을 선택하면 커밋이 Github에 푸시됩니다.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-10-pushing.png" alt="origin or branch" />

## 검토를 위해 변경 사항 제출

깃허브의 리포지토리로 이동하면 '비교 및 풀 리퀘스트' 버튼이 표시됩니다. 해당 버튼을 클릭합니다.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/compare-and-pull.png" alt="create a pull request" />

이제 풀 리퀘스트를 제출하세요.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/submit-pull-request.png" alt="submit pull request" />

곧 모든 변경 내용을 이 프로젝트의 마스터 브랜치에 병합할 것입니다. 변경사항이 병합되면 알림 이메일을 받게 됩니다.

## 이제 어디로 가야 하나요?

축하해요!  기여자로서 자주 접하게 되는 표준 _포크 -> 복제 -> 편집 -> PR_ 워크플로우를 방금 완료하셨습니다!

웹 앱]으로 이동하여 여러분의 기여를 축하하고 친구 및 팔로워와 공유하세요(https://firstcontributions.github.io/#social-share).

도움이 필요하거나 궁금한 점이 있는 경우 슬랙 팀에 가입할 수 있습니다. [슬랙 팀 가입하기](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).


### [추가 자료](../additional-material/git_workflow_scenarios/additional-material.md)


## 다른 도구를 사용한 튜토리얼
[메인 페이지로 돌아가기](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
