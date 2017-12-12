# First Contributions

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />
#### *Read this in [other languages](LANGUAGES.md)*


まだ Git をインストールしていない場合は、[ここ](https://help.github.com/articles/set-up-git/) からインストールしてください

## レポジトリをフォーク

Fork ボタンをクリックしてこのレポジトリをフォークしてください

## レポジトリをクローン

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

レポジトリをクローンします。Clone or Download ボタンをクリックしてクリップボードアイコンをクリックしてください。

ターミナルを開いて以下のコマンドを実行してください：

```
git clone "コピーした URL"
```
"コピーした URL" (ダブルクオーテーションは除いてください) をコピーしたレポジトリの URL と置き換えてください。

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

例：
```
git clone https://github.com/＜あなたのユーザー名＞/first-contributions.git
```
`あなたのユーザー名` はご自身の GitHub ユーザー名に置き換えてください。ここでは GitHub のリポジトリの内容をあなたのコンピュータにコピーします。

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

GitHub であなたのリポジトリに行くと、 `Compare & pull request` ボタンが表示されます。そのボタンをクリックしてください。

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

プルリクエストを作ってください：

<img style="float: right;" src="../assets/submit-pull.png" alt="submit pull request" />

## [ 次のステップ ](additional-material/additional-material.md)(日本語じゃないです)


## その他のツールを使用したチュートリアル(日本語じゃないです)

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.microsoft.com/net/images/vslogo.png" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|
