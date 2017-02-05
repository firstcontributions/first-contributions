# First Contributions

<img align="right" width="300" src="assets/fork.png" alt="fork this repository" />

*Read this in other languages: [英語](README.md), [スペイン語](README.es.md), [オランダ語](README.nl.md), [ヒンディー語](README.hi.md)　[ロシア語](README.ru.md)*

まだ Git をインストールしていない場合は、[ここ](https://help.github.com/articles/set-up-git/) からインストールしてください

## レポジトリをフォーク

Fork ボタンをクリックしてこのレポジトリをフォークしてください

## レポジトリをクローン

<img align="right" width="300" src="assets/clone.png" alt="clone this repository" />

レポジトリをクローンします。Clone or Download ボタンをクリックしてクリップボードアイコンをクリックしてください。

ターミナルを開いて以下のコマンドを実行してください：

```
git clone "コピーした URL"
```
"コピーした URL" (ダブルクオーテーションは除いてください) をコピーしたレポジトリの URL と置き換えてください。

<img align="right" width="300" src="assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

例：
```
git clone https://github.com/＜あなたのユーザー名＞/first-contributions.git
```
'あなたのユーザー名' はご自身の GitHub ユーザー名に置き換えてください。ここでは GitHub のリポジトリの内容をあなたのコンピュータにコピーします。

## ブランチを作成

もしレポジトリのディレクトリにいなければそこまで移動してください。

```
cd first-contributions
```
`git checkout command`　コマンドを使用してブランチを作成します：
```
git checkout -b <add-your-name>
```

例:
```
git checkout -b add-alonzo-church
```

## コードを変更してその変更をコミット

テキストエディタで `Contributors.md` ファイルを開いてあなたの名前を追加し、ファイルを保存します。プロジェクトディレクトリに移動して `git status` を実行すると、変更があることがわかります。以下の `git add` コマンドを使ってそれらの変更を適用してください。
```
git add Contributors.md
```


以下の `git commit`コマンドを使ってこれらの変更をコミットします。
```
git commit -m "Add <あなたの名前> to Contributors list"
```
`<あなたの名前>` をご自身の名前に置き換えてください

## GitHub に変更を push する

`git push` コマンドを使って変更を push してください
```
git push origin <ブランチ名>
```
`<ブランチ名>` を先程作ったブランチ名にへんこうしてください

## レビューのためにプルリクエストを送る

GitHub であなたのリポジトリに行くと、 `Compare＆pull request` ボタンが表示されます。そのボタンをクリックしてください。

<img style="float: right;" src="assets/compare-and-pull.png" alt="create a pull request" />

プルリクエストを作ってください：

<img style="float: right;" src="assets/submit-pull.png" alt="submit pull request" />

## ォークしたレポジトリと元のレポジトリを同期させる

今、私はこのプロジェクトの master ブランチにすべての変更をマージしています。しかしあなたのフォークしたレポジトリにはどのような変更は加えられていません。あなたのフォークしたレポジトリと元のレポジトリとの変更を同期させるために、私のレポジトリのURLを「上流のリモート URL 」として追加する必要があります：
```
git remote add upstream https://github.com/multunus/first-contributions
```
これは、指定された URL にこのプロジェクトの別のバージョンが存在することを Git に伝える方法で、これを upstream と呼んでいます。変更がマージされたら、新しいバージョンのリポジトリを取得します。
```
git fetch upstream
```


ここで私のフォークレポジトリ（上流のリモート）のすべての変更を取得しています。今度は、新しいリポジトリのリビジョンを master ブランチにマージする必要があります。
```
git rebase upstream/master
```

ここでは、取得したすべての変更を master ブランチに適用します。master ブランチを押した場合、フォークにも変更が加えられます
```
git push origin master
```
ここでは remote に移動していることに注目してください

## 次のステップ

初心者向けの不具合を [contributor.ninja](https://contributor.ninja) 見つけられます。

ここでは、人気のあるレポジトリにいくつかの初心者レベルの不具合がまとめてあります。レポジトリにアクセスして詳細を調べてみてください：

|[![exercism](https://avatars2.githubusercontent.com/u/5624255?v=3&s=100)](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[![fun-retro](https://avatars3.githubusercontent.com/u/15913975?v=3&s=100)](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[<img width="100" src="https://cdn.worldvectorlogo.com/logos/react.svg">](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[![habitat](https://avatars1.githubusercontent.com/u/18171698?v=3&s=100)](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![scikit-learn](https://avatars0.githubusercontent.com/u/365630?v=3&s=100)](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[<img width="100" src="https://camo.githubusercontent.com/0f302c808c8457f6460913e33aed3478124612c2/687474703a2f2f6c65696e696e67656e2e6f72672f696d672f6c65696e696e67656e2e6a7067">](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[<img width="100" src="https://images.plot.ly/plotly-documentation/thumbnail/numpy-logo.jpg">](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[![elasticsearch](https://avatars2.githubusercontent.com/u/6764390?v=3&s=100)](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|---|---|---|---|---|---|---|---|
|[exercism](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[Fun Retros](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[react](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[habitat](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[scikit-learn](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[Leiningen](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[numpy](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[elasticsearch](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|[![homebrew](https://avatars2.githubusercontent.com/u/1503512?v=3&s=100)](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[![rust](https://avatars1.githubusercontent.com/u/5430905?v=3&s=100)](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[![vuejs](https://avatars1.githubusercontent.com/u/6128107?v=3&s=100)](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[![Suave](https://avatars2.githubusercontent.com/u/5822862?v=3&s=100)](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[![OpenRA](https://avatars3.githubusercontent.com/u/409046?v=3&s=100)](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![PowerShell](https://avatars0.githubusercontent.com/u/11524380?v=3&s=100)](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[![coala](https://avatars2.githubusercontent.com/u/10620750?v=3&s=100)](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[![moment](https://avatars2.githubusercontent.com/u/4129662?v=3&s=100)](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[homebrew](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[Rust](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[vuejs](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[Suave](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[OpenRA](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[PowerShell](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[coala](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[moment](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[![ava](https://avatars0.githubusercontent.com/u/8527916?v=3&s=100)](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[![freeCodeCamp](https://avatars0.githubusercontent.com/u/9892522?v=3&s=100)](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![webpack](https://avatars3.githubusercontent.com/u/2105791?v=3&s=100)](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[![hoodie](https://avatars1.githubusercontent.com/u/1888826?v=3&s=100)](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![pouchdb](https://avatars3.githubusercontent.com/u/3406112?v=3&s=100)](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[![neovim](https://avatars0.githubusercontent.com/u/6471485?v=3&s=100)](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[![babel](https://avatars2.githubusercontent.com/u/9637642?v=3&s=100)](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[<img width="100" src="https://github.com/adobe/brackets/blob/gh-pages/images/brackets_128.png?raw=true">](https://github.com/adobe/brackets/labels/Starter%20bug)|
|[ava](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[webpack](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[hoodie](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[pouchdb](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[neovim](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[babel](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[brackets](https://github.com/adobe/brackets/labels/Starter%20bug)|
| [![Node.js](https://avatars1.githubusercontent.com/u/9950313?v=3&s=100)](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|[<img width="100" src="https://github.com/Semantic-Org/Semantic-UI-React/raw/master/docs/app/logo.png">](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|
| [Node.js](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |[Semantic-UI-React](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |
