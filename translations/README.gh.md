[![Love for Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Ntoboa a Edi Kan

Bere a edi kan a wobɛyɛ biribi no yɛ nea ɛyɛ den bere nyinaa. Suro a wusuro sɛ wubedi mfomso no nyɛ nea ahotɔ wom koraa, titiriw bere a woreyɛ biako no. Nanso wiase a ɛwɔ open source no fa adwumayɛkuw ne adwuma a wɔbɛyɛ sɛ kuw ho. Enti, yɛpɛ sɛ yɛma ɔkwan a wɔfa so ma wɔn a wɔde mmoa foforo kɔ open source no yɛ mmerɛw denam sɛnea wobɛkyerɛkyerɛ wo sɛnea wode wo ntoboa a edi kan bɛma no so.

Nsɛm ne nkyerɛkyerɛ akenkan betumi aboa, nanso dɛn na eye sen sɛ wobɛbɔ mmɔden a wunsuro sɛ wubedi mfomso? Saa dwumadie yi botaeɛ ne sɛ ɛbɛma akwankyerɛ na ama sɛdeɛ wɔn a wɔrefi aseɛ no de wɔn ntoboa a ɛdi kan de ma no ayɛ mmerɛ. Kae:dodow a wo ho adwo wo no, dodow no ara na wusua ade yiye.Sɛ wopɛ sɛ wode wo ntoboa a edi kan ma a, di anammɔn a ɛwɔ ase ha no akyi kɛkɛ.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Sɛ wo nni Git wɔ wo kɔmputa so a, . [fa hyɛ wo kɔmputa so](https://help.github.com/articles/set-up-git/).

## Fork Saa Adekorabea Yi

Fork saa adekorabea yi denam fork button a ɛwɔ kratafa no atifi a wobɛma so.
Wei bɛma woanya akoraeɛ no bi wɔ wo akonta so.

## Clone Saa Adekorabea

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Afei clone saa akoraeɛ yi kɔ wo kɔmputa so. Klik clone button no so na afei klik *kɔpi kɔ clipboard so* icon no so.

Bue ahyɛdeɛ kwan (sɛ wowɔ Windows so) anaa terminal (sɛ wowɔ MacOS anaa Linux so) na yɛ git ahyɛdeɛ a ɛdidi soɔ yi:

```
git clone "URL a woayɛ ho kɔpi nkyɛe no"
```
baabi a "URL a woayɛ ho kɔpi seesei ara" (a nsɛm a wɔafa aka no nka ho) yɛ akoraeɛ URL.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Nhwɛsoɔ:
```
git clone https://github.com/your-username/first-contributions.git
```
baabi a `wo-ɔdefoɔ din` yɛ wo GitHub dwumadie din. Ɛha na worekɔpi `ntoboa ahorow a edi kan` akoraeɛ no mu nsɛm afiri GitHub so akɔ wo kɔmputa so.

## Yɛ Baa Dwumadibea

Kɔ adwuma no ho kyerɛwtohɔ a wɔayɛ no foforo no so (sɛ woankɔ hɔ dedaw a):

```
cd first-contributions
```
Afei fa `git checkout` ahyɛdeɛ no yɛ baa dwumadibea:
```
git checkout -b <fa-wo-din ka ho>
```

Nhwɛsoɔ:
```
git checkout -b add-quarjo-wusu
```
(Ɛnsɛ sɛ baa dwumadibea din no kura asɛmfua *add*, nanso ntease wom sɛ wode bɛka ho efisɛ baa dwumadibea yi atirimpɔw ne sɛ wode wo din bɛka list bi ho.)

## Make Necessary Changes and Commit Them

Now, open the `Contributors.md` file in a text editor, add your name, and save the file. If you open the command prompt and run the `git status` command, you will see that there are modifications. Add these modifications to the branch you just created using the `git add` command:
```
git add Contributors.md
```

Now commit these changes using the `git commit` command:
```
git commit -m "Add <your-name> to Contributors list"
```
replace `<your-name>` with your name.

## Push Changes to GitHub

Push your changes using the `git push` command:
```
git push origin <add-your-name>
```
replace `<add-your-name>` with the name of the branch you created earlier.

## Submit Your Changes for Review

If you visit your repository on GitHub, you will see a `Compare & pull request` button. Click on this button.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Now submit the pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

I will merge all your changes into the main branch of this project soon. You will receive a notification email once the merge is complete.

The main branch of your fork will not be modified at this point. To keep your fork synchronized with mine, follow these steps.

## Keep Your Fork Synchronized with This Repository

First, switch to the main branch:
```
git checkout main
```

And add my repository URL as the `upstream remote url`:
```
git remote add upstream https://github.com/Roshanjossey/first-contributions
```
This is a way to tell Git that another version of this repository exists at the specified address, and we call it `upstream`. Once the changes are merged, look for the new version of my repository:
```
git fetch upstream
```

Here we are fetching all the changes in my upstream branch. Now you need to merge the new revision of my repository with your main branch:
```
git rebase upstream/main
```
Here we are applying all the changes you fetched to your main branch. If you push the main branch now, your fork will also have the changes:
```
git push origin main
```
Warning: This time, you're pushing to the remote repository called origin.

At this point, I merged your `<add-your-name>` branch with my main branch, and you merged my main branch with your main branch. Your `<add-your-name>` branch is no longer needed, so you can delete it:
```
git branch -d <add-your-name>
```
and you can also delete its remote version:
```
git push origin --delete <add-your-name>
```
This is not necessary, but the branch name indicates that its purpose is quite specific. Its lifespan can be short.

## Tutorials Using Other Tools

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></

a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |

## What's Next?

You can also join our team on Slack in case you need help or have any questions. [Join the team on Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)