## ನಿಮ್ಮ Fork ಅನ್ನು ಈ ರೆಪೊಸಿಟರಿಯೊಂದಿಗೆ ಸಮನ್ವಯಗೊಳಿಸುವುದು

ಮೊದಲು, ಪೂರ್ಣ ಸಮನ್ವಯದ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಬೇಕು. ಈ ಸಂದರ್ಭದಲ್ಲಿ, ನಮ್ಮಲ್ಲಿ ಮೂರು ಭಿನ್ನವಾದ ರೆಪೊಸಿಟರಿಗಳು ಇವೆ: ನನ್ನ ಸಾರ್ವಜನಿಕ ರೆಪೊಸಿಟರಿ GitHub ನಲ್ಲಿ `github.com/Roshanjossey/first-contributions/`, ನಿಮ್ಮ Fork GitHub ನಲ್ಲಿ `github.com/Your-Username/first-contributions/` ಮತ್ತು ನೀವು ಕೆಲಸ ಮಾಡುತ್ತಿರುವ ಸ್ಥಳೀಯ ರೆಪೊಸಿಟರಿ. ಈ ರೀತಿಯ ಸಹಯೋಗವನ್ನು *open source* (ಮುಕ್ತ ಆಕರ) ಪ್ರಾಜೆಕ್ಟ್‌ಗಳಲ್ಲಿ ಸಾಮಾನ್ಯವಾಗಿ `Triangle Workflow` ಎಂದು ಕರೆಯುತ್ತಾರೆ.

<img style="float;" src="https://firstcontributions.github.io/assets/additional-material/triangle_workflow.png" alt="triangle workflow" />

ನಿಮ್ಮ ಎರಡು ರೆಪೊಸಿಟರಿಗಳನ್ನು ನನ್ನ ಸಾರ್ವಜನಿಕ ರೆಪೊಸಿಟರಿಯೊಂದಿಗೆ ನವೀಕರಿಸಲು, ಮೊದಲು ನೀವು ನನ್ನ ರೆಪೊಸಿಟರಿಯಿಂದ ನಿಮ್ಮ ಸ್ಥಳೀಯ ರೆಪೊಸಿಟರಿಗೆ `Fetch` ಮತ್ತು `Merge` ಮಾಡಬೇಕು.
ಹಿಂದಿನ ಹಂತದ ನಂತರ, ನೀವು ನಿಮ್ಮ Fork ಗೆ ಸ್ಥಳೀಯ ಬದಲಾವಣೆಗಳನ್ನು `Push` ಮಾಡಬೇಕು. ನೀವು `Pull Request` ಅನ್ನು ಕೇವಲ ನಿಮ್ಮ Fork ನಿಂದ ಮಾತ್ರ ಮಾಡಬಹುದು, ಆದ್ದರಿಂದ Fork ನವೀಕರಿಸುವುದು ಅಂತಿಮ ಹಂತ.

### ಈ ಹಂತಗಳನ್ನು ಅನುಸರಿಸಿ:

#### 1. ನಿಮ್ಮ `master` ಶಾಖೆಯಲ್ಲಿ ಇರುವುದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ

ನೀವು ಯಾವ ಶಾಖೆಯಲ್ಲಿ ಇರುವಿರಿ ಎಂಬುದನ್ನು ಪರಿಶೀಲಿಸಲು:
```bash
git status
```

`master` ನಲ್ಲಿ ಇಲ್ಲದಿದ್ದರೆ, ಅದಕ್ಕೆ ಬದಲಾಯಿಸಿ:
```bash
git checkout master
```

#### 2. ನನ್ನ ರೆಪೊಸಿಟರಿಯನ್ನು `upstream` ಎಂದು ಸೇರಿಸಿ

```bash
git remote add upstream https://github.com/Roshanjossey/first-contributions
```

ಇದರಿಂದ Git ಗೆ ಈ URL ನಲ್ಲಿ ಇನ್ನೊಂದು ಆವೃತ್ತಿಯಿದೆ ಮತ್ತು ಅದನ್ನು `upstream` ಎಂದು ಕರೆಯುತ್ತೇವೆ ಎಂದು ತಿಳಿಯುತ್ತದೆ.

#### 3. `upstream` ರೆಪೊಸಿಟರಿಯಿಂದ ಬದಲಾವಣೆಗಳನ್ನು ಪಡೆಯುವುದು

```bash
git fetch upstream
```

ಇದು `upstream` ರೆಪೊಸಿಟರಿಯ ಎಲ್ಲಾ ಬದಲಾವಣೆಗಳನ್ನು ಪಡೆಯುತ್ತದೆ.

#### 4. ಬದಲಾವಣೆಗಳನ್ನು ನಿಮ್ಮ `master` ಶಾಖೆಯಲ್ಲಿ ಪರಿಷ್ಕರಿಸುವುದು

```bash
git rebase upstream/master
```

ಇದರಿಂದ ನೀವು `upstream` ನ ಬದಲಾವಣೆಗಳನ್ನು ನಿಮ್ಮ ಸ್ಥಳೀಯ `master` ಶಾಖೆಗೆ ಅನ್ವಯಿಸುತ್ತೀರಿ.

#### 5. ಬದಲಾವಣೆಗಳನ್ನು ನಿಮ್ಮ GitHub Fork ಗೆ ಅಪ್‌ಲೋಡ್ ಮಾಡುವುದು

```bash
git push origin master
```

ಇದು ನಿಮ್ಮ Fork (`origin`) ನಲ್ಲಿ ನಿಮ್ಮ `master` ಶಾಖೆಯನ್ನು ನವೀಕರಿಸುತ್ತದೆ.

ಈಗ, ನಿಮ್ಮ Fork ಮತ್ತು ಸ್ಥಳೀಯ ರೆಪೊಸಿಟರಿ ಅಪ್‌ಡೇಟ್ ಆಗಿದೆ! ನಿಮಗೆ ಶುಭವಾಗಲಿ!

ಪ್ರತಿಯೊಮ್ಮೆ ನಿಮ್ಮ GitHub Fork `commits behind` ಎಂಬ ಸಂದೇಶ ತೋರಿಸಿದಾಗ ಈ ಹಂತಗಳನ್ನು ಅನುಸರಿಸಿ.

