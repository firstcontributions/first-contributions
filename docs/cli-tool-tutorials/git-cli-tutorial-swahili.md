[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Mchango wa Kwanza

| <img alt="GitHub Desktop" src="https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png" width="200"> | GitHub Command Line Interface (CLI) |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |

Haya ni mwongozo kwetu sisi, watu wenye ujuzi wa terminal, ambao wanataka kufanya kila kitu kwenye terminal, na shukrani kwa Github-CLI((https://cli.github.com/)), tunaweza kufanikisha hili, tukikumbuka mchango wako wa kwanza unapaswa kuwa wa kufurahisha, wenye manufaa, na chachu ya kuendelea!

Mwongozo huu ni mgumu kidogo kwani hatutumii kiolesura chochote cha picha (graphical interface) kabisa, lakini bado ni wa kufurahisha sana na hakika unaweza kuufuata!

Sharti la kwanza ni kuwa na:
- Git imesakinishwa (jinsi ya kusakinisha[git](https://git-scm.com/downloads))
- Akaunti ya Github

Sasa tunahitaji kusakinisha zana ya github-cli kwenye mfumo wetu kwa kufuata nyaraka rasmi(https://github.com/cli/cli#installation)

Baada ya hapo, tunahitaji kuingia (login) kwenye CLI, kwa hivyo ingiza amri hii:

```bash
gh auth login
```

Fuata maelekezo na tutakuwa tayari!

# Fork hifadhi hii

Ni rahisi tu kama kuendesha amri hii:

```bash
gh repo fork firstcontributions/first-contributions
```

**Muhimu: Itakuuliza ikiwa unataka ku-clone pia, chagua chaguo la "ndiyo(yes)"**

# Unda tawi lako

Tutafanya hatua hii kwa kutumia git, kwa hivyo ingiza amri hii ukibadilisha jina na jina lako, kwa mfano:

```bash
git switch -c ongeza-john-doe
```

# Fanya mabadiliko muhimu na commit mabadiliko hayo

Sasa unaweza kufungua faili ya Contributors.md katika kihariri cha maandishi na kuongeza jina lako ndani yake. Weka jina lako mahali popote kati ya mwanzo na mwisho, kisha hifadhi faili.

Katika saraka ya mradi endesha git status na utaona mabadiliko.
<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Ongeza mabadiliko hayo kwenye tawi ulilounda kwa kutumia amri ya `git add`:
`git add Contributors.md`

Sasa commit mabadiliko hayo kwa kutumia amri ya `git commit`:
`git commit -m "Ongeza jina-lako kwenye orodha ya Wachangiaji"` ukibadilisha jina-lako na jina lako.

# Push mabadiliko kwa github

Push mabadiliko yako kwa kutumia amri `git push`:

```
git push origin -u your-branch-name
```

ukibadilisha `jina-la-tawi-lako` na jina la tawi ulilounda hapo awali.

<details>
<summary> <strong>Ikiwa unapata makosa yoyote wakati wa kufanya push, bofya hapa:</strong> </summary>

- ### Hitilafu ya Uthibitishaji
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  Go to [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) on generating and configuring an SSH key to your account.

</details>

# Tuma mabadiliko yako kwa ajili ya ukaguzi

Sasa kuendesha amri hii kwenye saraka ya hifadhi yetu kutaturuhusu kuunda pull request kwa ajili ya ukaguzi:

```bash
gh pr create --repo firstcontributions/first-contributions
```

Baada ya hapo tuma pull request.

Unaweza kutumia amri ya `gh status` kuona pull request yako ikifanya kazi.

## Pa kwenda kutoka hapa?

Hongera! Umemaliza hatua ya kawaida ya _fork -> clone -> edit -> pull_ request ambayo mara nyingi utakutana nayo kama mchangiaji!

Sherehekea mchango wako na ushiriki na marafiki na wafuasi wako kwa kwenda kwenye [web app](https://firstcontributions.github.io/#social-share).

Ikiwa ungependa mazoezi zaidi, angalia michango ya code.(https://github.com/roshanjossey/code-contributions).

Sasa tuanze kukufanya uchangie katika miradi mingine. Tumekusanya orodha ya miradi yenye masuala rahisi (easy issues) unayoweza kuanza nayo. Angalia orodha ya miradi katika web app.(https://firstcontributions.github.io/#project-list).

### [Nyenzo za Ziada](https://github.com/firstcontributions/first-contributions/blob/main/docs/additional-material/git_workflow_scenarios/additional-material.md)

[Rudi kwenye ukurasa kuu](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
