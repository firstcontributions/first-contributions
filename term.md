PS C:\open_source\first-contributions> git switch -c boooom   
Switched to a new branch 'boooom'
PS C:\open_source\first-contributions> git add .\Contributors.md
PS C:\open_source\first-contributions> git status
On branch boooom
nothing to commit, working tree clean
PS C:\open_source\first-contributions> git add .\Contributors.md
PS C:\open_source\first-contributions> git status
On branch boooom
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   Contributors.md

PS C:\open_source\first-contributions> git commit -m "Add Vishwanath to contributing list"
[boooom 6b84852a7] Add Vishwanath to contributing list
 1 file changed, 2 insertions(+)
PS C:\open_source\first-contributions> git push -u origin boooom
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 340 bytes | 340.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote: 
remote: Create a pull request for 'boooom' on GitHub by visiting:
remote:      https://github.com/VishwanathSK-IND/first-contributions/pull/new/boooom
remote: 
To https://github.com/VishwanathSK-IND/first-contributions.git
 * [new branch]          boooom -> boooom
branch 'boooom' set up to track 'origin/boooom'.
PS C:\open_source\first-contributions> git status
On branch boooom
Your branch is up to date with 'origin/boooom'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   Contributors.md

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\open_source\first-contributions> git status
On branch boooom
Your branch is up to date with 'origin/boooom'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   Contributors.md

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\open_source\first-contributions> git status
On branch boooom
Your branch is up to date with 'origin/boooom'.

nothing to commit, working tree clean
PS C:\open_source\first-contributions> 
 *  History restored 

PS C:\open_source\first-contributions> git checkout -b bean
Switched to a new branch 'bean'
PS C:\open_source\first-contributions> git switch -c helooo
Switched to a new branch 'helooo'
PS C:\open_source\first-contributions> cd
PS C:\open_source\first-contributions> cd ..
PS C:\open_source> cd .\first-contributions\
PS C:\open_source\first-contributions> git checkout -b bean
fatal: a branch named 'bean' already exists
PS C:\open_source\first-contributions> git status
On branch helooo
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   Contributors.md

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\open_source\first-contributions> git add .\Contributors.md
PS C:\open_source\first-contributions> git commit -m "huuu"
[helooo c6a589492] huuu
 1 file changed, 1 insertion(+), 1 deletion(-)
PS C:\open_source\first-contributions> git push -u origin helooo
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 328 bytes | 164.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote: 
remote: Create a pull request for 'helooo' on GitHub by visiting:
remote:      https://github.com/VishwanathSK-IND/first-contributions/pull/new/helooo
remote: 
To https://github.com/VishwanathSK-IND/first-contributions.git
 * [new branch]          helooo -> helooo
branch 'helooo' set up to track 'origin/helooo'.