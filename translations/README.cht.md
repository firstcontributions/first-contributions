[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" src="https://firstcontributions.herokuapp.com/badge.svg">](https://firstcontributions.herokuapp.com)

# 第一次參與開源

萬事起頭難。特別是和其他人合作時，犯錯格外令人不舒服。不過，開源的本質就是和其他人合作。我們希望為初學者帶來一個簡單的方法去學習及參與開源項目。

閱讀文章和觀看教學會有所幫助。不過，有什麼方法能比，在不會弄亂任何東西的情況下，實際動手做更好？本項目旨在指導初學者及簡化初學者參與開源的方式。記住：過程越輕鬆，學習效益越高。如果妳/你想要做出第一次貢獻，只需按照以下簡單步驟操作即可。跟你保證，這會很好玩 :)

#### *此文檔的 [其他語種](../Translations.md).*

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

如果你的電腦上尚未安裝 git, 請按照這個[ 安裝指引(英文) ](https://help.github.com/articles/set-up-git/)進行安裝。

## Fork（分叉）本代碼庫

點擊圖示中的按鈕去 Fork 這個代碼庫。
這個操作會將代碼庫分叉到你/妳的 Github 帳號下。

## Clone（複製）代碼庫

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

接下來，將複製後的代碼庫複製到你/妳的電腦上。點擊圖示中的綠色按鈕，接著點擊複製到剪切板按鈕（將代碼庫地址複製下來）

隨後打開命令行窗口，敲入如下 git 命令：

```
git clone "url you just copied"
```
"url you just copied"（去掉雙引號）就是複製到妳/你帳戶名下的代碼庫地址。獲取這鏈接地址的方法請見上一步。

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

譬如：
```
git clone https://github.com/this-is-you/first-contributions.git
```

'this-is-you' 指的就是你/妳自己的 Github 用戶名。這一步，會將你/妳的 first-contributions 這個代碼庫複製到本地電腦上。

## 新建一個分支

下面的命令能在命令行窗口中，把目錄切換到 first-contributions 

```
cd first-contributions
```
接下來使用 `git checkout` 命令新建一個程式碼分支
```
git checkout -b <add-your-name>
```

譬如：
```
git checkout -b add-david
```

(新分支的名稱不一定需要有* add *。然而，在這個新分支的名稱加入* add *是一件合理的事情，因為這個分支的目的是將妳/你的名字添加到貢獻者列表中。)

## 對程式碼進行修改，然後 Commit (提交) 修改

使用妳/你喜歡的文字編輯器打開 `Contributors.md` 這個文件，更新文件內容，將自己的名字加上去，然後存檔。在命令窗口執行 `git status` ，這會列出被更動的文件。接著 `git add` 這命令則可以添加更動項目到分支裡，就像以下這條命令。
```
git add Contributors.md
```

現在就可以使用 `git commit` 命令 commit (提交)你/妳的修改了。
```
git commit -m "Add <your-name> to Contributors list"
```
將 `<your-name>` 替換為自己的名字

## 將更動 Push（發佈）到 GitHub

使用 `git push` 命令發佈代碼
```
git push origin <add-your-name>
```
將 `<add-your-name>` 替換為之前新建的分支名稱。

## 提出 Pull Request 將你/妳的修改供他人審閱

前往先前自己 Fork 的 Github 代碼庫，會看到一個 `Compare & pull request` 的按鈕。點擊該按鈕。

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

接著再點擊 `Create pull request` 按鈕，正式提交 pull request。

<img style="float: right;" src="../assets/submit-pull.png" alt="submit pull request" />

不久之後，如果妳/你更改的文件與原本沒有衝突，我們會把所有的變化合併到這個項目的主分支。
更改合併後，妳/你會收到通知電郵。

## 接下來做什麼呢？

在[這個網站](https://roshanjossey.github.io/first-contributions/#social-share)慶祝妳/你的成就並跟朋友及追隨者分享

如果有任何疑問或想獲得更多協助，歡迎加入我們的 [Slack](https://firstcontributions.herokuapp.com)

現在就動手為其他專案貢獻你/妳的心力。我們整理了一個清單，裡面的專案都有簡單的議題可以著手。[去看看吧！](https://roshanjossey.github.io/first-contributions/#project-list)

### [ 更多資料 ](../additional-material/git_workflow_senarios/additional-material.md)

## 使用其他工具的教學

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

## 原作者的自我行銷

如果你/妳喜歡這個專案, 請給這個 [GitHub](https://github.com/Roshanjossey/first-contributions) 專案一顆星星 :star: 。
如果妳/你覺得這超佛心, 可以 follow [Roshan](https://roshanjossey.github.io/) 的
[Twitter](https://twitter.com/sudo__bangbang) 和
[GitHub](https://github.com/roshanjossey)。

<a href="http://saasgrids.com"> <img alt="http://saasgrids.com" src="../assets/saasgrids-banner.png" width="500"></a>
