[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# 第一次參與開源

萬事起頭難。特別是和其他人合作時，犯錯格外令人不舒服。不過，開源的本質就是和其他人合作。我們希望為初學者帶來一個簡單的方法來學習及參與開源項目。

閱讀文章和觀看教學會有所幫助。不過，有什麼方法能比在不會弄亂任何東西的情況下，實際動手做來得更好？本項目旨在指導初學者及簡化初學者參與開源的方式。記住：過程越輕鬆，學習效益越高。如果妳/你想要做出第一次貢獻，只需按照以下簡單步驟操作即可。跟你保證，這會很好玩 :)

_如果你不喜歡使用指令列，[這裡有使用圖形界面工具的教學。](#使用其他工具的教學)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="分叉本儲存庫" />

#### 如果你的電腦上尚未安裝 git，請按照這個[安裝指南（英文）](https://help.github.com/articles/set-up-git/)進行安裝。

## 分叉（Fork）本儲存庫

點選圖示中的按鈕來 Fork 這個 Git 儲存庫。
這個操作會將儲存庫分叉到你/妳的 GitHub 帳號下。

## 複製（Clone）儲存庫

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="複製本儲存庫" />

接下來，將分叉後的儲存庫複製到你/妳的電腦上。前往你/妳的GitHub帳號，打開分叉到帳號下的儲存庫，點選圖示中的綠色按鈕，接著在SSH分頁上點選*複製到剪貼簿*按鈕（將儲存庫網址複製下來）。

隨後打開命令列視窗，輸入如下 git 命令：

```bash
git clone "url you just copied"
```

"url you just copied"（去掉雙引號）就是複製到妳/你帳戶名下的儲存庫網址。取得這網址的方法請見上一步。

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="複製連結到剪貼簿" />

譬如：

```bash
git clone git@github.com:this-is-you/first-contributions.git
```

`this-is-you` 指的就是你/妳的 GitHub 用戶名。這一步會將你/妳的 first-contributions 儲存庫複製到你的電腦上。

## 新建一個分支（Branch）

下面的命令能在命令行窗口中，把目錄切換到 first-contributions（如果你/妳尚未切換到該目錄）：

```bash
cd first-contributions
```

接下來使用 `git switch` 命令建立一個分支：

```bash
git switch -c your-new-branch-name
```

譬如：

```bash
git switch -c add-david
```

（新分支的名稱不一定需要有 _add_。然而，在這個新分支的名稱加入 _add_ 是一件合理的事情，因為這個分支的目的是將妳/你的名字添加到貢獻者列表中。）

<details>
<summary> <strong>如果在使用 git switch 命令的過程中出現錯誤（error），點擊這裡：</strong> </summary>

如果顯示錯誤訊息 "Git: `switch` is not a git command. See `git –help`"，這可能是因為你/妳使用的是舊版的 git。

在這種情況下，請改為使用 `git checkout` 命令：

```bash
git checkout -b your-new-branch-name
```

</details>

## 對程式碼進行修改，然後提交 (Commit) 修改

使用妳/你喜歡的編輯器打開 `Contributors.md` 這個文件，將自己的名字加在檔案中，不要將其添加到文件的開頭或結尾。將其新增至文件中間的任意位置，然後存檔。

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="被更動的文件" />

在命令窗口執行 `git status`，這會列出被更動的文件。

接著 `git add` 這命令則可以添加更動項目到分支裡，就像以下這條命令：

```bash
git add Contributors.md
```

現在就可以使用 `git commit` 命令 commit（提交）你/妳的修改了：

```bash
git commit -m "Add your-name to Contributors list"
```

將 `your-name` 替換為自己的名字。

## 將更動發佈（Push）到 GitHub

使用 `git push` 命令發佈代碼：

```bash
git push -u origin your-branch-name
```

將 `your-branch-name` 替換為之前新建的分支名稱。

<details>
<summary> <strong>如果在發佈（push）過程中出現錯誤（error），點擊這裡：</strong> </summary>

- ### 身份驗證錯誤（Authentication Error）
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/&lt;your-username>/first-contributions.git/'</pre>
  去 [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) 學習如何生成新的 SSH 密匙以及配置。

  此外，你/妳可能需要執行 'git remote -v' 來檢查遠端儲存庫的URL。
  
  如果看起來與這樣有一點相似：
  
  <pre>origin	https://github.com/your-username/your_repo.git (fetch)
  origin	https://github.com/your-username/your_repo.git (push)</pre>
  
  使用以下命令更改它：
  ```bash
  git remote set-url origin git@github.com:your-username/your_repo.git
  ```
  否則，你/妳仍會收到要求輸入使用者名稱和密碼的提示，並出現身份驗證錯誤。
</details>

## 提出 Pull Request 將你/妳的修改供他人審閱

前往你/妳的GitHub帳號，打開分叉到帳號下的儲存庫，會看到一個 `Compare & pull request` 的按鈕，點選該按鈕。

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="建立一個 pull request" />

接著再點選 `Create pull request` 按鈕，正式提交 pull request。

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="提出 pull request" />

不久之後，如果妳/你更改的文件與原本沒有衝突，我們會把所有的變化合併到這個項目的主分支。
變更合併後，妳/你會收到通知 email。

## 下一步？

恭喜！妳/你剛剛完成了作為一個貢獻者會經常使用的標準工作流程：_fork -> clone -> edit -> pull request_！

在[這個網站](https://firstcontributions.github.io/#social-share)慶祝妳/你的貢獻並跟朋友及追隨者分享。

如果你想要更多練習，請看 [code contributions](https://github.com/roshanjossey/code-contributions)。

現在就動手為其他專案貢獻你/妳的心力。我們整理了一個清單，裡面的專案都有簡單的議題可以著手。[去看看吧！](https://firstcontributions.github.io/#project-list)

### [ 更多資料 ](../additional-material/git_workflow_scenarios/additional-material.md)

## 使用其他工具的教學

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |

<p>項目支持者:</p>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>
