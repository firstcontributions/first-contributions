[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# ആദ്യ സംഭാവനകൾ (First Contributions)

| <img alt="GitHub Desktop" src="https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png" width="100"> | GitHub കമാൻഡ് ലൈൻ ഇൻ്റർഫേസ് (CLI) |
| ------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |

ടെർമിനൽ ഉപയോഗിച്ച് എല്ലാം ചെയ്യാൻ ആഗ്രഹിക്കുന്ന നമുക്ക് വേണ്ടി ഉള്ളതാണ് ഈ വഴികാട്ടി (ഗൈഡ് ). [Github-CLI](https://cli.github.com/)ക്ക് നന്ദി , നമുക്ക് ഇപ്പോൾ അത് സാധ്യമാണ് . നിങ്ങളുടെ ആദ്യ സംഭാവന (first contribution) ഓർമ്മിക്കുന്നത് രസകരവും പ്രതിഫലദായകവും മുന്നോട്ട് പോകുവാൻ പ്രചോദനം നല്കുന്നതുമായിരിക്കണം !

ഒരു ഗ്രാഫിക്കൽ ഇൻ്റർഫേസും ഉപയോഗിക്കാത്തതിനാൽ ഈ ഗൈഡ് അൽപ്പം വെല്ലുവിളി നിറഞ്ഞതാണെങ്കിലും, ഇത് ഇപ്പോഴും വളരെ രസകരവും , തീർച്ചയായും നിങ്ങൾക്ക് പിന്തുടരാനാകുന്നതുമാണ് !

തുടങ്ങുന്നതിന് ആവശ്യമായ കാര്യങ്ങൾ:

- Git ഇൻസ്റ്റാൾ ചെയ്യുക ( എങ്ങിനെ [git](https://git-scm.com/downloads) ഇൻസ്റ്റാൾ ചെയ്യണം )
- Git അക്കൗണ്ട്

ഇനി നിങ്ങളുടെ കമ്പ്യൂട്ടറിലേക്ക് `github-cli` ടൂൾ ഇൻസ്റ്റാൾ ചെയ്യുന്നതിനായി [ഔദ്യോഗിക ഡോക്യൂമെന്റേഷൻ ](https://github.com/cli/cli#installation)'ൽ പറഞ്ഞിരിക്കുന്ന നിർദ്ദേശങ്ങൾ പിന്തുടരുക.

അതിനു ശേഷം CLI'ലേക്ക് ലോഗിൻ ചെയ്യുന്നതിനായി താഴെ പറയുന്ന കമാൻഡ് ഉപയോഗിക്കുക

```bash
gh auth login
```

താഴെ പറയുന്ന നിർദ്ദേശങ്ങൾ പാലിക്കുന്നതോടു കൂടി നിങ്ങൾ തയ്യാറായി കഴിഞ്ഞു

# ഈ റെപ്പോസിറ്ററി ഫോർക് ചെയ്യുക

ഇതിനായി താഴെ പറയുന്ന കമാൻഡ് റൺ ചെയ്‌താൽ മാത്രം മതി

```bash
git switch -c add-john-doe
```

# ആവശ്യമായ മാറ്റങ്ങൾ വരുത്തിയതിനു ശേഷം അത് കമ്മിറ്റ് ചെയ്യുക

ഇനി നിങ്ങൾക് `Contributors.md` ഫയൽ ഒരു ടെക്സ്റ്റ് എഡിറ്റർ ഉപയോഗിച്ച് തുറന്ന് നിങ്ങളുടെ പേര് അതിൽ ചേർക്കാവുന്നതാണ് . തുടക്കത്തിന്റെയും അവസാനത്ത്തിന്റെയും ഇടയിൽ എവിടെയെങ്കിലും ഒരു സ്ഥാനത്ത് നിങ്ങളുടെ പേര് ചേർത്തതിന് ശേഷം ഫയൽ സേവ് ചെയ്യുക.

പ്രൊജക്റ്റ് ഡിറക്ടറിയിൽ `git status` എന്ന കമാൻഡ് ഉപയോഗിച്ച് നിങ്ങൾക് നിങ്ങൾ വരുത്തിയ മാറ്റങ്ങൾ കാണാനാകുന്നതാണ്.
<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

ആ മാറ്റങ്ങൾ `git add` കമാൻഡ് ഉപയോഗിച്ച് നിങ്ങളുടെ ബ്രാഞ്ചിലേക്ക് ചേർക്കുക:
`git add Contributors.md`

ഇനി ഈ മാറ്റങ്ങൾ `git commit`കമാൻഡ് ഉപയോഗിച്ച് കമ്മിറ്റ് ചെയ്യുക:
`git commit -m "Add your-name to Contributors list`
`your-name`നു പകരം നിങ്ങളുടെ പേര് ആണ് ഉപയോഗിക്കേണ്ടത് .

# മാറ്റങ്ങൾ github'ലേക്ക് പുഷ് ചെയ്യുക

നിങ്ങൾ വരുത്തിയ മാറ്റങ്ങൾ `git push` കമാൻഡ് ഉപയോഗിച്ച് പുഷ് ചെയ്യുക:

```
git push origin -u your-branch-name
```

`your-branch-name`നു പകരം നിങ്ങൾ നേരത്തെ ഉണ്ടാക്കിയ ബ്രാഞ്ചിന്റെ പേര് വേണം ഉപയോഗിക്കാൻ.

<details>
<summary> <strong>പുഷ് ചെയ്യുന്നതിനിടക്ക് പ്രശനങ്ങൾ(errors) സംഭവിക്കുകയാണെങ്കിൽ ഇവിടെ ക്ലിക്ക് ചെയ്യുക :</strong> </summary>

- ### പ്രാമാണീകരണപിശക് (Authentication Error)
       <pre>റിമോട്ട്: പാസ്‌വേഡ് പ്രാമാണീകരണത്തിനുള്ള പിന്തുണ 2021 ഓഗസ്റ്റ് 13-ന് നീക്കം ചെയ്‌തു. പകരം ഒരു വ്യക്തിഗത ആക്‌സസ് ടോക്കൺ ഉപയോഗിക്കുക.
  റിമോട്ട്: കൂടുതൽ വിവരങ്ങൾക്ക് https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ കാണുക.
  fatal:'https://github.com/<your-username>/first-contributions.git/'ലേക്കുള്ള authentication പരാജയപ്പെട്ടു .</pre>
  നിങ്ങളുടെ അക്കൗണ്ടിലേക്ക് ഒരു SSH കീ നിർമ്മിക്കുവാനും ക്രമീകരിക്കുവാനുമായി ഈ ലിങ്കിലേക്ക് പോകുക [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) .
  </details>

## നിങ്ങളുടെ വ്യത്യാസങ്ങൾ പരിശോധനക്കായി (review) സമർപ്പിക്കുക

നിങ്ങളുടെ റെപ്പോസിറ്റോറിയിൽ താഴെ പറയുന്ന കമാൻഡ് റൺ ചെയ്യുന്നതോടെ പരിശോധനക്കായി ഒരു pull request ഉണ്ടാക്കുവാൻ നിങ്ങൾക് സാധിക്കും.

```bash
gh pr create --repo firstcontributions/first-contributions
```

അതിനു ശേഷം pull request സമർപ്പിക്കുക.
നിങ്ങളുടെ സൂചിപ്പിച്ച pull request പ്രവർത്തനക്ഷമമായി കാണുന്നതിന് നിങ്ങൾക്ക് `gh status`കമാൻഡ് ഉപയോഗിക്കാം.

## ഇവിടെ നിന്ന് ഇനി എങ്ങോട്ട്?

അഭിനന്ദനങ്ങൾ! ഒരു സംഭാവകൻ എന്ന നിലയിൽ നിങ്ങൾ പലപ്പോഴും അഭിമുഖീകരിക്കുന്ന സ്റ്റാൻഡേർഡ് ഫോർക്ക് -> ക്ലോൺ -> എഡിറ്റ് -> പുൾ അഭ്യർത്ഥന വർക്ക്ഫ്ലോ നിങ്ങൾ ഇപ്പോൾ പൂർത്തിയാക്കി!

തങ്ങളുടെ സംഭാവന സുഹൃത്തുക്കളും പിൻഗാമികളും ആയി പങ്കിടുന്നതിനും ആഘോഷിക്കുന്നതിനും ആയി [വെബ് ആപ്പ് ](https://firstcontributions.github.io/#social-share)ലേക്ക് പോകുക.

താങ്കൾക് എന്ധെങ്കിലും സഹായം വേണമെങ്കിലോ എന്ധെങ്കിലും ചോദ്യങ്ങൾ ഉണ്ടെങ്കിലോ നമ്മുടെ Slack ടീമിൽ ചേരാവുന്നതാണ് . [Slack ടീമിൽ ചേരുക ](https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA).

ഇനി താങ്കൾക് മറ്റു പ്രോജെക്ടസിലേക്കും സംഭാവന നടത്താൻ സാധിക്കും. താങ്കൾക് ചെയ്ത തുടങ്ങാവുന്ന എളുപ്പമുള്ള പിശകുകൾ ഉള്ള പ്രോജെക്ടസിന്റെ ഒരു ലിസ്റ്റ് ഞങ്ങൾ തയ്യാറാക്കിയിട്ടുണ്ട്. [പ്രോജക്ടുകളുടെ ലിസ്റ്റ് ](https://firstcontributions.github.io/#project-list) കാണുക .

### [കൂടുതൽ വായിക്കുക](../additional-material/git_workflow_scenarios/additional-material.md)

## മറ്റു ടൂൾസ് ഉപയോഗിച്ച് ചെയ്യുന്നതിനുള്ള നിർദ്ദേശങ്ങൾ

[പ്രധാന പേജിലേക്ക് പോകുക ](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
