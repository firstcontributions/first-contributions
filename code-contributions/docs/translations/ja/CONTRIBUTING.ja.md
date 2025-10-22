# 貢献するためのステップ

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="このリポジトリをフォークする" />

## fork ボタンをクリックしてこのリポジトリをフォークする

## このリポジトリのフォークをクローンする。

このリポジトリのフォークで、コードボタンをクリックします。SSHタブを選択し、`copy to clipboard` ボタンをクリックします。

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="このリポジトリをクローンする" />


ターミナルを開き、`git clone` コマンドを実行します。


```bash
git clone "コピーしたURL"
```

> [!IMPORTANT]
> 以下の手順では、`<your-github-id>` と表示されたら、それを自分の GitHub ID に置き換えてください。
> 例えば、あなたの GitHub ID が `aaronsw` の場合、
> git switch -c add-<your-github-id>` は `git switch -c add-aaronsw` となります。
> `contributors/<your-github-id>.html` は `contributors/aaronsw.html` になります。

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="URLをクリップボードにコピーする" />

## ブランチを作成する

リポジトリディレクトリに移動します。

```bash
cd code-contributions
```

`git switch` コマンドでブランチを作成する

```bash
git switch -c add-<your-github-id>
```

## カードの作成

カードをHTMLファイルとしてcontributorsディレクトリに追加することができます。contributorsディレクトリにあなたのユーザー名でファイルを作成します。以下のテンプレートをコピーしてください。

`contributors/<your-github-id>.html`
```html
<article>
  <h3>ユーザー名</h3>
  <p>あなたの略歴（任意）</p>
  <h4>使用しているプログラミング言語</h4>
  <section class="container">
    <div class="badge" style="background-color: #3874a4; color: white">
      Python
    </div>
    <div class="badge" style="background-color: #f7df1e; color: black;">
      JavaScript
    </div>
  </section>

  <h4>使用ツール</h4>
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
## 投稿者リストにカードを追加する

作成したファイル名を `scripts/contributors.js` ファイルに追加する。

`scripts/contributors.js`
```js
const contributorFiles = [
  "<your-github-id>.html", // ファイル名をここに追加する
  "roshanjossey.html",
  "gokultp.html",
];
```

## ウェブブラウザで変更内容を見る

ウェブブラウザで `index.html` を開くと、変更内容を見ることができます。前のステップで追加した新しいカードが見えるはずです。

引き続きカードに変更を加え、ウェブブラウザのタブを更新すると、その変更を見ることができます。

## 変更をコミットする

まず `git add` コマンドで変更をステージします。

```bash
git add contributors/<your-github-id>.html
```

次に `git commit` コマンドで変更をコミットします。

```bash
git commit -m "<あなたのgithub-id>を追加する"
```

## 変更を GitHub にプッシュする

```bash
git push -u origin add-<your-github-id>
```

## 変更内容をレビューに提出する

GitHub の自分のリポジトリに移動すると、`Compare & pull request` というボタンが表示されます。そのボタンをクリックします。

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="プルリクエストを作成する" />

プルリクエストを送信します。

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="プルリクエストの送信" />

変更がマージされると、通知メールが届きます。
