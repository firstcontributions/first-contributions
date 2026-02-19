[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Mchango wa Kwanza

| <img alt="GitHub Desktop" src="https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png" width="200"> | Amri ya Mstari wa GitHub (CLI) |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |

Hii ni mwongozo kwa wale wanachotaka kufanya kila kitu kwenye mwisho, na kwa shukrani kwa [Github-CLI](https://cli.github.com/), tunaweza kufikia, ukikumbuka kwamba mchango wako wa kwanza unapaswa kuwa wa kufurahisha, unaolipa na motisha ya kuendelea!

Mwongozo huu ni changamoto zaidi kidogo kwani hatumui kiolesula chochote, lakini bado ni really fun na unaweza kufuata!

Sharti la kwanza ni kuwa na:

- Git imewekwa (jinsi ya kusakinisha [git](https://git-scm.com/downloads))
- Akaunti ya Github

Sasa tunapaswa kusakinisha zana ya `github-cli` kwenye mfumo wetu kwa kufuata [hati rasmi](https://github.com/cli/cli#installation)

Baada ya hapo, tunapaswa kuingia kwenye CLI, kwa hiyo weka amri hii:

```bash
gh auth login
```

Fuata maagizo na tayari!

# Chomoza hifadhi hii

Ni rahisi kama kuendesha amri hii:

```bash
gh repo fork firstcontributions/first-contributions
```

Muhimu: Itakuchochea ikiwa unataka kukloni pia, chagua chaguo la "ndio"

# Unda tawi lako

Tutafanya hatua hii na git, kwa hiyo weka amri hii kubadilisha jina na jina lako, kwa mfano:

```bash
git switch -c add-john-doe
```

# Fanya mabadiliko yanayohitajika na commit

Sasa unaweza kufungua faili ya `Contributors.md` kwenye kihariri cha maandishi na kuongeza jina lako. Weka jina lako popote kati ya mwisho na mwisho, kisha uhifadhi faili.

Katika saraka ya mradi weka `git status` na utaona mabadiliko.
<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="hali ya git" />

Ongeza mabadiliko hayo kwenye tawi ulilouna hivi punde kwa kutumia amri ya `git add`:
`git add Contributors.md`

Sasa commit mabadiliko hayo kwa kutumia amri ya `git commit`:
`git commit -m "Ongeza jina lako kwenye orodha yawachangiaji"`
badilisha `jina lako` na jina lako.

# Wasilisha mabadiliko kwenye github

Wasilisha mabadiliko yako kwa kutumia amri ya `git push`:

```
git push origin -u jina-la-tawi-lako
```

badilisha `jina-la-tawi-lako` na jina la tawi ulilounda hapo awali.

<details>
<summary> <strong>Ukipata makosa yoyote wakati wa kushika, bonyeza hapa:</strong> </summary>

- ### Hitilafu ya Uhalali
     <pre>remote: Usaidizi wa nenosiri lilionezwa tathmini tarehe 13 Agosti 2021. Tafadhali tumia token ya ufikiaji badala yake.
  remote: Tafadhali angalia https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ kwa maelezo zaidi.
  fatale: Uhalali umeshindikana kwa 'https://github.com/<jina-lako>/first-contributions.git/'
  </summary>
  Nenda kwenye [mwongozo wa GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-account) ya kuunda na kusanya ufunguo wa SSH kwenye akaunti yako.

</details>

# Wasilisha mabadiliko yako kwa ukaguzi

Sasa kuendesha amri hii katika saraka ya repo yetu itaturuhusu kuunda pull request kwa ukaguzi:

```bash
gh pr create --repo firstcontributions/first-contributions
```

Baada ya hapo wasilisha pull request.

Unaweza kutumia amri `gh status` kuona pull request yako inavyotajwa.

## Kwenda wapi kutoka hapa?

Hongera! Umejifizilisha tu kazi ya kawaida ya _fork -> clone -> edit -> pull request_ ambayo utakumbana nayo mara nyingi kama mchangiaji!

Sherehekea mchango wako na ushiriki na marafiki na wafuasi kwa kwenda kwenye [programu ya wavuti](https://first-contributions.github.io/#social-share).

Ikiwa unataka mazoezi zaidi, angalia [mchango wa nambari](https://github.com/roshanjossey/code-c)
