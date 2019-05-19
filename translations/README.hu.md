<img align="right" width="300" src="assets/fork.png" alt="fork this repository" />

Ha még nincs git a gépeden, [installáld]( https://help.github.com/articles/set-up-git/).

## "Fork"old a repot

Kattints a "fork" gombra az oldal tetején, ezzel létrehozod a repo másolatát a saját fiókodban.

## Klónozd (Clone) a repot

<img align="right" width="300" src="assets/clone.png" alt="clone this repository" />

Most klónozd a forkolt repot a saját gépedre. Navigálj a GitHub fiókodra, nyisd meg a forkolt repot, kattints a "Clone" gombra, majd kattints a *copy to clipboard* (Vágólapra másolás) ikonra. 

Nzisd meg a terminált és futtasd ay alábbi git parancsot:

```
git clone "az url amit kimásoltál"
```
ahol "az url amit kimásoltál" (idézőjel nélkül) az url ami erre a repora (a saját forkolt projekted) mutat.
Az előző pontban láthatod, hogyan juthatsz hozzá az url-hez.

<img align="right" width="300" src="assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

Például:
```
git clone https://github.com/ez-a-te-neved/first-contributions.git
```
ahol `ez-a-te-neved` a GitHub felhasználóneved. Ezen a ponton másolod a GitHub first-contributions repo tartalmát a saját gépedre.

## Hozz létre egy branch-ot

Navigálj a repo könyvtárába a gépeden (ha még nem ott vagy):

```
cd first-contributions
```
Most hozz lére egy branch-ot a `git checkout` paranccsal:
```
git checkout -b <szabadon-választott-branch-név>
```

Például:
```
git checkout -b kis-pista-hozzaadasa
```

## Eszközöld a szükséges változtatásokat majd commitold őket

//FOLYTATÁS INNEN 

Now open `Contributors.md` file in a text editor, add your name to it. Don't add it at the beginning or end of the file. Put it anywhere in between. Now, save the file.

<img align="right" width="450" src="assets/git-status.png" alt="git status" />


If you go to the project directory and execute the command `git status`, you'll see there are changes.


Add those changes to the branch you just created using the `git add` command:

```
git add Contributors.md
```

Now commit those changes using the `git commit` command:
```
git commit -m "Add <your-name> to Contributors list"
```
replacing `<your-name>` with your name.

## Push changes to GitHub

Push your changes using the command `git push`:
```
git push origin <add-your-branch-name>
```
replacing `<add-your-branch-name>` with the name of the branch you created earlier.

## Submit your changes for review

If you go to your repository on GitHub, you'll see a  `Compare & pull request` button. Click on that button.

<img style="float: right;" src="assets/compare-and-pull.png" alt="create a pull request" />

Now submit the pull request.

<img style="float: right;" src="assets/submit-pull-request.png" alt="submit pull request" />

Soon I'll be merging all your changes into the master branch of this project. You will get a notification email once the changes have been merged.

## Where to go from here?

Congrats!  You just completed the standard _fork -> clone -> edit -> PR_ workflow that you'll encounter often as a contributor!

Celebrate your contribution and share it with your friends and followers by going to [web app](https://firstcontributions.github.io/#social-share).

You could join our slack team in case you need any help or have any questions. [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Now let's get you started with contributing to other projects. We've compiled a list of projects with easy issues you can get started on. Check out [the list of projects in web app](https://firstcontributions.github.io/#project-list).

### [Additional material](additional-material/git_workflow_scenarios/additional-material.md)


## Tutorials Using Other Tools

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|<a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|
|---|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|[Visual Studio Code](github-windows-vs-code-tutorial.md)|

## Self-Promotion

If you liked this project, star it on [GitHub](https://github.com/Roshanjossey/first-contributions).
If you're feeling especially charitable, follow [Roshan](https://roshanjossey.github.io/) on
[Twitter](https://twitter.com/sudo__bangbang) and
[GitHub](https://github.com/roshanjossey).

<a href="http://saasgrids.com"> <img alt="https://app.saasgrids.com" src="assets/saasgrids-banner.png" width="500"></a>
