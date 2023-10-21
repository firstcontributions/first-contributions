# Einen Zweig aus Ihrem Repository entfernen

Wenn Sie bisher unserem Tutorial gefolgt sind, hat Ihr `<add-your-name>`-Zweig sein Ziel erreicht und es ist Zeit, ihn aus Ihrem lokalen Repository zu entfernen. Dies ist optional, aber der Name dieses Zweigs zeigt seinen speziellen Zweck, anstatt dass er unnötig weiter existiert. Sein Leben kann ziemlich kurz sein.

Zuerst führen Sie Ihr `<add-your-name>` in Ihren Master-Zweig zusammen, damit gehen Sie zu Ihrem Master-Zweig:


git checkout master

Dann führen Sie den Merge von `<add-your-name>` in Ihren Master-Zweig durch:

git merge <add-your-name> master


Anschließend entfernen Sie Ihren `<add-your-name>` von Ihrem lokalen Repository:


git branch -d <add-your-name>



Jetzt haben Sie Ihren `<add-your-name>`-Zweig von Ihrem lokalen Computer entfernt und alles sieht aufgeräumt aus.
Allerdings sollten Sie zu diesem Zeitpunkt immer noch einen `<add-your-name>`-Zweig in Ihrem GitHub-Fork haben. Bevor Sie ihn löschen, denken Sie daran, dass Sie bereits eine Pull-Anfrage von diesem Remote-Zweig zu unserem Repository gesendet haben. Solange ich sie nicht gemerged habe, löschen Sie den Zweig nicht.

Wenn ich jedoch Ihren Zweig gemerged habe und Sie den Remote-Zweig entfernen möchten, verwenden Sie dies:

git push origin --delete <add-your-name>


Jetzt wissen Sie, wie Sie Ihre Zweige aufräumen. Im Laufe der Zeit werden viele Repositories zu meinen öffentlichen Repositories hinzugefügt. Und Ihre lokalen Maschinen und Ihre GitHub-Forks werden nicht mehr auf dem neuesten Stand sein. Um Ihre Repositories mit mir zu synchronisieren, befolgen Sie die unten stehenden Schritte.

#### [Halten Sie Ihren Fork mit diesem Repository synchronisiert] (keeping-your-fork-synced-with-this-repository.md)
