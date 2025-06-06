



First Contributions
We want to help and guide new contributors on how to get started with contributing. If you are looking to make your first contribution, follow the steps below.

If you're not comfortable with the command line, here are tutorials using GUI tools.
Fork this repository
If you don't have Git installed on your machine, install it here.

Fork this repo by clicking the Fork button at the top of this page. This will create a copy of the repository under your GitHub account.

Clone the repository
Now clone the repo to your machine. Go to your GitHub account, open the forked repository, click the Clone button and copy the URL.

Open your terminal and run this command:

bash
Copy
Edit
git clone "URL you just copied"
Example:

bash
Copy
Edit
git clone https://github.com/your-username/first-contributions.git
Replace your-username with your actual GitHub username. This command copies the contents of the forked GitHub repo to your local computer.

Create a branch
Change to the repository directory on your computer (if you're not already in it):

bash
Copy
Edit
cd first-contributions
Now create a new branch using the git checkout command:

bash
Copy
Edit
git checkout -b add-your-name
For example:

bash
Copy
Edit
git checkout -b add-adam-kowalski
(You don't need to prefix your branch name with “add-”, but it helps clarify the purpose.)

Make necessary changes and commit them
Open the Contributors.md file in a text editor and add your name to the list. Place your name anywhere in the file — not necessarily at the top or bottom.

Then save the file.

To see the changes, run:

bash
Copy
Edit
git status
Now stage the file using:

bash
Copy
Edit
git add Contributors.md
Then commit the changes:

bash
Copy
Edit
git commit -m "Add your-name to Contributors list"
Replace your-name with your actual name.

Push changes to GitHub
Push your changes using:

bash
Copy
Edit
git push origin add-your-branch-name
Replace add-your-branch-name with your actual branch name.

Submit your changes for review
Go to your GitHub repo and you'll see a Compare & pull request button. Click that.

Then submit your pull request.

I'll merge your changes into the main branch of this project. You'll receive a notification once it's done.

What next?
Congratulations! 🎉 You've just completed the standard workflow of forking → cloning → editing → pull request. You’ll follow this workflow in many projects.

Celebrate your contribution and share it with your friends and followers by visiting the web app.

You can also join our Slack team if you need any help or have questions:
👉 Join our Slack Team

Now let’s continue contributing to other projects.
Check out this project list for more beginner-friendly projects.

Additional Resources
					
GitHub Desktop Guide	Visual Studio 2017 Guide	GitKraken Guide	VS Code Guide	Sourcetree Guide	IntelliJ IDEA Guide

