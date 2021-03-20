[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# 初めてのコントリビュート

| <img alt="Visual Studio Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width="40"> | Visual Studio Code |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |

最初は何事も難しいもの。共同作業をしているときはなおのこと、些細なミスも居心地悪く感じてしまうもの。

しかしながら、オープンソースはコラボレーションと共同作業で成り立っています。そこで私たちは、新しいオープンソース・コントリビュータが初めてコントリビュートするときに、シンプルに学べるようにしたいしたいと考えました。

記事を読んだりチュートリアルを見たりすることも助けになりますが、何よりも実際にやってみるのが一番。

このプロジェクトは、新人コントリビュータのためにガイダンスを提供し、簡単な手順を通してはじめの一歩を踏み出してもらうことを目的としています。リラックスして進めることで、より良い学習ができます。もしあなたが最初のコントリビュートをしたいのであれば、以下の簡単なステップに従ってください。きっと楽しいものになるでしょう。

もし、まだ Visual Studio Code をインストールしていない場合は[ここからインストール](https://code.visualstudio.com/download)してください。

**注意:** このチュートリアルは、Windows 10 上で Visual Studio Code（バージョン 1.27.2）を使用することを想定しています。チュートリアルの後半でキーボードショートカットをいくつか使用します。これらは他の OS(macOS/Linux)では異なる場合があります。

## リポジトリをフォーク

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Fork ボタンをクリックしてこのリポジトリをフォークしてください。あなたの GitHub アカウントにこのリポジトリのコピーが作成されます。

GitHub は、あなたのリポジトリとフォーク元のリポジトリとの関係を記録しています。フォーク後のあなたのリポジトリは作業コピーとして考えることができます。

GitHub のトップレベルのリポジトリ (他のリポジトリからフォークされていないもの) のほとんどには、変更を直接コミットできる少人数のコアチームがいます。それ以外のコントリビュータは、そのレポをフォークして変更を加えた後で Pull Request を作成し、自分の変更をトップレベルのリポジトリにマージしてもらう必要があります。トップレベルリポジトリの管理者がその変更を気に入ればマージされ、あなたは瞬く間に富と名声を得ることになります！　その方法については後ほど。

## リポジトリをクローン

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

次に、リポジトリを自分のマシンにクローンして、変更を始められるようにしていきます。VS Code はあなたのリポジトリの URL を必要とするので、 `clone` ボタンをクリックし、 `copy to clipboard` アイコンをクリックしてください。

**注意：** 新人コントリビュータのありがちな間違いに、自分のリポジトリではなくフォーク元のリポジトリをクローンしてしまうというものがあります。ブラウザのアドレスバーをチェックして、自分のリポジトリをクローンしていることを確認してください。

では、Visual Studio Code を起動しましょう。VS Code のウェルカムページが表示されます。そこから `F1` を押すと、以下のようなバーが表示されます。テキストフィールドにはすでに `>`（大なり）の記号が入っていることに注意してください。また、`CTRL-P` を押して入力プロンプトを表示し、`>` 文字を入力することもできます。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone.png" alt="Clone Popup (Command Popup)" />

画像にはリスト上にいくつかコマンドがならんでいますが、これらは私が最近使ったコマンドです。気にしないでください。


<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone1.png" alt="Clone repo" />

ここで、 `git clone` と入力します。 `git` または `clone` とだけ入力しても OK です（候補がでてきます）。
リストから `Git: Clone` を選択して、 `Enter` を押します。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone2.png" alt="Paste Repository URL in" />

リポジトリの URL を貼り付けて、 `Enter` キーを押します。すると、Git リポジトリの保存先を選択する画面が出てきます。

**重要** フォーク元のオリジナルなリポジトリではなく、フォークされたあなたのリポジトリであることを確認してください。でないと動きません。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone3.png" alt="Status popup" />

Visual Studio Code の右下に、ポップアップでステータスが表示されます。完了したら、ダイアログ内のボタンを使ってクローンされたリポジトリ（リポジトリを保存したフォルダ）を開くことができます。

## ブランチを作成

`F1` を押して、再びコマンドパレットを開きます。そこで `branch` と入力し `create branch` コマンドを選択します。

次に新しいブランチの名前を入力します。例えば、 `add-david-kroell` と入力します。Enter キーを押すと、ブランチが作成されます。また、このブランチはすでにチェックアウトされています（※ [What does checkout mean? (checkoutとは)](https://www.git-scm.com/docs/git-checkout)）

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-branch.png" alt="Branches Command Palette" />

## コードを変更

`Contributors.md` を開き、ファイル内の任意の場所に自分の名前を追加します。このファイルには、<a href="https://en.wikipedia.org/wiki/Markdown">markdown</a>構文の派生である GFM（GitHub Flavored Markdown）が含まれています。

他のコントリビュータの行をコピーして、自分の名前を書き加えてください。構文が正しいかどうかも確認してくださいね。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-changes.png" alt="Add your name" />

## 変更をコミットして、GitHubに変更をpushする

VS Code の左側には、5 つのアイコンが表示されたメニューがあります。 `version control/Source Control` アイコンを選択します。
(ショートカット：Ctrl + Shift + G)

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-commit.png" alt="Commit changes" />

ファイルエクスプローラには、前回のコミット後に変更されたすべてのファイルが表示されます。ファイルにカーソルを合わせて、`+`（プラス）をクリックすると、ファイルがステージングエリアに移動します。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-commit1.png" alt="Stashed Files">

エクスプローラの上にある入力欄に何かしら入力し、チェックマークを押してください。これで、変更があなたのローカルコピーにコミットされました。今度は、その変更を GitHub にプッシュしなければなりません。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-push.png" alt="Stashed Files">

`…`（3 点リーダー）アイコンを使ってメニューを開き、 `Publish Branch` オプションを選択します。すると、GitHub の認証情報を入力するためのダイアログが表示されますのでログインしましょう。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-gh-auth.png" alt="Stashed Files">

## レビューのためにプルリクエストを送る

この時点でファイルの変更が完了しましたが、それはまだあなたのリポジトリにしか反映されてません。続いて、トップレベルのリポジトリの管理者に変更のマージを依頼する方法を説明します。

GitHub 上の自分のリポジトリで、新しいブランチの通知の横に `Compare & pull request` ボタンが表示されています。そのボタンをクリックしましょう。

<img src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

それでは、プルリクエストを送信しましょう。

<img src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

しばらくすると、あなたの変更点をすべてこのプロジェクトの master ブランチにマージされます。変更がマージされたときにはメールで通知されます。

## 次に何をすれば？

おめでとうございます。これであなたは、コントリビューターとして重要な _フォーク -> クローン -> 編集 -> プルリクエスト_ の基本的なワークフローを完了しました!

初のオープンソースへの貢献を祝ってこの[ウェブアプリ](https://firstcontributions.github.io#social-share) で、友人やフォロワーと共有してください。

ヘルプが必要な場合や質問がある場合は、slack チームに参加できます。[Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)をご覧ください。

### [追加リソース](../../additional-material/git_workflow_scenarios/additional-material.md)

## その他のツールを使用したチュートリアル
[日本語チュートリアルにもどる](https://github.com/firstcontributions/first-contributions/blob/master/translations/README.ja.md#その他のツールを使用したチュートリアル)
