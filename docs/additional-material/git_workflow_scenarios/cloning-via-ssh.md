# Cloning a Repository via SSH

When contributing to open-source projects, cloning via **SSH** is often preferred over HTTPS because it is more secure and eliminates the need to enter your username/password every time you push changes.

This guide explains how to set up SSH keys and clone a repository using SSH.

---

## 1. Fork the Repository
1. Go to the repository on GitHub that you want to contribute to.
2. Click the **Fork** button in the top-right corner.  
   This will create a copy of the repository under your own GitHub account.

---

## 2. Generate SSH Keys
Before cloning via SSH, you need an SSH key pair (public and private key).

1. Open a terminal and run the following command:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```
   - `-t rsa` → specifies RSA algorithm.  
   - `-b 4096` → generates a strong 4096-bit key.  
   - `-C` → adds a label (usually your email).

2. When prompted for a file location, press **Enter** to save in the default path:
   ```
   ~/.ssh/id_rsa
   ```

3. Set a passphrase (optional but recommended).

4. Your SSH key pair is now created:
   - **Private key** → `~/.ssh/id_rsa` (keep this safe, never share).  
   - **Public key** → `~/.ssh/id_rsa.pub` (this will be added to GitHub).

---

## 3. Add Your SSH Key to GitHub
1. Copy your public key:
   ```bash
   cat ~/.ssh/id_rsa.pub
   ```
   Copy the entire output.

2. Go to **GitHub → Settings → SSH and GPG keys → New SSH key**.

3. Give it a title (like "My Laptop") and paste the copied public key.

4. Save it.

---

## 4. Test Your SSH Connection
Run:
```bash
ssh -T git@github.com
```

If successful, you’ll see:
```
Hi username! You've successfully authenticated...
```

---

## 5. Clone the Forked Repository via SSH
Now, clone your fork using SSH:

1. Go to your forked repo on GitHub.  
2. Click the green **Code** button → select **SSH**.  
3. Copy the SSH link (looks like `git@github.com:your-username/first-contributions.git`).  
4. Clone it:
   ```bash
   git clone git@github.com:your-username/first-contributions.git
   ```

---

## 6. Next Steps
- Navigate to the project folder:
  ```bash
  cd first-contributions
  ```
- Create a new branch for your contribution:
  ```bash
  git checkout -b add-branch-name
  ```
- Add your `changed or new` file.  
- Commit and push the changes:
  ```bash
  git add cloning-via-ssh.md
  git commit -m "Add you commit message"
  git push origin add-branch-name
  ```
- Go to your fork on GitHub and create a **Pull Request** into the main repository.

---

## ✅ Summary
You have now:
1. Generated SSH keys.  
2. Added your public key to GitHub.  
3. Cloned the repo via SSH.  
4. Contributed your changes back to the project.
