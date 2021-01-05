[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# First Contributions

初めて行うときは苦労します。他人と協力するときは緊張し、できるだけ間違いたくありません。オープンソースの活動では他人との協力が必要です。私たちはオープンソースへの貢献を初めて行う人が、貢献する方法を簡単に学べるようにしたいと考えています。

記事やチュートリアルは役立ちますが、実際に行う方がより身につくでしょう。このプロジェクトはそのガイダンスを行い、初心者がオープンソースへの貢献を簡単に行えるように導きます。
オープンソースへの貢献を初めて行う人は以下のステップに従ってください。

#### *コマンドラインでの操作に慣れていない場合、[GUIツールでチュートリアルを行えます。]( #その他のツールを使用したチュートリアル )*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

まだGitをインストールしていない場合は、[ここ](https://help.github.com/articles/set-up-git/)からインストールしてください。

## リポジトリをフォークする

[**Fork**] ボタンをクリックして、このリポジトリをフォークしてください。
この作業は自分のアカウントに、このリポジトリのコピーを作ります。

## リポジトリをクローンする

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

次にリポジトリを自分のコンピュータにクローンします。[**Clone and download**] ボタンをクリックした後に[**Copy to clipboard**] アイコンをクリックしてください。

ターミナルを開いて以下のgitコマンドを実行してください：

```
git clone "コピーしたURL"
```
"コピーしたURL" は (ダブルクォーテーションを除いた) リポジトリのURLと置き換えてください。

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

例：
```
git clone https://github.com/＜your-name＞/first-contributions.git
```
`your-name` は自分のGitHubユーザー名に置き換えてください。この作業でGitHubのリポジトリが、自分のコンピュータにコピーされます。

## ブランチを作成する

もしリポジトリのディレクトリにいなければ、そこに移動してください。

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
(ブランチ名に*add*を必ず含ませる必要はありませんが、このブランチの目的が自分の名前をリストに加えることであれば含む方が適切です。)

## コードを変更してコミットする

テキストエディタで`Contributors.md`ファイルを開いて自分の名前を追加してください。だたし、リストの先頭や末尾に追加しないでください。名前が連なるリストのどこかの間に追加したら、ファイルを保存します。

<img align="float: right;" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

プロジェクトディレクトリに移動して`git status`を実行すると、変更したファイルを確認できます。`git add`コマンドを使って変更を適用してください。
```
git add Contributors.md
```

次に`git commit`コマンドを使って変更をコミットします。
```
git commit -m "Add <your-name> to Contributors list"
```
`<your-name>`を自分の名前に置き換えてください。

## GitHubに変更をpushする

`git push`コマンドを使って変更をpushしてください。
```
git push origin <ブランチ名>
```
`<ブランチ名>`には先ほど作成したブランチ名を入れてください。

## レビューのためにプルリクエストを送る

GitHub上で自分のリポジトリに行くと、[**Compare & pull request**] ボタンが表示されます。そのボタンをクリックしてください。

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

プルリクエストを作成してください：

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

加えられた変更をmasterブランチにマージします。マージが終了した際にはその旨のメールが送られます。

## 次に何をするべきか

おめでとうございます！  コントリビューターとして重要な _フォーク -> クローン -> 編集 -> プルリクエスト_　の基本的なワークフローが完了しました。

初のオープンソースへの貢献を祝って友達やフォロワーに、[このウェブアプリ](https://roshanjossey.github.io/first-contributions/#social-share)を使ってシェアしましょう。

もし何か質問があるようでしたら[Slack team](https://firstcontributors.slack.com/join/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)に入ってください。

他のプロジェクトへの貢献を始めましょう。簡単なイシューが立てられているプロジェクトのリストを作りました。ウェブアプリで[プロジェクトリスト](https://roshanjossey.github.io/first-contributions/#project-list)を確認してください。

### [追加リソース](../additional-material/git_workflow_scenarios/additional-material.md)

## その他のツールを使用したチュートリアル
|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/Readme/gk-icon.png" width="100"></a>|<a href="../github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|<a href="../sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a>|
|---|---|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|[Visual Studio Code](../github-windows-vs-code-tutorial.md)|[Atlassian Sourcetree](../sourcetree-macos-tutorial.md)|

