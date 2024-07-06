# Set up

Participation in the MSSE Bootcamp will require use of your own personal computer or laptop and installation of some software.

```{admonition} Windows users take note
:class: caution

If you are working on a Windows computer, participation in the course will require you to install the Windows Subsystem for Linux (WSL).
You should install WSL 2. You will need to have the Windows 10 OS with the following version requirements:

* For x64 systems: Version 1903 or higher, with Build 18362 or higher.
* For ARM64 systems: Version 2004 or higher, with Build 19041 or higher.  
 
If you haven't updated your computer in a while, these updates could take a considerable amount of time. 

Plan accordingly!

```

Please follow the instructions given here to make sure you have the necessary software installed. 
We will be using Python and the conda package manager. 
If you are on MacOS or Linux and you already have Anaconda (or miniconda) installed, skip to the compilers portion of these set-up instructions. 
If you do not have Anaconda or miniconda installed please see the appropriate section below.

```{admonition} Anaconda vs miniconda
:class: note

Anaconda is a distribution of Python, the conda package manager, and several third-party libraries which are commonly used in data science.

Miniconda contains only Python and the conda package manager. You will be able to install any package you would like later using miniconda. Miniconda will take up a lot less space on your computer.

We will be learning to manage conda environments and install the packages we need, so we consider miniconda to be the better option between the two.

If you already have Anaconda installed, however, there is no need to install miniconda.

```

## Installing miniconda and compilers

Click the appropriate tab for your operating system to see set-up instructions.

``````{tab-set}

`````{tab-item} Mac OS
### Miniconda Installation
You can download and run the installer at this [link](https://docs.conda.io/en/latest/miniconda.html).

### Compilers
MacOS users should [install XCode](https://developer.apple.com/xcode/). An easy way to install XCode is through the [Mac App Store](https://apps.apple.com/us/app/xcode/id497799835?mt=12).

`````

`````{tab-item} Linux

### Miniconda Installation
You can download and run the installer at this [link](https://docs.conda.io/en/latest/miniconda.html).

### Compilers
After installing miniconda, you will need to install compilers for the C++ section of the course. Use this command to install compilers

````{tab-set-code} 

```{code-block} shell
sudo apt install build-essential
```
````

`````

`````{tab-item} Windows

If your computer uses the Windows operating system, we require installing Windows Subsystem for Linux (WSL). Follow the installation instructions at [this link](https://docs.microsoft.com/en-us/windows/wsl/install-win10). If you don’t have a preference on Linux distribution, we recommend installing Ubuntu 20.04. 

Once WSL is installed, open your ‘Start’ menu and choose ‘Ubuntu’. This will open a terminal window. 
A terminal is an interface you can use to interact with your computer using text.
The first time you have opened Ubuntu, you may see a message which says “Installing, this may take a few minutes…”. 
After the installation is done, you will have to create a username and password. After these are created, you should be able to use the terminal.

The Windows Subsystem for Linux is like running another computer inside your computer. It is a different operating system and has different software installed than your Windows computer. For the WSL, you have to install miniconda from the terminal in your Linux operating system. Note that if you if you are using the WSL, your Linux OS is completely separated from your Windows operating system. This means that software installed on one operating system is not available in the other.

### WSL Miniconda Installation
You are now using a Linux OS under Windows. You must install miniconda from the command line. 
You should [open a terminal](https://towardsdatascience.com/a-quick-guide-to-using-command-line-terminal-96815b97b955).
If you are using WSL, a terminal is opened when you click your Linux Operating System from the start menu.

From your terminal execute the following lines:  

````{tab-set-code} 

```{code-block} shell
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```
````

After installation, close and reopen your terminal window. If you do not see (base) before your username on the command line, type

````{tab-set-code} 

```{code-block} shell
conda init
```
````


### Compilers
After installing miniconda, you will need to install compilers for the C++ section of the course. Use this command to install compilers

````{tab-set-code} 

```{code-block} shell
sudo apt install build-essential
```
````

`````

````````


# Creating a conda environment
Everyone should complete and read this section after installing miniconda.

To make a great deal of compilation and installation simpler we will create a conda environment. Environments isolate software from this project from the rest of the dependencies on your laptop.

After installing miniconda, type the following command into your terminal. This creates an environment called “msse-python” which runs Python 3.11.


````{tab-set-code} 

```{code-block} shell
conda create -n msse-python python=3.11
```
````

After creating the environment, activate it using the command

