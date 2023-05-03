[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# 最初の貢献

|<img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Visual_Studio_2017_logo_and_wordmark.svg/2000px-Visual_Studio_2017_logo_and_wordmark.svg.png" width="200">|Visual Studio 2017 Edition|
|---|---|

難しいですね。初めて何かをするときは、いつも難しいものです。特に共同作業をしているときは、間違いを犯すことは快適なことではありません。しかし、オープンソースは、コラボレーションと協力がすべてです。私たちは、オープンソースの新しい貢献者が初めて学び、貢献する方法を簡素化したいと考えました。

記事を読んだり、チュートリアルを見たりすることは助けになりますが、何も失敗せずに実際にやってみることよりも良いことがあります。このプロジェクトは、新人が最初の貢献をする際のガイダンスを提供し、その方法を簡素化することを目的としています。リラックスしていればいるほど、より良い学習ができることを忘れないでください。もし、あなたが最初の投稿をしようとしているのなら、以下の簡単なステップに従うだけです。きっと楽しくなるはずです。

マシンにVisual Studio 2017がない場合、 [install it](https://www.visualstudio.com/downloads/).

## このリポジトリをフォークする

<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/fork.png" alt="fork this repository" />

このページの上部にあるフォークボタンをクリックして、このリポジトリをフォークしてください。これで、あなたの GitHub アカウントにこのリポジトリのコピーが作成されます。

GitHub は、あなたのレポとフォークしたレポの関係を記録しています。 あなたのレポは作業コピーと考えることができます。

ほとんどのトップレベルの GitHub リポジトリ（他のリポジトリからフォークされていないもの）には、直接変更をコミットできる小さなコアチームがあります。 他のすべての貢献者は、そのレポをフォークして変更を加え、その変更をトップレベルレポにマージしてもらうために Pull Request を作成する必要があります。トップレベル・リポの管理者がその変更を気に入ればマージされ、あなたはすぐに名声と富を手に入れることができます！ この方法については、後で詳しく説明します。

## リポジトリのクローンを作成する

<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/clone.png" alt="clone this repository" />

次のステップは、変更を開始できるように、あなたのマシンにレポをクローンすることです。Visual StudioはリポジトリのURLを必要とするので、「clone」ボタンをクリックし、「copy to clipboard」アイコンをクリックします。

**CAREFUL:** 新しい貢献者がよく犯す間違いの1つは、自分のレポをクローンするのではなく、フォークしたレポを*から*クローンすることです。 ブラウザのアドレスバーを確認し、自分のレポをクローンしていることを確認してください。

いよいよVisual Studio 2017に飛び込むときが来ました！ このチュートリアルの大半は、チームエクスプローラー・タブで作業することになります。 デフォルトで開かれていない場合は `View > Team Explorer` それを開くには.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-01-clone1.png" alt="Team Explorer" />

Team Explorerには多くのビューがあり、上部にナビゲーションボタンが配置されているので、さまざまなエリアを見つけることができます。 レポをクローンするには、Connect ビューを表示する必要があります（デフォルトのビュー）。 クローン」ボタンが表示されない場合は、上部にある緑色のプラグをクリックします。

をクリックします。 `Clone` オプションで **Local Git Repositories** をクリックし、テキストボックスにあなたのリポのURLを貼り付けます。 これは、以前にGitHubからクリップボードにコピーしたURLである必要があります。

をクリックします。 `Clone`ボタンをクリックして、処理を開始します

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-02-clone2.png" alt="Clone repo" />

プロセスが完了すると、ソリューションエクスプローラタブに移動し、リポジトリの内容を確認することができます。 あなたのリポは、物事が変化するため、以下のスクリーンショットとは異なるように見えるでしょう！

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-03-clone3.png" alt="Solution Explorer" />

## ブランチを作成する

Team Explorerタブに戻り、メインナビゲーションドロップダウンで「Branches」ビューを開きます。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-04-branch1.png" alt="Branches view" />

が表示されるはずです。 **first-contributions** というレポと、デフォルトのブランチがあります。 `master`.  を右クリックします。 `master`を選んでください。 `New Local Branch From...`.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-05-branch2.png" alt="New branch" />

ブランチには次のような名前を付けます。 `add-<your_name_here>`,といった具合に： `add-alonzo-church`.

を残す。`Checkout branch` ボックスをチェックし `Create Branch` ボタンをクリックします。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-06-branch3.png" alt="Create branch" />

リストに新しいブランチが表示されるはずです。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-07-branch4.png" alt="See new branch" />

## 必要な変更を行う

オープン`Contributors.md` を作成し、リストの末尾に自分の名前を追加します。このファイルには、GFM (GitHub Flavored Markdown) が含まれています。 <a href="https://en.wikipedia.org/wiki/Markdown">markdown</a> のシンタックスになります。

他の投稿者をコピーする&apos; の行に自分の名前を入れて修正し、構文が正しいかどうかを確認します（うるさいかもしれません）。
<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-08-change1.png" alt="Add your name" />

## コミットして変更をGitHubにプッシュする

チームエクスプローラーに戻り、「変更」ビューに移動します。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-09-commit1.png" alt="Changes" />

コミットで投稿したい情報を入力し、クリックします。 `Save`. Visual Studioは、今後のコミットのためにそれを記憶しておきます。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-10-commit2.png" alt="Git user information" />

**NOTE:** Visual Studioでは、以下のような隠しフォルダを使用します。 `.vs` は、個人的な設定や好みを保存するためのものです。 このフォルダの内容 **should not be saved in Git**.
まだ無視されていない場合は、Git にこのフォルダを無視するように指示して、レポに送信しないようにする必要があるかもしれません。

このフォルダはこのレポではすでに無視されているので、この手順を実行する必要はないでしょう。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-11-commit3.png" alt="Ignore vs folder" />

これで、変更されたファイルのリストと、コミットコメントを入力するためのテキストボックスが表示されるはずです。 コメントは簡潔でありながら徹底したものであるべきです。 コミットコメントを読んでいて、これを見ることほど嫌なことはありません： `"I updated some stuff"`. 数秒かけて、コミットの概要を説明しましょう。 チームは後であなたに感謝するでしょうし、あなた自身も感謝するかもしれません！

クリック`Commit All and Push` を使えば、ローカルコミットを実行し、変更をリポジトリにプッシュする作業を一度に行うことができます。

**NOTE:** CommitはPushとは別に実行することができます。 ここでは便宜上両方行うことにします。Commit はローカルに変更を記録しますが、Push するまで GitHub リポジトリに反映されません。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-12-commit4.png" alt="Commit and Push" />

GitHub に初めてアクセスしたとき、Visual Studio は GitHub の認証情報を要求します。 この情報はキャッシュされるので、頻繁に表示されるわけではありません。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-13-commit5.png" alt="Login" />

Push操作が完了したら、GitHubで自分のリポジトリを開くと、最近Pushされたブランチを示すメッセージが表示されるはずです。

を開くと、変更内容を確認することができます。 `Branch: master`をクリックし、新しいブランチを選択します。おめでとうございます！ブランチのURLを世界中と共有することで、あなたの進歩を示すことができます！

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/vs2017-14-commit6.png" alt="View pushed branch on GitHub" />

## 変更内容を送信し、レビューを受ける

この時点で、あなたは変更を完了しましたが、それはまだあなたのリポジトリにしか存在しません。 このステップでは、トップレベルのレポの管理者に変更をマージするリクエストを提出する方法を紹介します

GitHub上のあなたのレポには、以下のように表示されています。 `Compare & pull request` のボタンが、新店舗のお知らせの横にあります。そのボタンをクリックする.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/compare-and-pull.png" alt="create a pull request" />

では、プルリクエストを送信します。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs2017-tutorial/submit-pull-request.png" alt="submit pull request" />

まもなく、あなたの変更点をすべてこのプロジェクトのmasterブランチにマージする予定です。変更がマージされると、通知メールが届きます。

## ここから先はどうすればいいのでしょうか？

おめでとうございます！ あなたは今、標準を完了しました _fork -> clone -> edit -> PR_ 投稿者としてよく遭遇するワークフロー！

投稿を祝い、友人やフォロワーと共有するために、以下のサイトにアクセスしてください。[web app](https://firstcontributions.github.io#social-share).

You can join our slack team in case you need any help or have any questions. [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).


### [Additional material](../additional-material/git_workflow_scenarios/additional-material.md)

## 他のツールを使ったチュートリアル
[Back to main page](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
