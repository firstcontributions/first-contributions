[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# 最初の貢献度

| <img alt="Visual Studio Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width="40"> | Visual Studio Code |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |


難しいですね。初めて何かをするときは、いつも難しいものです。特に共同作業をしているときは、間違いを犯すことは快適なことではありません。しかし、オープンソースは、コラボレーションと協力がすべてです。私たちは、オープンソースの新しい貢献者が初めて学び、貢献する方法を簡素化したいと考えました。

記事を読んだり、チュートリアルを見たりすることは助けになりますが、何も失敗せずに実際にやってみることよりも良いことがあります。このプロジェクトは、新人が最初の貢献をする際のガイダンスを提供し、その方法を簡素化することを目的としています。リラックスしていればいるほど、より良い学習ができることを忘れないでください。もし、あなたが最初の投稿をしようとしているのなら、以下の簡単なステップに従うだけです。私たちはあなたに約束します、それは楽しいでしょう。

もし、あなたのマシンにVisual Studio Codeがない場合、 [install it](https://code.visualstudio.com/download).

**お知らせ:** このチュートリアルは、Windows 10マシンでVisual Studio Code（バージョン1.27.2）を使用して作成しました。このチュートリアルの後半では、いくつかのキーボードショートカットを使用します。これらは、他のオペレーティングシステム（macOS/Linux）だけでなく、キーボードの言語（UK、DEなど）でも異なる場合があります。コマンドパレットで「ショートカット」と検索すると、ショートカットのリストに目を通すことができます。

## このリポジトリをフォークする

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

このページの右上にあるフォークボタンをクリックして、このレポをフォークしてください。これで、あなたの GitHub アカウントにこのリポジトリのコピーが作成されます。

GitHub は、あなたのレポとフォークしたレポの関係を記録しています。自分のレポは作業コピーと考えることができます。

ほとんどのトップレベルのGitHubリポジトリ（つまり、他のリポジトリからフォークされていないもの）には、直接変更をコミットできる小さなコアチームがあります。他のすべての貢献者は、そのレポをフォークして変更を加え、その変更をトップレベルレポにマージしてもらうために Pull Request を作成する必要があります。トップレベル・リポの管理者がその変更を気に入ればマージされ、あなたはすぐに名声と富を手に入れることができます！この方法については、後で詳しく説明します。

## リポジトリのクローンを作成する

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

次のステップは、変更を開始できるように、あなたのマシンにレポをクローンすることです。VS CodeはリポのURLを必要とするので、コードボタンをクリックし、「クリップボードにコピー」アイコンをクリックします。

**CAREFUL:** 新しい貢献者がよく犯す間違いは、自分のレポをクローンするのではなく、自分がフォークしたレポをクローンすることです。ブラウザのアドレスバーを確認し、自分のレポをクローンしていることを確認してください。

次に、Visual Studio Codeを開いてください。VS Codeのウェルカムページがポップアップします。そこで `F1` を押すと、以下のようなバーが表示されます。テキストフィールドにすでに `>` (greater than) 記号があることに注目してください。また、`CTRL-P` を押して `>` 文字を入力することでも、入力プロンプトを表示することができます。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone.png" alt="Clone Popup (Command Popup)" />

以下のリストに、すでによくわからないコマンドがあることにお気づきでしょうか。これらは、私が最近使ったコマンドです。だから、気にしないでください。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone1.png" alt="Clone repo" />

ここで、`git clone`と入力し、`git`または`clone`だけを入力します（検索のように動作します）。
Git.Clone`というエントリを選択します： Clone` を選択し、`Enter`キーを押します。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone2.png" alt="Paste Repository URL in" />

リポジトリの URL を貼り付けて、`Enter` キーを押します。ファイルエクスプローラーが開き、Git リポジトリを保存する場所を選択できます。

**重要**: 元のリポジトリではなく、フォークされたリポジトリであることを確認してください、そうでない場合は動作しません。
<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone3.png" alt="Status popup" />

Visual Studio Codeの右下にステータスのポップアップが表示されるはずです。終了後、ダイアログのボタンを使ってクローンされたリポジトリ（現在はマシン上のフォルダ）を開くことができます。

## ブランチを作成する

F1`を押して、再びコマンドパレットを開きます。branch`と入力し、そこから`create branch`コマンドを選択します。次のステップでは、新しいブランチの名前を入力します（例：`add-david-kroell`）。Enter キーを押すと、ブランチが作成されます。このブランチはすでにチェックアウトされています。 [What does checkout mean?](https://www.git-scm.com/docs/git-checkout)

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-branch.png" alt="Branches Command Palette" />

## 必要な変更を行う

Open `Contributors.md` and add your name anywhere in the file. This file contains GFM (GitHub Flavored Markdown) which is a proprietary flavor of the <a href="https://en.wikipedia.org/wiki/Markdown">markdown</a> syntax.

他の投稿者&apos;の行をコピーして、自分の名前を入れて修正することで、構文が正しいことを確認します。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-changes.png" alt="Add your name" />

## コミットして変更をGitHubにプッシュする

VS Codeの左側には、5つのアイコンが表示されたメニューがあります。バージョン管理/ソース管理」アイコンを選択します。
(Shortcut : Ctrl + Shift + G)

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-commit.png" alt="Commit changes" />

ファイルエクスプローラーには、最後のコミット以降に変更されたすべてのファイルが表示されます。ファイルをホバーして `+` (プラス) をクリックすると、ファイルがステージングされます。
<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-commit1.png" alt="Stashed Files">

Tエクスプローラー上部の行に何かを入力し、チェックマークを押してください。これで変更がローカルコピーにコミットされました。あとは、変更をGitHubにプッシュバックする必要があります。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-push.png" alt="Stashed Files">

三点アイコンを使ってメニューを開き、`Publish Branch` オプションを選択します。GitHub の認証情報を入力するためのダイアログが表示されます。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-gh-auth.png" alt="Stashed Files">

## 変更内容を送信し、レビューを受ける

この時点で、あなたは変更を完了しましたが、それはまだあなたのリポジトリにしか存在しません。このステップでは、トップレベルのリポの管理者に変更をマージするリクエストを提出する方法を紹介します。

GitHub のあなたのリポジトリに、新しいブランチの通知の隣に `Compare & pull request` というボタンが表示されているはずです。そのボタンをクリックします。

<img src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

では、プルリクエストを送信します。

<img src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

まもなく、あなたの変更点をすべてこのプロジェクトのmasterブランチにマージする予定です。変更がマージされると、通知メールが届きます。

## これからの方向性?

おめでとうございます！あなたは今、貢献者として頻繁に遭遇する標準的な_fork -> clone -> edit -> PR_のワークフローを完了しました！

あなたの貢献を称え、友人やフォロワーと共有しましょう。 [web app](https://firstcontributions.github.io#social-share).

ヘルプが必要な場合や質問がある場合に備えて、slackチームに参加することができます。 [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).


### [Additional material](../additional-material/git_workflow_scenarios/additional-material.md)

## Tutorials Using Other Tools
[Back to main page](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
