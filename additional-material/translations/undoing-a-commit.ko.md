## 로컬 커밋 되돌리기

로컬에서 이미 커밋을 완료한 소스를 되돌리기 위해서는 다음 명령어를 입력합니다.
```
git reset
```

위 명령어는 스테이징 영역에서 가장 최근에 반영한 커밋을 리셋합니다. 
하지만 여러분의 작업 디렉토리에 변경한 파일들은 수정하지 않습니다. 따라서 여러분이 수정한 소스를 다시 커밋할 수 있습니다. 
만일 이전에 커밋한 변경된 파일 중에서 하나의 파일만 제거하기를 원할 경우, 아래 명령을 실행하세요.

```
git reset <file>
```
The command will remove only the specified file from the staging area, but changes made on the file still remained.
이 명령어는 스테이징 영역에서 해당 파일만 제거합니다. 그러나 작업 디렉토리에서는 변경된 상태 그대로 남아 있습니다.

다음은 ```git reset``` 사용법에 관한 예제입니다.
```
# 먼저 index.php 와 tutorial.php 파일을 수정합니다.
# 스테이징 영역에 파일을 추가합니다.
$ git add .
# 두 파일을 각각 커밋해야하므로
# tutorial.php 파일을 스테이징 영역에서 제거합니다.
$ git reset tutorial.php
# index.php 파일을 먼저 커밋합니다.
$ git commit -m "Changed index.php"
# 다음으로 tutorial.php 파일을 커밋합니다.
$ git add tutorial.php
$ git commit -m "Changed tutorial.php"
```

로컬 저장소에 문제가 생겨 여러분의 마지막 커밋 상태로 되돌리고 싶다면 아래 명령을 실행할 수 있습니다.
```
git reset --hard 
```
The command will not only reset your staging area, but also revert all your changes on the files to your last commit.
The mode ```--hard``` tells Git to undo all the changes in the working directory too.
You should only run this when you are really sure of throwing your whole local development out.

이 명령어는 스테이징 영역을 마지막 커밋 상태로 되돌리는 것 뿐만 아니라 여러분의 로컬에 변경된 파일도 되돌릴 수 있습니다.
```--hard``` 모드는 Git으로 하여금 작업 디렉토리에 대한 변경들도 되돌릴 수 있도록 합니다.
따라서 로컬에서 개발한 모든 개발 내용을 초기화해도 되는지 반드시 확인 후 실행하셔야 합니다.

다음은 ```git reset --hard``` 사용에 관한 예제입니다.
```
# 엉뚱한 실험을 시작하기로 결정했습니다.
# 먼저 'crazy.php' 파일을 만들고 코드를 추가합니다.
# 그리고 crazy.php 파일을 커밋합니다.
$ git add crazy.php 
$ git commit -m "Started a crazy dev"
# crazy.php 파일을 다시 수정하고 기타 여러 파일들을 생성하고 수정합니다.
# 그리고 수정한 모든 파일을 스테이징 영역에 추가하고 커밋합니다.
$ git add .
$ git commit -m "Continued dev"
# 테스트하고 마칩니다.
# 실험하기 전 상태로 되돌리기 위해 모든 수정사항을 제거합니다.
$ git reset --hard HEAD~2
```
```git reset --hard HEAD~2``` 명령어는 현재 브랜치에서 여러분이 수정한 이전의 커밋들 중에 2번째 커밋 포인트 상태로 이동함과 동시에 해당 커밋들에 대한 변경사항들이 복구됩니다. 그리고 프로젝트 히스토리에서 이전에 추가된 2개의 스냅샷이 제거됩니다.
P.s. 만일 여러분의 공유 저장소로 이미 push를 한 상태에서 ```git reset --hard``` 명령을 실행할 경우, 해당 저장소를 사용하는 모든 사람들에게 문제를 일으킬 수 있으므로 절대 실행해서는 안됩니다.

