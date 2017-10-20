[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" src="https://firstcontributions.herokuapp.com/badge.svg">](https://firstcontributions.herokuapp.com)

# 第一次參與開源

萬事起頭難。特別是和其他人合作時，犯錯格外令人不舒服。不過，開源的本質就是和其他人合作。我們希望為初學者帶來一個簡單的方法去學習及參與開源項目。

閱讀文章和觀看教學會有所幫助。不過，有什麼方法能比，在不會弄亂任何東西的情況下，實際動手做更好？本項目旨在指導初學者及簡化初學者參與開源的方式。記住：過程越輕鬆，學習效益越高。如果你想要做出第一次貢獻，只需按照以下簡單步驟操作即可。跟你保證，這會很好玩 :)

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

*其他語言版本: [英語](../README.md), [西班牙語](README.es.md), [荷蘭語](README.nl.md), [印度語](README.hi.md), [俄語](README.ru.md), [日語](README.ja.md), [越南語](README.vn.md), [波蘭語](README.pl.md), [韓語](README.ko.md), [德語](README.de.md), [簡體中文](README.chs.md), [繁體中文](README.cht.md), [Greek](README.gr.md).*

如果你的電腦上尚未安裝 git, 請按照這個[ 安裝指引 ](https://help.github.com/articles/set-up-git/)進行安裝。

## Fork（分叉）本程式碼庫

點擊圖示中的按鈕去 Fork 這個程式碼庫。
這個操作會將程式碼庫分叉到你的Github帳號下。

## Clone（複製）程式碼庫

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

接下來，將複製後的程式碼庫複製到你的電腦上。點擊圖示中的綠色按鈕，接著點擊複製到剪切版按鈕（將程式碼庫地址複製下來）

隨後打開命令行窗口，敲入如下 git 命令：

```
git clone "剛才複製的 url 鏈接"
```
"剛才複製的 url 鏈接"（去掉雙引號）就是複製到你賬戶名下的程式碼庫地址。獲取這鏈接地址的方法請見上一步。

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

譬如：
```
git clone https://github.com/你的Github用戶名/first-contributions.git
```

'你的 Github 用戶名' 指的就是你的 Github 用戶名。這一步，你將複製到你賬戶名下的 first-contributions 這個程式碼庫複製到本地電腦上。

## 新建一個分支

下面的命令能在命令行窗口中，把目録切換到 first-contributions 

```
cd first-contributions
```
接下來使用 `git checkout` 命令新建一個程式碼分支
```
git checkout -b <新分支的名稱>
```

譬如：
```
git checkout -b add-myname
```

(新分支的名稱不一定需要有* add *。然而，在新分支的名稱加入* add *是一件合理的事情，因為這個分支的目的是將你的名字添加到列表中。)

## 對程式碼進行修改，然後 Commit (提交) 修改

打開 `Contributors.md` 這個文件，更新文件內容，將你的名字加上去，保存修改。`git status` 這命令會列出被改動的文件。接著 `git add` 這命令則可以添加你的改動，就像以下這條命令。
```
git add Contributors.md
```

現在就可以使用 `git commit` 命令 commit 你的修改了。
```
git commit -m "Add <你的名字> to Contributors list"
```
將 `<你的名字>` 替換為你的名字

## 將改動 Push（發佈）到 GitHub

使用 `git push` 命令發佈代碼
```
git push origin <分支的名稱>
```
將 `<分支的名稱>` 替換為之前新建的分支名稱。

## 提出 Pull Request 將你的修改供他人審閱

前往 Github 你的代碼庫，你會看到一個 `Compare & pull request` 的按鈕。點擊該按鈕。

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

接著再點擊 `Create pull request` 按鈕，正式提交 pull request。

<img style="float: right;" src="../assets/submit-pull.png" alt="submit pull request" />

不久之後，如果你更改的文件與原本沒有衝突，我們會把你所有的變化合併到這個項目的主分支。
更改合併後，你會收到通知電郵。

## 接下來做什麼呢？

在[這個網站](https://roshanjossey.github.io/first-contributions/#social-share)慶祝你的成就並跟你的朋友及追隨者分享

如果有任何疑問或想獲得更多協助，歡迎加入我們的 [Slack](https://firstcontributions.herokuapp.com)

現在就動手為其他專案貢獻你的心力。我們整理了一個清單，裡面的專案都有簡單的議題可以讓你著手。[去看看吧！](https://roshanjossey.github.io/first-contributions/#project-list)

### [ 更多資料 ](additional-material/additional-material.md)

## 使用其他工具的教學

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.microsoft.com/net/images/vslogo.png" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|
