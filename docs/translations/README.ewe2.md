[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# First Contributions

Nye taƒe sia na dɔwɔla bubuwo siwo katã le dzɔgbevi dome be woate ŋui ado wo ƒe gɔmedzedzea gbãtɔ le open source me. Ne wòle be nàwɔ wò ŋgɔmegbãtɔ gbãtɔ la, dzi wòanye fi nu siwo le ete si wokɔ kpli.

Ne mele be wònyɔ ŋgɔme kple command line o, megbe wòate ŋui dobia kple GUI tools, eye tutorial le eme.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Ne git mele wò kɔmputa me o, nà install (install it).

## Fork repo sia

Click na fork button si le ati dzi be nàfork repo sia. Esia náwɔ copy aɖe ɖe wò account me.

## Clone repo sia

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Afia ta nàclone repo la ɖe wò kɔmputa me. Yi wò GitHub account, nàbubu repo si wòfork la, click code button la eye click copy to clipboard icon la.

Open terminal eye run:

```bash
git clone "url you just copied"
```

"Url you just copied" nye URL aɖe siwo mele repo la me (wòfork la). Dzi triale steps sãa do go.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Example:

```bash
git clone git@github.com:this-is-you/first-contributions.git
```

Ne this-is-you nye wò GitHub username. Esia nye be wòtsɔ repo la ƒe content from GitHub ɖo wò kɔmputa.

## Nàtsɔ branch aɖe

Yi repository directory:

```bash
cd first-contributions
```

Wòate ŋui ɖo branch aɖe using command sia:

```bash
git switch -c <insert-your-new-branch-name>
```

Example:

```bash
git switch -c add-alonzo-church
```

<details>
<summary><strong>Ne wòkpɔ error kple git switch:</strong></summary>

Ne wòkpɔ “Git: 'switch' is not a git command…”, ene be version aɖe siwo le wòkɔmputa me nye yeyea.

Try:

```bash
git checkout -b your-new-branch-name
```
</details>

## Wòate ŋui wòwɔ changewo eye commit

Open `Contributors.md` le editor. Add wò ŋkɔ ɖe eme (menye top alo bottom o; ɖo le middle nu). Save file la.

```bash
git add Contributors.md
```

Commit changes:

```bash
git commit -m "Add <your-name> to Contributors list"
```

## Push changes ɖe GitHub

```bash
git push -u origin your-branch-name
```

<details>
<summary><strong>Ne wòkpɔ push error:</strong></summary>

### Authentication error

Wònɔ be password authentication remove le 13 August 2021.

Kpɔ SSH tutorial.

Ne output la nye:

```
origin https://github.com/your-username/your_repo.git (fetch)
origin https://github.com/your-username/your_repo.git (push)
```

Change remote:

```bash
git remote set-url origin git@github.com:your-username/your_repo.git
```
</details>

## Submit wò changes ɖe review

Yi wò GitHub repo la eye click button `Compare & pull request`.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Submit Pull Request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Wò changeswo ná merge to main branch soon eye wòakpɔ email notification.

## Ale gbɔna?

Wòtsɔ fla dzɔgbevi la! Wòwɔ full workflow la: fork → clone → edit → pull request.

Celebrate contribution eye share kple friends & followers using [web app](https://firstcontributions.github.io/#social-share).

Ne wòle be nàdzɔ do kple exercise bubuwo, kpɔ [code contributions](https://github.com/roshanjossey/code-contributions).

Start gake ɖe projects bubuwo — wòakpɔ beginner tasks le wò web page.
[Kpɔ list of projects here](https://firstcontributions.github.io/#project-list).

### [Additional materials](additional-material/git_workflow_scenarios/additional-material.md)

## Tutorials with GUI tools
(Links remain unchanged)

<p>Ta dɔa na project sia:</p>

<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>
