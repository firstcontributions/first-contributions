## 여러분의 저장소에서 브랜치 삭제하기

지금까지의 튜토리얼을 수행했다면, 우리의 `<add-your-name>` 브랜치가 목적을 완료했습니다. 이제는 로컬 저장소에서 삭제할 차례입니다. 필수사항은 아니지만 이 브랜치의 이름은 다소 특별한 목적을 나타내므로 이미 병합되었다면 그 수명을 다했다고 할 수 있습니다.
First, let's merge your `<add-your-name>` to your master, so to go your master branch:
먼저, `<add-your-name>`을 마스터에 합쳐야합니다. 마스터 브랜치로 이동합니다.:
```
git checkout master
```

`<add-your-name>`를 마스터에 병합합니다.:
```
git merge <add-your-name> master
```

`<add-your-name>`를 로컬 저장소에서 삭제합니다.:
```
git branch -d <add-your-name>
```

이제 로컬 머신의 `<add-your-name>`브랜치를 삭제했고 모든 것이 깔끔하게 보입니다.
이 시점에서 GitHub 포크에 여전히 `<add-your-name>` 브랜치가 있어야합니다. 그러나 이것을 삭제하기 전에 이 원격지의 브랜치에서 상위 저장소로 "PR(Pull request)"을 보냈음을 기억하십시오. 따라서 아직 병합되지 않았다면이 브랜치를 삭제하지 마십시오.
그러나 해당 브래치를 이미 병합했고 원격 브랜치를 삭제하려면 다음을 사용하십시오.:
```
git push origin --delete <add-your-name>
```

자, 여러분은 이제 자신의 브래치를 정리하는 법을 배웠습니다.
시간이 지나면 많은 커밋이 저장소에 추가됩니다. 그리고 로컬 머신과 GitHub 포크의 마스터 브랜치는 최신 버전이 아닙니다. 따라서 저장소를 내 것과 동기화 된 상태로 유지하려면 아래 단계를 따르십시오.

#### [여러분이 포크한 저장소와 싱크상태 유지하기](keeping-your-fork-synced-with-this-repository.ko.md)
