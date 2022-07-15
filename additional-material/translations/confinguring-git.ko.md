# git 설정하기

여러분이 git을 사용해서 처음 커밋을 시도하면, 아마 다음과 같은 prompt 메세지를 볼것입니다.

```bash
$ git commit
*** Please tell me who you are.

Run

git config --global user.email "you@example.com"
git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.
```

여러분이 커밋을 생성할때 git은 여러분이 누구인지 알 필요가 있습니다. 여러분이 공동으로 작업을 할 때, 여러분은 누가 프로젝트의 어떤 부분을, 그리고 언제 수정했는지, 그에 따라 git이 이름과 이메일에 연결된 커밋을 생성하는것을 알 수 있어야합니다.

`git commit` 커맨드에 여러분의 이메일과 이름을 제공하는 방법은 여러 가지가 있으며, 우리는 아래에서 그 중 몇가지를 살펴볼것입니다.

### 전역 설정

여러분이 어떤것을 전역 설정으로 설정하면, 여러분은 작업하는 시스템의 모든 레포지토리에 접근할 수 있습니다. 이것은 선호되는 방법이며 대부분의 경우에 동작합니다.

어떤것을 전역 설정으로 설정하려면, `config` 커맨드를 다음과 같이 사용합니다:

`$ git config --global <variable name> <value>`

유저 세부 설정의 경우에는, 다음과 같이 실행합니다:

```
$ git config --global user.email "you@example.com"
$ git config --global user.name "Your Name"
```

### 레포지토리 설정

제목에서와 같이, 이 설정들은 여러분의 현재 레포지토리에 맞춰져있습니다. 만약 여러분이 특정한 레포지토리나, 일과 관련된 프로젝트에 회사의 이메일로 커밋을 하고 싶다면, 이 방법을 사용할 수 있습니다.

어떤것을 레포지토리 설정으로 저장하려면, `config` 커맨드를 `--global` 옵션 없이 사용합니다:

`$ git config <variable name> <value>`

유저 세부 설정의 경우에는, 다음과 같이 실행합니다:

```
$ git config user.email "you@alternate.com"
$ git config user.name "Your Name"
```

### 커맨드라인 설정

이와 같은 형태의 설정들은 현재 커맨드에만 국한됩니다. 모든 깃 커맨드는 일시적인 설정을 하기전에 `-c` 인자를 취합니다.

어떤것을 커맨드라인 설정으로 저장하려면, 다음 커맨드를 실행합니다:

`$ git -c <variable-1>=<value> -c <variable-2>=<value> <command>`

우리의 예시에서, 다음과 같이 커밋 커맨드를 실행할것입니다:

`git -c user.name='Your Name' -c user.email='you@example.com' commit -m "Your commit message"`

### 우선순위에 관하여

여기 설명된 세가지 방법중에서, 우선도는 `command-line > repository > global` 순입니다. 이것은 변수가 커맨드라인에서 전역으로 설정되었다면, 커맨드라인 값은 연산에 사용됨을 뜻합니다.

## 유저 디테일을 넘어서

우리는 지금까지 설정에 관해서는 유저 설정만 다뤘습니다. 그러나, 다른 설정 옵션이 사용가능합니다. 몇가지는:

1. `core.editor` - 커밋 메세지나 다른것을 쓸때 쓰는 에디터의 이름을 특정합니다.
2. `commit.template` - 시스템의 파일을 초기 커밋 템플릿으로 특정합니다.
3. `color.ui` - git의 출력에 쓰이는 색의 불리언 값을 특정합니다.

우리는 약간의 세부설정을 이해하기쉽게 요약했습니다. 더 살펴보려면, [git-scm.com](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration)을 살펴보십시오.