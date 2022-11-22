# Odstrani vejo s svojega repository-ja

Če si sledil vodiču do tukaj, sedaj tvoja veja `<add-your-name>` ni več uporabna in jo lahko zbrišeš z lokalnega repository-ja. To ni nujno potrebno, vendar ime te veje kaže njen namen obstoja. Ker je opravila svoje delo, jo lahko zbrišeš.

Najprej združiš `<add-your-name>` z glavno ( master ) vejo, zato se postavi vanjo:
```
git checkout master
```

Združi `<add-your-name>` z master:
```
git merge <add-your-name> master
```

Odstrani `<add-your-name>` z lokalnega repository-ja:
```
git branch -d <add-your-name>
```

Sedaj si zbrisal `<add-your-name>` vejo s svojega računalnika in vse zgleda urejeno. Vendar ta veja še vedno obstaja v tvoji GitHub različici ( fork ). Preden jo zbrišeš tudi tam, vedi da moraš najprej poslati "Pull request" mojemu repository-ju. Tako da, če je še nisem združil v moj repository, te veje na GitHub-u še ne zbriši!

Če pa je tvoja GitHub veja že združena v moj projekt, in jo želiš zbrisati, uporabi naslednji ukaz:
```
git push origin --delete <add-your-name>
```

Sedaj veš kako počistiti neuporabne veje s svojega repository-ja.
S časom bo veliko commit-ov dodanih v moj javni repository, in glavni veji na tvojem računalniku in GitHub različici ne bosta več posodobljeni na zadnjo verzijo. Da bodo vsi tvoji repository-ji sinhronizirani z mojim, sledi korakom v tem vodiču:

#### [Kako imeti svojo različico sinhronizirano z oddaljenim repository-em](keeping-your-fork-synced-with-this-repository.sl.md)
