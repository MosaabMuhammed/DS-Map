<h1 style='color:darkcyan;text-decoration:underline'>Git</h1>
<div style='width:1000px;margin:auto'>

<details><summary style="font-weight:bold">Perfect Commit</summary>

<details><summary>Add a specific change from a file - NOT the whole file</summary>
<pre><code>git add filename.py -p</code></pre>
<pre><code>git add -p

# Loop over all the changes in all files</code></pre>
</details>

<details><summary>Add a commit message with a title and a body</summary>
<pre><code>git commit

#NOTE: this should open your prefered editor.
#if no changes happend, make sure you have -w after you write your editor.
# git config --global core.editor "code -w"</code></pre>
<pre><code>git commit -m "Subject" -m "Description..."

# Without opening an editor</code></pre>
</details>

<br></details>

<details><summary style="font-weight:bold">Branch</summary>

<details><summary>List the current branchs</summary>
<pre><code>git branch</code></pre>
</details>

<details><summary>Create a Branch while staying in the current branch</summary>
<pre><code>git branch new-feature</code></pre>
</details>

<details><summary>Create a Branch and make it the current working branch</summary>
<pre><code>git checkout -b name_of_branch</code></pre>
</details>

<details><summary>Switch to another branch</summary>
<pre><code>git checkout new-feature
git checkout - # switch to the last branch</code></pre>
</details>

<details><summary>Delete a Branch</summary>
<pre><code>git branch -d name_of_branch</code></pre>
</details>

<details><summary>Force Deleting a Branch</summary>
<pre><code>git branch -D name_of_branch</code></pre>
</details>

<details><summary>When merging branch-B on branch-A, How to combine all the commits in branch-B into one commit then merge it with branch-A</summary>
<pre><code>git checkout master 
git merge --squash bugfix 
git commit</code></pre>
</details>

<details><summary>Abort a Merge</summary>
<pre><code>git merge --abort</code></pre>
</details>
<br></details>

<details><summary style="font-weight:bold">Remote</summary>
<details><summary>Check all available remote links</summary>
<pre><code>git remote -v</code></pre>
</details>

<details><summary>Add a remote git link</summary>
<pre><code>git remote add name_of_link git_link.git</code></pre>
</details>

<details><summary>Push code to the remote repository</summary>
<pre><code>git push -u azure_postmuseum_deploy master</code></pre>
</details>

<details><summary>Push code to a branch in the remote repository </summary>
<pre><code>// git push [remote] [local branch name]:[remote branch to push into]
git push origin develop:master</code></pre>
</details>

<details><summary>Fetch a remote branch into local branch</summary>
<pre><code>git fetch {remote} {rbranch}:{lbranch}
git checkout {lbranch}
# your {lbranch} has not to be created first.</code></pre>
</details>

<details><summary>Force Push code to the remote repository</summary>
<pre><code>git push -f azure_postmuseum_deploy master</code></pre>
</details><br>
</details>

<details><summary style="font-weight:bold">Show all aliases</summary>
<pre><code>git config --global -l</code></pre>
</details>

<details><summary style="font-weight:bold">Set an Alias</summary>
<pre><code>git config --global alias.logg "log --oneline --graph --all --decorate --color"
git config --global alias.st "status -sb"
git config --global alias.gl "config --global -l"
git config --global alias.stu "status -uno"
git config --global alias.st "status"</code></pre>
</details>

<details><summary style="font-weight:bold">Undoing/Recovering Changes</summary>

<details><summary>Undo a change before staging it</summary>
<pre><code>git checkout filename_that_has_the_change.py</code></pre>
</details>

<details><summary>Undo a change after staging it (git add) to be untracked/unstaged</summary>
<pre><code>git reset HEAD path/to/file</code></pre>
</details>

<details><summary>Amend the last commit by combining its content with current added/staged content</summary>
NOTE: this command will remove the last commit and replace with a new one, make sure the last commit didn't go public<br>
the new commit will have the same message
<pre><code>git commit -amend</code></pre>
</details>

<details><summary>Undo/Revert the last/any commit</summary>
NOTE: revert creates a new commit to contain the inverse of all the changes made in the bad commit in order to cancel them out.
<pre><code># To revert the last commit
git revert HEAD

# To revert any commit, copy its SHA1 hash
git revert 21s32</code></pre>
</details>

<details><summary>Recover Delected Commits</summary>
<pre><code>git reset --hard HEAD~2 # delete the last 2 commits
git reflog # copy the id of the log that happend before deleting the commit
git branch happy-ending 213kj23 # create a new branch containing the removed commits.</code></pre>
</details>

<br></details>

<details><summary style="font-weight:bold">Rewriting History (Commits Log)</summary>
By using interactive rebase.
<pre><code>git rebase -i HEAD~3

# This command will select the first 3 commits</code></pre>
</details>

<details><summary style="font-weight:bold">Cherry-Picking</summary>
select individual and specific commits to be merged to another branch instead of merge the whole other branch
<pre><code>git checkout feature # go to the branch you want the commit to be placed in.
git cherry-pick 24bf134 # pick the SHA-1 hash for the other branch, you should do this before switching to feature branch.
git checkout master # go the parent branch
git reset --hard HEAD~1 # remove the picked commit
</code></pre>
</details>

<details><summary style="font-weight:bold">Remove commits</summary>
<pre><code>git reset --hard HEAD~1 # will remove the last commit
# you can use SHA-1 hashes
</code></pre>
</details>

<details><summary style="font-weight:bold">Search & Find</summary>
<pre><code># Search by date
git log --before="2021-2-1" --after="2021-12-30"

# Search by message signature/regular expression
git log --grep="fix"

# by author
git log --author="Mosaab"

# by file -- very handy
git log -- READ.md
</code></pre>
</details>

<details><summary style="font-weight:bold">Stash</summary>

<details><summary>Stash without a name</summary>
<pre><code># remove the current changes, and save them for later use.
git stash

# Pull the stashed changes, when ready with
git stash pop</code></pre>
</details>
<details><summary>Stash with a name</summary>
<pre><code># remove the current changes, and save them for later use with a name.
git stash save name_of_the_changes

# List all the current changes in the stash.
git stash list
git stash apply 0 # the index from list
</code></pre>
</details>

<details><summary>create a branch at the time you stashed changes</summary>
<pre><code>git stash branch originalwork stash@{0}</code></pre>
</details>

<br></details>

<details><summary style="font-weight:bold">Tags</summary>

<details><summary>show the available tags</summary>
<pre><code>git tag
git tag --list

# show the details of a tag
git show v1.0</code></pre>
</details>


<details><summary>create a simple tag</summary>
<pre><code>git tag v1.0</code></pre>
</details>

<details><summary>create an annotated tag</summary>
<pre><code>git tag -a v1.1 -m "tag for release version 1.1"</code></pre>
</details>

<details><summary>create a tag from a specific commit</summary>
<pre><code>git tag v1.3 5flkj3jf</code></pre>
</details>

<details><summary>Push tags to remote</summary>
<pre><code>git push origin v1.0
git push origin --tags # to push all the tags.
git push --tags</code></pre>
</details>

<details><summary>Delete a tag</summary>
<pre><code>git tag -d v1.0
git tag --delete v1.0</code></pre>
</details>

<details><summary>Delete a tag from remote repo</summary>
<pre><code>git push origin -d v1.0 v1.1
git push origin --delete v1.0 v1.1</code></pre>
</details>

<br></details>
</div>
































