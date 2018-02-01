## Entfernen eines Branchs aus deiner Repository

Wenn du das Tutorial nun also bis hier hin durchgeführt hast, hat unser `<add-DEIN-NAME>`-Branch seinen Zweck erfüllt und es ist nun Zeit ihn aus der Repository deines lokalen Rechners zu löschen. Das ist nicht unbedingt notwendig, aber der Name des Branchs zeigt seinen recht speziellen Zweck. Sein Leben ist also dementsprechend kurz.

Zuallererst, lass uns deinen `<add-DEIN-NAME>` zu deinem `master` hinzufügen. Also erstmal ab in den `master`:

```
git checkout master
```

Jetzt den `<add-DEIN-NAME>` in den `master` mergen:

```
git merge <add-DEIN-NAME> master
```

Und jetzt löschen wir den `<add-DEIN-NAME>` aus der Repo des lokalen Rechners:

```
git branch -d <add-DEIN-NAME>
```

Jetzt hast du `<add-DEIN-NAME>` aus der Repo deines lokalen Rechners gelöscht und alles sieht picobello aus.
Allerdings, wo wir nun soweit sind, ist dein `<add-DEIN-NAME>`-Branch immer noch in deinem GitHub-Fork. Bevor wir diesen jedoch löschen, bedenke, dass du mir über diese Repo einen *pull request* geschickt hast. Also bevor ich diesen nicht in das Hauptprojekt gemerget habe, solltest du ihn auf keinem Fall löschen!

Ist das allerdings passiert, kannst du ihn bedenkenlos aus deiner GitHub-Repository entfernen:

```
git push origin --delete <add-DEIN-NAME>
```

Jetzt weißt du also, wie man Branches auf Vordermann bringt.
Mit der Zeit werden viele Commits zur öffentlichen Repo hinzugefügt. Dadurch wird der `master` deines lokalen Rechners und deiner GitHub-Repo nicht mehr up-to-date sein. Damit du deine Repositorys mit meinem in Synchronisation hältst, folge den folgenden Schritten:

#### [ Keeping your fork synced with the repository ](keeping-your-fork-synced-with-this-repository.md)
