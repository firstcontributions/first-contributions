## ನಿಮ್ಮ Fork ಅನ್ನು ಈ Repository ಯೊಂದಿಗೆ ಸಮನ್ವಯಗೊಳಿಸುವದು

ಮೊದಲು, ಪೂರ್ಣ ಸಮನ್ವಯದ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ವದು. ಈ ಸಂದರ್ಭದಲ್ಲಿ, ನಮ್ಮಲ್ಲಿ ಮೂರು ಭಿನ್ನವಾದ Repository ಗಳುಂಡು: ನಡ ಸಾರ್ವಜನಿಕ Repository GitHub ನಲ್ಲಿ `github.com/Roshanjossey/first-contributions/`, ನಿಮ್ಮ Fork GitHub ನಲ್ಲಿ `github.com/Your-Username/first-contributions/` ಮತ್ತು ನಿಂಗ ಕೆಲಸ ಮಾಡುವ ಸ್ಥಳೀಯ Repository. ಈ ರೀತಿಯ ಸಹಯೋಗವನ್ನು *open source* (ಮುಕ್ತ ಆಕರ) ಪ್ರಾಜೆಕ್ಟ್‌ಗಳಲ್ಲಿ ಸಾಮಾನ್ಯವಾಗಿ `Triangle Workflow` ಎಂದು ಕಾಂಬ.

<img style="float;" src="https://firstcontributions.github.io/assets/additional-material/triangle_workflow.png" alt="triangle workflow" />

ನಿಮ್ಮ ಎರಡು Repository ಗಳ್ ನಡ ಸಾರ್ವಜನಿಕ Repository ಯೊಂದಿಗೆ ನವೀಕರಿಸುವಕ್, ಮೊದಲು ನಿಂಗ ನಡ Repository ಯಿಂದ ನಿಮ್ಮ ಸ್ಥಳೀಯ Repository ಗೆ `Fetch` ಮತ್ತು `Merge` ಮಾಡೋಕು.
ಹಿಂದಿನ ಹಂತದ ಪಿನ್ನೆ, ನಿಂಗ ನಿಮ್ಮ Fork ಗೆ ಸ್ಥಳೀಯ ಬದಲಾವಣೆಗಳ್ `Push` ಮಾಡೋಕು. ನಿಂಗ `Pull Request` ಅನ್ನು ಕೇವಲ ನಿಮ್ಮ Fork ನಿಂದ ಮಾತ್ರ ಮಾಡಲಕ್ಕು, ಆದ್ದರಿಂದ Fork ನವೀಕರಿಸುವದು ಅಂತಿಮ ಹಂತ.

### ಈ ಹಂತಗಳ್ ಅನುಸರಿಸಿ:

#### 1. ನಿಮ್ಮ `master` Branch ನಲ್ಲಿ ಉಂಡು ಖಚಿತಪಡಿಸಿ

ನಿಂಗ ಯಾವ Branch ನಲ್ಲಿ ಉಂಡು ಎಂಬುದನ್ನು ಪರಿಶೀಲಿಸುವಕ್:
```bash
git status
```

`master` ನಲ್ಲಿ ಇಲ್ಲದಿದ್ದರೆ, ಅದಕ್ಕೆ ಬದಲಾಯಿಸಿ:
```bash
git checkout master
```

#### 2. ನಡ Repository ಯನ್ನು `upstream` ಎಂದು ಸೇರಿಸಿ

```bash
git remote add upstream https://github.com/Roshanjossey/first-contributions
```

ಇದರಿಂದ Git ಗೆ ಈ URL ನಲ್ಲಿ ಇನ್ನೊಂದು ಆವೃತ್ತಿಯುಂಡು ಮತ್ತು ಅದನ್ನು `upstream` ಎಂದು ಕರೆಯುವ ಎಂಬುದು ತಿಳಿಯುವ.

#### 3. `upstream` Repository ಯಿಂದ ಬದಲಾವಣೆಗಳ್ ಪಡೆಯುವದು

```bash
git fetch upstream
```

ಇದು `upstream` Repository ಯ ಎಲ್ಲಾ ಬದಲಾವಣೆಗಳ್ ಪಡೆಯುವ.

#### 4. ಬದಲಾವಣೆಗಳ್ ನಿಮ್ಮ `master` Branch ನಲ್ಲಿ ಪರಿಷ್ಕರಿಸುವದು

```bash
git rebase upstream/master
```

ಇದರಿಂದ ನಿಂಗ `upstream` ನ ಬದಲಾವಣೆಗಳ್ ನಿಮ್ಮ ಸ್ಥಳೀಯ `master` Branch ಗೆ ಅನ್ವಯಿಸುವಿರ.

#### 5. ಬದಲಾವಣೆಗಳ್ ನಿಮ್ಮ GitHub Fork ಗೆ ಅಪ್‌ಲೋಡ್ ಮಾಡ್ವದು

```bash
git push origin master
```

ಇದು ನಿಮ್ಮ Fork (`origin`) ನಲ್ಲಿ ನಿಮ್ಮ `master` Branch ಅನ್ನು ನವೀಕರಿಸುವ.

ಈಗ, ನಿಮ್ಮ Fork ಮತ್ತು ಸ್ಥಳೀಯ Repository ಅಪ್‌ಡೇಟ್ ಆಗಿದೆ! ನಿಮಗೆ ಶುಭವಾಗಲಿ!

ಪ್ರತಿಯೊಮ್ಮೆ ನಿಮ್ಮ GitHub Fork `commits behind` ಎಂಬ ಸಂದೇಶ ತೋರಿಸಿದಾಗ ಈ ಹಂತಗಳ್ ಅನುಸರಿಸಿ.