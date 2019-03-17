# Clean and Alphabetize the Contributors.md file

According to this clean-up file, for a line to be 'acceptable' it must:


1. Contain a name
2. Contain a repository link from one of the following:
  - github
  - gitlab
  - bitbucket
3. Takes into consideration and corrects possible mistyped 'github' links (Ex. https://gihtub)
4. Corrects mistyped 'https://' and converts the old unsecure 'http://' style to 'https://'


Run this code from the command line (cmd.exe) in order to 'clean up' and alphabetize the Contributors.md file.

```
C:\your-path\first-contributions> python clean_and_alphabetize.py
```