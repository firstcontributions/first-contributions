[![오픈 소스 Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# 첫 번째 기여

|<img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Visual_Studio_2017_logo_and_wordmark.svg/2000px-Visual_Studio_2017_logo_and_wordmark.svg.png" width="200">|Visual Studio 2017 Edition|
|---|---|

힘들어요. 무언가를 처음 할 때는 항상 어렵습니다. 특히 협업할 때 실수를 하는 것은 편한 일이 아닙니다. 하지만 오픈소스는 협업과 함께 일하는 것이 핵심입니다. 저희는 새로운 오픈소스 기여자가 처음으로 배우고 기여하는 방식을 단순화하고자 했습니다.

기사를 읽고 튜토리얼을 보는 것도 도움이 될 수 있지만, 아무것도 엉망으로 만들지 않고 실제로 해보는 것보다 더 좋은 것은 없습니다. 이 프로젝트는 초보자가 처음 기여하는 방법을 안내하고 간소화하는 것을 목표로 합니다. 편안할수록 더 잘 배울 수 있다는 것을 기억하세요. 첫 번째 기여를 하고 싶으시다면 아래의 간단한 단계를 따르세요. 재미있을 거라고 약속합니다.

컴퓨터에 Visual Studio 2017이 설치되어 있지 않은 경우, [설치]하세요(https://www.visualstudio.com/downloads/).

## 이 리포지토리 포크

<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/fork.png" alt="fork this repository" />

이 페이지 상단의 포크 버튼을 클릭하여 이 리포지토리를 포크합니다. 그러면 GitHub 계정에 이 리포지토리의 복사본이 생성됩니다.

GitHub는 내 리포지토리와 포크한 리포지토리 간의 관계를 추적합니다.  리포지토리를 작업 복사본으로 생각하면 됩니다.

대부분의 최상위 GitHub 리포지토리(다른 리포지토리에서 포크되지 않은 리포지토리)에는 직접 변경 사항을 커밋할 수 있는 소규모의 핵심 팀이 있습니다.  다른 모든 기여자는 리포지토리를 포크하고 포크에서 변경한 다음 풀 리퀘스트를 만들어 변경 내용을 최상위 리포지토리에 다시 병합해 달라고 요청해야 합니다. 최상위 리포지토리 관리자가 변경 사항을 마음에 들어하면 병합되며, 즉시 명성과 부를 얻을 수 있습니다!  병합하는 방법은 나중에 자세히 설명합니다.

## 리포지토리 복제

<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/clone.png" alt="clone this repository" />

다음 단계는 변경을 시작할 수 있도록 리포지토리를 내 컴퓨터에 복제하는 것입니다. Visual Studio에서 리포지토리의 URL이 필요하므로 "복제" 버튼을 클릭한 다음 "클립보드에 복사" 아이콘을 클릭합니다.

**주의: 신규 기여자가 자주 저지르는 실수 중 하나는 리포지토리를 복제하지 않고 포크한 리포지토리를 *복제*하는 것입니다.  브라우저의 주소 표시줄을 확인하여 리포지토리를 복제하고 있는지 확인하세요.

이제 Visual Studio 2017을 시작할 시간입니다!  이 튜토리얼의 대부분을 팀 탐색기 탭에서 작업하게 됩니다.  기본적으로 열려 있지 않은 경우 '보기 > 팀 탐색기'를 클릭하여 엽니다.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-01-clone1.png" alt="Team Explorer" />

팀 탐색기에는 다양한 보기가 있으며 상단에 여러 영역을 찾는 데 도움이 되는 탐색 버튼이 있습니다.  리포지토리를 복제하려면 기본값인 연결 보기에 있어야 합니다.  '복제' 버튼이 보이지 않으면 상단의 녹색 플러그를 클릭합니다.

로컬 Git 리포지토리** 아래에서 '복제' 옵션을 클릭하고 텍스트 상자에 리포지토리의 URL을 붙여넣습니다.  이 URL은 이전에 GitHub에서 클립보드에 복사한 URL이어야 합니다.

복제` 버튼을 클릭하여 프로세스를 시작합니다.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-02-clone2.png" alt="Clone repo" />

프로세스가 완료되면 리포지토리의 내용을 볼 수 있는 솔루션 탐색기 탭으로 이동합니다.  변경 사항이 있으므로 아래 스크린샷과 다르게 보일 것입니다!

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-03-clone3.png" alt="Solution Explorer" />

## 브랜치 만들기

팀 탐색기 탭으로 돌아가서 기본 탐색 드롭다운을 사용하여 브랜치 보기를 엽니다.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-04-branch1.png" alt="Branches view" />

첫 번째 기여 리파와 '마스터'라고 하는 기본 브랜치가 보일 것입니다.  마스터`를 마우스 오른쪽 버튼으로 클릭하고 `새 로컬 브랜치를 다음에서...`를 선택합니다.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-05-branch2.png" alt="New branch" />

지점의 이름을 `add-<귀하의_이름_이름_여기>`와 같은 형식으로 지정합니다(예: `add-alonzo-church`).

체크아웃 브랜치` 상자를 체크한 상태로 두고 `브랜치 생성` 버튼을 클릭합니다.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-06-branch3.png" alt="Create branch" />

목록에 새 지점이 표시될 것입니다.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-07-branch4.png" alt="See new branch" />

## 필요한 변경 사항 적용

Open `Contributors.md` and add your name to the end of the list. 이 파일에는 깃허브의 독점적인 맛인 GFM(깃허브 맛 마크다운)이 포함되어 있습니다. <a href="https://en.wikipedia.org/wiki/Markdown">markdown</a> 구문을 사용합니다.

다른 기여자 중 한 명을 복사하고 자신의 이름으로 수정하여 구문이 올바른지 확인하세요(까다로울 수 있음).

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-08-change1.png" alt="Add your name" />

## GitHub에 변경 내용 커밋 및 푸시하기

팀 탐색기로 다시 전환하고 변경사항 보기로 이동합니다.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-09-commit1.png" alt="Changes" />

커밋과 함께 게시할 정보를 입력하고 '저장'을 클릭합니다. Visual Studio는 향후 커밋을 위해 해당 정보를 기억합니다.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-10-commit2.png" alt="Git user information" />

**참고: Visual Studio는 `.vs`라는 숨겨진 폴더를 사용하여 개인 설정 및 환경 설정을 저장합니다.  이 폴더의 내용은 **Git에 저장해서는 안 됩니다**.
이 폴더가 아직 무시되지 않은 경우, 이 폴더를 리포지토리에 보내지 않도록 Git에 이 폴더를 무시하도록 지시해야 할 수 있습니다.

이 폴더는 이미 이 리포지토리에서 무시되었으므로 이 단계를 수행할 필요가 없으며, 향후 프로젝트를 위한 참고용으로만 여기에 있습니다.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-11-commit3.png" alt="Ignore vs folder" />

이제 변경된 파일 목록과 커밋 코멘트를 입력할 수 있는 텍스트 상자가 표시됩니다.  코멘트는 짧지만 꼼꼼하게 작성해야 합니다.  커밋 코멘트를 읽다가 이런 걸 보는 것보다 더 나쁜 것은 없습니다: "몇 가지를 업데이트했습니다." 몇 초만 시간을 내어 커밋에 대한 개요를 작성하세요.  나중에 팀이 고마워할 것이고, 스스로에게도 고마워할 것입니다!

'모두 커밋하고 푸시'를 클릭하면 로컬 커밋을 수행하고 변경 내용을 리포지토리에 푸시하는 모든 과정을 한 번에 완료할 수 있습니다.

**참고: 커밋은 Push와 별도로 수행할 수 있습니다.  여기서는 편의를 위해 두 가지를 모두 수행합니다. 커밋은 로컬에 변경 내용을 기록하지만 푸시하기 전까지는 GitHub 리포지토리에 반영되지 않습니다.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-12-commit4.png" alt="Commit and Push" />

처음 GitHub에 푸시할 때 Visual Studio에서 GitHub 자격 증명을 요청합니다.  이 자격 증명은 캐시되므로 자주 표시되지 않을 것입니다.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-13-commit5.png" alt="Login" />

푸시 작업이 완료된 후 GitHub에서 리포지토리를 열면 최근에 푸시된 브랜치를 나타내는 메시지가 표시됩니다.

'브랜치: 마스터' 드롭다운을 열고 새 브랜치를 선택하면 변경 사항을 확인할 수 있습니다. 축하합니다, 브랜치 URL을 전 세계에 공유하여 진행 상황을 보여줄 수 있습니다!

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-14-commit6.png" alt="View pushed branch on GitHub" />

## 검토를 위해 변경 사항 제출

이 시점에서 변경을 완료했지만 아직 리포지토리에만 남아 있습니다.  이 단계에서는 최상위 리포지토리의 관리자에게 변경 내용을 병합하도록 요청하는 방법을 보여드립니다.

GitHub의 리포지토리에서 새 브랜치 알림 옆에 `비교 및 풀 리퀘스트` 버튼이 표시됩니다. 해당 버튼을 클릭합니다.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/compare-and-pull.png" alt="create a pull request" />

이제 풀 리퀘스트를 제출하세요.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/submit-pull-request.png" alt="submit pull request" />

곧 모든 변경 내용을 이 프로젝트의 마스터 브랜치에 병합할 것입니다. 변경 사항이 병합되면 알림 이메일을 받게 됩니다.

## 이제 어디로 가야 하나요?

축하합니다!  기여자로서 자주 접하게 될 표준 _포크 -> 복제 -> 편집 -> PR_ 워크플로우를 방금 완료하셨습니다!

웹 앱]으로 이동하여 여러분의 기여를 축하하고 친구 및 팔로워와 공유하세요.(https://firstcontributions.github.io#social-share).

도움이 필요하거나 궁금한 점이 있는 경우 슬랙 팀에 가입할 수 있습니다. [슬랙 팀 가입하기](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).


### [추가 자료](../additional-material/git_workflow_scenarios/additional-material.md)

## 다른 도구를 사용한 튜토리얼
[메인 페이지로 돌아가기](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
