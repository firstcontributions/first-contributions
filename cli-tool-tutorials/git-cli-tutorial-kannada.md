
---

[![ಓಪನ್ ಸೋರ್ಸ್ ಪ್ರೀತಿ](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![ಲೈಸೆನ್ಸ್: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![ಓಪನ್ ಸೋರ್ಸ್ ಸಹಾಯಕರು](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# ಮೊಟ್ಟ ಮೊದಲನೆಯ ಕೊಡುಗೆಗಳು

| <img alt="GitHub ಡೆಸ್ಕ್‌ಟಾಪ್" src="https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png" width="200"> | GitHub ಕಮಾಂಡ್ ಲೈನ್ ಇಂಟರ್‌ಫೇಸ್ (CLI) |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|

ಇದು ಟರ್ಮಿನಲ್ ನರ್ಡ್ಸ್ ಎಂದರೆ, ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ ಎಲ್ಲವನ್ನೂ ಮಾಡಲು ಬಯಸುವ ನಮಗೆ ಮಾರ್ಗದರ್ಶಿ ಮತ್ತು [Github-CLI](https://cli.github.com/) ಗೆ ಧನ್ಯವಾದಗಳು, ನಾವು ಇದನ್ನು ಸಾಧಿಸಬಹುದು, ನಿಮ್ಮ ಮೊದಲ ಕೊಡುಗೆಯನ್ನು ಮೋಜಿನ, ಪ್ರಶಸ್ತಿಯ ಮತ್ತು ಮುಂದುವರಿಯಲು ಉತ್ತೇಜಕವಾಗಿರಬೇಕು ಎಂದು ನೆನೆಸಿಕೊಳ್ಳಿ!

ಈ ಮಾರ್ಗದರ್ಶಿ ಸ್ವಲ್ಪ ಹೆಚ್ಚು ಸವಾಲಿನಂತಿರುತ್ತದೆ ಏಕೆಂದರೆ ನಾವು ಯಾವುದೇ ಗ್ರಾಫಿಕಲ್ ಇಂಟರ್‌ಫೇಸ್ ಅನ್ನು ಬಳಸುತ್ತಿಲ್ಲ, ಆದರೆ ಇದು ಹೀಗೆಯೇ ಸಿಹಿ ಮತ್ತು ನೀವು ಖಚಿತವಾಗಿ ಅದನ್ನು ಅನುಸರಿಸಬಹುದು!

ಮೊದಲ ಅಗತ್ಯವಂತದ್ದು:
- Git ಅನ್ನು ಸ್ಥಾಪಿತ ಮಾಡಬೇಕು (ಹೇಗೆ ಸ್ಥಾಪಿಸಲು [git](https://git-scm.com/downloads))
- Github ಖಾತೆ

ಇದಕ್ಕೆ ನಂತರ, ನಮ್ಮ ಸಿಸ್ಟಮ್‌ನಲ್ಲಿ `github-cli` ಸಾಧನವನ್ನು [ಆಧಿಕಾರಿಕ ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://github.com/cli/cli#installation) ಅನ್ನು ಅನುಸರಿಸಿ ಸ್ಥಾಪಿಸಬೇಕು.

ಆಮೇಲೆ, CLI ಗೆ ಲಾಗಿನ್ ಆಗಬೇಕಾಗಿದೆ, ಆದ್ದರಿಂದ ಈ ಕಮಾಂಡ್ ಅನ್ನು ನಮೂದಿಸಿ:
```bash 
gh auth login
```

ನಿರ್ದೇಶಗಳನ್ನು ಅನುಸರಿಸಿ ಮತ್ತು ನಾವು ತಯಾರಾಗಿದ್ದೇವೆ!

# ಈ ರೆಪೊಸಿಟರಿಯನ್ನು ಫೋರ್ಕ್ ಮಾಡಿ
ಇದು ಈ ಕಮಾಂಡ್ ಅನ್ನು ಓಡಿಸುವಷ್ಟು ಸುಲಭ:

```bash
gh repo fork firstcontributions/first-contributions
```
**ಮಹತ್ವಪೂರ್ಣ: ಇದು ನೀವು ಅದನ್ನು ಕ್ಲೋನ್ ಮಾಡಲು ಇಚ್ಛಿಸುತ್ತೀರಾ ಎಂದು ಕೇಳುತ್ತದೆ, "ಹೌದು" ಆಯ್ಕೆಯನ್ನು ಆಯ್ಕೆ ಮಾಡಿ**

# ನಿಮ್ಮ ಶಾಖೆಯನ್ನು ರಚಿಸಿ
ನಾವು ಈ ಹಂತವನ್ನು git ಮೂಲಕ ಮಾಡುತ್ತೇವೆ, ಆದ್ದರಿಂದ ಈ ಕಮಾಂಡ್ ಅನ್ನು ನೀವು ರಚಿಸಿದ ಶಾಖೆಯ ಹೆಸರು ಇನ್‌ಪುಟ್ ಮಾಡಬೇಕಾಗಿದೆ, ಉದಾಹರಣೆಗೆ:
```bash 
git switch -c add-john-doe
```

# ಅಗತ್ಯವಿರುವ ಬದಲಾವಣೆಗಳನ್ನು ಮಾಡಿ ಮತ್ತು ಇ那些 ಬದಲಾವಣೆಗಳನ್ನು ಕಮಿಟ್ ಮಾಡಿ
ಇದನ್ನು ಮಾಡಿದ ನಂತರ, `Contributors.md` ಫೈಲ್ ಅನ್ನು ಪಠ್ಯ ಸಂಪಾದಕದಲ್ಲಿ ತೆರೆಯಿರಿ ಮತ್ತು ನಿಮ್ಮ ಹೆಸರು ಸೇರಿಸಿ. ನಿಮ್ಮ ಹೆಸರನ್ನು ಆರಂಭ ಮತ್ತು ಅಂತ್ಯದ ನಡುವೆ ಎಲ್ಲಿಯೊ ಹಾಕಿ, ನಂತರ ಫೈಲ್ ಅನ್ನು ಉಳಿಸಿ.

ಪ್ರಾಜೆಕ್ಟ್ ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ `git status` ಅನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಿ ಮತ್ತು ನೀವು ಬದಲಾವಣೆಗಳನ್ನು ನೋಡಬಹುದು.
![image-git](https://camo.githubusercontent.com/a35c4722d7aab337eefc655d1488f7b4dc038508e6adaf5e88e2e052a976f010/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f6769742d7374617475732e706e67)

ಈ ಬದಲಾವಣೆಗಳನ್ನು ನೀವು ಹಾಲಿ ರಚಿಸಿದ ಶಾಖೆಗೆ ಸೇರಿಸಲು `git add` ಕಮಾಂಡ್ ಅನ್ನು ಬಳಸಿಸಿ:
`git add Contributors.md`

ಈ ಬದಲಾವಣೆಗಳನ್ನು ಕಮಿಟ್ ಮಾಡಲು `git commit` ಕಮಾಂಡ್ ಅನ್ನು ಬಳಸಿಸಿ:
`git commit -m "Add your-name to Contributors list"`
`your-name` ಅನ್ನು ನಿಮ್ಮ ಹೆಸರಿನಿಂದ ಬದಲಾಯಿಸಿ.

# Github ಗೆ ಬದಲಾವಣೆಗಳನ್ನು ಪುಷ್ ಮಾಡಿ
ನಿಮ್ಮ ಬದಲಾವಣೆಗಳನ್ನು `git push` ಕಮಾಂಡ್ ಅನ್ನು ಬಳಸಿಕೊಂಡು ಪುಷ್ ಮಾಡಿ:

```
git push origin -u your-branch-name
```

`your-branch-name` ಅನ್ನು ನೀವು ಮೊದಲು ರಚಿಸಿದ ಶಾಖೆಯ ಹೆಸರು ಮೂಲಕ ಬದಲಾಯಿಸಿ.

<details>
<summary> <strong>ನಿಮ್ಮ ಬದಲಾವಣೆಗಳನ್ನು ಪುಷ್ ಮಾಡುವಾಗ ಯಾವುದೇ ದೋಷಗಳನ್ನು ಎದುರಿಸಿದರೆ, ಇಲ್ಲಿ ಕ್ಲಿಕ್ ಮಾಡಿ:</strong> </summary>

- ### ಪ್ರಮಾಣೀಕರಣ ದೋಷ
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  [GitHub ಗಳು SSH ಕೀ ಅನ್ನು ನಿಮ್ಮ ಖಾತೆಗೆ ಸೇರಿಸಲು ಮತ್ತು ನಿಯಂತ್ರಣವನ್ನು configure ಮಾಡುವುದು](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) ಕುರಿತು ಟ್ಯುಟೋರಿಯಲ್ ಅನ್ನು ನೋಡಿ.

</details>

# ನಿಮ್ಮ ಬದಲಾವಣೆಗಳನ್ನು ವಿಮರ್ಶೆಗೆ ಸಲ್ಲಿಸಿ
ನಮ್ಮ ರೆಪೋಸಿಟರಿಯ ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ ಈ ಕಮಾಂಡ್ ಅನ್ನು ಓಡಿಸುವ ಮೂಲಕ, ವಿಮರ್ಶೆಗೆ ಪುಲ್ ರಿಕ್ವೆಸ್ಟ್ ಅನ್ನು ರಚಿಸಬಹುದು:

```bash 
gh pr create --repo firstcontributions/first-contributions
```

ಮರು submit the pull request.

ನಿಮ್ಮ ಪುಲ್ ರಿಕ್ವೆಸ್ಟ್ ಅನ್ನು ಚಲನೆಯಲ್ಲಿಯೂ ನೋಡಲು `gh status` ಕಮಾಂಡ್ ಅನ್ನು ಬಳಸಬಹುದು.

## ಈಗ ಎಲ್ಲಿ ಹೋಗಬೇಕು?

ಶುಭಾಶಯಗಳು! ನೀವು ಶ್ರೇಣೀಬದ್ಧವಾದ _fork -> clone -> edit -> pull request_ ಕಾರ್ಯಾಚರಣೆಯನ್ನು ಸಂಪೂರ್ಣವಾಗಿಸಿದ್ದೀರಿ, ಇದು ನೀವು ಕೊಡುಗೆಯಾಗಿ ಸಾಮಾನ್ಯವಾಗಿ ಭೇಟಿಯಾಗುವ ಪರಿಕ್ರಮೆ!

ನಿಮ್ಮ ಕೊಡುಗೆಯನ್ನು ಆಚರಿಸಿ ಮತ್ತು [ವೆಬ್ ಆಪ್](https://firstcontributions.github.io/#social-share) ಗೆ ಹೋಗಿ ಮತ್ತು ನಿಮ್ಮ ಸ್ನೇಹಿತರು ಮತ್ತು ಅನುಯಾಯಿಗಳಿಗೆ ಹಂಚಿಕೊಳ್ಳಿ.

ನೀವು ಸಹಾಯ ಅಥವಾ ಪ್ರಶ್ನೆಗಳಿದ್ದರೆ ನಮ್ಮ ಸ್ಲಾಕ್ ತಂಡವನ್ನು ಸೇರಿಕೊಳ್ಳಬಹುದು. [Slack ತಂಡವನ್ನು ಸೇರಿಕೊಳ್ಳಿ](https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA).

ಇಲ್ಲಿಯೇ ಇನ್ನೂ ಹೆಚ್ಚಿನ ಪ್ರಾಜೆಕ್ಟ್‌ಗಳಿಗೆ ಕೊಡುಗೆಯನ್ನೂ ಪ್ರಾರಂಭಿಸಲು ನಿಮಗೆ ಸಹಾಯವಾಗುತ್ತದೆ. ಸುಲಭವಾದ ಸಮಸ್ಯೆಗಳೊಂದಿಗೆ ಪ್ರಾಜೆಕ್ಟ್‌ಗಳ ಪಟ್ಟಿಯನ್ನು ನಾವು ಸಂಗ್ರಹಿಸಿದ್ದೇವೆ. [ವೆಬ್ ಆಪ್‌ನಲ್ಲಿ ಪ್ರಾಜೆಕ್ಟ್‌ಗಳ ಪಟ್ಟಿಯನ್ನು](https://firstcontributions.github.io/#project-list) ಪರಿಶೀಲಿಸಿ.

### [ಮೂಲಿಕ ವಸ್ತು](additional-material/git_workflow_scenarios/additional-material.md)

## ಇತರ ಸಾಧನಗಳನ್ನು ಬಳಸುವ ಟ್ಯುಟೋರಿಯಲ್‌ಗಳು

[ಮುಖ್ಯ ಪುಟಕ್ಕೆ ಹಿಂದಿರುಗಿ](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)

---

Feel free to let me know if you need any further adjustments or additions!