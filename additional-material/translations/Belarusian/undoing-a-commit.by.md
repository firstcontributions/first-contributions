# Адмяніць мясцовыя каміты

Каб адмяніць мясцовыя каміты, усё, што вам трэба зрабіць, гэта
```
git reset
```

Гэтая каманда прывядзе да скіду staging вобласці да апошні каміт, але змены, якія ўнесены ў ваш працоўны каталог, не зменіцца. Такім чынам, вы ўсё яшчэ можаце зноў камітаць тое, што вы змянілі.
Ці, калі вы хочаце выдаліць толькі адзін файл з папярэдняга каміту. Затым вы можаце зрабіць каманду ніжэй

```
git reset <file>
```
Каманда выдаліць толькі пазначаны файл з staging вобласці, але змены, унесеныя ў файл, усё яшчэ застануцца.

Прыклад выкарыстання ```git reset```
```
# Make changes in index.php and tutorial.php
# Add files into the staging area
$ git add .
# Remembered both files need to be committed separately
# Unstage tutorial.php
$ git reset tutorial.php
# Commit index.php first
$ git commit -m "Changed index.php"
# Commit tutorial.php now
$ git add tutorial.php
$ git commit -m "Changed tutorial.php"
```

Дапусцім, калі вы пераблыталі сваё лакальнае сховішча і проста хочаце скінуць яго на апошні ўдзел.
Затым вы можаце запусціць каманду ніжэй.
```
git reset --hard
```

Каманда не толькі скіне ваша staging вобласць, але і верне ўсе вашы змены ў файлах да вашай апошняй commit.
Рэжым `` --hard `` загадвае Git таксама адмяняць усе змены ў працоўным каталогу.
Вы павінны запускаць гэта толькі тады, калі вы сапраўды ўпэўненыя ў тым, што выкінеце цэлае local development.

Прыклад выкарыстання  ```git reset --hard``` 
```
# Decided to start a crazy experiment
# Create a new file 'crazy.php' and add some code to it
# Commit crazy.php
$ git add crazy.php
$ git commit -m "Started a crazy dev"
# Edit crazy.php file again and changed a lot other files
# Commit all tracked files
$ git add .
$ git commit -m "Continued dev"
# Tested and things went out of hand
# Decided to remove the whole things
$ git reset --hard HEAD~2
```

```git reset --hard HEAD~2``` перамяшчае бягучую галінку назад на 2 commits адначасова, аднаўляючы ўсе зробленыя вамі змены і выдаляючы 2 здымкі, якія мы толькі што стварылі з гісторыі праектаў.

P.s. Ніколі не выконвайце `` git reset --hard```, калі вы ўжо перанеслі свае commits ў агульнае сховішча, паколькі гэта прывядзе да праблем з усімі рэпазітарамі.
