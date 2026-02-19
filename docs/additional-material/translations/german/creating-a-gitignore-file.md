## .gitignore verstehen

Die Datei `.gitignore` ist ein wesentlicher Bestandteil des Git-Workflows. Sie teilt Git mit, welche Dateien und Ordner ignoriert werden sollen, und verhindert so, dass unnötige oder sensible Daten in Ihrem Repository nachverfolgt werden.

## Warum .gitignore verwenden?

Bestimmte Dateien sollten nicht in die Versionskontrolle aufgenommen werden, da sie entweder:
- temporär oder vom System generiert sind (z. B. Cache, Build-Dateien, Protokolle)
- große Abhängigkeiten, die neu installiert werden können (z. B. `node_modules`)
- persönliche oder sensible Konfigurationsdateien (z. B. API-Schlüssel, Umgebungsvariablen)
- IDE- oder editor-spezifische Dateien (z. B. `.vscode/`, `.idea/`)

Das Ignorieren dieser Dateien hält das Repository sauber, reduziert Konflikte und verhindert Sicherheitsrisiken.

## Erstellen einer .gitignore-Datei

So erstellen Sie eine `.gitignore`-Datei:
1. Erstellen Sie in Ihrem Projektstammverzeichnis eine neue Textdatei mit dem Namen `.gitignore`.
2. Listen Sie die Dateien und Ordner, die Sie ignorieren möchten, in einer Zeile auf.
3. Speichern Sie die Datei.

### Grundlegende Syntax für .gitignore
- `*` → Platzhalter für mehrere Dateien.
- `/` → Gibt den relativen Pfad zu `.gitignore` an.
- `#` → Fügt Kommentare hinzu.

### Beispiel für eine .gitignore-Datei:
```sh
# Mac-Systemdateien ignorieren
.DS_Store

# Abhängigkeitsordner ignorieren
node_modules/
venv/

# Protokoll- und Cache-Dateien ignorieren
*.log
.cache/

# Umgebungsdateien ignorieren
.env

# Alle Textdateien ignorieren
*.txt
```

## Globale .gitignore (für alle Projekte)
So erstellen Sie eine globale `.gitignore`-Datei (gilt für alle Repositorys):
```sh
git config --global core.excludesfile ~/.gitignore_global
```
Bearbeiten Sie anschließend `~/.gitignore_global` wie eine lokale `.gitignore`-Datei.

## Dateien aus der Git-Verfolgung entfernen

Wenn eine Datei bereits vor dem Hinzufügen zu `.gitignore` committet wurde, müssen Sie sie aus der Verfolgung entfernen:

- **Eine einzelne Datei aus der Verfolgung entfernen** (aber lokal behalten):
```sh
  git rm --cached Dateiname
  ```

- **Alle ignorierten Dateien aus der Verfolgung entfernen**:
```sh
  git rm -r --cached .
  git add .
  git commit -m „Updated .gitignore“
  ```

Um `git rm --cached filename` rückgängig zu machen, verwenden Sie:
```sh
git add filename
```
