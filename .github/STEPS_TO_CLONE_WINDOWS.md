Here is a step-by-step guide in Markdown for cloning a GitHub repository using SSH on Windows:

How to Clone a GitHub Repository on Windows (SSH)
1. Install Git for Windows
Download and install Git from: https://git-scm.com/download/win

2. Generate an SSH Key (if you haven't already)
Open PowerShell and enter:

text
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
Press Enter to accept the default save location.

Optionally enter a passphrase and remember it.

3. Start the SSH Agent and Add Your Key
powershell
Start-Service ssh-agent
ssh-add $env:USERPROFILE\.ssh\id_rsa
4. Copy Your SSH Public Key
powershell
Get-Content $env:USERPROFILE\.ssh\id_rsa.pub
Copy the whole output.

5. Add the SSH Key to Your GitHub Account
Go to https://github.com/settings/keys

Click "New SSH Key"

Enter a title and paste your public key

Click “Add SSH key”

6. Clone the Repository
Get the SSH clone URL from GitHub (e.g. git@github.com:username/repository.git).
In PowerShell, type:

text
git clone git@github.com:username/repository.git
7. Find Your Cloned Repository
It will be in a folder named after the repo (e.g., repository) inside the directory where you ran the clone command.

To move into the folder:

text
cd repository
To list the files:

text
dir
This step-by-step guide works for both public and private repositories as long as your SSH key is added and you have access rights​.