# Прыхаваць

Што рабіць, калі вы працуеце над вялікім кодам і раптам вам трэба пераключыць галіну, з якой вы зараз працуеце, на іншую. Паколькі код не з'яўляецца поўным і без якіх-небудзь тэстаў вы, верагодна, не хочаце яго commit. Але вы не можаце перайсці ў іншую галіну без унясення змяненняў, Git не дазволіць вам парушыць гэты паток. Што мы тады робім? Як мы прадухіляем непатрэбнае commit, маючы магчымасць скакаць з галінак? Вось што ахоплівае гэты падручнік.

## Схаванне працы

Дапусцім, што вы працуеце ў аддзяленні праекта, дзе вы змянілі некаторыя файлы. Цяпер, калі вы запусціце ``git status``, вы можаце ўбачыць змены ў файлах.

```
$ git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#      modified:   index.html
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#
#      modified:   lib/simplegit.rb
#
```

Цяпер вы хочаце пераключыць сваю галіну, але пакуль не хочаце ўносіць змены; каб вы захавалі змены.
Каб націснуць на stack новы сродак, запусціце `` git stash``:

```
$ git stash
Saved working directory and index state \
  "WIP on master: 049d078 added the index file"
HEAD is now at 049d078 added the index file
(To restore them type "git stash apply")
```

Цяпер ваш працоўны каталог чысты, выкарыстоўвайце ```git status```:

```
$ git status
# On branch master
nothing to commit, working directory clean
```

Цяпер вы можаце перайсці ў любую галіну і зрабіць сваю працу; схаваныя змены захоўваюцца ў выглядзе stack. Каб даведацца, якія stashes вы захоўваеце ў stack, вы можаце выкарыстоўваць `` git stash list``:

```
$ git stash list
stash@{0}: WIP on master: 049d078 added the index file
stash@{1}: WIP on master: c264051 Revert "added file_size"
stash@{2}: WIP on master: 21d80a5 added number to log
```

У выпадку, калі вы хочаце паўторна ўжыць змены, якія вы толькі што схавалі, вы можаце скарыстацца камандай `` git stash apply``. З дапамогай гэтай каманды вы можаце паўторна ўжыць апошні захованы файл. Для таго, каб паўторна прымяніць любы іншы файл, вы можаце пазначыць яго, назваўшы яго так: ```git stash apply <stash-name>```, замест `` `<stash-name>` `` напішыце імя stash i трэба зноў падаваць.

```
$ git stash apply
# On branch master
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#
#      modified:   index.html
#      modified:   lib/simplegit.rb
#
```

Вы можаце бачыць, што git паўторна змяняе файл, які вы выдалілі, калі вы захавалі пазыцыю. У гэтым выпадку ў вас быў чысты рабочы каталог, калі вы спрабавалі прымяніць stash, і вы паспрабавалі прымяніць яго ў той жа галіны, ад якой вы захавалі; але мець чыстую працоўную дырэкторыю і ўжываць яе ў той жа галінцы не трэба, каб паспяхова ўжываць скрыні. Вы можаце захаваць скрыні на адной галінцы, перайсці на іншую галінку пазней і зноў ужыць змены ў новай галінцы. Вы таксама можаце мець змененыя і неадкрытыя файлы ў вашым працоўным каталогу, калі вы ўжываеце stash, git дае канфлікты зліцця, калі што-небудзь больш не ўжываецца чыста.

Змены, унесеныя ў вашыя файлы, паўторна ўжываюцца, але файл, які вы стварылі, не быў перазагружаны. Для гэтага вам трэба выканаць каманду `` git stash apply`` з ```--index```, каб сказаць камандзе зноў прымяняць паэтапныя змены. Калі б вы запусцілі гэта, вы вярнуліся ў зыходнае становішча:

```
$ git stash apply --index
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#      modified:   index.html
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#
#      modified:   lib/simplegit.rb
#
```

Каманда ўжываць прымяняецца толькі для зачыненай працы, але ў вас усё яшчэ ёсць у вашым stack. Для таго, каб выдаліць яго, вы можаце запусціць `` git stash drop`` з іменем stack для выдалення.

```
$ git stash list
stash@{0}: WIP on master: 049d078 added the index file
stash@{1}: WIP on master: c264051 Revert "added file_size"
stash@{2}: WIP on master: 21d80a5 added number to log
$ git stash drop stash@{0}
Dropped stash@{0} (364e91f3f268f0900bc3ee613f9f733e82aaed43)
```

Вы можаце выкарыстоўваць `` git stash pop``, каб выдаліць апошнія змены, выдаліўшы іх са свайго stack.

## Адмена прымянення stash

У некаторых выпадках вы хочаце прымяніць затоеныя змены, выканаць некаторыя працы, але ўжываць змены, якія першапачаткова прыйшлі з stash. Git не падае такую каманду, як `` git unapply` ``, але можна дасягнуць гэтага эфекту, проста здабыўшы patch, звязаны са stash, і прымяніць яго ў зваротным парадку:

```$ git stash show -p stash@{0} | git apply -R```

Зноў жа, калі вы не ўкажыце stash, Git мяркуе самую свежую stash:

```$ git stash show -p | git apply -R```

Магчыма, вы захочаце стварыць псеўданім і эфектыўна дадаць каманду `` stash-unapply`` у свой Git. Напрыклад:

```
$ git config --global alias.stash-unapply '!git stash show -p | git apply -R'
$ git stash apply
$ #... work work work
$ git stash-unapply
```

## Стварэнне аддзялення з stash

Калі вы захоўваеце якую-небудзь працу, пакіньце яе там на некаторы час і працягвайце працу на той галінцы, з якой вы схавалі працу, у вас могуць паўстаць праблемы пры паўторнай працы. Калі заяўка паспрабуе змяніць файл, які вы ў свой час змянілі, у вас атрымаецца канфлікт аб'яднання, і вам прыйдзецца яго вырашыць. Калі вы хочаце больш проста пратэставаць схаваныя змены, вы можаце запусціць `` git stash branch``, які стварае для вас новае аддзяленне, правярайце абавязацельствы, якія вы выконвалі, калі вы прыхавалі працу, і зноў адпраўляе сваю працу. там, а затым скідае скрыню, калі яна паспяхова ўжываецца:

```
$ git stash branch testchanges
Switched to a new branch "testchanges"
# On branch testchanges
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#      modified:   index.html
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#
#      modified:   lib/simplegit.rb
#
Dropped refs/stash@{0} (f0dfc4d5dc332d1cee34a634182e168c4efc3359)
```

Гэта добры цэтлік, каб лёгка аднавіць схаваную працу і працаваць над ёй у новым аддзяленні.