# 커밋 로그 확인하기

특정 브랜치 및 파일과 관련된 커밋 로그를 확인하고 싶으시다면 다음 명령어를 유용하게 쓰실 수 있습니다:

`git log [options] [path]`

이 명령어는 기본적으로 커밋 로그를 시간 역순, 즉 내림차순으로 정렬하여 출력합니다.

## 명령어 출력 예시
```
$ git log
commit e3fabb30ab536bd5876461d8a749301a321e714f (HEAD -> check-commit-log-ko, upstream/main, origin/main, origin/HEAD, main)
Author: Dan Yunheum Seol <yunheum.seol@mail.mcgill.ca>
Date:   Tue Jun 4 01:07:25 2024 -0400

    Add dan-seol to Contributors list (#84962)

commit 4af4ec8a56e057ce8768af77eda528453974d0bc
Author: Edgar Humberto Tijerina Tamez <168693312+EdgarHTT@users.noreply.github.com>
Date:   Mon Jun 3 23:06:05 2024 -0600

    Add Edgar Tijerina to Contributors list (#84961)
```

## 명령어 변형(바리에이션) 및 선택 사항(옵션)

- 하나 혹은 여러 개의 특정 커밋 식별자(아이디)를 기준으로 접근 가능한 커밋 로그를 보고 싶으시다면 다음 명령어를 활용하세요: (`foo`나 `bar`를 예시로 들겠습니다)</i><br>
    `git log foo bar` 
- 반대로 특정 커밋 식별자를 기준으로 접근 가능한 커밋 로그를 출력에서 제외할 수도 있습니다. 커밋 식별자 앞에 삿갓표(캐럿 기호) `^`를 붙여 주세요: <i>(`baz`를 예시로 들자면)</i><br>
    `git log foo bar ^baz`
- 특정 파일과 관련된 커밋 로그를 볼 수도 있습니다. 아래 명령어를 사용해 보세요: <br> 
    `git log --all <filename>`
- 커밋 로그 목록의 항목 수를 제한 할 수도 있습니다: <i>(예를 들어 `5` 항목으로 줄여보겠습니다)</i><br> 
    `git log -n 5`

## 참조 및 더 알아보기
- [Official documentation](https://git-scm.com/docs/git-log)
