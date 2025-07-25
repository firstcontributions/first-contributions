# 여러분이 포크한 저장소와 싱크상태 유지하기

먼저, 전체 싱크과정을 이해해야합니다. 본 스키마에는 3개의 저장소들이 있습니다. 저의 GitHub에 있는 제 공개저장소인 `github.com/Roshanjossey/first-contributions/`와 여러분의 포크된 저장소인 `github.com/Your-Name/first-contributions/`, 그리고 로컬 머신에 위치해서 현재 작업중인 저장소가 있습니다. 오픈 소스 프로젝트에 특화된 이러한 조합을 `트라이앵글 워크플로우`라고 부릅니다.

<img style="float;" src="https://firstcontributions.github.io/assets/additional-material/triangle_workflow.png" alt="triangle workflow" />

여러분의 두 개의 저장소들을 제 공개 저장소의 최신 상태와 싱크상태를 유지하기 위해서는 제일 먼저여러분의 로컬머신에 위치한 저장소를 제 공개 저장소와 fetch와 merge를 해야합니다.
두번째는 여러분의 로컬 저장소를 포크된 GitHub의 저장소에 push하는 것 입니다. 이전 과정에서 봤듯이 "pull request"를 요청할 수 있는 곳은 오직 포크된 저장소에서만 가능합니다. 따라서 마지막으로 업데이트 되어야하는 저장소는 포크된 GitHub입니다.
자, 어떻게하는지 보겠습니다:
먼저 여러분은 main 브랜치에 위치해 있어야합니다. 현재 어떤 브래치에 있는지 확인합니다.:
```
git status
```
현재 main 브랜치가 아니라면 변경합니다.:
```
git checkout main
```

제 공개 저장소를 아직 여러분의 git에 추가하지 않았다면 다음 명령으로 추가합니다. `add upstream remote-url`:
```
git remote add upstream https://github.com/Roshanjossey/first-contributions
```
지정한 URL을 이용해 현재 프로젝트의 또 다른 최신 버전이 있는지 git에게 확인을 요청하는 방법입니다. 그리고 우리는 이를 `upstream` 이라고 부르기로합니다. 일단 git이 이러한 이름을 가지고 있다면 다음과 같이 공개 저장소의 최진 버전을 가지고 옵니다. :
```
git fetch upstream
```

여러분은 이제 제 포크(upstream remote)에서 최신 버전을 내려 받았습니다. 이제 공개 저장소의 변경된 내용을 여러분의 main 브랜치에 병합해야합니다.
```
git rebase upstream/main
```

여러분의 main 브랜치와 공개 저장소를 병합하고 나면 이제 여러분의 로컬머신의 main 브랜치는 최신 상태입니다. 마지막으로 여러분의 main 브랜치를 여러분의 포크에 push하게 되면 포크한 GitHub 또한 변경사항들이 반영됩니다.:
```
git push origin main
```
origin으로 명명된 리모트에 push하는 것에 주의하세요.
이제 여러분의 모든 저장소가 최신 상태를 유지하게 되었습니다. 
잘 하셨습니다! GitHub 저장소에 커밋이 추가적으로 발생할 때마다 이러한 작업을 해야합니다.


