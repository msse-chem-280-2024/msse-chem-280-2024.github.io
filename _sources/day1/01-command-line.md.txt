# Introduction to the Command Line

````{admonition} Overview
:class: overview

Questions:
- What is the command line?
- How can I navigate files and directories on the command line?

Objectives:
- Learn basic shell commands for navigating and creating directories.
````

## Lesson Slides

{download}`Lesson Slides <../_files/day-1-topics.pdf>`

## Opening the Terminal

In this course, we will be navigating files and using git (a software for version control) using the command line. 
The Linux command line is a text interface to your computer. 
When you use the command line, you use something called a shell.
You can access the command line or shell using a *terminal*. 
If you are using WSL, the only interface to your Linux operating system is a command line or terminal.

In scientific computing, you often need to use the Linux command line on high-performance computing (HPC) servers.
Knowing the command line will allow you to perform repetitive tasks quickly through shell scripting.
You will learn more about the command line and scripting in Chem 274A.
This course will focus on basic navigation, file creation, and using git from the command line.

Most modern operating systems have graphical user interfaces, or GUIs (often pronounced "gooey"), used to interact with the computer.
However, you can also interact with the computer using text only.

[Open your terminal](https://towardsdatascience.com/a-quick-guide-to-using-command-line-terminal-96815b97b955). 
If you are using a Mac, you should open your terminal application.
If you are using WSL, open your Linux distribution.
You can use this interface to issue commands to your computer using text.

## Viewing Directory Contents

The first command we will discuss is the command `pwd`. 
`pwd` stands for "**p**rint **w**orking **d**irectory." 
This command gives the name of the folder you are currently in.
In Linux, "directory" means the same thing as "folder."

````{tab-set-code} 

```{code-block} shell
pwd
```
````


````{tab-set-code} 

```{code-block} output
/YOUR/PATH
```
````


When you open a terminal initially, you will be in your home directory. 
The path displayed as your output will be whatever your home directory is if you type `pwd` immediately after opening your terminal.

The `ls` command shows you the contents of the directory you are in. 
`ls` stands for "list," and the command shows you the contents of the directory you are in.

````{tab-set-code} 

```{code-block} shell
ls
```
````


If you want to see the contents of another directory, you can follow `ls` with the path to that directory. 
In the command below, you should substitute a directory you can see from the previous `ls` command.

````{tab-set-code} 

```{code-block} shell
ls DIRECTORY_NAME
```
````

```{admonition} Clearing the screen
:class: note

If you'd like to make room on your screen, you can use the `clear` command to get a fresh terminal.
Pressing `ctrl+L` on your keyboard will also clear the screen.
```

:::{admonition} The `tab` key
:class: tip

When typing a file or folder name into your terminal, you can autocomplete the name by pressing the `tab` key.

For example, if you have a folder called `my_folder`, you can type `my_f` and then press `tab`. If there is only one folder that starts with `my_f`, the terminal will complete the name for you. If there are multiple folders that start with `my_f`, pressing `tab` twice will show you the options.
:::

## Creating and navigating directories
We will make a directory to keep our work in for the course.
These directions will tell you how to create a folder in your home directory for the sake of uniformity.
If you have another preference for where you would like to store your files and you can navigate files, you can use that location.

The command to **m**a**k**e a **dir**ectory is `mkdir`.

````{tab-set-code} 

```{code-block} shell
mkdir chem_280
```
````

``````{admonition} Check Your Understanding
:class: exercise

What command have you learned so far that you could use to see if your newly created folder is in your current location?

````{admonition} Solution
:class: solution dropdown

You could use the `ls` command to confirm that there is now a folder called `chem_280` in your home directory.

``````


This has created an empty folder, or directory, named `chem_280` in your home directory.
To navigate inside that directory, we need to **c**hange the **d**irectory using the `cd` command.

```{admonition} Spaces in file and directory names
:class: note

In general, you will notice that most file and directory names created on systems where the command line is used do not contain spaces.

On the command line, many applications and scripts may not work with file names or directories containing spaces. 
Underscores `_` or dashes `-` are used in place of spaces to separate words in file names.

```


````{tab-set-code} 

```{code-block} shell
cd chem_280
```
````


We will create a file describing what is in this folder. 

You can verify what folder you are in using the `pwd` command.

````{tab-set-code} 

```{code-block} shell
pwd
```
````


Open a text file in your text editor of choice. 
If you installed [VSCode](https://code.visualstudio.com/download)  , you will be able to open a file called `README.md` using VSCode with the following command. **Note** If you are on MacOS, you will need to [add VSCode to your path manually](https://code.visualstudio.com/docs/setup/mac).

````{tab-set-code} 

```{code-block} shell
code README.md
```
````


The Visual Studio Code text editor will open with a file called `README.md`. 
Type some information in the file and save it.

````{tab-set-code} 

```{code-block} README.md
# Chem 280
This folder contains files and directories associated with Chem 280 - 
Foundations of Programming and Software Engineering.
```
````


This file uses [Markdown](https://www.markdownguide.org/), a text formatting language.
Markdown is often used for README files, and we will use it throughout this course and the following courses. 
The hashtag (`#`) followed by the space results indicates a title.
Save this file and exit.

Now, when you type `ls`, you will see that a file called `README.md` is in your directory.

To navigate out of this folder, you can use `..` as the file location. 

````{tab-set-code} 

```{code-block} shell
cd ..
```
````


The command above will move you back to your home directory. 

```{admonition} Changing to the home directory from anywhere
:class: note

If you use the `cd` command followed by no path, you will always be returned to your home directory.
```

Other commands that will be useful to you are `mv`, which is used for moving files from one place to another, and `cp` for copying files from one place to another. For example, you can create a copy of your README.md file:

````{tab-set-code} 

```{code-block} shell
cp chem_280/README.md .
```
````


This command will create a copy of the README.md file in your current directory. 
The dot (`.`) is a shortcut for your current directory. 
In this case, the created file will have the same name as the one you copied it from.
You could also give the file another name:

````{tab-set-code} 

```{code-block} shell
cp chem_280/README.md README_copy.md
```
````


The `mv` command behaves similarly, except the original file is removed.

You can remove a file using the `rm` command.
Let's get rid of those copies we just made:

````{tab-set-code} 

```{code-block} shell
rm README.md
rm README_copy.md
```
````

``````{admonition} Challenge
:class: exercise

Navigate to your `chem_280` directory and list the directory contents.

`````{admonition} Solution
:class: dropdown solution

The commands you should execute are

````{tab-set-code} 
```{code-block} shell
cd chem_280
ls
```
````
`````
``````


````{admonition} Key Points
:class: key

- The terminal or "command line" is a text interface to your computer.
- You can use text commands in the command line to navigate directories and change files.
- We will use a text mark-up notation called "markdown." This will be in text files and doesn't directly involve the terminal.
````
