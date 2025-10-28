"""
Auto Git Setup Script
---------------------
This script helps new contributors correctly configure Git before committing.

It checks:
1. If username/email are configured.
2. If default branch is 'main'.
3. Guides through staging and committing with friendly prompts.
"""

import os
import subprocess

def run_command(cmd):
    return subprocess.getoutput(cmd)

def check_git_config():
    username = run_command("git config user.name")
    email = run_command("git config user.email")

    if not username:
        print("⚠️  Git username not configured.")
        name = input("Enter your Git username: ")
        os.system(f'git config --global user.name "{name}"')
    else:
        print(f"✅ Git username: {username}")

    if not email:
        print("⚠️  Git email not configured.")
        email = input("Enter your Git email: ")
        os.system(f'git config --global user.email "{email}"')
    else:
        print(f"✅ Git email: {email}")

def check_default_branch():
    branch = run_command("git symbolic-ref --short HEAD")
    if branch != "main":
        print(f"⚠️  Default branch is '{branch}'. Recommended: 'main'")
        choice = input("Rename current branch to 'main'? (y/n): ")
        if choice.lower() == "y":
            os.system("git branch -m main")
            print("✅ Branch renamed to 'main'")
    else:
        print("✅ Default branch is already 'main'")

def safe_commit():
    print("\n🧩 Preparing to commit changes safely.")
    os.system("git status")
    choice = input("\nStage all changes and commit? (y/n): ")
    if choice.lower() == "y":
        os.system("git add .")
        message = input("Enter commit message: ")
        os.system(f'git commit -m "{message}"')
        print("✅ Commit created successfully.")
    else:
        print("❌ Commit canceled by user.")

if __name__ == "__main__":
    print("🚀 Starting Git Setup Helper for New Contributors...\n")
    check_git_config()
    check_default_branch()
    safe_commit()
