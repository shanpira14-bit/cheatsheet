# Git cheatsheet


## Basics
Create empty Git repo in specified directory. 
Run with no arguments to initialize the current directory as a git repository.
``` 
git init
```

Clone repo located at <repo> onto local machine. 
Original repo can be located on the local filesystem or on a remote machine via HTTP or SSH
```
git clone <repo url>
```

## Stage & Snapshot
List which files are staged, unstaged, and untracked.
```
git status
```
Stage all changes in <directory> for the next commit.
Replace <directory> with a <file> to change a specific file.
```
git add <directory/file>
```
Commit the staged snapshot, but instead of launching a text editor, use <message> as the commit message.
```
git commit -m <message>
```

## Branch & Merge
Create and check out a new branch named <branch>.
Drop the -b flag to checkout an existing branch.
```
git checkout -b <branch>
```
  

If your branch is behind by master then do:
  
```
git checkout master (you are switching your branch to master)
git pull 
git checkout yourBranch (switch back to your branch)
git merge master
```
