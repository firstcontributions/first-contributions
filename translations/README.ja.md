[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# First Contributions

初めてのことは何でも大変なものです。特に他人と協力する時はそうで、間違うのは気持ちの良いことではありません。しかし、オープンソースにおける活動では協力することが全てです。私たちは初めてオープンソースへの貢献を始める人たちが簡単に貢献する方法を学べるようにしたいと考えています。

記事を読んだりチュートリアルをやってみることはためになりますが、実際にやってみる方が良いでしょう。このプロジェクトはそのガイダンスを行い、初心者が最初のオープンソースへの貢献を簡単に行えるようにするためのものです。
覚えておいてください: リラックスしているほどより良く学ぶことができます。もし初めてのオープンソースへの貢献を行いたいのなら以下の簡単なステップに従ってください。それはとても面白いものになるはずです。

#### *コマンドラインでの操作に慣れていない場合、[グラフィカルなツールでもチュートリアルを行えます。]( #その他のツールを使用したチュートリアル )*

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

まだGitをインストールしていない場合は、[ここ](https://help.github.com/articles/set-up-git/)からインストールしてください

## レポジトリをフォーク

Forkボタンをクリックしてこのレポジトリをフォークしてください。
この作業はあなたのアカウントにこのレポジトリのコピーを作ります。

## レポジトリをクローン

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

次にレポジトリをクローンします。*Clone and download*ボタンをクリックした後に*Copy to clipboard*アイコンをクリックしてください。

ターミナルを開いて以下のgitコマンドを実行してください：

```
git clone "コピーしたURL"
```
"コピーしたURL" (ダブルクオーテーションは除いてください) は先ほどコピーしたレポジトリのURLと置き換えてください。

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

例：
```
git clone https://github.com/＜あなたのユーザー名＞/first-contributions.git
```
`あなたのユーザー名` はご自身のGitHubユーザー名に置き換えてください。この作業でGitHub のリポジトリの内容はあなたのコンピュータにコピーされました。

## ブランチを作成

もしレポジトリのディレクトリにいなければそこまで移動してください。

```
cd first-contributions
```
`git checkout` コマンドを使用してブランチを作成します：
```
git checkout -b <add-your-name>
```

例:
```
git checkout -b add-alonzo-church
```
(ブランチの名前には必ずしも*add*が含まれていなければならないわけではありませんが、このブランチの目的があなたの名前をリストに加えることであることを考慮すれば含むのが適切です。)

## コードを変更してその変更をコミット

テキストエディタで`Contributors.md`ファイルを開いてあなたの名前を追加し、ファイルを保存します。プロジェクトディレクトリに移動して`git status`を実行すると、変更がなされたことが確認できると思います。`git add`コマンドを使ってそれらの変更を適用してください。
```
git add Contributors.md
```

次に`git commit`コマンドを使ってこれらの変更をコミットします。
```
git commit -m "Add <あなたの名前> to Contributors list"
```
`<あなたの名前>`をご自身の名前に置き換えてください。

## GitHubに変更をpushする

`git push`コマンドを使って変更をpushしてください。
```
git push origin <ブランチ名>
```
`<ブランチ名>`には先ほど作成したブランチ名を入れてください。

## レビューのためにプルリクエストを送る

GitHub上であなたのリポジトリに行くと、`Compare & pull request`ボタンが表示されます。そのボタンをクリックしてください。

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

プルリクエストを作ってください：

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />

すぐに私が加えられた変更をmasterブランチにマージします。マージが終了した際にはその旨のメールが送られます。

## 次に何をするべきか

初のオープンソースへの貢献を祝って友達やフォロワーにそのことを[このウェブアプリ](https://roshanjossey.github.io/first-contributions/#social-share)を使ってシェアしましょう。

もし何かしら質問があるようでしたら[私たちのSlack team](https://firstcontributors.slack.com/join/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)に入ってください。

他のプロジェクトへの貢献を始めましょう。簡単なイシューが立てられているプロジェクトのリストを作りました。ウェブアプリで[プロジェクトリスト](https://roshanjossey.github.io/first-contributions/#project-list)を確認て見てください。

### [追加リソース](../additional-material/git_workflow_scenarios/additional-material.md)

## その他のツールを使用したチュートリアル
|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="../assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

# 宣伝
このプロジェクトがお気に召しましたら[Github](https://github.com/Roshanjossey/first-contributions)上でstarしてくださると幸いです。特にお気に召した場合には[Twitter](https://twitter.com/sudo__bangbang)上や[GitHub](https://github.com/roshanjossey)などで
[Roshan](https://roshanjossey.github.io/)をフォローしてくださると幸いです。
