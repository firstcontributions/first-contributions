

##  SSH Key Generation Guide (Markdown Content):

```markdown
##  How to Generate and Add an SSH Key to GitHub

If you're seeing an error like:

```

[git@github.com](mailto:git@github.com): Permission denied (publickey)

````

You probably haven’t added an SSH key yet. Follow these steps:

---

### Step 1: Generate SSH Key

Open **Git Bash** and run:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
````

Press `Enter` to accept the default save location. Optionally, add a passphrase.

---

### Step 2: Copy the Public Key

Run:

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy the full output that starts with `ssh-ed25519`.

---

###  Step 3: Add Key to GitHub

1. Go to [https://github.com/settings/keys](https://github.com/settings/keys)
2. Click **New SSH Key**
3. Give it a title like `My Laptop`
4. Paste the key and click **Add SSH Key**
5. Leave it set to **Authentication** (not Signing)

---

### Step 4: Test the SSH Connection

Run:

```bash
ssh -T git@github.com
```

Expected result:

```
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
```

---

Now you can clone or push using SSH without issues. ✅

````

---

## ✅ Step 4: Commit and Push

```bash
git add .
git commit -m "Added SSH key generation guide"
git push origin main
````

Or if you're working on a separate branch:

```bash
git checkout -b add-ssh-guide
git push origin add-ssh-guide
```

Then make a pull request if needed.

---


