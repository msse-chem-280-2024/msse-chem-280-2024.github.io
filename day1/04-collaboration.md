# Code Collaboration using GitHub

````{admonition} Overview
:class: overview

Questions:
- How can others contribute to my project on GitHub?
- How can I contribute to the projects of others?

Objectives:
- Understand how to open a pull request.
````

## Repository collaborators

Now that we know the basics of git, we might want to know about code collaboration. 
There are several ways for people to contribute to your project. 
If you are working with a small number of people who you know well, you may simply choose to add them as collaborators to your repo. 
This will give them the ability to push to your repository.

To add collaborators to your project, navigate to your repository on GitHub
Click the "Settings" button to the right of the little gear.
This will take you to some options that will help you to maintain your repository.

This page lets you do several important things, including rename, relocate, transfer, or delete your repository.

Underneath the "Features" heading you will notice an option to "Restrict editing to collaborators only".
This option prevents random strangers from being able to push changes to your repository, and should always be kept on.
To allow other people to work with you, you can assign collaborators.
Click the "Manage access" tab on the left. 
This will bring up a page where you can see some details about your repository. 
The box under the heading "Manage access" will allow you to invite collaborators to your project.

A pop up with a search bar will appear where you can search for the names of other GitHub users.
By finding someone using the search bar and then clicking "Add collaborator", you can allow specific people to contribute to your project.
Generally speaking, you should only list someone as a collaborator if you work with them closely and trust that they won't do anything especially unwise with your repository.

Adding them to the repository as a collaborator will allow them to push to the repository the same way you do. 

People you don't know very well shouldn't be listed as collaborators, but there are still ways for them to contribute improvements to your project.

