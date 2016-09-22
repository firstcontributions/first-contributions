# First-contributions

If you don't have git on machine, [ install it ]( https://help.github.com/articles/set-up-git/ )

Fork this repo by clicking on the fork button

<img style="float: right;" src="assets/fork.png">

Now clone this repo to your machine. Click on clone button and then copy to clipboard icon

<img style="float: right;" src="assets/clone.png">
<img style="float: right;" src="assets/copy-to-clipboard.png">

Open a terminal and run

```
git clone https://github.com/this-is-you/first-contributions.git
```

Where the url can be pasted from clipboard

Go in to that directory

```
cd first-contributions
```

Now cut a branch using `git checkout command`

```
git checkout -b add-your-name
```

Now open Contributors.md file in a text editor and add your name to it, save the file

If you go to the project directory and do `git status`, you'll see there are changes

Add those change using `git add`

```
git add Contributors.md
```

Now commit those changes using `git commit`

```
git commit -m "Add your-name to Contributors list"
```

Push your changes using `git push`

```
git push origin add-your-name
```

If you go to your repo on github, you'll see a button to open a pull request. click on that button

Now submit the pull request 
