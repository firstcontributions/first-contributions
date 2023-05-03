[![오픈 소스 Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# First Contributions

| <img alt="Visual Studio Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width="40"> | Visual Studio 코드 |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |


힘들어요. 무언가를 처음 할 때는 항상 어렵습니다. 특히 협업할 때 실수를 하는 것은 편한 일이 아닙니다. 하지만 오픈소스는 협업과 함께 일하는 것이 핵심입니다. 저희는 새로운 오픈소스 기여자가 처음으로 배우고 기여하는 방식을 단순화하고자 했습니다.

기사를 읽고 튜토리얼을 보는 것도 도움이 될 수 있지만, 아무것도 엉망으로 만들지 않고 실제로 해보는 것보다 더 좋은 것은 없습니다. 이 프로젝트는 초보자가 처음 기여하는 방법을 안내하고 간소화하는 것을 목표로 합니다. 편안할수록 더 잘 배울 수 있다는 것을 기억하세요. 첫 번째 기여를 하고 싶으시다면 아래의 간단한 단계를 따르세요. 재미있을 거라고 약속합니다.

컴퓨터에 Visual Studio Code가 없는 경우 [설치]하세요.(https://code.visualstudio.com/download).

**참고: **이 튜토리얼은 Windows 10 컴퓨터에서 Visual Studio Code(버전 1.27.2)를 사용하여 제작되었습니다. 이 튜토리얼의 후반부에서는 몇 가지 키보드 단축키를 사용할 것입니다. 이 단축키는 다른 운영 체제(macOS/Linux)와 키보드 언어(영국, 독일어 등)에 따라 다를 수 있습니다. 명령 팔레트에서 "단축키"를 검색하여 단축키 목록을 살펴볼 수 있습니다.

## 이 리포지토리 포크

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

이 페이지 오른쪽 상단의 포크 버튼을 클릭하여 이 리포지토리를 포크합니다. 그러면 이 리포지토리의 복사본이 GitHub 계정에 생성됩니다.

GitHub는 내 리포지토리와 포크한 리포지토리 간의 관계를 추적합니다. 리포지토리를 작업 복사본으로 생각하면 됩니다.

대부분의 최상위 GitHub 리포지토리(다른 리포지토리에서 포크되지 않은 리포지토리)에는 직접 변경 사항을 커밋할 수 있는 소규모의 핵심 팀이 있습니다. 다른 모든 기여자는 리포지토리를 포크하고 포크에서 변경한 다음 풀 리퀘스트를 만들어 변경 내용을 최상위 리포지토리에 다시 병합해 달라고 요청해야 합니다. 최상위 리포지토리 관리자가 변경 사항을 마음에 들어하면 병합되며, 즉시 명성과 부를 얻을 수 있습니다! 이 방법은 나중에 자세히 설명합니다.

## 리포지토리 복제

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

다음 단계는 변경을 시작할 수 있도록 리포지토리를 머신에 복제하는 것입니다. VS Code에는 리포지토리의 URL이 필요하므로 코드 버튼을 클릭한 다음 "클립보드에 복사" 아이콘을 클릭합니다.

**주의: **신규 기여자가 자주 저지르는 실수 중 하나는 리포지토리를 복제하지 않고 _에서_ 포크한 리포지토리를 복제하는 것입니다. 브라우저의 주소 표시줄을 확인하여 리포지토리를 복제하고 있는지 확인하세요.

이제 Visual Studio Code를 엽니다. VS Code의 시작 페이지가 나타납니다. 거기에서 `F1`을 눌러 아래 표시된 바를 엽니다. 텍스트 필드에 이미 `>`(보다 큰) 기호가 있는 것을 확인할 수 있습니다. Ctrl-P`를 눌러 입력 프롬프트로 이동한 다음 `>` 문자를 입력할 수도 있습니다.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone.png" alt="Clone Popup (Command Popup)" />

아래에 이미 몇 가지 잘 알려지지 않은 명령어가 나열되어 있는 것을 볼 수 있습니다. 제가 최근에 사용한 명령어들입니다. 그러니 신경 쓰지 마세요.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone1.png" alt="Clone repo" />

이제 `git clone`을 입력하되, `git` 또는 `clone`만 입력합니다(검색처럼 작동합니다).
항목 `Git: Clone` 항목을 선택하고 `Enter`를 누릅니다.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone2.png" alt="Paste Repository URL in" />

리포지토리의 URL을 붙여넣고 'Enter'를 누릅니다. 그러면 파일 탐색기가 열리고 여기서 Git 리포지토리를 저장할 위치를 선택할 수 있습니다.

**중요**: 원본 리포지토리가 아닌 포크된 리포지토리인지 확인하세요. 그렇지 않으면 작동하지 않습니다.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone3.png" alt="Status popup" />

Visual Studio Code의 오른쪽 하단에 상태 팝업이 표시됩니다. 완료되면 대화 상자의 버튼을 사용하여 복제된 리포지토리(이제 컴퓨터의 폴더)를 열 수 있습니다.

## 브랜치 만들기

F1`을 눌러 명령 팔레트를 다시 엽니다. 브랜치`를 입력하고 거기에서 `브랜치 만들기` 명령을 선택합니다. 다음 단계에서 새 브랜치 이름을 입력합니다(예: `add-david-kroell`). Enter 키를 누르면 브랜치가 생성됩니다. 브랜치는 이미 체크 아웃되어 있습니다. [체크아웃이란 무슨 뜻인가요?](https://www.git-scm.com/docs/git-checkout)

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-branch.png" alt="Branches Command Palette" />

## Make necessary changes

Open `Contributors.md` and add your name anywhere in the file. 이 파일에는 GFM(GitHub Flavored Markdown)이 포함되어 있습니다. <a href="https://en.wikipedia.org/wiki/Markdown">markdown</a> 구문을 사용합니다.

다른 기여자 중 한 명을 복사하고 자신의 이름으로 수정하여 구문이 올바른지 확인하세요(까다로울 수 있음).

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-changes.png" alt="Add your name" />

## GitHub에 변경 사항 커밋 및 푸시하기

VS Code의 왼쪽에는 5개의 아이콘이 표시된 메뉴가 있습니다. 버전 제어/소스 제어 아이콘을 선택합니다.
(단축키: Ctrl + Shift + G)

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-commit.png" alt="Commit changes" />

파일 탐색기는 마지막 커밋 이후에 변경된 모든 파일을 표시합니다. 파일을 마우스로 가리키고 `+`(더하기)를 클릭하면 파일이 스테이징됩니다.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-commit1.png" alt="Stashed Files">

탐색기 상단의 줄에 내용을 입력하고 확인 표시를 누릅니다. 이제 변경 내용이 로컬 복사본에 커밋됩니다. 이제 변경 내용을 GitHub로 다시 푸시해야 합니다.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-push.png" alt="Stashed Files">

점 3개 아이콘을 사용하여 메뉴를 열고 '브랜치 게시' 옵션을 선택합니다. 그러면 GitHub 자격 증명을 입력할 수 있는 대화 상자가 열립니다.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-gh-auth.png" alt="Stashed Files">

## 검토를 위해 변경 사항 제출

이 시점에서 변경을 완료했지만 아직 리포지토리에만 저장되어 있습니다. 이 단계에서는 최상위 리포지토리의 관리자에게 변경 내용을 병합하도록 요청하는 방법을 보여드립니다.

GitHub의 리포지토리에서 새 브랜치 알림 옆에 `비교 및 풀 리퀘스트` 버튼이 표시됩니다. 해당 버튼을 클릭합니다.

<img src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

이제 풀 리퀘스트를 제출하세요.

<img src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

곧 모든 변경 내용을 이 프로젝트의 마스터 브랜치에 병합할 것입니다. 변경사항이 병합되면 알림 이메일을 받게 됩니다.

## 이제 어디로 가야 하나요?

축하해요! 기여자로서 자주 접하게 되는 표준 _포크 -> 복제 -> 편집 -> PR_ 워크플로우를 방금 완료하셨습니다!

웹 앱]으로 이동하여 여러분의 기여를 축하하고 친구 및 팔로워와 공유하세요(https://firstcontributions.github.io#social-share).

도움이 필요하거나 궁금한 점이 있는 경우 슬랙 팀에 가입할 수 있습니다. [슬랙 팀 가입하기](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).


### [추가 자료](../additional-material/git_workflow_scenarios/additional-material.md)

## 다른 도구를 사용한 튜토리얼
[메인 페이지로 돌아가기](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
