# Home Assistant Git Cheatsheet
## To remove cache inside "git add ."
git rm -rf --cached .

## To delete initial commit
git update-ref -d HEAD

## To push to GitHub
git add .
git commit -m "<Message here>"
git push -u origin master
