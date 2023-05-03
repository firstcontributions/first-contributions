[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# 最初の貢献

|<img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="200">|GitKraken Edition|
|---|---|

難しいですね。初めて何かをするときは、いつも難しいものです。特に共同作業をしているときは、間違いを犯すことは快適なことではありません。しかし、オープンソースは、コラボレーションと協力がすべてです。私たちは、オープンソースの新しい貢献者が初めて学び、貢献する方法を簡素化したいと考えました。

記事を読んだり、チュートリアルを見たりすることは助けになりますが、何も失敗せずに実際にやってみることよりも良いことがあります。このプロジェクトは、新人が最初の貢献をする際のガイダンスを提供し、その方法を簡素化することを目的としています。リラックスしていればいるほど、より良い学習ができることを忘れないでください。もし、あなたが最初の投稿をしようとしているのなら、以下の簡単なステップに従うだけです。私たちはあなたに約束します、それは楽しいでしょう.


##ギット・クラーケン

ダウンロード[GitKraken](https://www.gitkraken.com), インストールして開いてみてください。


Welcome to GitKraken」モーダルダイアログが表示されます - GitHubでサインインし、GitKrakenがGitHubアカウントにアクセスできるようにしましょう。

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-login.png" alt="login to GitHub" />

(オプション)「ファイル」→「環境設定」で、プロジェクトディレクトリをローカルリポジトリのルートに設定します。


## このリポジトリをフォークする

このページの上部にあるフォークボタンをクリックして、このレポをフォークしてください。
<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/fork.png" alt="fork this repository" />
これにより、あなたのアカウントにこのリポジトリのコピーが作成されます。


## リポジトリのクローンを作成する

GitKrakenで、「File」→「Clone Repo」と進みます


<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-clone.png" alt="clone this repository" />


右ペインでGitHub.comを選択します。ユーザー名の下に、first-contributionsが表示されているはずです。 そのリポジトリをクリックし、このペインの下部に表示されているフルパスを確認します。

パスに問題がなければ、「レポをクローンする！」をクリックします。

## ブランチを作成する

ツールバーの分岐ボタンをクリックします。

ブランチに "add-your-name "のような名前を付けます： "add-william-sutton "のように。

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-branch.png" alt="name your branch" />


## 必要な変更を行い、その変更をコミットする

オープンしました `Contributors.md` ファイルをテキストエディタで編集し、名前を付けて保存してください。

GitKraken でリポジトリが開かれていれば、変更があることがわかります。これらの変更をレビューし、ステージアップするには、"// WIP"、変更されたファイルの数、変更の種類でマークされた最新のコミットを選択します。

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-edit.png" alt="edit some file(s)" />

変更されたファイルを確認し、ステージングするファイルを決めます。 ステージングは、このコミットでどのようなファイルを変更したいのかを git に正確に伝えるために重要です。


<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-stage.png" alt="stage your changes" />


良いコミットメッセージが出来たら ("Add <your-name> to Contributors list "は説明的で良いですね）、変更に満足したら、"Stage all changes "を押して、変更されたすべてのファイルをステージングするか、"Stage File "を押して、個々のファイルをステージングすることができます。

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-commit.png" alt="clone this repository" />


もし気が変わったら、その変更点をアンステージすることもできますし、まとめて破棄することも可能です。
警告: 廃棄という言葉が示すように、これは破壊的な操作です。この操作は、あなたがいるリポジトリからの変更が不要な場合のみ行ってください。

コミットを実行します。

おめでとうございます！これで、first-contributionsのフォークのブランチのローカルコピーに、すべての変更をコミットしました。 次に進みます！


## 変更をGitHubにプッシュする

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-push.png" alt="push your changes" />

ツールバーの「Push」ボタンをクリックします。

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-origin.png" alt="origin or branch" />

変更を直接masterブランチに反映させたい場合はoriginブランチで変更を送信し、それ以外の場合はプッシュしたい適切なブランチを選択します。


## 変更内容を送信し、レビューを受ける

githubの自分のリポジトリにアクセスすると  `Compare & pull request`ボタンをクリックします。そのボタンをクリックします。

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/compare-and-pull.png" alt="create a pull request" />

では、プルリクエストを送信します。

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/submit-pull-request.png" alt="submit pull request" />

まもなく、あなたの変更点をすべてこのプロジェクトのmasterブランチにマージする予定です。変更がマージされると、通知メールが届きます。

## ここから先はどうすればいいのでしょうか？

おめでとうございます！ あなたは今、標準を完了しました _fork -> clone -> edit -> PR_ 投稿者としてよく遭遇するワークフロー！
投稿を祝い、友人やフォロワーと共有するために、以下のサイトにアクセスしてください [web app](https://firstcontributions.github.io/#social-share).

何か困ったことや質問がある場合に備えて、スラックチームに参加するのもいいでしょう。 [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).


### [Additional material](../additional-material/git_workflow_scenarios/additional-material.md)


## 他のツールを使ったチュートリアル
[Back to main page](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
