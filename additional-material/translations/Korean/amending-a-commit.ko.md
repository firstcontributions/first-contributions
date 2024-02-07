## 커밋 수정하기

만약 커밋 메시지에 오타가 있거나 가장 최근의 커밋에서 몇줄을 빼먹은 걸 나중에 깨닫고 원격 저장소로 커밋을 수정하고자 하는 경우 어떻게 할까요? 이 자습서는 이러한 내용을 다룹니다.

### Github에 이미 푸시한 후에 최근 커밋 메시지 변경하기
파일을 열지 않고 수행할 경우:
*   다음을 타이핑합니다. ```git commit --amend -m "followed by your new commit message"```
*   변경사항을 저장소에 커밋하려면 다음을 실행합니다. ```git push origin <branch-name>```

참고: 단지 ```git commit --amend``` 이것만 입력한다면, 텍스트 편집기가 커밋 메시지를 입력하라고 할 것입니다. ``-m`` 플래그를 추가하면 이것을 막을 수 있습니다.

### Modifying on a single commit

그럼 한 단어를 변경하는 것과 같이 사소한 변경사항을 깜빡하고 커밋을 이미 원격 저장소에 푸시했다면 어떻게 해야 할까요?

이를 설명하기 위해 여기 제 커밋 로그가 있습니다:
```
g56123f create file bot file
a2235d updated contributor.md
a5da0d modified bot file
```
봇 파일에 한 단어를 추가하는 것을 깜빡했다고 해 봅시다.

이 경우 두가지 방법이 있습니다. 첫번째는 다음과 같이 변경사항을 포함하는 완전히 새로운 커밋을 수행하는 것입니다:
```
g56123f create file botfile
a2235d updated contributor.md
a5da0d modified botfile
b0ca8f added single word to botfile
```
두번째 방법은 a5da0d 커밋을 수정하고, 새 단어를 추가하고 이를 하나의 커밋으로 Github에 푸시하는 것 입니다.
이 방법은 사소한 변화이기 때문에 더 나을수도 있습니다.

이를 위해 다음을 수행하십시오:
*   파일을 수정하십시오. 이 경우, 이전에 빠뜨린 단어를 포함하여 봇 파일을 수정합니다.
*   그 다음, ```git add <filename>``` 을 실행하여 파일을 스테이징 영역으로 추가합니다.

보통 파일을 스테이징 영역에 추가하고 나면, 다음으로 우리가 해야할 일은 git commit -m "our commit message" 입니다.
그러나 여기서 우리가 원하는 것은 이전 커밋을 수정하는 것이므로, 다음을 실행합니다:

* ```git commit --ammend```
그러면 텍스트 편집기가 뜨고 메시지를 수정하라는 프롬프트가 뜰 것입니다. 이전 그대로 메시지를 두거나 변경할 수 있습니다.
* 에디터를 빠져나오십시오.
* ```git push origin <branch-name``` 으로 변경사항을 푸시하십시오.

이렇게 하면 두 변경사항이 단일 커밋이 됩니다.
