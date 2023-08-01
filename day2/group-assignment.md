# Day 2 - Group Assignment 

Day 2 contains four possible homework tasks.
Divide the tasks up among your team members. 
Each person should complete one task for homework and review the task of at least one teammate.

For each task, create a jupyter notebook with a file name of the format `lastname_firstname_task_x.ipynb` where `x` is your task number.

## Reviewing your teammate's change
You may need too pull the changes from your teammate's branch when you are reviewing their pull request. You can pull their branch to your local computer by doing

````{tab-set-code} 

```{code-block} shell
git switch main
git fetch 
git switch -c TEAMMATE_BRANCH --track origin/TEAMMATE_BRANCH
```
````

You should then be able to see your teammates files. You should open their Jupyter notebook and review their code. If any changes are needed, leave this in your review on GitHub.

## Task 1 - Systematic Investigation of Error in Monte Carlo Calculation

For this task, you will return to your notebook where we calculated the value of $\pi$ using Monte Carlo Methods.

Your task is to investigate the effect of increasing the number of samples on the error of the calculation.

Modify your Monte Carlo code to print the percent error in your pi calculation for `10`, `100`, `1000`, `10,000`, `100,000`, and `1,000,000` points. For an extra challenge, try visualizing your results using `matplotlib`.

```{admonition} Reference Values
:class: tip

You can use `math.pi` as a reference value and `math.fabs` to get an absolute value when calculating your percent error.

```

In your submission, include a markdown cell that contains a reflection (at least five sentences) on your approach and observations.

## Task 2 - Investigating the Lennard Jones Equation

Write a `calculate_LJ` function that includes parameters for setting $\sigma$ and $\epsilon$.

After writing the function, perform a set of calculations with $\sigma$ and $\epsilon$ both equal to one. Using these values, calculate the Lennard Jones potential energy for a range of distances, r, from r = 0.1 to r = 5 in increments of 0.1. Save your results in a list.

Next, perform a set of calculations where $\sigma$ is equal to 2 and $\epsilon$ is equal to one. Then set $\sigma$ equal to 1 and $\epsilon$ equal to two. For each set of calculations, save your result in a list.

Visualize all three results on a graph using `matplotlib`.

In your submission, include a markdown cell that contains a reflection (at least five sentences) on your approach and observations.

## Task 3 - Calculating the distance betweent two points

Write a function called `calculate_distance` that takes in two coordinates as lists(`[x, y, z]`) and returns the distance between the two points.

Use the information in the following docstring to write your funtion:

```python
def calculate_distance(coord1, coord2):
   """
   Calculate the distance between two 3D coordinates.
  
   Parameters
   ----------
   coord1, coord2: list
       The atomic coordinates
   
   Returns
   -------
   distance: float
       The distance between the two points.
   """
```

After writing your function, include a few test cases "sanity checks" to ensure that your function is behaving correctly.

```{admonition} The distance function
:class: warning
 
You cannot use a predefined distance function like `math.dist`
for this task.
```

In your submission, include a markdown cell that contains a reflection (at least five sentences) on your approach and observations.
