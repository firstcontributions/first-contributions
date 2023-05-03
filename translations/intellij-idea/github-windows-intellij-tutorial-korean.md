[![오픈 소스 Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# First Contributions

| <img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/9/9c/IntelliJ_IDEA_Icon.svg" width="40"> | IntelliJ 아이디어 |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |


힘들어요. 무언가를 처음 할 때는 항상 어렵습니다. 특히 협업할 때 실수를 하는 것은 편한 일이 아닙니다. 하지만 오픈소스는 협업과 함께 일하는 것이 핵심입니다. 저희는 새로운 오픈소스 기여자가 처음으로 배우고 기여하는 방식을 단순화하고자 했습니다.

기사를 읽고 튜토리얼을 보는 것도 도움이 될 수 있지만, 아무것도 엉망으로 만들지 않고 실제로 해보는 것보다 더 좋은 것은 없습니다. 이 프로젝트는 초보자가 처음 기여하는 방법을 안내하고 간소화하는 것을 목표로 합니다. 편안할수록 더 잘 배울 수 있다는 것을 기억하세요. 첫 번째 기여를 하고 싶으시다면 아래의 간단한 단계를 따르세요. 재미있을 거라고 약속합니다.

컴퓨터에 IntelliJ IDEA가 없는 경우, [설치]하세요(https://www.jetbrains.com/idea/download/#section=windows).

**참고:** 이 튜토리얼은 Windows 10 컴퓨터에서 IntelliJ IDEA(버전 2019.3.2)를 사용하여 제작되었습니다. 이 튜토리얼의 후반부에서는 몇 가지 키보드 단축키를 사용할 것입니다. 다른 운영 체제(macOS/Linux)에서는 다를 수 있습니다.

## 이 리포지토리 포크

<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/fork.png" alt="fork this repository" />

이 페이지 오른쪽 상단의 포크 버튼을 클릭하여 이 리포지토리를 포크합니다. 그러면 이 리포지토리의 복사본이 GitHub 계정에 생성됩니다.

GitHub는 내 리포지토리와 포크한 리포지토리 간의 관계를 추적합니다. 리포지토리를 작업 복사본으로 생각하면 됩니다.

대부분의 최상위 GitHub 리포지토리(다른 리포지토리에서 포크되지 않은 리포지토리)에는 직접 변경 사항을 커밋할 수 있는 소규모의 핵심 팀이 있습니다. 다른 모든 기여자는 리포지토리를 포크하고 포크에서 변경한 다음 풀 리퀘스트를 만들어 최상위 리포지토리에 변경 내용을 다시 병합하도록 요청해야 합니다. 최상위 리포지토리 관리자가 변경 사항을 승인하면 병합되며, 즉시 명성과 부를 얻을 수 있습니다! 방법은 나중에 자세히 설명합니다.

## 리포지토리 복제

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

다음 단계는 변경을 시작할 수 있도록 리포지토리를 머신에 복제하는 것입니다. IntelliJ IDEA는 리포지토리의 URL을 필요로 하므로 "복제" 버튼을 클릭한 다음 "클립보드에 복사" 아이콘을 클릭합니다.

**주의: **신규 기여자가 자주 저지르는 실수 중 하나는 리포지토리를 복제하지 않고 _에서_ 포크한 리포지토리를 복제하는 것입니다. 브라우저의 주소 표시줄을 확인하여 리포지토리를 복제하고 있는지 확인하세요.

이제 IntelliJ IDEA를 엽니다. 

IntelliJ IDEA를 사용하면 기존 리포지토리를 체크아웃(Git 용어로는 복제)하고 다운로드한 데이터를 기반으로 새 프로젝트를 만들 수 있습니다.

주 메뉴에서 VCS | 버전 관리에서 가져오기를 선택하거나, 현재 열려 있는 프로젝트가 없는 경우 시작 화면에서 버전 관리에서 가져오기를 클릭합니다.

버전 관리에서 가져오기 대화 상자에서 복제하려는 원격 리포지토리의 URL을 지정하거나(테스트를 클릭하여 원격에 연결할 수 있는지 확인할 수 있음) 왼쪽에 있는 VCS 호스팅 서비스 중 하나를 선택합니다. 선택한 호스팅 서비스에 이미 로그인되어 있는 경우, 완료하면 복제할 수 있는 사용 가능한 리포지토리 목록이 표시됩니다.

복제를 클릭합니다. 복제된 소스를 기반으로 IntelliJ IDEA 프로젝트를 생성하려면 확인 대화 상자에서 예를 클릭합니다. Git 루트 매핑이 프로젝트 루트 디렉터리로 자동 설정됩니다.

프로젝트에 서브모듈이 포함된 경우 해당 서브모듈도 복제되어 프로젝트 루트로 자동 등록됩니다.

**중요**: 원본 리포지토리가 아닌 포크된 리포지토리인지 확인하세요. 그렇지 않으면 작동하지 않습니다.

## 브랜치 만들기

Git에서 브랜치는 예를 들어 기능에 대한 작업이 필요하거나 릴리스를 위해 코드베이스의 특정 상태를 고정해야 할 때 등 주요 개발 라인에서 벗어날 수 있는 강력한 메커니즘입니다.

IntelliJ IDEA에서 브랜치를 사용한 모든 작업은 Git 브랜치 팝업에서 수행됩니다. 이 팝업을 호출하려면 상태 표시줄에서 Git 위젯을 클릭하거나 Ctrl+Shift+`를 누르세요.

현재 체크 아웃된 브랜치의 이름이 상태 표시줄의 Git 위젯에 표시됩니다.

브랜치 팝업에서 새 브랜치를 선택합니다.

대화 상자가 열리면 브랜치 이름을 지정하고 해당 브랜치로 전환하려면 체크아웃 브랜치 옵션이 선택되어 있는지 확인합니다.

새 브랜치는 현재 HEAD에서 시작됩니다. 현재 브랜치 HEAD 대신 이전 커밋에서 브랜치를 시작하려면 버전 관리 도구 창의 로그 탭에서 이 커밋을 선택하고 Alt+9를 누른 후 컨텍스트 메뉴에서 새 브랜치를 선택합니다.

## 필요한 변경을 수행한다

O펜으로 `Contributors.md`를 열고 파일 아무 곳에나 이름을 추가하세요. 이 파일에는 GFM(GitHub Flavored Markdown)이 포함되어 있습니다<a href="https://en.wikipedia.org/wiki/Markdown">markdown</a> 구문을 사용합니다.

다른 기여자 중 한 명의 줄을 복사하고 자신의 이름으로 수정하여 구문이 올바른지 확인하세요 - 까다로울 수 있습니다.

## GitHub에 변경사항 커밋 및 푸시하기

버전 관리 도구 창의 로컬 변경사항 탭에서 커밋하려는 파일 또는 전체 변경목록을 선택하고 Ctrl+9를 누르거나 도구 모음에서 커밋 버튼을 클릭합니다.

변경사항 커밋 대화 상자가 열리면 마지막 커밋 이후 수정된 모든 파일과 새로 추가된 버전이 없는 모든 파일이 나열됩니다.

의미 있는 커밋 메시지를 입력합니다.

커밋 메시지 내역 커밋 메시지 내역 Ctrl+M을 클릭하여 최근 커밋 메시지 목록에서 선택할 수 있습니다.

커밋을 푸시하기 전에 나중에 커밋 메시지를 편집할 수도 있습니다.

Ctrl+Shift+K를 누르거나 메인 메뉴에서 VCS | Git | Push를 선택합니다. 푸시 커밋 대화 상자가 열리고 모든 Git 리포지토리(여러 리포지토리 프로젝트의 경우)가 표시되며 마지막 푸시 이후 각 리포지토리의 현재 브랜치에서 수행한 모든 커밋이 나열됩니다.

## 검토를 위해 변경 내용 제출

이 시점에서 변경을 완료했지만 아직 리포지토리에만 있습니다. 이 단계에서는 최상위 리포지토리의 관리자에게 변경 내용을 병합하도록 요청하는 방법을 보여 줍니다.

GitHub의 리포지토리에서 새 브랜치 알림 옆에 `비교 및 풀 리퀘스트` 버튼이 표시됩니다. 해당 버튼을 클릭합니다.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/compare-and-pull.png" alt="create a pull request" />

이제 풀 리퀘스트를 제출하세요.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/submit-pull-request.png" alt="submit pull request" />

곧 모든 변경 내용을 이 프로젝트의 마스터 브랜치에 병합할 것입니다. 변경사항이 병합되면 알림 이메일을 받게 됩니다.

## 이제 어디로 가야 하나요?

축하해요! 기여자로서 자주 접하게 되는 표준 _포크 -> 복제 -> 편집 -> PR_ 워크플로우를 방금 완료하셨습니다!

웹 앱]으로 이동하여 여러분의 기여를 축하하고 친구 및 팔로워와 공유하세요(https://firstcontributions.github.io#social-share).

도움이 필요하거나 궁금한 점이 있는 경우 슬랙 팀에 가입할 수 있습니다. [슬랙 팀 가입하기](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).


### [추가 자료](../additional-material/git_workflow_scenarios/additional-material.md)

## 다른 도구를 사용한 튜토리얼
[메인 페이지로 돌아가기](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
