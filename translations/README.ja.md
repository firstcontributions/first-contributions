[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# First Contributions

あなたにとって新しいことは難しいかもしれません。特に他の人と協力するとき、間違いを犯すのは楽しいことではありません。しかし、オープンソースでは、協力がすべてです。初めてのオペを簡単にしたい

#### _コマンドラインでの操作に慣れていない場合、[グラフィカルなツールでもチュートリアルを行えます。](#その他のツールを使用したチュートリアル)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

まだ Git をインストールしていない場合は、[ここ](https://help.github.com/articles/set-up-git/)からインストールしてください

## レポジトリをフォーク

[フォーク] ボタンをクリックして、このリポジトリをフォークします。これにより、アカウントにこのリポジトリのコピーが作成されます。

## レポジトリをクローン

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

次にレポジトリをクローンします。*Clone and download*ボタンをクリックした後に*Copy to clipboard*アイコンをクリックしてください。

ターミナルを開いて以下の git コマンドを実行してください：

```
git clone "コピーしたURL"
```

"コピーした URL" (ダブルクオーテーションは除いてください) は先ほどコピーしたレポジトリの URL と置き換えてください。

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

例：

```
git clone https://github.com/＜あなたのユーザー名＞/first-contributions.git
```

`あなたのユーザー名` はご自身の GitHub ユーザー名に置き換えてください。この作業で GitHub のレポジトリの内容はあなたのコンピュータにコピーされました。

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

テキストエディタで`Contributors.md`ファイルを開いてあなたの名前を追加してください。ただし、ファイルの始めや終わりにあなたの名前をつけないようにしましょう。名前リストの間のどこか好きな場所に、あなたの名前を追加するようにしましょう。あなたの名前をファイルに加えたら、ファイルを保存します。

<img align="float: right;" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

プロジェクトディレクトリに移動して`git status`を実行すると、変更がなされたことが確認できると思います。`git add`コマンドを使ってそれらの変更を適用してください。

```
git add Contributors.md
```

次に`git commit`コマンドを使ってこれらの変更をコミットします。

```
git commit -m "Add <あなたの名前> to Contributors list"
```

`<あなたの名前>`をご自身の名前に置き換えてください。

## GitHub に変更を push する

`git push`コマンドを使って変更を push してください。

```
git push origin <ブランチ名>
```

`<ブランチ名>`には先ほど作成したブランチ名を入れてください。

## レビューのためにプルリクエストを送る

GitHub 上であなたのリポジトリに行くと、`Compare & pull request`ボタンが表示されます。そのボタンをクリックしてください。

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

プルリクエストを作ってください：

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

加えた変更をすぐにマスターブランチにマージします。マージが完了すると、メールが届きます。

## 次に何をするべきか

おめでとうございます！ コントリビューターとして重要な *フォーク -> クローン -> 編集 -> プルリクエスト*　の基本的なワークフローが完了しました。

初のオープンソースへの貢献を祝って友達やフォロワーにそのことを[このウェブアプリ](https://roshanjossey.github.io/first-contributions/#social-share)を使ってシェアしましょう。

もし何かしら質問があるようでしたら[私たちの Slack team](https://firstcontributors.slack.com/join/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)に入ってください。

他のプロジェクトへの貢献を始めましょう。簡単なイシューが立てられているプロジェクトのリストを作りました。ウェブアプリで[プロジェクトリスト](https://roshanjossey.github.io/first-contributions/#project-list)を確認て見てください。

### [追加リソース](../additional-material/git_workflow_scenarios/additional-material.md)

## その他のツールを使用したチュートリアル

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |
