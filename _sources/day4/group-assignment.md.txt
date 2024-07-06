# Group Homework Assignment Day 4

Like previous days, your task should be placed in the appropriate folder (`day4`), with the file name `lastname_firstname_taskX` with the appropriate extension.

In additon to code, each task should also include a markdown cell reflection that is at least five sentences.

## Task 1 - Exploring the Acceptance Criteria
Write code to calculate the probability of accepting a Monte Carlo move for energies ranging from -2 to 2 for T = 0.9, T = 0.4, and T = 1.4. 
What is the effect of temperature on the probability of a MC move being accepted? Does this make sense based on your intuition or from what you know about thermodynamics? Why or why not? Create a plot showing your results. Note that you aren’t going to be able to use your function `accept_or_reject`` for this. You will have to take `p_acc` out of it to make the plot.

## Task 2 - Comparing Performance
In our implementation, we've made a smart choice about our algorithm. 
We noticed that we only need to calculate the energy for the moved particle rather than the whole system.
For this task, you should alter the code to perform a naive implementaiton where this choice was not made. 
Change your code to calculate the total energy for every step. 
Compare timings for 10,000 steps.

You can compare timings by using the `time` module in Python. 
A common pattern is 

````{tab-set-code}
```{code-block} python
import time

start = time.time()
# put code you want to time here.
end = time.time()

elapsed_time = end - start
print(elapsed_time)
```
````

## Task 3 - Investigating Initial Configuration Sensitivity
In this task, you will explore the sensitivity of the Monte Carlo (MC) simulation to the initial configuration of the Lennard Jones (LJ) fluid system. Your objective is to understand how different initial configurations can influence the convergence and accuracy of the simulation results.

Start simulations from the NIST sample configuration, a random configuration, and from a cubic lattice. 
What differences, if any, do you observe in the total system energy and trend?