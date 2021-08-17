<h1 style='color:darkcyan;text-decoration:underline'>Git</h1>
<div style='width:1000px;margin:auto'>

<details><summary>Branch</summary>
<details><summary>Create a Branch and make it the current working branch</summary>
<pre><code>git checkout -b name_of_branch</code></pre>
</details>

<details><summary>Delete a Branch</summary>
<pre><code>git branch -d name_of_branch</code></pre>
</details>

<details><summary>Force Deleting a Branch</summary>
<pre><code>git branch -D name_of_branch</code></pre>
</details><br>
</details>

<details><summary>Remote</summary>
<details><summary>Check all available remote links</summary>
<pre><code>git remote -v</code></pre>
</details>

<details><summary>Add a remote git link</summary>
<pre><code>git remote add name_of_link git_link.git</code></pre>
</details>

<details><summary>Push code to the remote repository</summary>
<pre><code>git push -u azure_postmuseum_deploy master</code></pre>
</details>

<details><summary>Force Push code to the remote repository</summary>
<pre><code>git push -f azure_postmuseum_deploy master</code></pre>
</details><br>
</details>

<details><summary>Show all aliases</summary>
<pre><code>git config --global -l</code></pre>
</details>

<details><summary>Set an Alias</summary>
<pre><code>git config --global alias.logg "log --oneline --graph --all --decorate --color"
git config --global alias.st "status -sb"
git config --global alias.gl "config --global -l"
git config --global alias.stu "status -uno"
git config --global alias.st "status"</code></pre>
</details>

</div>
































