# Commit ಅನ್ನು ಬೇರೆ Branch ಗೆ ಸ್ಥಳಾಂತರಿಸುವದು

ನಿಂಗ Commit ಮಾಡಿದ ಪಿನ್ನೆ, ಅದು ತಪ್ಪಾಗಿ ಬೇರೆ Branch ನಲ್ಲಿ ಆಗಿದೆ ಎಂದು ಗಮನಿಸಿದರೆ ಏನ್ ಮಾಡ್ವದು?
ಈ ಟ್ಯುಟೋರಿಯಲ್ ಇದನ್ನು ಸರಿಪಡಿಸುವ ಬಗ್ಗೆ ಉಂಡು.

## ಆಗಲೇ ಅಸ್ತಿತ್ವದಲ್ಲಿರುವ Branch ಗೆ Commit ಸ್ಥಳಾಂತರಿಸುವದು

ಈ ಕೆಳಗಿನ ಆಜ್ಞೆಗಳ್ ಬಳಸಿ:

```bash
git reset HEAD~ --soft  # ಕೊನೆಯ Commit ಅನ್ನು ಹಿಂದಕ್ಕೆ ಕೊಡುವ, ಆದರೆ ಪರಿಷ್ಕರಣೆಗಳ್ ಉಳಿಸುವ.
git stash  # ಪ್ರಸ್ತುತ ಸ್ಥಿತಿಯನ್ನು ಸಂಗ್ರಹಿಸುವ.

git checkout name-of-the-correct-branch  # ಸರಿಯಾದ Branch ಗೆ ತೆರಳುವ.
git stash pop  # ಹಿಂದಿನ ಸ್ಥಿತಿಯನ್ನು ಪುನಃ ಪ್ರಸ್ತಾಪಿಸುವ.
git add .  # ಎಲ್ಲಾ ಪರಿಷ್ಕರಣೆಗಳ್ stage ಮಾಡುವ.
git commit -m "your message here"  # Commit ಮಾಡುವ.
```

ಈಗ ನಿಮ್ಮ ಪರಿಷ್ಕರಣೆಗಳ್ ಸರಿಯಾದ Branch ನಲ್ಲಿ ಉಂಡು.

## ಹೊಸ Branch ಗೆ Commit ಸ್ಥಳಾಂತರಿಸುವದು

```bash
git branch newbranch  # ಹೊಸ Branch ರಚಿಸುವ.
git reset --hard HEAD~#  # # ಗಿಂತ ಹಳೆಯ Commit ಗಳ್ ಹಿಂದಕ್ಕೆ ತೆಗೆದುಕೊಳ್ಳುವ (ಈಗಿನ Branch ನಿಂದ ಅಳಿಸಿಬಿಡುವ!).
git checkout newbranch  # ಹೊಸ Branch ಗೆ ಸ್ಥಳಾಂತರವಾಗುವ.
```

**ಗಮನಿಸಿ:** ಯಾವುದೇ Commit ಆಗದ ಪರಿಷ್ಕರಣೆಗಳ್ ಇಲ್ಲವಾಗುವ!