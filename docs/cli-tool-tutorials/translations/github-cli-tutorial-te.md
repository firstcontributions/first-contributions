[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# మొదటి సహకారం

| <img alt="GitHub Desktop" src="https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png" width="200"> | GitHub Command Line Interface (CLI) |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |

ఇది మాకు ఒక గైడ్, టెర్మినల్ నెర్డ్స్, ఎవరైతే టెర్మినల్‌లో ప్రతిదీ చేయాలనుకుంటారు, మరియు [Github-CLI](https://cli.github.com/)కు ధన్యవాదాలు, మేము దీన్ని సాధించగలము, మీ మొదటి సహకారం సరదాగా, బహుమతినిచ్చేది మరియు కొనసాగించడానికి ప్రేరేపకంగా ఉండాలని గుర్తుంచుకోండి!

ఈ గైడ్ కొంచెం ఎక్కువ సవాలుగా ఉంటుంది ఎందుకంటే మేము ఏదైనా గ్రాఫికల్ ఇంటర్‌ఫేస్‌ను ఉపయోగించడం లేదు, కానీ ఇది ఇప్పటికీ నిజంగా సరదాగా ఉంటుంది మరియు మీరు ఖచ్చితంగా దీన్ని అనుసరించగలరు!

మొదటి అవసరం:

- Git ఇన్‌స్టాల్ చేయబడి ఉండాలి ([git](https://git-scm.com/downloads) ఎలా ఇన్‌స్టాల్ చేయాలి)
- Github ఖాతా

ఇప్పుడు మన సిస్టమ్‌లో `github-cli` టూల్‌ను [అధికారిక డాక్యుమెంటేషన్](https://github.com/cli/cli#installation)ను అనుసరించి ఇన్‌స్టాల్ చేయాలి

దాని తర్వాత, మనం CLIలో లాగిన్ అవ్వాలి, కాబట్టి ఈ కమాండ్‌ను ఎంటర్ చేయండి:

```bash
gh auth login
```

సూచనలను అనుసరించండి మరియు మేము సిద్ధంగా ఉన్నాము!

# ఈ రిపోజిటరీని ఫోర్క్ చేయండి

ఈ కమాండ్‌ను రన్ చేయడం ఎంత సులభమో:

```bash
gh repo fork firstcontributions/first-contributions
```

**ముఖ్యమైనది: మీరు దీన్ని కూడా క్లోన్ చేయాలనుకుంటున్నారా అని అడుగుతుంది, "yes" ఆప్షన్‌ను ఎంచుకోండి**

# మీ బ్రాంచ్‌ను సృష్టించండి

మేము ఈ దశను gitతో చేస్తాము, కాబట్టి ఈ కమాండ్‌ను మీ పేరుతో ఎంటర్ చేయండి, ఉదాహరణకు:

```bash
git switch -c add-రామ-కృష్ణ
```

# అవసరమైన మార్పులు చేయండి మరియు ఆ మార్పులను కమిట్ చేయండి

ఇప్పుడు మీరు `Contributors.md` ఫైల్‌ను టెక్స్ట్ ఎడిటర్‌లో తెరవవచ్చు మరియు దానిలో మీ పేరును జోడించవచ్చు. ప్రారంభం మరియు ముగింపు మధ్య ఎక్కడైనా మీ పేరును ఉంచండి, తర్వాత ఫైల్‌ను సేవ్ చేయండి.

ప్రాజెక్ట్ డైరెక్టరీలో `git status` ని ఎక్సిక్యూట్ చేయండి మరియు మీరు మార్పులను చూస్తారు.
<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

`git add` కమాండ్‌ను ఉపయోగించి ఆ మార్పులను మీరు సృష్టించిన బ్రాంచ్‌లో జోడించండి:
`git add Contributors.md`

ఇప్పుడు `git commit` కమాండ్‌ను ఉపయోగించి ఆ మార్పులను కమిట్ చేయండి:
`git commit -m "Add your-name to Contributors list`
`your-name` ను మీ పేరుతో మార్చండి.

# GitHubకి మార్పులను పుష్ చేయండి

`git push` కమాండ్‌ను ఉపయోగించి మీ మార్పులను పుష్ చేయండి:

```
git push origin -u your-branch-name
```

`your-branch-name` ను మీరు ముందుగా సృష్టించిన బ్రాంచ్‌ పేరుతో మార్చండి.

<details>
<summary> <strong>మీరు పుష్ చేస్తున్నప్పుడు ఏవైనా లోపాలు వస్తే, ఇక్కడ క్లిక్ చేయండి:</strong> </summary>

- ### ప్రమాణీకరణ లోపం
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  మీ ఖాతాకు SSH కీని రూపొందించడం మరియు కాన్ఫిగర్ చేయడంపై [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) వెళ్లండి.

</details>

# సమీక్ష కోసం మీ మార్పులను సమర్పించండి

ఇప్పుడు మా రిపో డైరెక్టరీలో ఈ కమాండ్‌ను రన్ చేయడం ద్వారా మేము సమీక్ష కోసం ఒక పుల్ రిక్వెస్ట్‌ను సృష్టించగలము:

```bash
gh pr create --repo firstcontributions/first-contributions
```

దాని తర్వాత పుల్ రిక్వెస్ట్‌ను సమర్పించండి.

మీ పేర్కొన్న పుల్ రిక్వెస్ట్‌ను చర్యలో చూడటానికి మీరు `gh status` కమాండ్‌ను ఉపయోగించవచ్చు.

## ఇక్కడ నుండి ఎక్కడికి వెళ్లాలి?

అభినందనలు! మీరు స్టాండర్డ్ _fork -> clone -> edit -> pull request_ వర్క్‌ఫ్లోను పూర్తి చేసారు, దీన్ని మీరు తరచుగా ఒక కంట్రిబ్యూటర్‌గా ఎదుర్కొంటారు!

[వెబ్ యాప్‌కి](https://firstcontributions.github.io/#social-share) వెళ్లడం ద్వారా మీ సహకారాన్ని జరుపుకోండి మరియు మీ స్నేహితులు మరియు అనుచరులతో భాగస్వామ్యం చేయండి.

మీకు ఏదైనా సహాయం అవసరమైతే లేదా ఏవైనా ప్రశ్నలు ఉంటే మీరు మా స్లాక్ టీమ్‌లో చేరవచ్చు.[స్లాక్ జట్టులో చేరండి](https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA)

ఇక, ఇప్పుడు మీరు ఇతర ప్రాజెక్టులకు తోడ్పడటం ప్రారంభించండి. మీరు ప్రారంభించగల సులభమైన సమస్యలతో ప్రాజెక్టుల జాబితాను మేము రెడీ చేసాము. [వెబ్ యాప్‌లోని ప్రాజెక్టుల జాబితాను](https://firstcontributions.github.io/#project-list) చూడండి.

### [అదనపు విషయం](additional-material/git_workflow_scenarios/additional-material.md)

## ఇతర సాధనాలను ఉపయోగించి ట్యుటోరియల్స్

[ముఖ్య పేజీకి తిరిగి](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
