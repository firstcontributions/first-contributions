[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![](https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/join-slack-team.png)](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# మొదటి సహకారాలు (First Contributions)

| [![GitHub Desktop](https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png)](https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png) | GitHub Command Line Interface (CLI) |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- |

ఇది టెర్మినల్‌లో అన్ని పనులు చేయాలనుకునే మనలాంటి గీక్స్ కోసం ఒక గైడ్. [Github-CLI](https://cli.github.com/) సహాయంతో, మనం ఇది సాధించవచ్చు — మరియు మీ మొదటి సహకారం ఆనందంగా, సంతృప్తికరంగా మరియు మళ్ళీ మళ్ళీ చేయాలనిపించేలా ఉండాలి!

ఈ గైడ్ కొంచెం కష్టంగా ఉంటుంది, ఎందుకంటే మనం గ్రాఫికల్ ఇంటర్‌ఫేస్ అస్సలు వాడం — కానీ ఇది చాలా ఆసక్తికరంగా ఉంటుంది మరియు మీరు తప్పకుండా దీన్ని అనుసరించగలరు!

మొదట కావలసినవి:

- Git ఇన్‌స్టాల్ చేయబడి ఉండాలి ([git ఇన్‌స్టాల్ చేయడం ఎలా](https://git-scm.com/downloads))
- GitHub అకౌంట్ ఉండాలి

ఇప్పుడు, [అధికారిక డాక్యుమెంటేషన్](https://github.com/cli/cli#installation) అనుసరించి మన సిస్టమ్‌లో `github-cli` టూల్ ఇన్‌స్టాల్ చేయాలి.

తర్వాత CLI లో లాగిన్ అవ్వాలి, కాబట్టి ఈ కమాండ్ నమోదు చేయండి:

```
gh auth login
```

సూచనలు అనుసరించండి, అంతే!

---

# ఈ రిపోజిటరీని Fork చేయండి

ఇది చాలా సులభం, ఈ కమాండ్ అమలు చేయండి:

```
gh repo fork firstcontributions/first-contributions
```

**ముఖ్యమైనది: Clone కూడా చేయాలా అని అడుగుతారు, "yes" అని ఎంచుకోండి.**

---

# మీ Branch తయారు చేయండి

ఈ దశలో git వాడతాం, కాబట్టి ఈ కమాండ్ నమోదు చేయండి — `name` స్థానంలో మీ పేరు పెట్టండి, ఉదాహరణకు:

```
git switch -c add-john-doe
```

---

# అవసరమైన మార్పులు చేసి Commit చేయండి

ఇప్పుడు `Contributors.md` ఫైల్ ఒక టెక్స్ట్ ఎడిటర్‌లో తెరవండి మరియు మీ పేరు దానిలో జోడించండి. ఫైల్ మొదట్లో లేదా చివర్లో కాకుండా, మధ్యలో ఎక్కడైనా మీ పేరు జోడించి, ఫైల్ సేవ్ చేయండి.

ప్రాజెక్ట్ డైరెక్టరీలో `git status` అమలు చేయండి, అప్పుడు మార్పులు కనిపిస్తాయి.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

ఈ మార్పులను మీరు తయారు చేసిన branch కి `git add` కమాండ్ ద్వారా జోడించండి:

```
git add Contributors.md
```

ఇప్పుడు `git commit` కమాండ్ ద్వారా ఆ మార్పులను commit చేయండి:

```
git commit -m "Add your-name to Contributors list"
```

`your-name` స్థానంలో మీ అసలు పేరు పెట్టండి.

---

# GitHub కి మార్పులు Push చేయండి

`git push` కమాండ్ ద్వారా మీ మార్పులు push చేయండి:

```
git push origin -u your-branch-name
```

`your-branch-name` స్థానంలో మీరు ముందు తయారు చేసిన branch పేరు పెట్టండి.

<details>
<summary> <strong>Push చేసేటప్పుడు errors వస్తే, ఇక్కడ క్లిక్ చేయండి:</strong> </summary>

- ### Authentication Error

<pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
fatal: Authentication failed for 'https://github.com/&lt;your-username&gt;/first-contributions.git/'</pre>

SSH key తయారు చేసి GitHub అకౌంట్‌కు జోడించడానికి [GitHub యొక్క ట్యుటోరియల్](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) చూడండి.

</details>

---

# మీ మార్పులను Review కి Submit చేయండి

ఇప్పుడు, మన రిపోజిటరీ డైరెక్టరీలో ఈ కమాండ్ అమలు చేయడం ద్వారా review కోసం pull request తయారు చేయవచ్చు:

```
gh pr create --repo firstcontributions/first-contributions
```

తర్వాత pull request పంపండి.

మీ pull request యొక్క స్థితి చూడటానికి `gh status` కమాండ్ వాడవచ్చు.

---

## తదుపరి ఏమి చేయాలి?

అభినందనలు! మీరు contributor గా తరచుగా ఉపయోగించే సాధారణ *fork → clone → edit → pull request* వర్క్‌ఫ్లో పూర్తి చేశారు!

మీ సహకారాన్ని సంబరంగా జరుపుకోండి మరియు [web app](https://firstcontributions.github.io/#social-share) కి వెళ్ళి మీ స్నేహితులతో మరియు followers తో share చేసుకోండి.

సహాయం అవసరమైతే లేదా మీకు ఏమైనా ప్రశ్నలు ఉంటే మన Slack టీమ్‌లో చేరవచ్చు. [Slack టీమ్‌లో చేరండి](https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA).

ఇప్పుడు ఇతర ప్రాజెక్ట్‌లకు సహకరించడం మొదలుపెడదాం. మీరు ప్రారంభించగల సులభమైన సమస్యలతో ఉన్న ప్రాజెక్ట్‌ల జాబితా కోసం [web app లో ప్రాజెక్ట్ జాబితా](https://firstcontributions.github.io/#project-list) చూడండి.

### [అదనపు మెటీరియల్](additional-material/git_workflow_scenarios/additional-material.md)

---

## ఇతర టూల్స్ ఉపయోగించి ట్యుటోరియల్స్

[ప్రధాన పేజీకి తిరిగి వెళ్ళండి](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
