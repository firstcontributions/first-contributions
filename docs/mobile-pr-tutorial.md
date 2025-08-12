# 📱 Reviewing & Managing Pull Requests on Mobile Devices

Open-source contributions are not limited to laptops or desktops. With modern mobile apps, you can review, edit, and manage Pull Requests (PRs) directly from your phone or tablet.

---

## 1️⃣ Using the GitHub Mobile App (iOS & Android)
The official [GitHub Mobile](https://github.com/mobile) app allows you to:
- Review PRs
- Approve or request changes
- Comment on code lines
- Merge PRs

**Steps:**
1. Install **GitHub** from App Store (iOS) or Play Store (Android).
2. Log in with your GitHub account.
3. Navigate to the repository and open the **Pull Requests** tab.
4. Select a PR, read the changes, and leave comments or approve.
5. If you have merge rights, tap **Merge Pull Request**.

---

## 2️⃣ Using Working Copy (iOS)
[Working Copy](https://workingcopyapp.com/) is a powerful Git client for iOS.

**Steps:**
1. Install the **Working Copy** app from App Store.
2. Clone the repository by tapping **+ → Clone Repository**.
3. Check out the PR branch:
   - Tap **Branches** → select the PR branch.
4. Make changes in any linked code editor (e.g., Textastic, Buffer Editor).
5. Commit your changes and push to the remote branch.

---

## 3️⃣ Using Termux (Android)
[Termux](https://termux.dev/) provides a Linux terminal on Android.

**Steps:**
1. Install **Termux** from F-Droid.
2. Install Git:
   ```bash
   pkg install git

   Clone the repository:

   git clone <repo-url>

   Checkout the PR branch:

   git checkout <branch-name>

   Edit files with a terminal editor like nano or vim.
 
   Commit and push your changes:

   git commit -am "Updated via mobile"
   git push origin <branch-name>
   
  ```
