# Coisas Que Não-Programadores Podem Fazer
## Começar escutando

Tudo em código aberto envolve outras pessoas.
Você está procurando se juntar a um time, e isso significa entender a comunidade e como ela funciona.
Entrar num projeto e dizer: "Ei, é isso o que eu acho que deveriam fazer", não é visto com bons olhos.
Alguns projetos talvez tolerem esse tipo de abordagem mas, se o projeto já existe há algum tempo, as chances dessa atitude ser aceita será bem pequena.

**Escutar é a melhor maneira de conhecer as necessidades de um projeto**

- [ ] **TODO:** algum BR pode traduzir mais alguns §§? ;-)
1. **Join a mailing list**: For many projects, the mailing list is the main conduit of communication about the development of the project.
On large projects, there are many mailing lists to choose from.
For example, the PostgreSQL project has no fewer than 12 user-oriented lists and six developer lists on its mailing list page.
I suggest you follow the main user-oriented list and the core developer list in which to start listening.

2. **Follow a blog**: Blogs maintained by core developers often give information about what's coming up in future releases,
and what it's taken to get there. A planet site aggregates news and blog entries from many sources related to the project.
If there is a planet site, like planet.gnome.org or planet.mysql.com, start there. Just search Google for "planet <projectname>."

3. **Join an IRC channel**: Many open source projects have dedicated Internet relay chat (IRC) channels where developers and users hang out to discuss problems and development.
Check the project's website for the details of what the channel is called and what IRC network it's found on.

**Work with Tickets**  
Code is the heart of any open source project, but don't think that writing code is the only way to contribute.
Maintenance of code and the systems surrounding the code often are neglected in the rush to create new features and to fix bugs.
Look to these areas as an easy way to get your foot into a project.
Most projects have a publicly visible trouble ticket system, linked from the front page of the project's website and included in the documentation.
It's the primary conduit of communication between the users and the developers. Keeping it current is a great way to help the project.
You may need to get special permissions in the ticketing system, which most project leaders will be glad to give you when you say you want to help clean up the tickets.

4. **Diagnose a bug**: Bugs are often poorly reported.
Diagnosing and triaging a bug can help save the developers time with the legwork of figuring out the specifics of the problem.
If a user reported, "The software doesn't work when I do X," spend some time to figure out the specifics of what goes into that problem.
Is it repeatable? Can you create a set of steps to cause the problem repeatedly? Can you narrow down the problem, such as only happening on one browser but not another, or one distro but not another?

Even if you don't know what causes the problem, the effort you put into narrowing down the circumstances makes it easier for someone else to fix it.
Whatever you discover, add it to the ticket in the bug system for all to see.

5. **Close fixed bugs**: Often bugs are fixed in the codebase but tickets reported about them don’t get updated in the ticketing system.
Cleaning up this cruft can be time-consuming, but it's valuable to the whole project.

Start by querying the ticket system for tickets older than a year and see if the bug still exists.
Check the project's release change log to see if the bug was fixed and can be closed.
If it's known to be fixed, note the version number in the ticket and close it.

Try to recreate the bug with the latest version of the software.
If it can't be recreated with the latest version, note that in the ticket and close it.
If it still exists, note that in the ticket as well and leave it open.

Working with Code
Programmers of all experience levels can help with the code in the project.
Don't think that you have to be a coding genius to make real contributions to your favorite project.

If your work involves modification to the code, investigate the method that the project uses for getting code from contributors.
Each project has its own workflow, so ask about how to do it before you set out to submit code.

For example, the PostgreSQL project is very rigorous in its process: Code modifications are sent in patch form to a mailing list where core developers scrutinize every aspect of the change. On the other end is a project like Parrot where it's easy to get commit privileges to the codebase. If the project uses GitHub, there may be a workflow that uses the pull request feature of GitHub. No two projects are the same.

Whenever you modify code, make sure that you act as a responsible member of the community and keep your code style to match the rest of the codebase. The code you add or modify should look like the rest. You might not like the bracing style or the handling of spaces for indentation, but it's rude to submit a code change that doesn't match the existing standards. It's the same as saying "I don't like your style, and I think mine is better, so you should do it my way."

6. **Test a beta or release candidate**: Any project that's designed to run on multiple platforms can have all sorts of portability problems.
When a release approaches and a beta or release candidate is published, the project leader hopes that it will be tested by many different people on many different platforms.
You can be one of those people and help ensure that the package works on your platform.

Typically you only need to download, build, and test the software, but the value to the project can be huge if you're on an uncommon distribution or hardware.
Just reporting back that the build and test works helps the project leaders know that the impending release is solid.

