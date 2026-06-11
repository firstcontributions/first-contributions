# First Contributions

初めて何かをするのは大変なことです。特にオープンソースへの貢献は、間違いを恐れたり、不安を感じたりすることが多いでしょう。私たちは、初心者が初めてオープンソースに貢献する方法を簡単に学べるよう、このプロジェクトを作りました。

記事を読んだり、チュートリアル動画を見たりすることも役立ちますが、実際にやってみることほど良い学習方法はありません。このプロジェクトは、初心者が最初の貢献を行うための手順を分かりやすく案内することを目的としています。

初めて貢献する方は、以下の手順に従ってください。

#### *コマンドラインに慣れていない場合は、[GUIツールを使ったチュートリアル](#guiツールを使ったチュートリアル)をご覧ください。*

## このリポジトリをフォークする

このページ上部にある **Fork** ボタンをクリックして、このリポジトリをフォークしてください。

これにより、このリポジトリのコピーがあなたのGitHubアカウントに作成されます。

## リポジトリをクローンする

次に、このリポジトリをあなたのPCにクローンします。

GitHubアカウントでフォークしたリポジトリを開き、**Code** ボタンをクリックし、URLをコピーしてください。

ターミナルを開いて、次のコマンドを実行します。

```bash
git clone "コピーしたURL"
```

ここで「コピーしたURL」は、あなたがフォークしたリポジトリのURLです。

例：

```bash
git clone https://github.com/your-username/first-contributions.git
```

`your-username` の部分はあなたのGitHubユーザー名に置き換えてください。

## ブランチを作成する

リポジトリのディレクトリに移動します。

```bash
cd first-contributions
```

次に、新しいブランチを作成します。

```bash
git checkout -b <新しいブランチ名>
```

例：

```bash
git checkout -b add-taro-yamada
```

ブランチ名に `add` を含める必要はありませんが、目的が分かりやすくなるのでおすすめです。

## 必要な変更を行い、コミットする

テキストエディタで `Contributors.md` ファイルを開き、自分の名前を追加してください。

ファイルの先頭や末尾ではなく、既存の名前一覧の途中に追加してください。

保存した後、ターミナルで以下を実行します。

```bash
git status
```

変更内容が表示されるはずです。

変更をステージングします。

```bash
git add Contributors.md
```

その後、コミットします。

```bash
git commit -m "Add <あなたの名前> to Contributors list"
```

`<あなたの名前>` を実際の名前に置き換えてください。

## GitHubへプッシュする

変更内容をGitHubへプッシュします。

```bash
git push origin <ブランチ名>
```

例：

```bash
git push origin add-taro-yamada
```

## プルリクエストを作成する

GitHub上であなたのフォークしたリポジトリを開くと、

**Compare & pull request**

というボタンが表示されます。

それをクリックしてください。

次に、プルリクエスト（Pull Request）を作成します。

しばらくすると、管理者があなたの変更をメインブランチへマージします。

マージが完了すると、GitHubから通知メールが届きます。

## 次は何をする？

おめでとうございます！

あなたはオープンソースでよく使われる

**Fork → Clone → Edit → Pull Request**

という基本的なワークフローを完了しました。

ぜひあなたの貢献を友人やフォロワーに共有してください。

また、他のオープンソースプロジェクトへの貢献にも挑戦してみましょう。

初心者向けの簡単なIssueをまとめたプロジェクト一覧もあります。

### [追加資料](../additional-material/git_workflow_scenarios/additional-material.md)

## GUIツールを使ったチュートリアル

| ツール | チュートリアル |
|---------|---------------|
| GitHub Desktop | GitHub Desktop チュートリアル |
| Visual Studio 2017 | Visual Studio 2017 チュートリアル |
| GitKraken | GitKraken チュートリアル |
| Visual Studio Code | VS Code チュートリアル |
| Atlassian Sourcetree | Sourcetree チュートリアル |
| IntelliJ IDEA | IntelliJ IDEA チュートリアル |
