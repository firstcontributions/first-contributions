# First Contributions

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

*其他語言版本: [英語](README.md), [西班牙語](README.es.md), [荷蘭語](README.nl.md), [印度語](README.hi.md), [俄語](README.ru.md), [日語](README.ja.md), [越南語](README.vn.md), [波蘭語](README.pl.md), [韓語](README.ko.md), [德語](README.de.md), [簡體中文](README.chs.md), [繁體中文](README.cht.md), [Greek](README.gr.md).*

如果你的電腦上尚未安裝 git, 請按照這個[ 安裝指引 ]( https://help.github.com/articles/set-up-git/ )進行安裝。

## Fork（複製）本代碼倉庫

通過點擊圖示中的按鈕，Fork 這個代碼倉庫。
這個操作會將這個代碼倉庫複製到你的賬戶名下。

## Clone（克隆）代碼倉庫

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

接下來將複製後的代碼倉庫克隆到你的電腦上，點擊圖示中的綠色按鈕，接著再點擊複製到剪切版按鈕（將代碼倉庫地址複製下來）

隨後打開命令行窗口，敲入如下 git 命令：

```
git clone "才複製的 url 鏈接"
```
"才複製的 url 鏈接"（去掉雙引號）就是複製到你賬戶名下的代碼倉庫地址。如何獲取這個鏈接地址請見上一步。

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

譬如：
```
git clone https://github.com/你的Github用戶名/first-contributions.git
```
'你的 Github 用戶名' 指的就是你的 Github 用戶名。在這一步中，你是將複製到你賬戶名下的 first-contributions 這個代碼倉庫克隆到本地電腦上。

## 新建一個分支

通過下面這個命令在命令行窗口中切換到 first-contributions 這個目錄下面

```
cd first-contributions
```
接下來使用 `git checkout` 命令新建一個代碼分支
```
git checkout -b <新分支的名稱>
```

譬如：
```
git checkout -b 新分支的名稱
```

## 對代碼進行修改，而後 commit 修改

打開 `Contributors.md` 這個文件，更新文件內容，將你的名字加上去，保存修改。通過 `git status` 這個命令你可以看到被改動了的文件被列了出來。接著通過 `git add` 命令則可以添加你的改動（以便隨後提交改動），就像如下這條命令。
```
git add Contributors.md
```

現在就可以使用 `git commit` 命令 commit 你的修改了。
```
git commit -m "Add <你的名字> to Contributors list"
```
將 `<你的名字>` 替換為你的名字

## 將改動 Push（提交）到 Github

使用 `git push` 命令提交代碼
```
git push origin <分支的名稱>
```
將 `<分支的名稱>` 替換為之前新建的分支名稱

## 提交你的變動供他人審閱

前往 Github 你的代碼倉庫，你會看到一個 `Compare & pull request` 的按鈕。點擊該按鈕。

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

接著再點擊 `Create pull request` 按鈕，正式提交 pull request。

<img style="float: right;" src="../assets/submit-pull.png" alt="submit pull request" />

## 讓你複製的代碼倉庫和本倉庫保持一致

收到你提交的變動後，我會將你提交到新分支中的改動，合併到 master（主分支）中。而你複製的代碼倉庫不會自動獲取到合併後的更新內容。為了讓你複製的代碼倉庫和我的代碼倉庫內容保持一致，首先你需要將我的代碼倉庫的地址使用 `upstream remote url` 命令添加到你的倉庫配置信息中。
```
git remote add upstream https://github.com/multunus/first-contributions
```
如此一來，你就讓 git 知道了你本地的這個代碼倉庫在遠端還存在另一個版本（即我的代碼倉庫），而那個版本我們將其叫做 upstream。一旦我合併了你提交的改動到我的代碼倉庫後，你在本地通過下面這個命令便能將更新的內容同步到本地。
```
git fetch upstream
```

通過上面這個命令，我們便將遠端我的代碼倉庫（upstream remote）中所有新增的改動抓回到了本地。但這樣還沒有結束，接下來，你也需要將更新 rebase（按照 git 中文文檔將其翻譯為 '衍合'）進入你本地的 master 主分支中。
```
git rebase upstream/master
```
通過上面這個命令，你就能夠將從遠端抓下來的所有改動衍合到本地的 master 主分支中。接著如果你再做一次 push master 提交你本地代碼到你自己的遠端主分支的操作，你在 Github 上複製的遠端代碼倉庫就也包含最新的代碼了。
```
git push origin master
```
注意，上面這個命令中，你遠端的代碼倉庫的名字叫做 origin。

## 接下來做什麼呢？

你在這個鏈接頁面中可以看到很多初學者友好的 issues（問題）：
[contributor.ninja](https://contributor.ninja).

通過下面這些鏈接，你能看到當前流行的眾多代碼倉庫中，適合初學者解決的問題列表，還等什麼，去吧 :)

|[![exercism](https://avatars2.githubusercontent.com/u/5624255?v=3&s=100)](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[![fun-retro](https://avatars3.githubusercontent.com/u/15913975?v=3&s=100)](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[<img width="100" src="https://cdn.worldvectorlogo.com/logos/react.svg">](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[![habitat](https://avatars1.githubusercontent.com/u/18171698?v=3&s=100)](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![scikit-learn](https://avatars0.githubusercontent.com/u/365630?v=3&s=100)](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[<img width="100" src="https://camo.githubusercontent.com/0f302c808c8457f6460913e33aed3478124612c2/687474703a2f2f6c65696e696e67656e2e6f72672f696d672f6c65696e696e67656e2e6a7067">](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[<img width="100" src="https://images.plot.ly/plotly-documentation/thumbnail/numpy-logo.jpg">](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[![elasticsearch](https://avatars2.githubusercontent.com/u/6764390?v=3&s=100)](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|---|---|---|---|---|---|---|---|
|[exercism](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[Fun Retros](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[react](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[habitat](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[scikit-learn](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[Leiningen](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[numpy](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[elasticsearch](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|[![homebrew](https://avatars2.githubusercontent.com/u/1503512?v=3&s=100)](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[![rust](https://avatars1.githubusercontent.com/u/5430905?v=3&s=100)](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[![vuejs](https://avatars1.githubusercontent.com/u/6128107?v=3&s=100)](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[![Suave](https://avatars2.githubusercontent.com/u/5822862?v=3&s=100)](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[![OpenRA](https://avatars3.githubusercontent.com/u/409046?v=3&s=100)](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![PowerShell](https://avatars0.githubusercontent.com/u/11524380?v=3&s=100)](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[![coala](https://avatars2.githubusercontent.com/u/10620750?v=3&s=100)](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[![moment](https://avatars2.githubusercontent.com/u/4129662?v=3&s=100)](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[homebrew](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[Rust](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[vuejs](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[Suave](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[OpenRA](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[PowerShell](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[coala](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[moment](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[![ava](https://avatars0.githubusercontent.com/u/8527916?v=3&s=100)](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[![freeCodeCamp](https://avatars0.githubusercontent.com/u/9892522?v=3&s=100)](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![webpack](https://avatars3.githubusercontent.com/u/2105791?v=3&s=100)](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[![hoodie](https://avatars1.githubusercontent.com/u/1888826?v=3&s=100)](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![pouchdb](https://avatars3.githubusercontent.com/u/3406112?v=3&s=100)](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[![neovim](https://avatars0.githubusercontent.com/u/6471485?v=3&s=100)](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[![babel](https://avatars2.githubusercontent.com/u/9637642?v=3&s=100)](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[<img width="100" src="https://github.com/adobe/brackets/blob/gh-pages/images/brackets_128.png?raw=true">](https://github.com/adobe/brackets/labels/Starter%20bug)|
|[ava](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[webpack](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[hoodie](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[pouchdb](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[neovim](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[babel](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[brackets](https://github.com/adobe/brackets/labels/Starter%20bug)|
| [![Node.js](https://avatars1.githubusercontent.com/u/9950313?v=3&s=100)](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|[<img width="100" src="https://github.com/Semantic-Org/Semantic-UI-React/raw/master/docs/app/logo.png">](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|
| [Node.js](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |[Semantic-UI-React](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |

[Tutorial for Github desktop app - English](github-desktop-tutorial.md)
