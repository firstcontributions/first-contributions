# squashing이란 무엇일까?

git에서, squashing은 커밋 기록을 다시 쓰는 것을 의미하므로, 수행된 변경 사항에 대한 설명과 함께 한 번에 커밋으로 완료합니다. 일반적으로 오픈 소스 프로젝트에서 주로 사용됩니다. 오픈 소스 프로젝트의 branch 기록의 대부분은 해당 branch를 만든 개발자에게만 관련되어 있기 때문입니다. squashing은 변경 사항을 더 쉽게 설명하고 필요하다면, 변경 사항을 되돌릴 수 있습니다.

# squash commits은 어떻게 하나요?

첫 번째, 먼저 git log 명령어를 수행하여 현재 branch에서 병합할 커밋을 검토합니다.

```
git log
```

다음과 같이 일련의 커밋들이 표시됩니다.

```
commit 예제
Author: omguhh
Date:   10/10/20
    Commit message 1

commit 예제2
Author: omguhh
Date:   10/10/20
    Commit message 2
```

이제 하나로 병합하려는 커밋을 확인하였으므로 git rebase를 사용하여 이 커밋을 하나로 만드는 작업을 수행할 수 있습니다. git rebase가 이미 익숙하다고 가정하면 다음과 같이 활성화할 수 있는 git rebase의 대화형 모드에서 squashing commits을 시작할 수 있습니다 :

```
git rebase -i
```

이제 대화형 rebase를 사용하여 다음과 같은 commit으로 얼마나 거슬러 올라가는지 시작점과 끝점을 지정할 수 있습니다.

```
git rebase -i HEAD~2
```

이 명령어를 실행하면 다음과 같은 내용이 표시됩니다 :

```
pick blablabla Changing test01.txt file
pick blablabla2 Adding dummy01.txt file

#
# 명령어 :
#  p, pick = 커밋을 사용합니다.
#  r, reword = 커밋을 사용하지만, 커밋 메시지를 수정합니다.
#  e, edit = 커밋을 사용하지만, 수정을 위해 중지합니다. 
#  s, squash = 커밋을 사용하지만, 이전의 커밋을 흡수시킵니다.
#  f, fixup = squash와 같지만, 커밋 로그 메시지를 버립니다.
#  x, exec = 셸을 사용하여 명령을 실행합니다. (나머지 라인)
#
# 이 라인들은 순서를 다시 정할 수 있으며, 위에서 아래로 실행됩니다. 
#
# 만약 여기서 한 줄을 제거하면 커밋이 손실됩니다. 
#
# 그러나, 모든 항목을 제거하면 rebase가 중단됩니다.
#
# 비어있는 커밋은 주석 처리 됩니다.
```

따라서 blablabla2를 blablabla로 압축하려면 다음을 변경합니다 :

```
pick blablabla Changing test01.txt file
squash blablabla2 Adding dummy01.txt file

```

모든 것이 잘 동작하였다면, 다음과 같은 결과를 얻을 수 있습니다 :

```
# 두 개의 결합된 commits 입니다.
# 첫 번째 커밋 메시지
commit message 1

# 두 번째 커밋 메시지

commit message 2
```

That you can freely change before you decide to exit the editor to save these changes.

Running git log again should show you the commit message you entered before exiting the screen with the commits combined into one.
