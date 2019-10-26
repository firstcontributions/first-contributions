# Was ist der Nutzen verschiedener branches?

Branches sind lediglich Hinweise / Referenzen zu commits.

Beim erstellen eines neuen branchs erzeugt Git im Wesentlichen einen neuen Zustand deines aktuellen codes, an welchem du arbeiten kannst, ohne den code der master branch zu beeinflussen.

Sobald du zufrieden bist und den neuen branch mit dem master branch zusammenführen möchtest, kannst du `git merge <branch-name>` ausführen.

Dadurch wird Git alle Änderungen dem master hinzufügen.

Auf diese Weise wird es bei der Arbeit an einem open source Projekt mit einer Vielzahl von Mitwirkenden einfacher, den am besten geeigneten code zusammenzuführen, ohne den Hauptcode oder den master branch zu verändern.