7. **Fix a bug**: This is usually where contributors wanting to get working on code start.
It’s simple: Find an interesting-sounding bug in the ticket system and try to fix it in the code.
Document the fix in the code if it's appropriate.
It's a good idea to add a test to the test suite to test the spot of code you fixed; some projects require bug fixes to include tests. Keep notes as you poke around this unfamiliar codebase. Even if you aren't able to fix the bug, document in the ticket what you discovered as part of the fix attempt. What you find helps those who come after you.

8. **Write a test**: Most projects have a test suite that tests the code, but it's hard to imagine a test suite that couldn't have more tests added to it.
Use a test coverage tool like gcov for C, or Devel::Cover for Perl to identify areas in the source code that aren't tested by the test suite.
Then, add a test to the suite to cover it.

9. **Silence a compiler warning**: The build process for many C-based projects often spew the odd compiler warning flag to the screen.
These warnings are usually not indicators of a problem, but they can look like it.
Having too many warnings can make the compiler sound like it's crying wolf.
Check to see if the code could actually be hiding a bug. If not, modifying the source to silence helps to hide these false positives.

10. **Add a comment**:
When you're digging through the code, you may find some spots that are confusing.
Chances are if you were confused, others will be  as well. Document them in the code and submit a patch.
Work with Documentation
Documentation is typically the part of a project that gets short shrift.
It also can suffer from having been written from the point of view of those who are familiar with the project, rather than through the eyes of someone just getting into it.
If you've ever read docs for a project where you think, "It's as though this manual expects that I already know how to use the package," you know what I'm talking about.
Often a set of fresh eyes can point out deficiencies in the documentation that those close to the project don't notice.

11. **Create an example**: There is no project that has too many how-to examples.
Whether it's a web API, a library of routines, a GUI app like Gimp or a command line tool,
a good example of proper usage can more clearly and quickly explain proper usage of software than pages of documentation.
For an API or library, create an example program that uses the tool. This could even be extracted from code you've written, trimmed down to the bare necessities.
For a tool, show real-world examples of how you've used it in your daily life. If you’re visually oriented,
consider creating a screen-capture of an important process, such as how to install the application.

Work with Community
Open source is only partly about code. Community makes open source work. Here are ways you can help build it up.

12. **Answer a question**: The best way to help build the community is by helping others.
Answering a question, especially from someone who is just getting their feet wet, is crucial to helping the project grow and thrive.
The time you take to help a beginner, even if they're asking a question where you could easily throw back a quick "RTFM," pays off down the road in getting another active member of the community.
Everyone starts out somewhere, and projects need a constant inflow of people if they're to stay vital.

13. **Write a blog post**:
If you've got a blog, write about your experiences with the project that you're using.
Tell about a problem you faced using the software and what you did to solve it.
You'll be helping in two ways, both by helping keep the project on the minds of others around you,
and by creating a record for anyone else who has your problem in the future  and searches the web for the answer.
(A blog of your technical adventures is also an excellent way to show real-world experience with the software in question next time you go hunting for a job using it.)

14. **Improve a website**:
If you've got skills in web design and can help improve the website, and thus the public-facing image of the project, that's time well spent.
Perhaps the project could use a graphic overhaul, or a logo to identify the project.
These may be skills lacking in the community. I know I'd love it if I could get some graphic design help on my projects' websites.
  
15. **Write technical documentation**
  If you can write about how an application or piece of software works, you could write technical documentation about it. Especially open source projects that are looking to update, revamp, expand, or create technical docs for the general public to read. The more you write in plain english, the better. The best part, you don't have to be a programmer to write technical docs.

Most of all, listen to what people around you discuss. See if you can recognize a pressing need. For instance, recently on the Parrot developers' mailing list, it was decided to use GitHub as the trouble ticket system, abandoning the old Trac installation they had. Some people were against the move because there was no way to convert the tickets to GitHub's system. After a day of back and forth arguing, I piped up and said "How about if I write a converter?" People were thrilled at the idea. I spent the time to write a conversion program for the 450+ tickets, so we lost none of our ticket history. It was a great success.  I got to pitch in, and the core developers stayed focused on the business of working on Parrot.

15. **Teach and Help others**:
The best way to learn more about a topic is to try to teach it.
The best teacher is the one who can explain complex stuff with simple examples. So you need to try to be the best teacher to be the best learner and the best in your programming world. Teaching others will make you feel better about yourself and it will help you get better skills and knowledge in your profession. When you get help from someone don't keep it to yourself share it with others. Make the world a better place to live.
