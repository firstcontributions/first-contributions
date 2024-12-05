# Што такое squashing?

У git, squashing маецца на ўвазе перапісванне гісторыі вашых учынкаў, таму вы ў канчатковым выніку займаецеся апісаннем зробленых змяненняў.
Звычайна гэта робіцца ў праектах з адкрытым зыходным кодам, таму што шмат гісторыяў філіялаў у праектах з адкрытым зыходным кодам мае дачыненне толькі да распрацоўшчыка, які іх стварыў, і гэта дае больш просты спосаб апісаць унесеныя змены, а таксама пры неабходнасці аднавіць іх.

# Як вы робіце squash камітаў?

Па-першае, выканаць часопіс git, каб прааналізаваць каміт, якія вы хацелі б аб'яднаць у вашай бягучай галіны.

```
git log
```

Вы павінны ўбачыць шэраг сваіх абавязацельстваў так:

```
commit blablabla
Author: omguhh
Date:   10/10/20
    Commit message 1

commit blablabla2
Author: omguhh
Date:   10/10/20
    Commit message 2
```

Такім чынам, зараз, калі вы бачыце каміты, якія вы хочаце злучыць з адным, мы можам перайсці да гэтага з `` git rebase `` . Зыходзячы з таго, што вы ўжо знаёмыя з `` git rebase `` , мы можам пачаць squashing камітаў ў інтэрактыўным рэжыме git rebase, які можна актываваць так:

```
git rebase -i
```

Цяпер, пры дапамозе інтэрактыўнага rebasing вы можаце вызначыць пачатковую і канчатковую кропку таго, як далёка вы хочаце ісці з такімі ўчынкамі:

```
git rebase -i HEAD~2
```

Запуск гэтай каманды пакажа вам нешта падабаецца наступнае:

```
pick blablabla Changing test01.txt file
pick blablabla2 Adding dummy01.txt file

#
# Commands:
#  p, pick = use commit
#  r, reword = use commit, but edit the commit message
#  e, edit = use commit, but stop for amending
#  s, squash = use commit, but meld into previous commit
#  f, fixup = like "squash", but discard this commit's log message
#  x, exec = run command (the rest of the line) using shell
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
#
# However, if you remove everything, the rebase will be aborted.
#
# Note that empty commits are commented out
```

Такім чынам, калі вы хочаце squash ``` blablabla2``` на ``` blablablabla```, вы змяніце наступнае:

```
pick blablabla Changing test01.txt file
squash blablabla2 Adding dummy01.txt file

```

Калі ўсё пойдзе добра, вы атрымаеце такі вынік:

```
# This is a combination of 2 commits.
# The first commit's message is:
commit message 1

# This is the 2nd commit message:

commit message 2
```

Што вы можаце свабодна змяніць, перш чым вырашыць выйсці з рэдактара, каб захаваць гэтыя змены.

Запуск часопіса git павінен паказаць вам паведамленне аб здзяйсненні, якое вы ўвялі перад выхадам на экран, з абавязацельствамі, аб'яднанымі ў адзін.
