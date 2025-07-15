Title: Things I Like to Do with Git
Date: 2025-07-13 16:55
Modified: 2025-07-13 16:55
Category: Git
Tags: git, github, scm, linux, command line, source code management
Slug: things-i-like-to-do-with-git
Authors: Craig Derington
Summary: Git commands I use on the daily...

## THINGS I LIKE TO DO WITH GIT

Little Things I Like to Do with Git


Short Log


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$ git shortlog -sn

$ git shortlog -sn --since='10 weeks' --until='2 weeks'

-- alias git stats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Blame


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$ git blame -L5,10 _components.buttons.css

$ git config --global alias.praise blame

$ git praise -L18,23 _includes/head.html
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Diff - Show Changed Words Instead of Whole Lines


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$ git diff --word-diff
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


See Which Branches You Recently Worked On


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$ git for-each-ref --count=10 --sort=-committerdate refs/heads/ --format="%(refname:short)"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


See What Your Team Has Been Up To


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$ git log -all --oneline --no-merges
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Remind Yourself What You Have Been Up To


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$ git log --all --oneline --no-merges --author=<your_email_address>

-- alias git recap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Today's Work


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$ git log --since=00:00:00 --all --no-merges --oneline --author=<your email address>

--alias git today
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Check Out What Your Are About to Pull


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$ git log --oneline --no-merges HEAD..<remote>/<branch>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Example:


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$ git checkout feature/fonts
$ git fetch
$ git log --oneline --no-merges ..origin/feature/fonts

--alias git upstream
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Review What You Are About to Push


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
git log --oneline --no-merges <remote>/<branch>..HEAD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Example:


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$ git fetch
$ git log --oneline --no-merges origin/feature/fonts..HEAD

--alias git local
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


View Complex Logs


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$ git log --graph --all --decorate --stat --date=iso

--alias git graph
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
