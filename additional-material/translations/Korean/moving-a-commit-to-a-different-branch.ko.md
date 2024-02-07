## 커밋을 다른 브랜치로 옮기기

What if you commit a change, and then realize that you committed to a different branch?
How can you change that? This is what this tutorial covers.
만일 변경사항을 반영했는데 전혀 다른 브랜치에 커밋한 사실을 알았다면 어떻게할까요?
이걸 어떻게 바로잡을 수 있을까요? 바로 이 장에서 다룰 내용입니다.

### 가장 최근 커밋들을 기존에 있는 브랜치로 이동시키기
사용예:

```git reset HEAD~ --soft``` - 마지막 커밋을 되돌립니다. 물론 수정한 내용은 그대로 남아있습니다.  
```git stash``` - 현재까지 수정한 모든 작업내용들의 상태를 저장합니다.  

```git checkout name-of-the-correct-branch``` - 실제 반영하고자하는 브랜치를 체크아웃합니다.
```git stash pop``` - 마지막으로 저장한(stash) 변경내역들을 현재 브랜치에 반영하고 저장한 내역에서 삭제합니다.  
```git add .``` - 또는 커밋에 반영할 변경내역들을 개별적으로 추가합니다.  
```git commit -m "your message here"``` - 저장하고 변경내역을 커밋합니다.  

자 이제 변경사항이 올바른 브랜치에 반영되었습니다.

### 가장 최근 커밋들을 신규 브랜치를 생성하여 이동시키기

사용예:  
```git branch newbranch``` -  신규 브랜치를 생성하고 모든 커밋들을 저장합니다.  
```git reset --hard HEAD~#``` - master 브랜치의 #번째 커밋을 되돌립니다. 되돌린 커밋들은 master에서 완전히 삭제되므로 주의하세요.  
```git checkout newbranch``` - 생성한 브랜치로 이동합니다. 모든 커밋들을 가지고 있을겁니다.  

주의: 커밋하지 않은 변경사항들은 사라집니다.
