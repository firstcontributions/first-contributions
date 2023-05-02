[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# 最初の貢献度

|<img alt="SourceTree" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-logo.png" width="200">|Atlassian Sourcetree|
|---|---|

難しいですね。初めて何かをするときは、いつも難しいものです。特に共同作業をしているときは、間違いを犯すことは快適なことではありません。しかし、オープンソースは、コラボレーションと協力がすべてです。私たちは、オープンソースの新しい貢献者が初めて学び、貢献する方法を簡素化したいと考えました。

記事を読んだり、チュートリアルを見たりすることは助けになりますが、何も失敗せずに実際にやってみることよりも良いことがあります。このプロジェクトは、新人が最初の貢献をする際のガイダンスを提供し、その方法を簡素化することを目的としています。リラックスしていればいるほど、より良い学習ができることを忘れないでください。もし、あなたが最初の投稿をしようとしているのなら、以下の簡単なステップに従うだけです。私たちは、それが楽しいことを約束します。

## ソースツリー

このチュートリアルはMacOS用ですのでご注意ください。WindowsのSourcetreeと同様ですが、一部異なって見える場合があります。
<!--
	****************************************
	*** This is commented out until      ***
	*** a Windows tutorial can be created***
	****************************************
Please note, this tutorial is for MacOS. Please refer to the [Windows Tutorial]() for Sourcetree if that is what you want to use.
-->

Download [Sourcetree](https://www.sourcetreeapp.com), Install and open it.

Sourcetree」モーダルダイアログが表示されるはずです。

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-1-main.png" alt="SourceTree Main" />

ここから、「Remote」をクリックします。初めてインストールする場合は、まだ GitHub のアカウントに接続していない可能性があります。Connect Button "をクリックしてください。

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-2-main-connect.png" alt="SourceTree Connect" />

Accounts*ダイアログが表示されます。左下の "Add "をクリックします。次に、GitHub（または他の任意のアカウント）をクライアントに追加するための適切な設定を選択します。GitHubの設定を選択した後、"Connect Account "をクリックします。

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-4-accounts-add.png" alt="SourceTree Connect Add" />

ウェブブラウザにページが表示されます。表示された手順に従って、アカウントを認証してください。

## このリポジトリをフォークする

このページの上部にあるフォークボタンをクリックして、このレポをフォークしてください。
<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/fork.png" alt="fork this repository" />
これにより、あなたのアカウントにこのリポジトリのコピーが作成されます。


## リポジトリのクローンを作成する

Sourcetreeで、"Remote "ボタンをクリックします。これで、GitHubに登録されているすべてのGitHubレポが読み込まれる。

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-5-cloning.png" alt="clone this repository" />

クローン」ボタンをクリックすると、いくつかの異なることを定義するための別のビューが表示されます。

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-6-cloning-confirm.png" alt="clone this repository" />

1) **ソースURL:** これは自動的に入力されるので、変更する必要はありません。GitHubのプロジェクトが存在するURLです。

2) **デスティネーションパス:**このプロジェクトが保存されるコンピュータの物理的な場所です。

3) **名称:** これは、Sourcetreeがあなたのプロジェクトを参照する方法の「ブックマーク」です。ショートカットのようなものだと考えてください。
*注：通常、これらのフィールドはデフォルトで問題ありません。
**確認したら、"Clone "をクリックします。**

これで、リポジトリのメインリポジトリブラウザが表示されます！

## ブランチを作成する

ツールバーのブランチボタンをクリックします。

ブランチの名前を "add-your-name-to-contribution "などとします： "add-sally-to-contribution "と名付けます。

そのためには、**ブランチ(1)**をクリックすると、ネーミングダイアログが起動します。次に、先ほど説明したように、**名前を追加する(2)**。最後に、**Create Branch**をクリックします。これで、先ほど命名した内容のブランチが作成されます。

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-7-branching.png" alt="name your branch" />


## 必要な変更を行い、その変更をコミットする

次に、テキストエディタで `Contributors.md` ファイルを開き、あなたの名前と Github URL リンクを追加し、ファイルを保存します。

変更されたファイルを見て確認し、ステージングしたいものを決めることができるはずです。 ステージングは、このコミットに関連づけたいファイルの変更を正確にgitに伝えるために重要です。

*Note: ファイルの diff が表示されない場合は、ダイアログの一番上にある **Uncommitted Files** をクリックしてください*。

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-8-viewing-changed-files.png" alt="edit some file(s)" />

次にダイアログの左上にある「**Commit**」ボタンをクリックします。これで、ステージングエリアが表示されます。

チェックボックス*をクリックして、ステージングエリアにファイルを**追加**します。次に、コミットメッセージを入力します。

*注：スペースバーを使用して、ファイル（ステージング領域と非ステージ領域の両方）を選択し、それぞれの領域からファイルを追加/削除することもできます*。

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-9-committing.png" alt="stage your changes" />


変更点を追加し、コミットメッセージを追加したら、最後に **Commit** ボタンを押してコミットを行います。

おめでとうございます、あなたはfirst-contributionsのあなたのフォークのブランチのあなたのローカルコピーにすべての変更をコミットしました。 先に進みます！


## 変更をGitHubにプッシュする

これで、変更をgithubにプッシュする準備が整いました。これは、フォークしたあなた自身のプロジェクトのコピーにプッシュすることになります。以下の手順で、ブランチをプッシュしてください。まず、**Push (1)**をクリックすると、リモート/プッシュのダイアログが表示されます。**プッシュしたいブランチのチェックボックスをクリックします。OK (3)**を選択すると、Githubにコミットがアップさ れます。

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-10-pushing.png" alt="origin or branch" />

## 変更内容を送信し、レビューを受ける

githubの自分のリポジトリにアクセスすると、「Compare & pull request」ボタンが表示されます。そのボタンをクリックします。

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/compare-and-pull.png" alt="create a pull request" />

では、プルリクエストを送信します。

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/submit-pull-request.png" alt="submit pull request" />
まもなく、あなたの変更点をすべてこのプロジェクトのmasterブランチにマージする予定です。変更がマージされると、通知メールが届きます。

## ここから先はどうすればいいのでしょうか？

おめでとうございます！ あなたは、コントリビューターとしてよく遭遇する、標準的な「フォーク→クローン→編集→PR」のワークフローを完了したところです！

Celebrate your contribution and share it with your friends and followers by going to [web app](https://firstcontributions.github.io/#social-share).

You could join our slack team in case you need any help or have any questions. [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).


### [Additional material](../additional-material/git_workflow_scenarios/additional-material.md)


## 他のツールを使ったチュートリアル
[Back to main page](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
