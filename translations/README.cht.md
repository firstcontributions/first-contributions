[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)

# 第一次的開源貢獻

*以下的「你」通稱中文的你或妳。*

萬事起頭難。特別是和其他人合作時，犯錯格外令人不舒服。不過，開源的本質就是和其他人合作。我們希望為初學者帶來一個簡單的方法去學習及參與開源專案。

閱讀文章和觀看教學會有所幫助。不過，有什麼方法能比，在不會弄亂任何東西的情況下，實際動手做更好？本專案旨在指導初學者及簡化初學者參與開源的方式。如果你想要做出第一次貢獻，只需按照以下簡單步驟操作即可。跟你保證，這會很好玩 :)

*如果你不習慣使用終端機介面，可以嘗試[圖形介面的教程](#tutorials-using-other-tools)*

#### *你可以選擇使用[其他語言](../Translations.md)閱讀此份文件*

[🇮🇳](translations/README.hi.md) [🇲🇲](translations/README.mm_unicode.md) [🇮🇩](translations/README.id.md) [🇫🇷](translations/README.fr.md) [🇪🇸](translations/README.es.md) [<img src="assets/catalan1.png" width="22">](translations/README.ca.md) [🇳🇱](translations/README.nl.md) [🇷🇺](translations/README.ru.md) [🇯🇵](translations/README.ja.md) [🇻🇳](translations/README.vn.md) [🇵🇱](translations/README.pl.md) [🇮🇷](translations/README.fa.md) [🇮🇷](translations/README.fa.en.md) [🇰🇷 🇰🇵](translations/README.ko.md) [🇩🇪](translations/README.de.md) [🇨🇳](translations/README.chs.md) [🇹🇼](translations/README.cht.md) [🇬🇷](translations/README.gr.md) [🇪🇬](translations/README.eg.md) [🇸🇦](translations/README.ar.md) [🇺🇦](translations/README.ua.md) [🇧🇷](translations/README.pt_br.md) [🇵🇹](translations/README.pt-pt.md) [🇮🇹](translations/README.it.md) [🇹🇭](translations/README.th.md) [🏴󠁥󠁳󠁧󠁡󠁿](translations/README.gl.md) [🇵🇰](translations/README.ur.md) [:bangladesh:](translations/README.bn.md) [🇲🇩 🇷🇴](translations/README.ro.md) [🇹🇷](translations/README.tr.md) [🇸🇪](translations/README.se.md) [:slovenia:](translations/README.sl.md) [🇮🇱](translations/README.hb.md) [<img src="assets/pirate.png" width="22">](translations/README.en-pirate.md)

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

如果你的電腦上尚未安裝 git，請按照[安裝指引](https://help.github.com/articles/set-up-git/)進行安裝。

## Fork（分叉）儲存庫

點擊頁面上方的 Fork 圖示來 fork 儲存庫。
這個操作會將儲存庫複製一份到你的 Github 帳號下。

## Clone（複製）儲存庫

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

現在將 fork 後的儲存庫複製到你的電腦上。前往你 fork 的儲存庫頁面，點擊 Clone 按鈕（圖示中的綠色按鈕），接著點擊*複製到剪切板*按鈕（複製儲存庫地址）

隨後打開終端機，輸入以下 git 指令：

```
git clone "url you just copied"
```
"url you just copied"（去掉雙引號）為你所屬帳戶的 fork 儲存庫地址。取得這連結的方法請見上一步。

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

例如：
```
git clone https://github.com/this-is-you/first-contributions.git
```

`this-is-you` 指的是你自己的 Github 帳號。這一步，會將你的 first-contributions 這個儲存庫複製到本地電腦上。

## 建立分支

切換你的電腦目錄到 first-contributions

```
cd first-contributions
```
接下來使用 `git checkout` 指令建立一個程式碼分支
```
git checkout -b <add-your-name>
```

例如：
```
git checkout -b add-david
```

（分支的名稱不一定要有 *add* 。然而，在這個新分支的名稱加入 *add* 是一件合理的事情，因為這個分支的目的是將你的名字加到貢獻者列表中。)

## 對程式碼進行修改，然後 Commit (提交) 修改

使用你喜歡的文字編輯器打開 `Contributors.md` 這個文件，將自己的名字加上去；不要加名字加在檔案的開頭或結尾，而是將之放置開頭與結位的任意位置，將檔案存檔。

<img align="right" width="450" src="../assets/git-status.png" alt="git status" />

在專案路徑底下執行 `git status` 指令可以看到更動的部份。

使用 `git add` 指令則可以添加更動項目到分支裡：

```
git add Contributors.md
```

現在可以使用 `git commit` 指令提交你的修改了：
```
git commit -m "Add <your-name> to Contributors list"
```
將 `<your-name>` 替換為自己的名字。

## 將更動 Push（發佈）到 GitHub

使用 `git push` 指令發佈更動
```
git push origin <add-your-name>
```
將 `<add-your-name>` 替換為之前新建的分支名稱。

## 送出 Pull Request 將你的修改供他人審閱

前往先前自己 Fork 的 GitHub 儲存庫，會看到一個 `Compare & pull request` 的按鈕。點擊該按鈕。

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

點擊 `Create pull request` 按鈕送出 pull request。

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />

不久之後，如果你更改的文件與原本沒有衝突，我們會把所有的更動合併到這個專案的主分支。
更動合併後，你會收到對應的電子郵件通知。

## 接下來做什麼呢？

恭喜你！你剛剛完成了 *fork -> clone -> edit -> PR*  的標準工作流，在之後的貢獻旅程中將會經常使用此方法。

在[這個網站](https://roshanjossey.github.io/first-contributions/#social-share)慶祝你的貢獻並跟朋友及追隨者分享

如果有任何疑問或想獲得更多協助，歡迎加入我們的 [Slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)

現在就動手為其他專案貢獻你的心力。我們整理了一個清單，裡面的專案都有簡單的議題可以著手。[去看看吧！](https://roshanjossey.github.io/first-contributions/#project-list)

### [ 更多資料 ](../additional-material/translations/additional-material.cht.md)

## 使用其他工具的教學

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|<a href="../github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>
|---|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|[Visual Studio Code](../github-windows-vs-code-tutorial.md)|

## 原作者的自我行銷

如果你喜歡這個專案，請給這個 [GitHub](https://github.com/Roshanjossey/first-contributions) 專案一顆星星 :star: 。
如果你覺得這超佛心，可以 follow [Roshan](https://roshanjossey.github.io/) 的[Twitter](https://twitter.com/sudo__bangbang) 和 [GitHub](https://github.com/roshanjossey)。

<a href="http://saasgrids.com"> <img alt="http://saasgrids.com" src="../assets/saasgrids-banner.png" width="500"></a>