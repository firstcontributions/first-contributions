[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# 첫 기여

| <img alt="GitHub Desktop" src="https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png" width="200"> | GitHub 명령줄 인터페이스 (CLI) |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |

이 가이드는 모든 것을 터미널로 처리하고 싶은 우리 터미널 덕후를 위한 것입니다. [Github-CLI](https://cli.github.com/)가 이를 가능하게 합니다. 첫 기여는 즐겁고, 기여를 계속 이어나갈 계기가 되어야 한다는 것을 기억하세요!

이 가이드는 그래픽 인터페이스를 사용하지 않아서, 약간 도전적이지만, 여전히 재미있고, 따라하기 쉽습니다!

먼저, 다음 작업이 필요합니다:

- Git 설치 (설치방법 [git](https://git-scm.com/downloads))
- Github 계정

그리고 [공식 문서](https://github.com/cli/cli#installation)를 참고하여 `github-cli`를 설치합니다.

그 다음, 아래 명령으로 CLI에 로그인 합니다: 

```bash
gh auth login
```

지시사항을 따라 로그인을 하면, 준비 완료입니다!

# 저장소 Fork 하기

다음 명령으로 간단히 진행합니다:

```bash
gh repo fork firstcontributions/first-contributions
```

**중요: Clone 여부에 대한 질문이 나오면 "yes"를 선택하세요**

# Branch 만들기

이 단계에서는 git을 사용하므로, 아래 명령에서 이름(역주: john-doe 부분)을 변경해서 사용하세요.

```bash
git switch -c add-john-doe
```

# 필요한 내용을 수정하고, Commit 하기

이제 문서 편집기로 `Contributors.md` 파일을 열어서 수정 할 수 있습니다. 여러분의 이름을 중간 부분에 적은 후 파일을 저장하세요.

프로젝트 디렉토리에서 `git status`를 실행하면 변경내용을 확인 할 수 있습니다.
<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

이 변경 사항을 위에서 만든 branch에 추가 하기 위해 `git add`명령을 사용합니다:
`git add Contributors.md`

그리고 `git commit`명령으로 추가된 변경 사항들을 branch에 commit 합니다:
`git commit -m "Add your-name to Contributors list`
명령에서 `your-name` 부분을 여러분의 이름으로 변경해서 사용하세요.

# github에 변경 사항을 Push 하기

`git push` 명령으로 수정한 내용을 Push 합니다:

```
git push origin -u your-branch-name
```

위 명령에서 `your-branch-name` 부분에 위에서 만들었던 branch 이름으로 변경해서 사용하세요.

<details>
<summary> <strong>Push 과정에서 에러가 발생하면, 여기를 클릭하세요:</strong> </summary>

- ### 인증 오류
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  SSH키 생성이 필요합니다. [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)를 참고하세요.

</details>

# 검토를 받기 위해 수정한 내용을 제출

다음 명령으로 프로젝트 디렉토리에서 실행하여 변경사항 검토를 위한 pull request를 만들 수 있습니다:

```bash
gh pr create --repo firstcontributions/first-contributions
```

그 다음 작성한 pull request를 제출하세요.

`gh status`명령으로 pull request가 실제로 실행되는 모습을 확인할 수 있습니다.

## 이제 무얼 할까요?

축하합니다! 기여자로서 자주 마주하게 되는 _fork -> clone -> 수정 -> pull request_ 단계를 완료 하셨습니다!

[web app](https://firstcontributions.github.io/#social-share)에서 여러분의 기여를 축하하고 공유하세요.

도움이 필요하거나, 질문이 있으면 [slack에 참여하세요](https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA).

이제 다른 프로젝트에 기여해보세요. 시작하기 쉬운 이슈가 있는 프로젝트 목록을 정리했습니다. [web app에서 목록을 확인해보세요](https://firstcontributions.github.io/#project-list).

### [추가 자료](../additional-material/git_workflow_scenarios/additional-material.md)

## 다른 도구에 대한 튜토리얼

[첫 페이지로 돌아가기](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
