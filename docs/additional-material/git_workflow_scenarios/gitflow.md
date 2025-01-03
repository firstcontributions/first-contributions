# Gitflow

Gitflow is a branching model for Git made by Vincent Driessen. Here the discussion would be the requirements and use-cases of Gitflow.<br />
The Gitflow workflow defines a strict branching model designed around the project release, which provides a robust framework for managing larger projects. Gitflow is ideally suited for projects that have a scheduled release cycle and for the DevOps best practice of continuous delivery. It assigns very specific roles to different branches and defines how and when they should interact. It uses individual branches for preparing, maintaining and recording releases.


## Implementation

1. **Develop and Master Branches**: Instead of a single master branch, Git Flow uses two branches to record the history of the project. It is based on two main branches with infinite lifetime namely master and develop:
  - **Master Branch**: The master branch contains the production code and stores the official release history.
  - **Develop Branch**: The develop branch contains pre-production code and serves as an integration branch for features.
  - **Creating a Develop Branch**:<br />
    Without using the Gitflow extensions:
    ```
    git branch develop
    git push -u origin develop
    ```
    Using the Gitflow extensions: When using the gitflow extension library, executing `git flow init` on an existing repo will create the develop branch.
    ```
    git flow init
    ```
2. **Feature Branch**: Each new feature should reside in its branch, which can be pushed to the central repository for backup/collaboration. Feature branches use the latest develop as their parent branch. When a feature is complete, it gets merged back into develop. Features should never interact directly with the master branch.
  - **Creating a Feature Branch**: <br />
    Without git-flow extensions:
    ```
    git checkout develop
    git checkout -b feature_branch
    ```
    With gitflow extensions:
    ```
    git flow feature start feature_branch
    ```
  - **Finishing a Feature Branch**: <br />
    Without git-flow extensions:
    ```
    git checkout develop
    git merge feature_branch
    ```
    With git-flow extensions:
    ```
    git flow feature finish feature_branch
    ```
3. **Release Branch**: Once develop has acquired enough features for a release (or a predetermined release date is approaching), we fork a release branch off of develop. Creating this branch starts the next release cycle, so no new features can be added after this point—only bug fixes, documentation generation, and other release-oriented tasks should go in this branch. Release branch may branch off from develop and must merge into both master and develop. <br />
Using a dedicated branch to prepare releases makes it possible for one team to polish the current release while another team continues working on features for the next release.
  - **Creating a Release Branch**: <br />
    Without the git-flow extensions:
    ```
    git checkout develop
    git checkout develop
    git checkout -b release/0.1.0
    ```
    When using the git-flow extensions:
    ```
    git flow release start 0.1.0
    ```
    Switched to a new branch 'release/0.1.0'
  - **Finishing a Release Branch**: <br />
    Without git-flow extensions:
    ```
    git checkout master
    git merge release/0.1.0
    ```
    With git-flow extensions:
    ```
    git flow release finish 0.1.0
    ```
4. **Hotfix Branch**: Maintenance or “hotfix” branches are used to quickly patch production releases. Hotfix branches are necessary to act immediately upon an undesired status of master. Hotfix branches are a lot like release branches and feature branches except they’re based on master instead of develop. This is the only branch that should fork directly off of master. As soon as the fix is complete, it should be merged into both master and develop (or the current release branch), and the master branch should be tagged with an updated version number.
  - **Creating a Hotfix Branch**: <br />
    Without git-flow extensions:
    ```
    git checkout master
    git checkout -b hotfix_branch
    ```
    With git-flow extensions: 
    ```
    git flow hotfix start hotfix_branch
    ```
  - **Finishing a Hotfix Branch**: <br />
  Without git-flow extensions:
    ```
    git checkout master
    git merge hotfix_branch
    git checkout develop
    git merge hotfix_branch
    ```
    With git-flow extensions:
    ```
    git branch -D hotfix_branch
    git flow hotfix finish hotfix_branch
    ```


## Advantages

- Ensures a clean state of branches at any given moment in the life cycle of a project.
- The naming convention of branches follows a systematic pattern making it easier to comprehend.
- Has extensions and support on most used git tools.
- Ideal in case of maintaining multiple versions in production.
- Great for a release-based software workflow.
- Offers a dedicated channel for hotfixes to production.


## Disadvantages

- Git history becomes unreadable.
- The master/ develop branch split is considered redundant and makes the Continuous Delivery/ Integration harder.
- Not recommended in case of maintaining a single version in production.


## Summary

Here we discussed the Git Flow Workflow. Git Flow is one of the many styles of Git workflows you and your team can utilize. Let’s summarize the whole workflow of Git Flow:
1. A develop branch is created from master.
1. Feature branches are created from develop.
1. When a feature is complete it is merged into the develop branch.
1. A release branch is created from develop.
1. When the release branch is done it is merged into develop and master.
1. If an issue in the master is detected a hotfix branch is created from master.
1. Once the hotfix is complete it is merged to both develop and master.
