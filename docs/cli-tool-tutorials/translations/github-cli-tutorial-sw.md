[![Upendo wa Chanzo Huria](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)  
[![Leseni: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)  
[![Wasaidizi wa Chanzo Huria](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Mchango wa Kwanza

| <img alt="GitHub Desktop" src="https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png" width="200"> | Kiolesura cha Amri za GitHub (CLI) |
| ------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |

Huu ni mwongozo kwa sisi, wapenzi wa kutumia terminal, ambao tunataka kufanya kila kitu kupitia terminal, na shukrani kwa [Github-CLI](https://cli.github.com/), tunaweza kufanikisha hili, tukikumbuka kwamba mchango wako wa kwanza unapaswa kuwa wa kufurahisha, wenye thawabu na kuwa motisha ya kuendelea!

Mwongozo huu ni changamoto kidogo kwani hatutatumii kiolesura cha picha kabisa, lakini bado ni furaha na unaweza kufuata kwa urahisi!

Kitu cha kwanza unachohitaji ni:

- Git imewekwa (jifunze jinsi ya kusakinisha [git](https://git-scm.com/downloads))
- Akaunti ya Github

Sasa tunahitaji kusakinisha zana ya `github-cli` kwenye mfumo wetu kwa kufuata [nyaraka rasmi](https://github.com/cli/cli#installation).

Baada ya hapo, tunahitaji kuingia kwenye CLI kwa kutumia amri hii:

```bash
gh auth login
```

Fuata maelekezo na tuko tayari!

---

# Tengeneza nakala (Fork) ya hazina hii

Ni rahisi kama kutekeleza amri hii:

```bash
gh repo fork firstcontributions/first-contributions
```

**Muhimu:** Itakuuliza kama unataka pia kupakua nakala (clone), chagua jibu **"ndio" (yes)**.

---

# Tengeneza tawi lako (branch)

Tutafanya hatua hii kwa git, ingiza amri hii ukibadilisha jina na jina lako, kwa mfano:

```bash
git switch -c add-john-doe
```

---

# Fanya mabadiliko muhimu na yafanye commit

Sasa unaweza kufungua faili `Contributors.md` kwa mhariri wa maandishi na kuongeza jina lako. Weka jina lako mahali popote kati ya mwanzo na mwisho kisha hifadhi faili.

Ndani ya directory ya mradi tumia `git status` utaona mabadiliko yaliyofanyika.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Ongeza mabadiliko hayo kwenye tawi ulilotengeneza kwa kutumia amri `git add`:

```bash
git add Contributors.md
```

Sasa fanya commit ya mabadiliko kwa kutumia amri:

```bash
git commit -m "Add your-name to Contributors list"
```

Badilisha `your-name` na jina lako halisi.

---

# Tuma mabadiliko yako kwenye GitHub

Tuma mabadiliko kwa kutumia amri:

```bash
git push origin -u your-branch-name
```

Badilisha `your-branch-name` na jina la tawi ulilotengeneza.

<details>
<summary><strong>Ukikumbwa na makosa wakati wa kusukuma (push), bofya hapa:</strong></summary>

- ### Tatizo la Uthibitishaji (Authentication Error)
       <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/&lt;your-username&gt;/first-contributions.git/'</pre>
  Tembelea [mafunzo ya GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) ya jinsi ya kutengeneza na kuweka SSH key kwenye akaunti yako.

</details>

---

# Wasilisha mabadiliko yako kwa ajili ya uhakiki (review)

Sasa tumia amri hii kwenye directory ya mradi kuunda pull request kwa uhakiki:

```bash
gh pr create --repo firstcontributions/first-contributions
```

Baada ya hapo wasilisha pull request.

Unaweza pia kutumia amri `gh status` kuona hali ya pull request yako.

---

## Nifanye nini sasa?

Hongera! Umekamilisha mzunguko wa kawaida wa **_Nakili -> Pakua nakala -> Hariri -> Omba muunganiko_ (_fork -> clone -> edit -> pull request_)** ambao utakuwa ukikutana nao mara nyingi kama mchangiaji!

Sherehekea mchango wako na uushirikishe marafiki na wafuasi kwa kutembelea [tovuti](https://firstcontributions.github.io/#social-share).

Kama unataka mazoezi zaidi, tembelea [michango ya code](https://github.com/roshanjossey/code-contributions).

Sasa tukuanzishe kuchangia miradi mingine. Tumekusanya orodha ya miradi yenye masuala rahisi ya kuanzia. Angalia [orodha ya miradi kwenye tovuti](https://firstcontributions.github.io/#project-list).

---

### [Nyenzo za ziada](https://github.com/firstcontributions/first-contributions/blob/main/docs/additional-material/git_workflow_scenarios/additional-material.md)

[Rudi kwenye ukurasa mkuu](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
