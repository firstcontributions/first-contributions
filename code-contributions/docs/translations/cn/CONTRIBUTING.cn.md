# 提交的步骤

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

## 点击Fork按钮来Fork这个代码仓库（repo）

## Clone（克隆）你对这个项目的Fork

在你对这个项目的Fork仓库中 , 点击code按钮。选择SSH项然后点击 `copy to clipboard` 按钮。

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />
打开一个终端然后运行 `git clone` 命令

```bash
git clone "url you copied"
```

> [!IMPORTANT]
> 在以下步骤当中，当你看见 `<your-github-id>` 的时候，你应该用你的GitHub ID代替它。
>
> 举个例子，如果你的GitHub ID 是  `aaronsw`,  
> `git switch -c add-<your-github-id>`实际上就应该是`git switch -c add-aaronsw`  
> `contributors/<your-github-id>.html` 实际上是 `contributors/aaronsw.html`
>
> 

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

## 创建一个分支（branch）

如果当前不在代码仓库路径下的话，请移动到那里。

```bash
cd code-contributions
```

用 `git switch` 命令创建一个分支

```bash
git switch -c add-<your-github-id>
```


## 创建属于你自己的卡片

在提交者目录下，你可以以HTML文件的形式添加你的卡片。在提交者目录中用你的用户名创建一个文件。为了方便你开始，你可以复制下面的网页模板。

`contributors/<your-github-id>.html`
```html
<article>
  <h3>Your username</h3>
  <p>A small bio about you (optional)</p>
  <h4>Programming languages I use</h4>
  <section class="container">
    <div class="badge" style="background-color: #3874a4; color: white">
      Python
    </div>
    <div class="badge" style="background-color: #f7df1e; color: black;">
      JavaScript
    </div>
  </section>

  <h4>Tools I use</h4>
  <section class="container">
    <img
      class="icon"
      src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/bash/bash-original.svg"
    />
    <img
      class="icon"
      src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linux/linux-original.svg"
    />
  </section>
</article>
<style>
  body {
    font-family: sans-serif;
  }
  .container {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
  }
  .badge {
    padding: 0.5rem;
    border-radius: 0.25rem;
  }
  .icon {
    width: 2rem;
  }
</style>

```
## 在贡献者列表里添加属于你的卡片

把你创建的文件的名字添加到  `scripts/contributors.js` 文件。

`scripts/contributors.js`
```js
const contributorFiles = [
  "<your-github-id>.html", // add your file name here
  "roshanjossey.html",
  "gokultp.html",
];
```

## 在一个网页浏览器里看你带来的变化

你可以在一个浏览器里打开`index.html` 文件来查看你带来的变化。 你应该可以看见你在前几个步骤中添加的卡片。

你可以继续在你的卡片上做出改变，然后刷新浏览器界面来看这些变化。

## 提交你做出的改变

首先用 `git add` 指令把你做出的改变添加到本地git仓库

```bash
git add contributors/<your-github-id>.html
```

然后用 `git commit` 指令 提交你做出的改变

```bash
git commit -m "add <your-github-id>"
```

## 把你做的东西上传到GitHub

```bash
git push -u origin add-<your-github-id>
```

## 为了便于检查和回顾，提交你所做出的具体是什么改变。

如果你前往自己的GitHub对这个项目的Fork仓库，你可以看见一个`Compare & pull request` 按钮。点击这个按钮。

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

然后提交合并分支的请求（pull request，简称pr）

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

一旦你做出的改变被合并，你将会收到一封提示性的邮件。
