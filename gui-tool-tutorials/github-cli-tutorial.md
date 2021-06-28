[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# First Contributions

<table>
  <tr>
    <td>
      <svg width="200" height="200" viewBox="0 0 16 16" aria-hidden="true">
  		<path full-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z">
  		</path>
			</svg>
    </td>
    <td><b>Github CLI</b></td>
  </tr>
</table>
It's hard. It's always hard, when you do something for the first time. Especially when you are collaborating, making mistakes isn't a comfortable thing. But open source is all about collaboration & working together. We wanted to simplify the way new open-source contributors learn & contribute for the first time.

Reading articles & watching tutorials can help, but what comes better than actually doing the stuff without messing up anything. This project aims at providing guidance & simplifying the way rookies make their first contribution. Remember the more relaxed you are, the better you learn. If you are looking for making your first contribution just follow the simple steps below. We promise you, it will be fun.


## Github CLI

Please note, this tutorial is for MacOS. It is similar with Windows Terminal on Windows but some things may look different.

<!--
************************************
​	*** This is commented out until      ***
​	*** a Windows tutorial can be created***
************************************
Please note, this tutorial is for MacOS. Please refer to the [Windows Tutorial]() for Sourcetree if that is what you want to use.
-->

Download [Github CLI](https://cli.github.com/), then open Terminal(or any Commandline Tools). I used the [iTerm2](https://iterm2.com/).

If you want to install Github CLI via Homebrew, you can download it as shown below the command line.

~~~
brew install gh
~~~



If the download is successful, you can view the console log as shown below the screenshot.

~~~
gh --version
~~~

<img style="float: right;" src="https://user-images.githubusercontent.com/33862991/123590149-39338780-d825-11eb-8293-b730bb3e6c9e.png" alt="Github CLI version" />

## Fork this repository

Fork this repo in command line.

~~~
gh repo fork [repository-owner]/[repository-name]
~~~

<img style="float: right;" src="https://user-images.githubusercontent.com/33862991/123590154-3afd4b00-d825-11eb-91b0-99c28d87bfc7.png" alt="Fork repository via Github CLI" />

When you answered yes, begins forking the repository.

<img style="float: right;" src="https://user-images.githubusercontent.com/33862991/123590161-3c2e7800-d825-11eb-8e28-f60ecb6b8be7.png" alt="Fork repository via Github CLI" />

After the repository is forked. You can see the repository in the list.

~~~
gh repo list
~~~

<img style="float: right;" src="https://user-images.githubusercontent.com/33862991/123590165-3d5fa500-d825-11eb-98d0-a0d97fa6844c.png" alt="Repository List" />

## Create a branch

From now on, you can just use Git CLI.

Create a new branch.

~~~
git branch [your-new-branch-name]
~~~

Then switch the branch.

~~~
git switch [your-new-branch-name]
~~~

<img style="float: right;" src="https://user-images.githubusercontent.com/33862991/123590170-3e90d200-d825-11eb-8c51-12e0f1c0f903.png" alt="Create branch and switch" />

## Make necessary changes and commit those changes

Now open `Contributors.md` file in a text editor, scroll to the bottom of the page and add your name to it, then save the file.

Example: If your name is Chris Wanstrath, It should look like this.

[Chris Wanstrath]\(https://github.com/defunkt)



Then commit changes.

~~~
git commit -m "[commit-message]"
~~~

<img style="float: right;" src="https://user-images.githubusercontent.com/33862991/123590172-3f296880-d825-11eb-9c06-1d362b1bd5ff.png" alt="Commit changes" />

## Push changes to Github

Now you are ready to push your changes to github. This will be pushing it to your repository forked. 

First, push your commit to repository forked, copy of the project.

~~~
git push --set-upstream origin [your-branch-name]
~~~

![Push changes into repository forked](https://user-images.githubusercontent.com/33862991/123590173-3fc1ff00-d825-11eb-9980-66bb309f2c89.png)

## Submit your changes for review

Finally you can submit your commit to repository. 

~~~
gh pr create [repository-owner]/[repository-name]
~~~

`-R` or `--repo` is command for target repository.

![Source : Github CLI](https://user-images.githubusercontent.com/33862991/123590175-40f32c00-d825-11eb-92c5-af0e6ba637fd.png)



You can check PR list.

~~~
gh pr list
~~~

![PR List in console](https://user-images.githubusercontent.com/33862991/123590174-405a9580-d825-11eb-8c2a-e607d2aa192f.png)

Check your pr in web browser.

![PR List in web view](https://user-images.githubusercontent.com/33862991/123590177-40f32c00-d825-11eb-81e9-66a2a9d79e3b.png)

If your commit has not problem, It will be merging all your changes into the master branch of this project. And then you will get a notification email once the changes have been merged.

## Where to go from here?

Congrats!  You have just completed the standard _fork -> clone -> edit -> PR_ workflow that you'll encounter often as a contributor!

Celebrate your contribution and share it with your friends and followers by going to [web app](https://firstcontributions.github.io/#social-share).

You could join our slack team in case you need any help or have any questions. [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).


### [Additional material](../additional-material/git_workflow_scenarios/additional-material.md)


## Tutorials Using Other Tools
[Back to main page](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
