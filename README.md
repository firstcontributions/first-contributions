[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

#### _Read this in [other languages](docs/translations/Translations.md)._
<kbd>[<img title="Shqip" alt="Shqip" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/al.svg" width="22">](docs/translations/README.sq.md)</kbd>
<kbd>[<img title="Armenian" alt="Armenian" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/am.svg" width="22">](docs/translations/README.arm.md)</kbd>
<kbd>[<img title="Uzbek" alt="Uzbek language" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/uz.svg" width="22">](docs/translations/README.uz.md)</kbd>
<kbd>[<img title="Azərbaycan dili" alt="Azərbaycan dili" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/az.svg" width="22">](docs/translations/README.aze.md)</kbd>
<kbd>[<img title="বাংলা" alt="বাংলা" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/bd.svg" width="22">](docs/translations/README.bn.md)</kbd>
<kbd>[<img title="Bulgarian" alt="Bulgarian" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/bg.svg" width="22">](docs/translations/README.bg.md)</kbd>
<kbd>[<img title="Português (Brasil)" alt="Português (Brasil)" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/br.svg" width="22">](docs/translations/README.pt_br.md)</kbd>
<kbd>[<img title="Català" alt="Català" src="https://firstcontributions.github.io/assets/Readme/catalan1.png" width="22">](docs/translations/README.ca.md)</kbd>
<kbd>[<img title="中文 (Simplified)" alt="中文 (Simplified)" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/cn.svg" width="22">](docs/translations/README.zh-cn.md)</kbd>
<kbd>[<img title="Czech" alt="Czech" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/cz.svg" width="22">](docs/translations/README.cs.md)</kbd>
<kbd>[<img title="Deutsch" alt="Deutsch" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/de.svg" width="22">](docs/translations/README.de.md)</kbd>
<kbd>[<img title="Dansk" alt="Dansk" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/dk.svg" width="22">](docs/translations/README.da.md)</kbd>
<kbd>[<img title="Español" alt="Español" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/es.svg" width="22">](docs/translations/README.es.md)</kbd>
<kbd>[<img title="Française" alt="Française" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/fr.svg" width="22">](docs/translations/README.fr.md)</kbd>
<kbd>[<img title="日本語" alt="日本語" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/jp.svg" width="22">](docs/translations/README.ja.md)</kbd>
<kbd>[<img title="한국어" alt="한국어" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/kr.svg" width="22">](docs/translations/README.ko.md)</kbd>
<kbd>[<img title="Русский язык" alt="Русский язык" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/ru.svg" width="22">](docs/translations/README.ru.md)</kbd>
<kbd>[<img title="Tiếng Việt" alt="Tiếng Việt" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/vn.svg" width="22">](docs/translations/README.vn.md)</kbd>

[👉 View all 117+ language translations](docs/LANGUAGES.md)

# First Contributions

This project aims to simplify and guide the way beginners make their first contribution. If you are looking to make your first contribution, follow the steps below.

_If you're not comfortable with command line, [here are tutorials using GUI tools.](#tutorials-using-other-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork the repository" />

#### If you don't have git on your machine, [install it](https://docs.github.com/en/get-started/quickstart/set-up-git).

## 🚀 Quick Start

### Fork this repository

Fork this repository by clicking on the fork button on the top of this page.
This will create a copy of this repository in your account.

### Clone the repository

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone the repository" />

Now clone the forked repository to your machine. Go to your GitHub account, open the forked repository, click on the code button, then on SSH tab and then click the _copy url to clipboard_ icon.

Open a terminal and run the following git command:

```bash
git clone "url you just copied"
```

where "url you just copied" (without the quotation marks) is the url to this repository (your fork of this project). See the previous steps to obtain the url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

For example:

```bash
git clone git@github.com:this-is-you/first-contributions.git
```

where `this-is-you` is your GitHub username. Here you're copying the contents of the first-contributions repository on GitHub to your computer.

### Create a branch

Change to the repository directory on your computer (if you are not already there):

```bash
cd first-contributions
```

Now create a branch using the `git switch` command:

```bash
git switch -c your-new-branch-name
```

For example:

```bash
git switch -c add-alonzo-church
```

<details>
<summary> <strong>If you get any errors using git switch, click here:</strong> </summary>

If the error message "Git: `switch` is not a git command. See `git –help`" appears, it's likely because you're using an older version of git.

In this case, try to use `git checkout` instead:

```bash
git checkout -b your-new-branch-name
```

</details>

### Make necessary changes and commit those changes

Now open `Contributors.md` file in a text editor, add your name to it. Don't add it at the beginning or end of the file. Put it anywhere in between. Now, save the file.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

If you go to the project directory and execute the command `git status`, you'll see there are changes.

Add those changes to the branch you just created using the `git add` command:

```bash
git add Contributors.md
```

Now commit those changes using the `git commit` command:

```bash
git commit -m "Add your-name to Contributors list"
```

replacing `your-name` with your name.

### Push changes to GitHub

Push your changes using the command `git push`:

```bash
git push -u origin your-branch-name
```

replacing `your-branch-name` with the name of the branch you created earlier.

<details>
<summary> <strong>If you get any errors while pushing, click here:</strong> </summary>

- ### Authentication Error
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/&lt;your-username&gt;/first-contributions.git/'</pre>
  Go to [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) on generating and configuring an SSH key to your account.

  Also, you might want to run 'git remote -v' to check your remote address.
  
  If it looks anything like this:
  <pre>origin	https://github.com/your-username/your_repo.git (fetch)
  origin	https://github.com/your-username/your_repo.git (push)</pre>
  
  change it using this command:
  ```bash
  git remote set-url origin git@github.com:your-username/your_repo.git
  ```
  Otherwise you'll still get prompted for username and password and get authentication error.
</details>

### Submit your changes for review

If you go to your repository on GitHub, you'll see a `Compare & pull request` button. Click on that button.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="compare and create pull request" />

Now submit the pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Soon I'll be merging all your changes into the main branch of this project. You will get a notification email once the changes have been merged.

## 📚 Learning Resources

### [📖 Additional Material](docs/additional-material/git_workflow_scenarios/additional-material.md)

Comprehensive guide covering:
- Git workflow scenarios
- Advanced git concepts
- Real-world contribution examples

### [🎥 Video Tutorials](docs/VIDEO_TUTORIALS.md)

Step-by-step video guides in multiple languages covering:
- Command line tutorials
- GUI tool tutorials
- Platform-specific guides

### [🌍 Language & Regional Guides](docs/LANGUAGES.md)

- **117+ Languages** supported
- Organized by region
- Community resources for each language

### [❓ Troubleshooting Guide](docs/TROUBLESHOOTING.md)

Common issues and solutions:
- Authentication errors
- Git conflicts
- Platform-specific issues
- Language-specific help

### [🙏 Contributors & Translators](docs/CONTRIBUTORS.md)

Meet the amazing people who made this project possible!

## 🛠️ Tutorials Using Other Tools

| <a href="docs/gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> |
| --- | --- |
| [GitHub Desktop](docs/gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md) |

## 🎯 Where to go from here?

Congrats! You just completed the standard _fork -> clone -> edit -> pull request_ workflow that you'll often encounter as a contributor!

Celebrate your contribution and share it with your friends and followers by going to [web app](https://firstcontributions.github.io/#social-share).

If you'd like more practice, checkout [code contributions](https://github.com/roshanjossey/code-contributions).

Now let's get you started with contributing to other projects. We've compiled a list of projects with easy issues you can get started on. Check out [the list of projects in the web app](https://firstcontributions.github.io/#project-list).

## 💬 Community & Support

- **[GitHub Discussions](https://github.com/firstcontributions/first-contributions/discussions)** - Ask questions, share experiences
- **[Language Communities](docs/LANGUAGES.md#community-discussions)** - Join discussions in your language
- **[Report Issues](https://github.com/firstcontributions/first-contributions/issues)** - Found a problem? Let us know

## 📊 Project Statistics

- **117+** Languages Supported
- **10,000+** Contributors
- **50+** Translations
- **Active** Community

## 🤝 Contributing Translations

Want to help translate this project? [Check out our translation guide](docs/LANGUAGES.md#contributing-translations)

---

<p>This project is supported by:</p>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>