### Protecting your main Branch
If you choose to work with collaborators, there are still ways for you to protect your code. 
Click the "Branches" tab. 
You will see a heading which says "Branch protection rule". 
Adding the name of a branch here will make it a "protected branch" and the rules you choose in the section below will protect the branch (under the heading "protect matching branches"). 
For example, you may want to choose to protect the `main` branch so that pull requests and reviews are required to change the branch. 
This way, your collaborators will not be able to push to the main branch, and must submit a `pull request` more on this later in order for their changes to be incorporated. 
You can read more about [branch protection](https://help.github.com/en/enterprise/2.18/admin/developer-workflow/configuring-protected-branches-and-required-status-checks#enabling-a-protected-branch-for-a-repository).

### Pull Requests - Branch and Pull Request (PR)
Protecting your main branch will require contributors to submit their changes through a process called a Pull Request. 
As the repository owner, you can also change the code through a pull request on GitHub.

Previously, we discussed that all changes should take place on branches. 
This is still true, however, we are now going to incorporate those changes through a pull request on GitHub rather than through a merge.

Create a new branch in your repository to make a small change.

````{tab-set-code} 

```{code-block} shell
git switch -c collab_instructions
```
````

Add the following to your README and commit the change.

````{tab-set-code} 

```{code-block} README.md
To submit your feature to be incorporated to the main branch, you should submit a `Pull Request`. 
The repository maintainers will review your pull request before accepting your changes.
```
````

````{tab-set-code} 

```{code-block} shell
git add README.md
git commit -m "add collaboration instructions to readme"
```
````

We want these changes incorporated into the main branch. 
You could do as we did before and switch to the `main` branch, `merge` then changes, and push to GitHub for the changes to be present there on the `main` branch. 
If you are the repository owner, this will work even if you have branch protection rules. 
However, if you are not, your push from main will be rejected by GitHub.

We will want to push to a new branch on the repo then open a pull request. 

````{tab-set-code} 

```{code-block} shell
git push origin collab_instructions
```
````

You will get an output similar to the following:

````{tab-set-code} 

```{code-block} output
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 470 bytes | 470.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote: 
remote: Create a pull request for 'collab_instructions' on GitHub by visiting:
remote:      https://github.com/YOUR_USERNAME/molecool/pull/new/collab_instructions
remote: 
To https://github.com/YOUR_USERNAME/molecool.git
 * [new branch]      collab_instructions -> collab_instructions
```
````

This message tells you that a new branch has been created on your repository, and also tells you that you may want to open a pull request. 
You can click this link or copy and paste it to open a pull request. 
Write a description of the pull request in the box, then click "Create Pull Request".

Once the PR is created, you will see a page describing the PR. 
On the top of the repo, you should see a button called "Pull Requests" and it should show that one is open for your repo. 
You can then choose to review the PR, or in this case you can just merge it without a review. 
To review a PR, click the 'Files changed' tab. 
You can review the changes (green Review changes button). 
Since you are looking at your own PR, you won't be able to "Approve" if you have put in the branch protection rule. However, you can comment on and merge the changes if you wish.

(collaboration)=
## Contributing to a repository with multiple collaborators - HOMEWORK

During this section, we will all start from central repository where we are listed as collaborators, make changes, then submit something called a Pull Request to have those changes incorporated into the code. 
We will leave the package we are developing for this section.

Navigate to the URL https://github.com/msse-2023-bootcamp/periodic-table in your web browser. 
You should see a GitHub repo. 
This repository contains code to make a website which has the periodic table. 
View the website https://msse-2023-bootcamp.github.io/periodic-table/ . 
On the website page, elements which appear with a blue background and gold text have a page and information filled in. 
You can read more about each element by clicking on it. 
Elements with a white background do not yet have a page. 
Take a minute or two to click around. 

You have all been added as collaborators to the project, so you can make changes. 
However, the `main` branch has been protected by the the repository owners so that you cannot push to main. 
We will have to make our changes on a branch.

Make a clone of the repository on your personal computer. 
Before you make the clone, MAKE SURE YOU ARE NOT IN A GIT REPOSITORY.

Type

````{tab-set-code} 

```{code-block} shell
git status
```
````

You should see the message

````{tab-set-code} 

```{code-block} output
fatal: not a git repository (or any of the parent directories): .git
```
````

If you do not see this message, navigate using `cd` until you do.

Next, clone the repository to your computer. 

````{tab-set-code} 

```{code-block} shell
git clone git@github.com:msse-chem-280-2023/periodic-table.git
cd periodic-table
```
````

## Developing a new page
We will implement a new element for the webpage. 
Pick an element you would like to add information about. 
Create an issue on the central repository to let everyone else know you are planning to add a feature.

Create a new branch in your repo with your element of choice. 
For this demo, I will be editing the sodium page. 
You should choose another element. 
This can either be an element that exists (blue background), or an element that doesn't exist yet (white background).

````{tab-set-code} 

```{code-block} shell
git switch -c YOUR_CHOSEN_ELEMENT
```
````

You will see the output

````{tab-set-code} 

```{code-block} output
Switched to a new branch 'YOUR_CHOSEN_ELEMENT'
```
````

We have now created a new branch called `YOUR_CHOSEN_ELEMENT` and checked it out.

## Editing our element

Now it's time to edit our periodic table element. 
If you have picked an element which exists already, there will be a file with the name `element_name.md` where element name is the element you've chosen. 
If the file does not exist, create it.

Once the file is created, open it in your text editor of choice. 
It is important that every element have the following at the top of the page (note - spacing is very important!)

```
---
layout: page
title: ELEMENT_NAME
---
```

If you are creating a new page, fill in the appropriate element name. 
Add some text about the element below the heading. 
For example, our sodium page might look like the following.

```
---
layout: page
title: Sodium
---

Symbol : Na  
Atomic Number : 11  
```

Save your file after you edit it.

### Testing out the website

If you have [jekyll](https://jekyllrb.com) installed, you can view a local copy of the webpage. 
This is not a necessary step. I
If you do not have jekyll installed, or do not wish to install Jekyll skip this step. 

Execute the command

````{tab-set-code} 

```{code-block} shell
bundle exec jekyll serve
```
````

in the terminal the top level of your project to render a local copy of the webpage. 
Navigate to the local address to view your website and make sure your new element is working. 

## Committing the change

Let's add and commit these changes.

````{tab-set-code} 

```{code-block} shell
git add elements/YOUR_ELEMENT.md
git commit -m "update YOUR_ELEMENT page"
```
````

Next, we must push these changes. 
But, where do we want to push the changes?
We would like to have our changes incorporated into the main branch, but our main branch is protected (you can try pushing to it if you don't believe me). 
We will have to push to origin on the `sodium` branch (or whatever branch you're working on), then we will request that our collaborators incorporate our changes, or pull from our branch. 

````{tab-set-code} 

```{code-block} shell
git push origin sodium
```
````

Here, the last line indicates that we are pushing to `origin` to the `sodium` branch. 
The branch name you type in place of sodium should match the name of the branch you are working on. 
If you view your repository on GitHub, you should now see that you have another branch in addition to the main branch.

As part of the output from this command, you should see the following:

````{tab-set-code} 

```{code-block} output
remote:
remote: Create a pull request for 'sodium' on GitHub by visiting:
remote:      https://github.com/msse-2022-bootcamp/periodic-table/pull/new/sodium
remote:
```
````

`git` is correct. 
What we will want to do next is create a pull request on the original repository to get our changes incorporated.

## Pull requests

It is now time to incorporate the edits you have made in your branch into the `main` branch.
To do this, we must create a `Pull Request`.

Navigate to the URL of the repository. 
You should see a highlighted area and green button which says "Compare and Pull Request". 
Alternatively, you can navigate to the URL given in the message where you did a push.

Once you are on the page that says "Open a pull request", 
you should see fields which ask for the name of the pull request, 
as well as a larger text box which has space for a description. 
Make the title of this pull request "add YOUR_ELEMENT page". 
Edit the description to describe what you have done in your pull request.

Submit the pull request.

Now, your collaborators can review your material, and request changes if they feel it necessary. 

You should find one other student's pull request.
You can view the diffs for the files which were changed by clicking the "Files changed" tab.
From here, you can make comments on particular lines, or start a code review.
Take some time to review another student's pull request.
Consider the following:
1. Did they use the right page format?
1. Is their file name correct?
1. Did they add information about the element?

If all three of these things are done, approve the pull request.
If there are any mistakes, let the person know, and "request changes" on their pull request.

If you requested changes, they should address those, and tag you for review again.

Once your pull request has been accepted and merged, main will have the changes you made. 

## Incorporating upstream changes to local

After your change has been accepted to main, you will want to incorporate the changes into your local main branch. 
First, switch to your main branch.

````{tab-set-code} 

```{code-block} shell
git switch main
```
````

You can get changes to your local main by either doing a `git pull` from main.

````{tab-set-code} 

```{code-block} shell
git pull origin main
```
````

If you are done working with your feature branch, you can now delete it. 

````{tab-set-code} 

```{code-block} shell
git branch -d sodium
```
````

The `-d` option means to delete the branch.

To delete the branch on your origin repository on GitHub, you can use the command

````{tab-set-code} 

```{code-block} shell
git push origin --delete sodium
```
````


### Branching

[Git Branching Tutorial](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)

### Rebasing

[Git Rebasing Tutorial](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)