````{tab-set-code} 

```{code-block} shell
conda activate msse-python
```
````

Next, install the Python libraries JupyterLab and matplotlib.

````{tab-set-code} 

```{code-block} shell
conda install -c conda-forge jupyterlab matplotlib
```
````

You now have a new environment `msse-python` created which has the Python Standard Library, matplotlib, and Jupyter Lab installed. This is the environment we will be using for our initial coding projects.

To deactivate the environment, use

````{tab-set-code} 

```{code-block} shell
conda deactivate
```
````


## Installing and configuring git

### Installation
We will be using the `git` software for version control during this course. This portion walks you through installing and configuring `git`.

If you do not have the environment activated, activate it first:

````{tab-set-code} 

```{code-block} shell
conda activate msse-python
```
````


Next, make sure you have git installed.

You can check if git is installed using the following command in your terminal:

````{tab-set-code} 

```{code-block} shell
git --version
```
````


Make sure that this outputs at least version 2.28. If you do not have git installed, or if it is an older version of git, 
you can install git using conda:

````{tab-set-code} 

```{code-block} shell
conda install -c conda-forge git
```
````


Note that because of the solver that conda uses to decide which version of a package to install you may end up with a version that is < 2.28. 
you can use the same command from above `git --version` to see what version has been installed.

If the output of that command is < 2.28 you will want to use the following command to specify the version to install. Any version >=2.28 is acceptable.

````{tab-set-code} 

```{code-block} shell
conda install -c conda-forge git"=>2.28"
```
````

### Configuring Git

The first time you use Git on a particular computer, you need to configure some things.

First, you should set your identity.
One of the most important things that version control like Git does is to keep track of who changes what.
This helps repository maintainers coordinate the efforts of all the people who contribute to the project.
Most importantly, it makes it easier to figure out who to blame when something goes wrong.
You can provide git your name and contact information with the following commands:

```{admonition} Configuring git
:class: tip

In the command below, you do not need to put your name or email address in all caps
```

````{tab-set-code} 

```{code-block} shell
git config --global user.name "YOUR_FIRSTNAME YOUR_LASTNAME"
git config --global user.email "YOUR_EMAIL_ADDRESS"
```
````


Next, you will need to set the name of the default branch git uses.
We will discuss in more detail during the bootcamp.
The following command will set your default branch name to be "main"

````{tab-set-code} 

```{code-block} shell
git config --global init.defaultBranch main
```
````


Next, you might want to change the Git text editor.
As we will see later, certain Git commands will open text files.
When this happens, Git will use your environment's default text editor, which might not be the editor you are most comfortable using.
Using configuration commands, you can tell Git to use your favorite editor.

We recommend installing [Visual Studio Code](https://code.visualstudio.com/) as your text editor in the last portion of this set-up.
Note that using VS Code on Windows or Mac requires additional set-up, which is outlined in the section [Installing a text editor](text-editor).
To make VS Code your default editor for git, do

````{tab-set-code} 

```{code-block} shell
$ git config --global core.editor "code --wait"
```
````

A more complete list of possible editors is available [here](http://swcarpentry.github.io/git-novice/02-setup/index.html).

You can check the configuration commands that you have set using:

````{tab-set-code} 

```{code-block} shell
$ git config --list
```
````


## GitHub

If you do not yet have a GitHub account, you will need to create one.
To create an account, navigate to [github.com](https://github.com/), and click "Sign up". 
When creating your GitHub username, remember that this is a professional profile where you can showcase your work.
Keeping this in mind, make sure that your GitHub username is both **professional** and **recognizable**.

### GitHub Credentials
We will be using the command line interface for GitHub. 
GitHub *very recently* deprecated using a username and password from the command line.
Instead, you will need to create something called an ssh key to verify your account.

Follow the [instructions given by GitHub](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh) to create an SSH key and add it to your account.

(text-editor)=
## Text Editor
Everyone should have a text editor they can use to edit Python and C++. 
If you do not have a preference for text editors, we recommend [Visual Studio Code](https://code.visualstudio.com/). 
If you are using WSL, see [these instructions](https://code.visualstudio.com/docs/remote/wsl) for installing Visual Studio Code for use with WSL.
If you are using Mac, follow [these instructions](https://code.visualstudio.com/docs/setup/mac#:~:text=Launching%20from%20the%20command%20line,code'%20command%20in%20PATH%20command.) to set-up VS Code so that you can use it from the command line.



