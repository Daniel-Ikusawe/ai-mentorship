# Git Cheatsheet

A reference for every Git command and terminal command used so far.

---

## Git Commands

### Setting Up

| Command | What it does |
|--------|--------------|
| `git init` | Initialise a new Git repository in the current folder |
| `git clone <url>` | Copy a remote repository onto your local machine |
| `git remote add origin <url>` | Link your local repo to a remote GitHub repository |

**Examples:**
```bash
git init
git clone https://github.com/Daniel-Ikusawe/projects.git
git remote add origin https://github.com/Daniel-Ikusawe/my-repo.git
```

---

### Saving Changes

| Command | What it does |
|--------|--------------|
| `git add <file>` | Stage a specific file ready for committing |
| `git add .` | Stage all changed files at once |
| `git commit -m "message"` | Save staged changes with a descriptive message |

**Examples:**
```bash
git add tracker.html
git add .
git commit -m "add daily tracker tool"
```

---

### Syncing with GitHub

| Command | What it does |
|--------|--------------|
| `git push` | Upload local commits to the remote repository |
| `git push -u origin main` | Push to remote and set it as the default upstream (first push) |
| `git pull` | Download and merge the latest changes from the remote |

**Examples:**
```bash
git push
git push -u origin main
git pull
```

---

### Branches

| Command | What it does |
|--------|--------------|
| `git branch` | List all local branches |
| `git branch <name>` | Create a new branch |
| `git branch -M main` | Rename the current branch to `main` |
| `git branch -d <name>` | Delete a local branch (safe — only if merged) |
| `git checkout <branch>` | Switch to an existing branch |
| `git checkout -b <name>` | Create a new branch and switch to it immediately |
| `git merge <branch>` | Merge another branch into your current branch |
| `git push origin --delete <name>` | Delete a branch on the remote (GitHub) |

**Examples:**
```bash
git branch
git branch feature/new-page
git branch -M main
git checkout main
git checkout -b feature/new-page
git merge feature/new-page
git branch -d feature/new-page
git push origin --delete feature/new-page
```

---

### Useful Extras

| Command | What it does |
|--------|--------------|
| `git status` | Show which files are staged, changed, or untracked |
| `git log --oneline` | View recent commits in a compact format |
| `git diff` | Show unstaged changes line by line |

**Examples:**
```bash
git status
git log --oneline
git diff
```

---

## Terminal Commands

These work in both PowerShell and bash unless marked otherwise.

| Command | What it does |
|--------|--------------|
| `pwd` | Print the current directory path |
| `ls` | List files and folders in the current directory |
| `cd <folder>` | Move into a folder |
| `cd ..` | Move up one folder level |
| `mkdir <name>` | Create a new folder |
| `New-Item <name>` | Create a new file *(PowerShell only)* |
| `Remove-Item <name>` | Delete a file or folder *(PowerShell only)* |

**Examples:**
```powershell
pwd
ls
cd AI-Mentorship
cd ..
mkdir new-project
New-Item notes.txt
Remove-Item notes.txt
```

> **Note:** `New-Item` and `Remove-Item` are PowerShell-specific. The equivalent in bash is `touch` (create file) and `rm` (remove).

---

## Quick Reference: Starting a New Project

```bash
# 1. Create and enter folder
mkdir my-project
cd my-project

# 2. Initialise Git
git init

# 3. Create your files, then stage and commit
git add .
git commit -m "first commit"

# 4. Link to GitHub and push
git remote add origin https://github.com/your-username/my-project.git
git branch -M main
git push -u origin main
```

---

## Quick Reference: Pushing an Update

```bash
git add <file>
git commit -m "describe what changed"
git push
```
