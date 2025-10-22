# 기여 방법 안내

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="이 저장소를 포크하세요" />

## 이 저장소를 포크하세요

## 포크한 저장소를 클론하세요

포크한 저장소에서 Code 버튼을 클릭하고, SSH 탭을 선택한 다음 `copy to clipboard` 버튼을 클릭하세요.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="저장소 클론하기" />
터미널을 열고 `git clone` 명령어를 실행하세요.

```bash
git clone "복사한 URL"
```

> [!important]
> 아래 단계에서 `<your-github-id>`가 등장하면, 당신의 GitHub 사용자명으로 바꿔야 합니다.
> 예: GitHub ID가 `aaronsw`인 경우,
> `git switch -c add-<your-github-id>`는 `git switch -c add-aaronsw`이 됩니다.
> `contributors/<your-github-id>.html`는 `contributors/aaronsw.html`이 됩니다.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="URL 복사" />

## 브랜치를 생성하세요

아직 저장소 디렉토리가 아니라면 저장소 디렉토리로 이동하세요.

```bash
cd code-contributions
```

`git switch` 명령어로 새로운 브랜치를 생성합니다.

```bash
git switch -c add-<your-github-id>
```


## 나만의 카드 만들기

나만의 카드를 contributors 디렉터리 내에 HTML 파일 형식으로 추가하세요. 아래 템플릿을 참고하여 GitHub 시작하시고, 본인의 사용자명을 파일 이름으로 사용하세요.

`contributors/<your-github-id>.html`
```html
<article>
  <h3>Your username</h3>
  <p>A small bio about you (optional)</p>
  <h4>Programming languages I use</h4>
  <section class="container">
    <div class="badge" style="background-color: #3874a4; color: white">
      Python
    </div>
    <div class="badge" style="background-color: #f7df1e; color: black;">
      JavaScript
    </div>
  </section>

  <h4>Tools I use</h4>
  <section class="container">
    <img
      class="icon"
      src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/bash/bash-original.svg"
    />
    <img
      class="icon"
      src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linux/linux-original.svg"
    />
  </section>
</article>
<style>
  body {
    font-family: sans-serif;
  }
  .container {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
  }
  .badge {
    padding: 0.5rem;
    border-radius: 0.25rem;
  }
  .icon {
    width: 2rem;
  }
</style>

```

## 기여자 목록에 카드 추가

만든 파일 이름을 `scripts/contributors.js` 파일에 추가하세요.

`scripts/contributors.js`
```js
const contributorFiles = [
  "<your-github-id>.html", // 여기에 파일 이름을 추가하세요
  "roshanjossey.html",
  "gokultp.html",
];
```

## 웹 브라우저에서 변경 사항 확인

`index.html`을 웹 브라우저에서 열어 변경 사항을 확인할 수 있습니다. 이전 단계에서 추가한 새 카드를 볼 수 있어야 합니다.
카드를 계속 수정하고 웹 브라우저 탭을 새로고침하여 변경 사항을 확인할 수 있습니다.

## 변경 사항 커밋하기

먼저 `git add` 명령으로 변경된 파일을 스테이징 영역에 추가하세요.

```bash
git add contributors/<your-github-id>.html
```

이제 `git commit` 명령으로 변경 사항을 커밋하세요.

```bash
git commit -m "add <your-github-id>"
```

## GitHub에 변경 사항 푸시

```bash
git push -u origin add-<your-github-id>
```

## 검토를 위해 변경 사항 제출

GitHub에서 저장소로 이동하면 `Compare & pull request` 버튼이 표시됩니다. 해당 버튼을 클릭하세요.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

이제 풀 요청(Pull Request)을 제출하세요.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

변경 사항이 병합되면 알림 이메일을 받게 됩니다.
