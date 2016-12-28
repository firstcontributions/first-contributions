# First Contributions

*Read this in other languages: [English](README.md), [Spanish](README.es.md)*

<h2>Instructions for contributing to this repository</h2><br />

1. If you don't have git on your machine, [ install it ]( https://help.github.com/articles/set-up-git/).
2. Fork this repository by clicking on the fork button: <img style="float: right;" width="300" src="assets/fork.png" alt="Fork this repo." />
3. Now clone this repo to your machine. Click on the clone button and then click the copy to clipboard icon:&nbsp;<img style="float: right;" width="300" src="assets/clone.png" alt = "Clone this repo." />&nbsp;<img style="float: right;" width="300" src="assets/copy-to-clipboard.png" alt="Copy to clipboard." />
4. In a terminal, type the following command followed by the ENTER key: git clone https://github.com/this-is-you/first-contributions.git, where 'this-is-you' is your github username. Here you're copying the contents of first-contributions repository in github to your computer.
5. Go in to that directory by typing the following command followed by the ENTER key: cd first-contributions.
6. Now create a branch using git checkout -b <add-your-name>.
7. Now open `Contributors.md` file in a text editor and add your name to it, save the file.

If you go to the project directory and do `git status`, you'll see there are changes.

8. Add those changes using `git add`: git add *
9. Now commit those changes using `git commit`: git commit -m "Add <your-name> to Contributors list", where `<your-name>` is your name
10. Push your changes using `git push`: git push origin <add-your-name>, where `<add-your-name>` is the name of the branch you created earlier.
11. Ggo to your repo on github, you'll see a button to open a pull request. click on that button:&nbsp;<img style="float: right;" src="assets/compare-and-pull.png">
12. Submit the pull request:&nbsp;<img style="float: right;" src="assets/submit-pull.png">
<h2> Keeping your fork synced with this repo</h2>

Now I'll be merging all your changes in to master branch of this project. Then your fork won't have those changes. In order to keep your fork synced with mine, add my repo's url as `upstream remote url`.
13. git remote add upstream https://github.com/Roshanjossey/first-contributions. This is a way of telling git that another version of this project exists in the specified url and we're calling it master.
14. git fetch upstream. Here we're fetching all the changes in my fork (upstream remote).
15. git rebase upstream/master. Here you're applying all the changes you fetched to master branch.
16. Push master branch now, your fork will also have the changes: git push origin master. Notice here you're pushing to the remote named origin
