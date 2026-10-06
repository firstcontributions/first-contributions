# First Contributions

| GitHub Desktop | GitHub Command Line Interface (CLI) |
|---|---|

இது terminal-ஐ பயன்படுத்த விரும்பும் நபர்களுக்கான வழிகாட்டி. GitHub CLI (`gh`) மூலம் முழு First Contribution workflow-ஐ graphical interface இல்லாமல் terminal-லேயே செய்யலாம்.

உங்கள் முதல் contribution **fun-ஆவும், rewarding-ஆவும், தொடர்ந்து Open Source-ல் contribute செய்ய motivation கொடுப்பதாகவும்** இருக்க வேண்டும்!

இந்த guide-ல் எந்த graphical interface-ஐயும் பயன்படுத்தப் போவதில்லை. கொஞ்சம் challenging-ஆ இருக்கும், ஆனால் ரொம்ப useful-ஆ இருக்கும்.

## தேவையானவை

முதலில் உங்களிடம் இவை இருக்க வேண்டும்:

- Git install செய்யப்பட்டிருக்க வேண்டும்.
- GitHub account இருக்க வேண்டும்.

Git-ஐ install செய்ய [Git](https://git-scm.com/downloads)-ன் official website-ஐ பயன்படுத்தலாம்.

அடுத்து உங்கள் system-ல் `GitHub CLI` (`gh`) install செய்ய வேண்டும். அதற்காக [official documentation](https://github.com/cli/cli#installation)-ஐ follow செய்யுங்கள்.

### GitHub CLI-ல் Login செய்வது

CLI-ல் login செய்ய:

```bash
gh auth login
```

Terminal காட்டும் instructions-ஐ follow செய்யுங்கள். Login முடிந்ததும் ready!

# Repository-ஐ Fork செய்வது

இந்த repository-ஐ fork செய்ய இந்த command-ஐ run செய்யுங்கள்:

```bash
gh repo fork firstcontributions/first-contributions
```

**முக்கியம்:** Repository-ஐ clone செய்ய வேண்டுமா என்று terminal கேட்கும்.

**"Yes" என்பதை select செய்யுங்கள்.**

இதனால் repository உங்கள் GitHub account-க்கு fork ஆகி, உங்கள் computer-லும் clone ஆகும்.

# உங்கள் Branch-ஐ உருவாக்குங்கள்

இந்த step-ல் Git-ஐ பயன்படுத்துவோம்.

உங்கள் பெயருக்கு ஏற்ற branch name-ஐ வைத்து:

```bash
git switch -c add-john-doe
```

உதாரணமாக, உங்கள் பெயர் John Doe என்றால்:

```bash
git switch -c add-john-doe
```

இது `add-john-doe` என்ற புதிய branch-ஐ உருவாக்கி அதற்கு switch செய்யும்.

# தேவையான மாற்றங்களை செய்து Commit செய்யுங்கள்

இப்போது `Contributors.md` file-ஐ text editor-ல் open செய்யுங்கள்.

அதில் உங்கள் பெயரை add செய்யுங்கள்.

உங்கள் பெயரை file-ன் beginning மற்றும் end-க்கு இடையில் எங்கு வேண்டுமானாலும் add செய்யலாம்.

File-ஐ save செய்த பிறகு project directory-ல்:

```bash
git status
```

என்று run செய்யுங்கள்.

இதனால் நீங்கள் செய்த changes-ஐ பார்க்கலாம்.

அடுத்து அந்த changes-ஐ staging area-க்கு add செய்யுங்கள்:

```bash
git add Contributors.md
```

பிறகு commit செய்யுங்கள்:

```bash
git commit -m "Add your-name to Contributors list"
```

இங்கே `your-name` என்பதற்கு உங்கள் பெயரை பயன்படுத்துங்கள்.

உதாரணம்:

```bash
git commit -m "Add John Doe to Contributors list"
```

# Changes-ஐ GitHub-க்கு Push செய்வது

இப்போது உங்கள் branch-ல் இருக்கும் changes-ஐ GitHub-க்கு push செய்ய வேண்டும்:

```bash
git push origin -u your-branch-name
```

உதாரணமாக உங்கள் branch:

```bash
add-john-doe
```

என்றால்:

```bash
git push origin -u add-john-doe
```

இதனால் உங்கள் branch GitHub-ல் உங்கள் fork செய்யப்பட்ட repository-க்கு push ஆகும்.

## Push செய்யும்போது Error வந்தால்

### Authentication Error

இப்படி ஒரு error வரலாம்:

```text
remote: Support for password authentication was removed on August 13, 2021.
Please use a personal access token instead.
```

GitHub இப்போது Git operations-க்கு சாதாரண password authentication-ஐ support செய்யாது.

இதற்கு GitHub account-ல் SSH key configure செய்யலாம்.

GitHub-ன் [SSH key tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)-ஐ follow செய்யுங்கள்.

# உங்கள் Changes-ஐ Review-க்கு Submit செய்வது

இப்போது உங்கள் changes-ஐ original repository-க்கு Pull Request ஆக submit செய்யலாம்.

இந்த command-ஐ run செய்யுங்கள்:

```bash
gh pr create --repo firstcontributions/first-contributions
```

GitHub CLI உங்களிடம் Pull Request பற்றிய சில details கேட்கும்.

அவற்றை fill செய்து Pull Request-ஐ submit செய்யுங்கள்.

உங்கள் Pull Request-ன் status-ஐ பார்க்க:

```bash
gh status
```

என்று பயன்படுத்தலாம்.

# அடுத்து என்ன?

🎉 **Congratulations!**

நீங்கள் இப்போது Open Source contribution-ல் பயன்படுத்தப்படும் ஒரு முக்கியமான workflow-ஐ complete செய்துவிட்டீர்கள்:

**Fork → Clone → Branch → Edit → Commit → Push → Pull Request**

இந்த workflow-ஐ நீங்கள் பல Open Source projects-ல் மீண்டும் மீண்டும் பயன்படுத்துவீர்கள்.

உங்கள் முதல் contribution-ஐ celebrate செய்யுங்கள்! அதை உங்கள் friends மற்றும் followers-உடன் [web app](https://firstcontributions.github.io/#social-share) மூலம் share செய்யலாம்.

மேலும் practice செய்ய விரும்பினால் [Code Contributions](https://github.com/roshanjossey/code-contributions)-ஐ பாருங்கள்.

அதற்குப் பிறகு மற்ற Open Source projects-ல் contribute செய்ய ஆரம்பிக்கலாம். Beginner-friendly issues கொண்ட projects-ஐ [project list](https://firstcontributions.github.io/#project-list)-ல் பார்க்கலாம்.

### கூடுதல் தகவல்கள்

[Additional Material](https://github.com/firstcontributions/first-contributions/blob/main/docs/additional-material/git_workflow_scenarios/additional-material.md)

[Main Page-க்கு திரும்ப](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)