[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![ലൈസൻസ്: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Contributors](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# ആദ്യ സംഭാവനകൾ

\| <img alt="Git Bash" src="https://cdn.icon-icons.com/icons2/2699/PNG/512/git_scm_logo_icon_170096.png" width="200"> | Git Bash പതിപ്പ് |
\| ------------------------------------------------- ------------------------------------------------- ------------- | ---------------- |

ആദ്യമായി എന്തെങ്കിലും ചെയ്യുമ്പോൾ എല്ലായ്പ്പോഴും അത് കഠിനമായി തോന്നും. പ്രത്യേകിച്ച് സഹകരിച്ച് പ്രവർത്തിക്കുമ്പോൾ തെറ്റുകൾ ചെയ്യുന്നത് ആരും ഇഷ്ടപ്പെടില്ല. പക്ഷേ **ഓപ്പൺ സോഴ്‌സ്** സഹകരണവും കൂട്ടായ പ്രവർത്തനവുമാണ്. പുതിയ സംഭാവനക്കാർക്ക് അവരുടെ **ആദ്യ സംഭാവന** നൽകുന്നത് എളുപ്പമാക്കാൻ ഞങ്ങൾ ആഗ്രഹിക്കുന്നു.

ലേഖനങ്ങൾ വായിക്കുകയോ ട്യൂട്ടോറിയലുകൾ കാണുകയോ ചെയ്യുന്നത് സഹായകരമാണ്, പക്ഷേ നേരിട്ട് ചെയ്യുന്നതിന് പകരമൊന്നുമില്ല.
ഈ പ്രോജക്റ്റ് പുതിയവർക്ക് അവരുടെ ആദ്യ സംഭാവന നൽകുന്നത് ലളിതമാക്കുകയാണ് ലക്ഷ്യം.
ഒരുപക്ഷേ നിങ്ങൾക്ക് ശാന്തമായിരുന്നാൽ നിങ്ങൾ കൂടുതൽ മികച്ച രീതിയിൽ പഠിക്കും.

 നിങ്ങൾ നിങ്ങളുടെ ആദ്യ സംഭാവന നൽകാൻ ആഗ്രഹിക്കുന്നുവെങ്കിൽ, താഴെ കാണുന്ന ലളിതമായ ഘട്ടങ്ങൾ പിന്തുടരുക.

നിങ്ങളുടെ **Windows കമ്പ്യൂട്ടറിൽ Git Bash ഇല്ലെങ്കിൽ**, [ഇവിടെ നിന്ന് ഇൻസ്റ്റാൾ ചെയ്യുക](https://git-scm.com/download/win).

<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/fork.png" alt="ഈ റീപോസിറ്ററി Fork ചെയ്യുക" />  

## ഈ റീപോസിറ്ററി Fork ചെയ്യുക

ഈ പേജിന്റെ മുകളിലെ വലത് വശത്ത് കാണുന്ന **Fork** ബട്ടൺ അമർത്തി ഈ റീപോയെ Fork ചെയ്യുക.
ഇത് നിങ്ങളുടെ GitHub അക്കൗണ്ടിൽ ഒരു പകർപ്പ് സൃഷ്ടിക്കും.

## റീപോസിറ്ററി Clone ചെയ്യുക

ഇപ്പോൾ നിങ്ങളുടെ **Fork ചെയ്ത റീപോ** നിങ്ങളുടെ കമ്പ്യൂട്ടറിലേക്ക് Clone ചെയ്യുക.

 പ്രധാനമാണ്: **ഒറിജിനൽ റീപോ** Clone ചെയ്യരുത്. നിങ്ങളുടെ Fork ചെയ്‌തത് മാത്രം Clone ചെയ്യുക.

Clone ചെയ്യാൻ “Code” അമർത്തി, താഴെ കാണുന്ന URL copy ചെയ്യുക.

```bash
git clone <repo-url>
```

പിന്നീട് നിങ്ങൾ Clone ചെയ്ത റീപോ തുറക്കാൻ git bash (അല്ലെങ്കിൽ VS Code) ഉപയോഗിക്കുക.

## ഒരു ബ്രാഞ്ച് സൃഷ്ടിക്കുക

ഒരു പുതിയ ബ്രാഞ്ച് സൃഷ്ടിക്കാൻ:

```bash
git checkout -b <branch-name>
```

 ഉദാഹരണം: `add-your-name`

## ആവശ്യമായ മാറ്റങ്ങൾ വരുത്തുക

ഇപ്പോൾ `Contributors.md` ഫയൽ തുറന്ന്, ഏറ്റവും അവസാനം നിങ്ങളുടെ പേര് ചേർത്ത് **save** ചെയ്യുക.

ഉദാഹരണം:

```
[ജിതിൻ പി](https://github.com/jithin-dotcom)
```

ഫയൽ മാറ്റം വന്നിട്ടുണ്ടോ എന്ന് പരിശോധിക്കാൻ:

```bash
git status
```

## മാറ്റങ്ങൾ Commit ചെയ്യുക

```bash
git add Contributors.md
git commit -m "നിങ്ങളുടെ പേര് Contributors പട്ടികയിൽ ചേർത്തു"
```

Commit വിജയമായോ എന്ന് അറിയാൻ:

```bash
git log --oneline
```

## മാറ്റങ്ങൾ GitHub-ലേക്ക് Push ചെയ്യുക

```bash
git push origin <branch-name>
```

ഇതിന് ശേഷം, GitHub-ൽ നിങ്ങളുടെ Fork തുറക്കുമ്പോൾ **Compare & pull request** ബട്ടൺ കാണും.
അത് അമർത്തി **Pull Request** തുറക്കുക. 🎉

---
