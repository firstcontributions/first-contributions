[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# 最初の貢献度

| <img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/9/9c/IntelliJ_IDEA_Icon.svg" width="40"> | IntelliJ IDEA |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |


難しいですね。初めて何かをするときは、いつも難しいものです。特に共同作業をしているときは、間違いを犯すことは快適なことではありません。しかし、オープンソースは、コラボレーションと協力がすべてです。私たちは、オープンソースの新しい貢献者が初めて学び、貢献する方法を簡素化したいと考えました。

記事を読んだり、チュートリアルを見たりすることは助けになりますが、何も失敗せずに実際にやってみることよりも良いことがあります。このプロジェクトは、新人が最初の貢献をする際のガイダンスを提供し、その方法を簡素化することを目的としています。リラックスしていればいるほど、より良い学習ができることを忘れないでください。もしあなたが最初の投稿をしようとしているなら、以下の簡単なステップに従うだけです。きっと楽しくなるはずです。

あなたのマシンにIntelliJ IDEAがない場合、 [install it](https://www.jetbrains.com/idea/download/#section=windows).

**Notice:** このチュートリアルは、Windows 10マシンでIntelliJ IDEA（バージョン2019.3.2）を使用して作成しました。このチュートリアルの後半では、いくつかのキーボードショートカットを利用する予定です。これらは他のオペレーティングシステム（macOS/Linux）で異なる場合があります。

## このリポジトリをフォークする

<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/fork.png" alt="fork this repository" />

このページの右上にあるフォークボタンをクリックして、このレポをフォークしてください。これで、あなたの GitHub アカウントにこのリポジトリのコピーが作成されます。

GitHub は、あなたのレポとフォークしたレポの関係を記録しています。自分のレポは作業コピーと考えることができます。

ほとんどのトップレベルの GitHub リポジトリ（他のリポジトリからフォークされていないもの）には、直接変更をコミットできる小さなコアチームがあります。他のすべての貢献者は、そのレポをフォークして変更を加え、その変更をトップレベルのレポにマージするよう Pull Request を作成する必要があります。トップレベルのレポの管理者が変更を承認すれば、マージされ、あなたはすぐに名声と富を手に入れることができます！この方法については、後で詳しく説明します。

## リポジトリのクローンを作成する

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

次のステップは、変更を開始できるように、あなたのマシンにレポをクローンすることです。IntelliJ IDEAはあなたのリポのURLを必要とするので、「clone」ボタンをクリックし、「copy to clipboard」アイコンをクリックします。

**CAREFUL:** 新しい貢献者がよく犯す間違いの1つは、自分のレポをクローンするのではなく、自分がフォークしたレポをクローンすることです_from_。ブラウザのアドレスバーを確認し、自分のレポをクローンしていることを確認してください。

次に、IntelliJ IDEAを開いてください。

IntelliJ IDEAでは、既存のリポジトリをチェックアウト（Git用語ではclone）して、ダウンロードしたデータをもとに新しいプロジェクトを作成することができます。

メインメニューから「VCS｜バージョン管理から取得」を選択するか、現在プロジェクトが開かれていない場合は、「ようこそ」画面の「バージョン管理から取得」をクリックします。

バージョン管理から取得］ダイアログで、クローンを作成するリモートリポジトリのURLを指定するか（［テスト］をクリックしてリモートへの接続が確立できることを確認できます）、左側にあるVCSホスティングサービスのいずれかを選択します。選択したホスティングサービスにすでにログインしている場合、完了すると、クローンできる利用可能なリポジトリのリストが表示されます。

クローン］をクリックします。クローンしたソースに基づいて IntelliJ IDEA プロジェクトを作成する場合は、確認ダイアログで [はい] をクリックします。Git ルートマッピングがプロジェクトのルートディレクトリに自動的に設定されます。

プロジェクトにサブモジュールが含まれている場合は、サブモジュールもクローンされ、プロジェクトルートとして自動的に登録されます。

**Important**： 重要**：フォークされたリポジトリであることを確認し、元のリポジトリではないことを確認してください。そうでない場合は動作しません。

## ブランチを作成する

Gitでは、ブランチは、例えば、ある機能に取り組む必要があるときや、リリースのためにコードベースのある状態を凍結するときなど、メインの開発ラインから分岐させることができる強力なメカニズムです。

IntelliJ IDEAでは、ブランチに関するすべての操作はGit Branchesポップアップで行われます。これを呼び出すには、ステータスバーのGitウィジェットをクリックするか、Ctrl+Shift+`を押してください。

ステータス・バーのGitウィジェットに、現在チェックアウトされているブランチの名前が表示されます。

ブランチ」ポップアップで、「新規ブランチ」を選択します。

開いたダイアログでブランチ名を指定し、そのブランチに切り替える場合はチェックアウトのブランチ・オプションが選択されていることを確認します。

新しいブランチは、現在のHEADから開始されます。現在のブランチ HEAD ではなく、以前のコミットからブランチを開始したい場合は、バージョン管理ツールのウィンドウ Alt+9 のログタブでこのコミットを選択し、コンテキストメニューから New Branch を選択します。

## 必要な変更を加える
Open `Contributors.md` and add your name anywhere in the file. This file contains GFM (GitHub Flavored Markdown) which is a proprietary flavor of the <a href="https://en.wikipedia.org/wiki/Markdown">markdown</a> syntax.

他の投稿者&apos;の行をコピーして、自分の名前で修正し、構文が正しいかどうか確認します。

コミットして変更をGitHubにプッシュする##。

バージョン管理ツールウィンドウのローカル変更タブで、コミットしたいファイルまたは変更リスト全体を選択します。 Alt+9 と Ctrl+K キーを押すか、ツールバーの Commit Commit ボタンをクリックします。

開いた [変更のコミット] ダイアログには、前回のコミット以降に変更されたすべてのファイルと、新しく追加されたバージョン管理されていないすべてのファイルが表示されます。


意味のあるコミット・メッセージを入力します。

コミットメッセージ履歴 Commit Message history Ctrl+M をクリックすると、最近のコミットメッセージの一覧から選択できます。

コミットをプッシュする前に、コミットメッセージを後で編集することもできます。

Ctrl+Shift+K を押すか、メインメニューから VCS | Git | Push を選びます。プッシュコミットダイアログが開き、すべての Git リポジトリ（複数のリポジトリを持つプロジェクトの場合）が表示され、前回のプッシュ以降に各リポジトリの現在のブランチで行われたすべてのコミットが一覧表示されます。

## 変更をレビューのために提出する

この時点で、あなたは変更を完了しましたが、それはまだあなたのリポジトリにしか存在しません。このステップでは、トップレベルのリポの管理者に変更をマージするリクエストを提出する方法を紹介します。

GitHub のあなたのリポジトリに、新しいブランチの通知の隣に `Compare & pull request` というボタンが表示されているはずです。そのボタンをクリックします。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/compare-and-pull.png" alt="create a pull request" />

では、プルリクエストを送信します。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/submit-pull-request.png" alt="submit pull request" />

Soon I'll be merging all your changes into the master branch of this project. You will get a notification email once the changes have been merged.

## これからどこへ行くのか？

おめでとうございます！あなたは、投稿者としてよく遭遇する、標準的な「フォーク→クローン→編集→PR」のワークフローを完了したところです！

あなたの貢献を称え、友人やフォロワーと共有しましょう。 [web app](https://firstcontributions.github.io#social-share).

You can join our slack team in case you need any help or have any questions. [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).


### [Additional material](../additional-material/git_workflow_scenarios/additional-material.md)

## 他のツールを使ったチュートリアル
[Back to main page](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
