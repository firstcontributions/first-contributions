What is “version control”? 

Version control systems are a category of software tools that helps in record changes made to the files by keeping a track of modifications done in the code. 

Why it is so important?

We know that a software is developed in collaboration by a group of developers they might be located at different locations and each one of them contributes to some specific kind of functionality/features. So in order to contribute to the product, they made modifications to the source code(either by adding or removing). A version control system is a kind of software that helps the developer team to efficiently communicate and manage(track) all the changes that have been made to the source code along with the information like who made and what changes have been made. A separate branch is created for every contributor who made the changes and the changes aren’t merged into the original source code unless all are analyzed as soon as the changes are green signaled they merged to the main source code. It not only keeps source code organized but also improves productivity by making the development process smooth.

Benefits of the version control system:

1. Enhances the project development speed by providing efficient collaboration.
2. Leverages the productivity, expedites product delivery, and skills of the employees through better communication and assistance.
3. Reduce possibilities of errors and conflicts meanwhile project development through traceability to every small change.
4. Helps in recovery in case of any disaster or contingent situation.
5. Informs us about Who, What, When, Why changes have been made.

Types of Version Control Systems: 

1. Local Version Control Systems
2. Centralized Version Control Systems
3. Distributed Version Control Systems

1. Local Version Control Systems: It is one of the simplest forms and has a database that kept all the changes to files under revision control. RCS is one of the most common VCS tools. It keeps patch sets (differences between files) in a special format on disk. By adding up all the patches it can then re-create what any file looked like at any point in time. 

2. Centralized Version Control Systems: Centralized version control systems contain just one repository globally and every user need to commit for reflecting one’s changes in the repository. It is possible for others to see your changes by updating. 

Two things are required to make your changes visible to others which are:  

You commit
They update

The benefit of CVCS (Centralized Version Control Systems) makes collaboration amongst developers along with providing an insight to a certain extent on what everyone else is doing on the project. It allows administrators to fine-grained control over who can do what. 

3. Distributed Version Control Systems: Distributed version control systems contain multiple repositories. Each user has their own repository and working copy. Just committing your changes will not give others access to your changes. This is because commit will reflect those changes in your local repository and you need to push them in order to make them visible on the central repository. Similarly, When you update, you do not get others’ changes unless you have first pulled those changes into your repository. 

To make your changes visible to others, 4 things are required:  

You commit
You push
They pull
They update

The most popular distributed version control systems are Git, and Mercurial. They help us overcome the problem of single point of failure.  

Purpose of Version Control: 

1. Multiple people can work simultaneously on a single project. Everyone works on and edits their own copy of the files and it is up to them when they wish to share the changes made by them with the rest of the team.
2. It also enables one person to use multiple computers to work on a project, so it is valuable even if you are working by yourself.
3. It integrates the work that is done simultaneously by different members of the team. In some rare cases, when conflicting edits are made by two people to the same line of a file, then human assistance is requested by the version control system in deciding what should be done.
4. Version control provides access to the historical versions of a project. This is insurance against computer crashes or data loss. If any mistake is made, you can easily roll back to a previous version. It is also possible to undo specific edits that too without losing the work done in the meanwhile. It can be easily known when, why, and by whom any part of a file was edited.


**Ref: GFG