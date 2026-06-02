# Git ಸಂರಚನೆ

ನಿಂಗ ಮೊದಲು Git ಅನ್ನು ಬಳಸುವಕ್ ಪ್ರಯತ್ನಿಸಿದಾಗ, ನಿಂಗ ಈ ರೀತಿಯ ಸಂದೇಶವನ್ನು ಸ್ವೀಕರಿಸಿದ್ದೀರಾ:

```bash
$ git commit
*** ದಯವಿಟ್ಟು ನಿಮ್ಮ ಬಗ್ಗೆ ಮಾಹಿತಿ ನೀಡಿ.

ನಿಂಗ ಈ ಕೆಳಗಿನ ಆಜ್ಞೆಯನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಿ:

git config --global user.email "you@example.com"
git config --global user.name "Your Name"

ನಿಮ್ಮ ಖಾತೆಯ ಪೂರ್ವನಿಯೋಜಿತ ಗುರುತನ್ನು ಹೊಂದಿಸುವಕ್.
"--global" ಅನ್ನು ಹೊರತುಪಡಿಸಿ ಈ ಪರಿಚಯವನ್ನು ಮಾತ್ರ ಈ Repository ಗೆ ಬಳಸಲು.
```

Git ನಲ್ಲಿ Commit ಮಾಡುವಕ್ ನಿಂಗ ಯಾರು ಎಂಬುದನ್ನು ಅದು ತಿಳಿದುಕೊಳ್ಳಬೇಕಾಗುವ. ನಿಂಗ ತಂಡವಾಗಿ ಕೆಲಸ ಮಾಡುವಾಗ, ಯಾರು ಯಾವ ಭಾಗವನ್ನು ಪರಿಷ್ಕರಿಸಿದ್ದಾರೆ ಮತ್ತು ಯಾವಾಗ ಎಂಬುದನ್ನು ಗಮನಿಸುವ ಸಾಮರ್ಥ್ಯ ಇರೋಕು. ಆದ್ದರಿಂದ Git ಪ್ರತಿಯೊಂದು Commit ಅನ್ನು ಹೆಸರು ಮತ್ತು ಇಮೇಲ್ ಗೆ ಲಿಂಕ್ ಮಾಡುವಕ್ ವಿನ್ಯಾಸಗೊಳಿಸಿದು.

Git Commit ಆಜ್ಞೆಗೆ ನಿಮ್ಮ ಇಮೇಲ್ ಮತ್ತು ಹೆಸರನ್ನು ಒದಗಿಸುವಕ್ ಹಲವು ವಿಧಾನಗಳ್ ಉಂಡು. ನಾಂಗ ಕೆಲವು ವಿಧಾನಗಳ್ ಇಲ್ಲಿ ನೋಡುವ.

### ಜಾಗತಿಕ ಸಂರಚನೆ (Global Configuration)

ನಿಂಗ ಜಾಗತಿಕ ಸಂರಚನೆಯಲ್ಲಿ (global configuration) ಏನಾದರೂ ಭದ್ರಗೊಳಿಸಿದರೆ, ಅದು ನಿಂಗ ಬಳಸುವ ಎಲ್ಲಾ ಸಿಸ್ಟಂಲ್ ಮತ್ತು Repository ಗಳಲ್ಲಿ ಲಭ್ಯವಪ್ಪ. ಇದು ಸಾಮಾನ್ಯವಾಗಿ ಬಳಸುವ ವಿಧಾನ.

ಜಾಗತಿಕ ಸಂರಚನೆಯಲ್ಲಿ ಸಂಗ್ರಹಿಸುವಕ್, ನಿಂಗ ಈ ಕೆಳಗಿನ ಆಜ್ಞೆಯನ್ನು ಬಳಸಲಕ್ಕು:

```bash
$ git config --global <variable name> <value>
```

ಬಳಕೆದಾರ ವಿವರಗಳಿಗಾಗಿ:

```bash
$ git config --global user.email "you@example.com"
$ git config --global user.name "Your Name"
```

### Repository-ನಿರ್ದಿಷ್ಟ ಸಂರಚನೆ (Repository-specific Configuration)

