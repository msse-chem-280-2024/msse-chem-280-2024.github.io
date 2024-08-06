# Meet your group

To start today's class you will be meeting with your team and 
collaborating with your team on a group repository.
You should first interview your team members to get to know them better.
Then, in the second part, you will create a group repository and each submit a pull request.

## Interviewing Team Members

For today, you should interview and create a markdown file that has information about someone else on your team. Some questions you might think about…

- Where is your team member from?
- Where do they live?
- What is your favorite food? What is your least favorite food?
- What is one thing the two of you have in common (that isn’t the MSSE program)?
- Why did they choose the MSSE degree?

Be creative with your questions, these are only suggestions.

## Starting a Group Repository

Before beginning this assignment, take some time to come up with a name for your group.

Next, click the linke below to start your group repository.
The first person who clicks the link will enter your group name.
Other members will be able to choose the team once it exists.

Start your group repository, [click this link](https://classroom.github.com/a/SzcOh_yv).
The first person who clicks this link will be responsible for putting a team name. 
Each person who clicks the link after will be able to join the team.

To start, someone in the group should add a **branch protection rule** to the repository. 
To add a branch protection rule, go to the repository settings and click on "Branches". 
Then, click on "Add rule" and add a rule for the "main" branch.
The image below shows screenshots with numbers next to what you click.

```{image} ../fig/branch-protection-1.png
:align: center
```

After clicking "Add classic branch protection rule", you will see the following screen.
Type "main" into the box that says "Branch name pattern".
Next, click "require a pull request before merging" and "Require approvals" and save the rule.

```{image} ../fig/branch-protection-2.png
:align: center
```

You will need to clone this repository to your local computer.
To clone your repository, navigate to your repository in your browser.
The URL will be `github.com/msse-chem-280-2024/group-repository-YOUR-TEAMNAME`.

You should then click the buttons shown below to get the location for cloning your repository. 

```{image} ../fig/clone-repo.png
:align: center
```

Once have copied this to your clipboard, go to your `chem_280` folder and do `git clone URL` where `URL` is the URL you copied.

Then, create a file in the `group_bios` folder that contains an interview of your group member (save the file with `theirLastName_theirFirstName.md`) and submit a pull request. 
Be sure that your file has a title (using `#`) and other markdown formatting.
Be sure to include your name as the author!
