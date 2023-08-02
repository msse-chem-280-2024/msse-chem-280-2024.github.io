# Group Homework Assignment Day 3

```{admonition} Comparing to NIST Benchmarks

You can see NIST benchmark energies [on this page](https://www.nist.gov/mml/csd/chemical-informatics-group/lennard-jones-fluid-reference-calculations-cuboid-cell).

We are using configuration 1.

```

## Group Discussion 

Answer the following discussion questions.
Everyone should include the answers in a markdown cell in their task assignment.

### Discussion Questions

1. Consider a system of 2, 3, 4, and 5 particles. How many pairwise particle-particle interactions will there be? What about 10 or 100 particles? A common cutoff distance is $3 \sigma$. Modify your total energy calculation to take a cut-off into account. Do you agree with this choice of cutoff? Why or why not? Justify your answer with numbers using the sample configuration from NIST.

2. Can you think of the benefits associated with using a cut-off? What could be the drawbacks?
3. To get a better idea of periodic boundaries, consider two particles in a periodic box with a length of 10 $\sigma$ (remember that when we used reduced units, our units of length are $\sigma$). 
One particle is at `(0, 0, 0)`, and the second is at `(0, 0, 8)`. If we were to measure the distance between these two particles using our `calculate_distance` function, that distance would be 8 $\sigma$. 
However, because we are using periodic boundary conditions, that is not the distance between the particles. 
There is another copy, or image, of the particle in the adjacent periodic boxes. 
If you have ever played the game Pac-Man, it is a very similar idea to how the characters in this game behave. 
If they exit through one side of the box, they reappear on the other.

	Consider the following questions:

	1. What is the maximum distance any particle can be from another in each dimension? (this will have to do with the box length). Justify your answer.
	1. What is the actual distance of our example? (`(0, 0, 0)`, `(0, 0, 8)`)

## Task 1 - Alternate Initial Configuration - Random Points
So far we have only used an initial configuration from a file. For this task, you will write a function which can generate initial system configurations from a number of particles and a desired system density. Make sure your function includes docstrings!

For density, use the number density. For example, in our sample configuration from NIST, the density is 0.8. This is calculated by dividing the number of atoms by the box volume - 800 atoms / (10 * 10 * 10), since 10 was our box length.
You will need to calculate a box length depending on the number of atoms and the desired density.

Write a function that makes a configuration by randomly placing points in a 3 dimensional box. The function should return `coordinates``, `box_length` the same way our `read_xyz` function does so we can switch out the two without changing our code.

## Task 2 - Alternate Initial Configuration - Cubic Lattice

This task is similar to task 1 except that for this function, you should generate points on a cubic lattice. Similar to the random configuration generator, the function should accept arguments for the number of atoms and the desired system density.

## Task 3 - Tail Correction
Truncating interactions using a cutoff removes contribution to the potential energy that might be non-negligible.  The tail correction for our system makes a correction for use of the cutoff. We only have to calculate this once at the start of our simulation. The formula is:

$$ U_{tail} = \frac{8 \pi N^2}{3 V} \epsilon \sigma^3
	\left[\frac{1}{3} \left(\frac{\sigma}{r_c} \right)^9 
	- \left(\frac{\sigma}{r_c} \right)^3 \right]
$$

In our reduced units:

$$ U_{tail} = \frac{8 \pi N^2}{3 V}
	\left[\frac{1}{3} \left(\frac{1}{r_c} \right)^9 
	- \left(\frac{1}{r_c} \right)^3 \right]
$$

where $V$ is the volume of the simulation box, and $N$ is the number of particles. 

1. Write a function `calculate_tail_correction` which calculates the tail correction. Your function should have `box_length`, `n_particles` (number of particles) and `cut-off` as function parameters. You can calculate the volume of the box from the `box_length`. Assume a cubic box.
   
2. Write an `assert` statement to check against the reported value from [NIST](https://www.nist.gov/mml/csd/chemical-informatics-research-group/lennard-jones-fluid-reference-calculations). The value you are looking for is $U_{LRC}$. We were using `Configuration 1` in class. 


### Task 4 - Periodic boundaries (most difficult)

This is a very important function, and a version will be provided to you.
If your group contains a member who would like a challenge, they should attempt this task. 

1. Modify the calculate distance function to account for periodic boundaries. Your function should take an additional keyword argument, `box_length`, which has a default value of `None`.  If `box_length` is specified, the `box_length` value should be used to calculate the minimum image distance (in other words, the distance considering periodic boundaries). 
When calculating the minimum image distance, follow this procedure:
    - Calculate the distance in each dimension as we did previously (ie $x_2 - x_1$ )
    - From your group discussion you should have arrived at the conclusion that the maximum distance in any direction (`x`, `y`, or `z`) was  $\frac {l_B}{2}$ (where $l_B$ is the box length). Therefore, if our calculated distance in any direction is greater than $\frac {l_B}{2}$, we will want to subtract $l_B$ from the value. If there is more than one box length between the two points, you will want to subtract the appropriate number. 

2. Make sure to test behavior of your function using a few (at least 2) test cases and `assert` statements. Write explanations of the test cases you chose.
    
## Reviewing your teammate's change
You may need too pull the changes from your teammate's branch when you are reviewing their pull request. You can pull their branch to your local computer by doing

````{tab-set-code} 

```{code-block} shell
git switch main
git fetch 
git switch -c TEAMMATE_BRANCH --track origin/TEAMMATE_BRANCH
```
````

## Turning in this Assignment

You should turn in links to your Pull Request and your Pull Request Review on bCourses like usual!