ಈ ಸಂರಚನೆ ನಿರ್ದಿಷ್ಟ Repository ಯ ಮೇಲೆ ಮಾತ್ರ ಪರಿಣಾಮ ಬೀರುವ. ಉದಾಹರಣೆಗೆ, ನಿಂಗ ಕೆಲಸಕ್ಕೆ ಸಂಬಂಧಿಸಿದ ಒಬ್ಬ Repository ಲ್ಲಿ ನಿಮ್ಮ ಕಂಪನಿಯ ಇಮೇಲ್ ಅನ್ನು ಬಳಸುವಕ್ ಇಚ್ಛಿಸಿದರೆ, ಈ ವಿಧಾನ ಉಪಯುಕ್ತ ಉಂಡು.

```bash
$ git config user.email "you@alternate.com"
$ git config user.name "Your Name"
```

### ಆಜ್ಞಾ ಸಾಲಿನ ಸಂರಚನೆ (Command-line Configuration)

ಈ ಸಂರಚನೆ ಕೇವಲ ಆಜ್ಞೆ ಕಾರ್ಯಗತಗೊಳ್ಳುವ ಸಮಯದಲ್ಲಿ ಮಾತ್ರ ಅನ್ವಯವಾಗುವ. ಎಲ್ಲ Git ಆಜ್ಞೆಗಳಿಗೂ `-c` ಆರ್ಗ್ಯೂಮೆಂಟ್ ಅನ್ನು ಬಳಸಲಕ್ಕು.

```bash
$ git -c <variable-1>=<value> -c <variable-2>=<value> <command>
```

ಉದಾಹರಣೆಗೆ, Commit ಆಜ್ಞೆಯನ್ನು ಈ ರೀತಿ ಕಾರ್ಯಗತಗೊಳಿಸಲಕ್ಕು:

```bash
git -c user.name='Your Name' -c user.email='you@example.com' commit -m "Your commit message"
```

### ಆದ್ಯತೆ ಬಗ್ಗೆ ಟಿಪ್ಪಣಿ (Precedence Note)

ಮೇಲಿನ ಮೂರು ವಿಧಾನಗಳಲ್ಲಿ, ಆದ್ಯತೆ ಕ್ರಮ ಹೀಗುಂಡು: **ಆಜ್ಞಾ ಸಾಲು (Command-line) > Repository (Repository) > ಜಾಗತಿಕ (Global)**

ಹಾಗಾಗಿ, ಒಂದು ಸ್ಟ್ರಿಂಗ್ ಅನ್ನು ಆಜ್ಞಾ ಸಾಲಿನಲ್ಲಿ ಮತ್ತು ಜಾಗತಿಕವಾಗಿ ಎರಡೂ ಹೊಂದಿಸಿದರೆ, ಆಜ್ಞಾ ಸಾಲಿನ ಸಂಯೋಜನೆಯು ಪ್ರಸ್ತಾಪಿತ Git ಕಾರ್ಯಾಚರಣೆಗೆ ಅನ್ವಯವಾಗುವ.

## ಬಳಕೆದಾರ ವಿವರಗಳ ಹೊರತಾಗಿ (Beyond User Details)

ನಾಂಗ ಈವರೆಗೆ ಬಳಕೆದಾರ ವಿವರಗಳ ಬಗ್ಗೆ ಮಾತ್ರ ಚರ್ಚಿಸುವ, ಆದರೆ Git ನಲ್ಲಿ ಹಲವಾರು ಇತರ ಸಂರಚನಾ ಆಯ್ಕೆಗಳೂ ಲಭ್ಯ ಉಂಡು:

1. `core.editor` - Commit ಸಂದೇಶಗಳ್ ಬರೆಯುವಕ್ ಬಳಸುವ ಎಡಿಟರ್ ಅನ್ನು ನಿರ್ಧರಿಸಲು.
2. `commit.template` - Commit ಸಂದೇಶದ ಮಾದರಿಯನ್ನು ಒದಗಿಸಲು.
3. `color.ui` - Git ಔಟ್‌ಪುಟ್‌ನಲ್ಲಿ ಬಣ್ಣ ಬಳಸುವ ಅಥವಾ ಬಳಸದಿರಬಹುದೆಂಬುದನ್ನು ನಿರ್ಧರಿಸಲು.

Git ಸಂರಚನೆ ಬಗ್ಗೆ ಹೆಚ್ಚಿನ ಮಾಹಿತಿಗಾಗಿ, ಈ ಲಿಂಕ್ ಅನ್ನು ಭೇಟಿ ನೀಡಿ:

[git-scm.com](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration).