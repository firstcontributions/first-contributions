# commit ಅನ್ನು ಬೇರೆ branch ಗೆ ಸ್ಥಳಾಂತರಿಸುವುದು

ನೀವು commit ಮಾಡಿದ್ದ ನಂತರ, ಅದು ತಪ್ಪಾಗಿ ಬೇರೆ branch ನಲ್ಲಿ ಆಗಿದೆ ಎಂದು ಗಮನಿಸಿದರೆ ಏನು ಮಾಡಬೇಕು?
ಈ ಟ್ಯುಟೋರಿಯಲ್ ಇದನ್ನು ಸರಿಪಡಿಸುವ ಬಗ್ಗೆ.

## ಈಗಾಗಲೇ ಅಸ್ತಿತ್ವದಲ್ಲಿರುವ branch ಗೆ commit ಸ್ಥಳಾಂತರಿಸುವುದು

ಈ ಕೆಳಗಿನ ಆಜ್ಞೆಗಳನ್ನು ಬಳಸಿ:

```bash
git reset HEAD~ --soft  # ಕೊನೆಯ commit ಅನ್ನು ಹಿಂದಕ್ಕೆ ಕೊಂಡು ಬರುತ್ತದೆ, ಆದರೆ ಪರಿಷ್ಕರಣೆಗಳನ್ನು ಉಳಿಸುತ್ತದೆ.
git stash  # ಪ್ರಸ್ತುತ ಸ್ಥಿತಿಯನ್ನು ಸಂಗ್ರಹಿಸುತ್ತದೆ.

git checkout name-of-the-correct-branch  # ಸರಿಯಾದ branch ಗೆ ತೆರಳುತ್ತದೆ.
git stash pop  # ಹಿಂದಿನ ಸ್ಥಿತಿಯನ್ನು ಪುನಃ ಪ್ರಸ್ತಾಪಿಸುತ್ತದೆ.
git add .  # ಎಲ್ಲಾ ಪರಿಷ್ಕರಣೆಗಳನ್ನು stage ಮಾಡುತ್ತದೆ.
git commit -m "your message here"  # commit ಮಾಡುತ್ತದೆ.
```

ಈಗ ನಿಮ್ಮ ಪರಿಷ್ಕರಣೆಗಳು ಸರಿಯಾದ branch ನಲ್ಲಿ ಇವೆ.

## ಹೊಸ branch ಗೆ commit ಸ್ಥಳಾಂತರಿಸುವುದು

```bash
git branch newbranch  # ಹೊಸ branch ರಚಿಸುತ್ತದೆ.
git reset --hard HEAD~#  # # ಗಿಂತ ಹಳೆಯ commit ಗಳನ್ನು ಹಿಂದಕ್ಕೆ ತೆಗೆದುಕೊಳ್ಳುತ್ತದೆ (ಈಗಿನ branch ನಿಂದ ಅಳಿಸಿಬಿಡುತ್ತದೆ!).
git checkout newbranch  # ಹೊಸ branch ಗೆ ಸ್ಥಳಾಂತರವಾಗುತ್ತದೆ.
```

**ಗಮನಿಸಿ:** ಯಾವುದೇ commit ಆಗದ ಪರಿಷ್ಕರಣೆಗಳು ಇಲ್ಲವಾಗುತ್ತವೆ!

