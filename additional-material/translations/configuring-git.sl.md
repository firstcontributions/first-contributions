# Nastavljanje Git okolja

Ko si prvič poskusil narediti commit z Git-om, je možno da se je prikazalo naslednje sporočilo:

```bash
$ git commit
*** Please tell me who you are.

Run

git config --global user.email "you@example.com"
git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.
```

Git mora vedeti kdo si, da lahko ustvari commit. Ko delaš v skupini z več ljudmi, naj bi se vedno vedelo kdo je naredil katero spremembo v projektu in kdaj jo je nardil. V ta namen je bil Git ustvarjen tako, da so commit-i vezani na ime in e-pošto.

Obstaja več načinov kako ukazu `git commit` podati svoje ime in e-pošto in nekaj jih bomo pregledali v naslednjih vrsticah.

### Globalna konfiguracija

Ko nekaj shranimo v globalno konfiguracijo (global config), je ta nastavitev dosegljiva vsem repository-em na katerih delaš. Ta način se priporoča in deluje v večini primerov.

Da nekaj shranimo v globalno konfiguracijo, uporabimo ukaz `config`:

`$ git config --global <variable name> <value>`

V primeru uporabniških podatkov:

```
$ git config --global user.email "you@example.com"
$ git config --global user.name "Your Name"
```

### Konfiguracija repository-ja

Kot nam že samo ime pove, so te konfiguracije omejene samo na en repository. Če želiš narediti commit v točno določen repository, recimo službeni projekt, s svojo službeno e-pošto, potem uporabimo to metodo.

Da nekaj shranimo v konfiguracijo repository-ja, uporabimo ukaz `config` in spustimo zastavico `--global`:


`$ git config <variable name> <value>`

V primeru uporabniških podatkov:

```
$ git config user.email "you@alternate.com"
$ git config user.name "Your Name"
```

### Konfiguracija ukazne vrstice

Te konfiguracije so omejene samo na trenutno ukazno vrstico. Vsi Git ukazi sprejmejo predpono `-c` pred glagolom ukaza. S tem ustvarimo začasno konfiguracijo.

Da nekaj shranimo v konfiguracijo ukazne vrstice:

`$ git -c <variable-1>=<value> -c <variable-2>=<value> <command>`

V našem primeru bi ukaz commit uporabili takole:

`git -c user.name='Your Name' -c user.email='you@example.com' commit -m "Your commit message"`

### O prednosti

Zaporedje uporabe med zgoraj omenjenimi metodami je sledeče `command-line > repository > global`. To pomeni da, če je spremenljivka shranjena v ukazni vrstici in globalno, bi bila uporabljena vrednost v konfiguraciji ukazne vrstice.

## Dodatno

Do sedaj smo delali samo z nastavitvami uporabnika, vendar obstaja še nekaj drugih konfiguracij. Nekatere med njimi so: 

1.  `core.editor` - za določitev urejevalnika besedila, ki se uporabi za pisanje komentarjev, itd.
2.  `commit.template` - za določitev datoteke v sistemu, ki se uporabi kot začetna predloga za commit 
3.  `color.ui` - za določitev boolean vrednosti za uporabo barv v Git-ovem izpisu.

Nekaj podrobnosti smo poenostavili za lažje razumevanje. Več si lahko prebereš na [git-scm.com](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration).
