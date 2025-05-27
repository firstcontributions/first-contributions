[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)

# 第一次參與開源

萬事起頭難。尤其係同其他人合作時，犯錯會令人特別唔自在。不過，開源嘅本質就係同人一齊合作。我哋希望為新手提供一個簡單嘅方法，去學習同參與開源項目。

睇文章同睇教學當然有幫助。但係，有咩方法會比喺唔會搞亂嘢嘅情況下親手去做更好呢？呢個項目旨在指導新手同簡化新手參與開源嘅方式。記住：過程越輕鬆，學習效果就越好。如果您想作出第一次貢獻，只需要跟住以下簡單步驟去做就得。向您保證，呢個過程會好有趣 :)

#### *如果你唔鍾意用指令列，[呢度有使用圖形界面工具嘅教學。]( #使用其他工具的教學)*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

如果你嘅電腦上未安裝 git，請按照呢個[安裝指引（英文）](https://help.github.com/articles/set-up-git/)進行安裝。

## 分叉（Fork）本代碼庫

喺圖示入面撳「Fork」呢個掣嚟分叉呢個 Git 儲存庫。
呢個操作會將儲存庫複製到你嘅 GitHub 帳號下面。

## 複製（Clone）代碼庫

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

跟住落嚟，將複製後嘅儲存庫複製到你/妳嘅電腦上。喺圖示入面揀綠色按鈕，然後再揀「複製到剪貼簿」按鈕（將儲存庫地址複製落嚟）

之後開啟命令列視窗，輸入以下 git 指令：

```bash
git clone "url you just copied"
```
"url you just copied"（唔要雙引號）將複製到你帳戶名下嘅儲存庫地址。取得呢個鏈接地址嘅方法請睇上一步。

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

例如：
```bash
git clone https://github.com/<this-is-you>/first-contributions.git
```

'this-is-you' 指的就是你嘅 GitHub 用戶名。呢一步會將你嘅 first-contributions 儲存庫複製到您嘅電腦上。

## 新建一個分支

以下嘅命令可以喺命令列視窗中，將目錄切換到 first-contributions。

```bash
cd first-contributions
```
跟住落嚟用 git switch 命令建立一個新嘅程式碼分支，請喺命令列視窗輸入以下命令：
```bash
git switch -c <add-your-name>
```

例如：
```bash
git switch -c add-david
```

（新分支嘅名稱唔一定需要有 *add*。不過，喺呢個新分支嘅名稱加入 *add* 係一個合理嘅做法，因為呢個分支嘅目的係將您嘅名字添加到貢獻者列表中。）

## 對程式碼進行修改，跟住提交 (Commit) 修改

用你鍾意嘅文字編輯器打開 `Contributors.md` 這個文件，更新文件內容，將您嘅名加進去，然後存檔。喺命令視窗度執行 `git status`，佢會列出被更改嘅檔案。跟住你可以用 `git add` 呢個指令，將更改嘅項目加到分支度，好似下面呢條命令咁。

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

```bash
git add Contributors.md
```

而家你就可以用 `git commit` 呢個指令，去 commit（提交）你嘅修改啦。
```bash
git commit -m "Add <your-name> to Contributors list"
```
將 `<your-name>` 換做自己個名

## 將更新發佈（Push）到 GitHub

用 `git push` 命令發佈代碼
```bash
git push origin <add-your-name>
```
將 `<add-your-name>` 換做你啱啱新建嗰個分支個名。

<details>
<summary> <strong>如果喺 push（發佈）嘅時候出現 error（錯誤），請撳呢度</strong> </summary>

- ### Authentication Error
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  去 [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) 學習點樣生成新嘅 SSH 密匙同埋點樣設定。

</details>

## 提出 Pull Request 將你嘅修改畀其他人審閱

去返你之前 fork 嘅 GitHub 儲存庫，會見到一個 `Compare & pull request` 嘅掣，撳落去嗰個掣。

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

跟住再撳 `Create pull request` 嗰個掣，就正式遞交 pull request 啦。

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

過唔耐，如果你改嘅檔案同原本冇衝突，我哋會將所有改動合併去呢個項目嘅主分支。
合併完成之後，你會收到通知 email。

## 咁之後要做咩呀？

喺[呢個網站](https://firstcontributions.github.io/#social-share) 慶祝你的成就並跟朋友同追隨者分享啦

假如你有任何疑問或者想搵到更多幫手，歡迎加入我哋嘅 [Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)

即刻動手為其他專案出一分力啦！我哋整咗一份清單，入面嘅專案都有啲簡單嘅議題可以開始做。[去睇睇啦！](https://firstcontributions.github.io/#project-list)

### [ 更多資料 ](../additional-material/git_workflow_scenarios/additional-material.md)

## 使用其他工具嘅教學

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |

<p>項目支持者:</p>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>
