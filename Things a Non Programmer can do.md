# Things a non Programmer can do

## Start listening

Everything in open source involves other people.
You're looking to join a team, and that means understanding the community and how it works.
Walking into a project and saying "Hi, here's what I think this project should be doing" is usually not taken as a good thing.
Some projects may welcome that sort of approach, but if the project has been running a while, the chances of that attitude being embraced are small.
**Listening is the best way to know what the project needs.**

1. **Join a mailing list**: For many projects, the mailing list is the main conduit of communication about the development of the project.
On large projects, there are many mailing lists to choose from.
For example, the PostgreSQL project has no fewer than 12 user-oriented lists and six developer lists on its mailing list page.
I suggest you follow the main user-oriented list and the core developer list in which to start listening.

2. **Follow a blog**: Blogs maintained by core developers often give information about what's coming up in future releases,
and what it's taken to get there. A planet site aggregates news and blog entries from many sources related to the project.
If there is a planet site, like planet.gnome.org or planet.mysql.com, start there. Just search Google for "planet <projectname>."

3. **Join an IRC channel**: Many open source projects have dedicated Internet relay chat (IRC) channels where developers and users hang out to discuss problems and development.
Check the project's website for the details of what the channel is called and what IRC network it's found on.

## Work with Tickets  

Code is the heart of any open source project, but don't think that writing code is the only way to contribute.
Maintenance of code and the systems surrounding the code often are neglected in the rush to create new features and to fix bugs.
Look to these areas as an easy way to get your foot into a project.
Most projects have a publicly visible trouble ticket system, linked from the front page of the project's website and included in the documentation.
It's the primary conduit of communication between the users and the developers. Keeping it current is a great way to help the project.
You may need to get special permissions in the ticketing system, which most project leaders will be glad to give you when you say you want to help clean up the tickets.

4. **Diagnose a bug**: Encourage non-programmers to help diagnose bugs by providing detailed steps to reproduce issues and adding findings to bug reports.
5. **Close fixed bugs**: Guide non-programmers on how to verify and close resolved bugs in the ticketing system, helping maintain an organized and up-to-date record of issues.

## Working with Code  

Programmers of all experience levels can help with the code in the project.
Don't think that you have to be a coding genius to make real contributions to your favorite project.

If your work involves modification to the code, investigate the method that the project uses for getting code from contributors.
Each project has its own workflow, so ask about how to do it before you set out to submit code.

For example, the PostgreSQL project is very rigorous in its process: Code modifications are sent in patch form to a mailing list where core developers scrutinize every aspect of the change. On the other end is a project like Parrot where it's easy to get commit privileges to the codebase. If the project uses GitHub, there may be a workflow that uses the pull request feature of GitHub. No two projects are the same.

Whenever you modify code, make sure that you act as a responsible member of the community and keep your code style to match the rest of the codebase. The code you add or modify should look like the rest. You might not like the bracing style or the handling of spaces for indentation, but it's rude to submit a code change that doesn't match the existing standards. It's the same as saying "I don't like your style, and I think mine is better, so you should do it my way."

6. **Test a beta or release candidate**: Non-programmers can contribute by testing pre-release versions of the software and reporting their findings, ensuring the stability of upcoming releases.
7. **Fix a bug**: While programming skills are helpful, non-programmers can still attempt to fix bugs by providing detailed bug reports or collaborating with developers to understand and address issues.
8. **Write a test**: Non-programmers can enhance code quality by writing test cases for specific features or functionalities, ensuring comprehensive test coverage.
9. **Silence a compiler warning**: Guide non-programmers on how to address compiler warnings, helping maintain code cleanliness and improving overall code quality.
10. **Add a comment**: Encourage non-programmers to contribute to code readability by adding comments to explain complex or confusing sections of code.

## Working with Documentation  

Documentation is typically the part of a project that gets short shrift.
It also can suffer from having been written from the point of view of those who are familiar with the project, rather than through the eyes of someone just getting into it.
If you've ever read docs for a project where you think, "It's as though this manual expects that I already know how to use the package," you know what I'm talking about.
Often a set of fresh eyes can point out deficiencies in the documentation that those close to the project don't notice.

11. **Create an example**: Encourage non-programmers to create usage examples or tutorials to supplement project documentation, providing clear and practical guidance for users.
12. **Write technical documentation**: Non-programmers can contribute by documenting software functionalities or usage scenarios in plain language, making the project more accessible to a wider audience.

## Community Engagement  

Open source is only partly about code. Community makes open source work. Here are ways you can help build it up.

13. **Answer a question**: Guide non-programmers on how to engage with the community by providing helpful responses to questions or issues raised by other users.
14. **Write a blog post**: Encourage non-programmers to share their experiences with the project through blog posts, helping raise awareness and attract new contributors.
15. **Improve a website**: Non-programmers with web design skills can contribute to enhancing project websites, improving the project's public-facing image and usability.
16. **Teach and Help others**: Foster a culture of learning and collaboration by encouraging non-programmers to share their knowledge and help others understand project concepts or processes.

Most of all, listen to what people around you discuss. See if you can recognize a pressing need. For instance, recently on the Parrot developers' mailing list, it was decided to use GitHub as the trouble ticket system, abandoning the old Trac installation they had. Some people were against the move because there was no way to convert the tickets to GitHub's system. After a day of back and forth arguing, I piped up and said "How about if I write a converter?" People were thrilled at the idea. I spent the time to write a conversion program for the 450+ tickets, so we lost none of our ticket history. It was a great success.  I got to pitch in, and the core developers stayed focused on the business of working on Parrot.

17. **Listen and Contribute**: Encourage non-programmers to actively listen to community discussions and identify opportunities to contribute, such as writing tools to address specific needs.
