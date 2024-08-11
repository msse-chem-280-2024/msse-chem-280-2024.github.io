# Introduction to Monte Carlo Methods

````{admonition} Overview
:class: overview

Questions:
- What are Monte Carlo methods?
- How can I use Monte Carlo to estimate pi?

Objectives:
- Explain Monte Carlo methods.
- Apply Monte Carlo method to calculate pi.
- Apply Monte Carlo to calculate integrals
````
## Day 2  - Overview Slides

{download}`Overview Slides <../_files/day-2-topics.pdf>`

## Introduction

{download}`Lecture Slides <../_files/pi_calculation.pdf>`

This module will cover calculating $\pi$ using Monte Carlo integration. 
For this module, as well as for the initial Monte Carlo code, we will use only libraries and functions which are part of the [Python Standard Library](https://docs.python.org/3/library/). 
The Python Standard Library is the set of modules and functions that are distributed with Python. 
We will use Matplotlib (not part of Python standard library) for visualization.

## Monte Carlo (MC) Integration

Monte Carlo methods estimate values (such as integrals or other statistical properties) through random sampling techniques. 
They provide approximate solutions, particularly useful when exact solutions are difficult or impossible to obtain analytically.

Consider a function $y = f(x)$.
In calculus courses, you have learned that the integral of $f(x)$ over a certain interval gives the area under the curve of this function. 
This area can be calculated exactly for many simple functions using analytical techniques.
In fact, the example shown in this lesson could be easily calculated.
However, for more complex functions finding the exact integral can be challenging or even impossible.
In this lesson, we introduce Monte Carlo using a simple integral. 
Later in the course, we will see Monte Carlo applied to high dimensional integrals.

### Procedure

In order to use MC for a funtion, we will generate random points on our interval of interest.
For high-dimensional functions, this domain is sometimes informally referred to as the []"phase space,"](https://en.wikipedia.org/wiki/Phase_space) particularly in fields like physics or statistical mechanics.

* Generate a set of uniformly distributed random points ($N_{trial}) over the area of interest, $A_{tested}$. For example, if we were to evaluate a generic function $f(x)$ over -3 to 3 in the x dimension and 0 to 3 in the y dimension, $A_{tested} = 6 * 3 = 18$

* Count the number of points that fall underneath the curve $f(x)$.
This number, is $N_{accept}$ in the equation below. 
With a large number of points, dividing the number of points under the curve to the total number of points will give you the ratio of the area under the curve to the total area tested.

* Multiply the area of consideration ($A_{tested}$) by the calculated ratio.


$$
A_{curve} = \frac{N_{accept}}{N_{trial}} * A_{tested} 
$$


## Calculation of $ \pi $ using MC Integration

In this lesson, we will be using Monte Carlo integration to estimate the value of $\pi$. Monte Carlo techniques depend on the generation of random numbers.

For our Monte Carlo integration, our

We calculate $\pi$ using random numbers and the unit circle. 
We will generate $N$ random $(x, y)$ points with x and y values between zero and one. This corresponds to points in the first quadrant of a Cartesian coordinate system. We start with a counter equal to zero. If a randomly generated point lies inside of the unit circle, we will increase our counter by one. After $N$ random numbers are generated, we can estimate the area of one quarter of the unit circle:

$$
A_{curve} = \frac{N_{accept}}{N_{trial}} * A_{tested} 
$$

We will see a more mathematically rigorous explanation for this formula later. In our case, the tested area, $A_{tested}$ is equal to 1, so the estimate of the area is simply the ratio of points inside the circle to the total number of points. 

The area of a circle is related to $\pi$ by $A_{circle} = \pi*r^{2}$, meaning that for the unit circle, the total area is equal to $\pi$.

Therefore, we can estimate the value of $\pi$ for our points by multiplying our calculated area by 4 (since our points will all be in the first quadrant)

$$ 
\pi \approx  4 * \frac{N_{accept}}{N_{trial}} 
$$

## Writing our MC code

To generate our random points, we will use the Python module [`random`](https://docs.python.org/3/library/random.html). The `random` library has functions related to random number generation.

We will also be using Python's built in [`math`](https://docs.python.org/3/library/math.html) module for operations like raising numbers to powers and accessing a reference value for pi.

First import the libraries:

````{tab-set-code} 

```{code-block} python
import random
import math
```
````

We will begin our calculation with 100 randomly generated points. 
We define a variable called `n_samples` to contain this information. 

````{tab-set-code} 

```{code-block} python
n_samples = 100
```
````


Next, we start a counter (`num_inside`) for keeping track of how many points have fallen inside our unit circle.

````{tab-set-code} 

```{code-block} python
num_inside = 0
```
````


To generate `n_samples` points, we use a `for` with the range function.

````{tab-set-code} 

```{code-block} python
for i in range(n_samples):
    print(i)
```
````


As a reminder, this `for` loop will print all numbers from `0` to `99`. In this `for` loop, we don't really care about the value of `i`, we are just using it to make sure the operation is done 100 times. For each loop iteration we need to 

1. Generate a random x point on the range 0 to 1
1. Generate a random y point on the range 0 to 1
1. Calculate the associated value ($x^2 + y^2$). If the value is less than 1, increase `num_inside` by 1.

````{tab-set-code} 

```{code-block} python
n_samples = 100

num_inside = 0

for i in range(n_samples):

    # Generate a random point between 0 and 1 for x.
    x = random.random()

    # Generate a random point between 0 and 1 for y.
    y = random.random()

    # Calculate the radius of this point
    r = math.sqrt(x ** 2 + y ** 2)

    if r < 1:
        num_inside += 1
```
````


After running this code, we can get a guess for the value of $\pi$.

````{tab-set-code} 

```{code-block} python
# Calculate pi
4 * num_inside / n_samples
```
````


````{tab-set-code} 

```{code-block} output
3.24
```
````


Your number will vary based on the random numbers which were generated. You will get a slightly different value for each calculation.

## Visualization

To get a better idea of what's going on, we can add visualization using the Python library matplotlib. Matplotlib is not part of the Python standard library, but is widely used for data visualization.


To use the matplotlib library, add the following import to your notebook.

````{tab-set-code} 

```{code-block} python
import matplotlib.pyplot as plt

```
````


We next create an empty figure using the `plt.figure` command. We then add an axis to this figure. Capturing the output of these commands as variables will allow us to continue to manipulate the figure.

````{tab-set-code} 

```{code-block} python
fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111)
fig.show()
```
````


Next, modify the loop where you calculated pi to add points to this plot when they are generated. We will modify this so that accepted points (points inside the circle) are plotted with blue circles while points outside of the unit circle are plotted with red stars. After the points are generated, we constrain the limits of the x and y axes.

````{tab-set-code} 

```{code-block} python
# This time add points to plot as they're calculated.

# Start by using 100 samples.
n_samples = 100

num_inside = 0
for i in range(n_samples):
    # Generate a random point between 0 and 1 for x.
    x = random.random()
    
    # Generate a random point between 0 and 1 for y.
    y = random.random()
    
    ## Calculate the radius of this point.
    r = math.sqrt(x ** 2 + y ** 2)
    
    # if this value is less than 1, the point is inside the circle.
    if r < 1:
        num_inside += 1
        # if inside add to plot
        ax.plot(x, y, 'ob')
    else:
        ax.plot(x, y, 'r*')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
```
````


An example output is shown below:

```{image} ../fig/100points_pi.png
:align: center
```

### Improving the visualization

We can add a circle to our visualization so that we can see the boundary of the unit circle
````{tab-set-code} 

```{code-block} python
# Use patch in matplotlib to make a circle for better visualization

from matplotlib.patches import Circle

circle = Circle((0, 0), 1, color='k', alpha=0.2)
ax.add_patch(circle)
fig.show()
```
````

```{image} ../fig/100points_pi_circle.png
:align: center
```

## Monte Carlo in more detail
Monte Carlo methods are numerical techniques
frequently used to estimate complex multidimensional integrals which otherwise could not be performed. The idea of Monte Carlo integration is to estimate the value of an integral by generating random points from the probability density.

For instance, the integral of the function $f(\textbf{x})$, where $\textbf{x} \in \Re^{M}$, is approximated as

 \begin{equation}
	 I = \int_V f(\textbf{x}) \, d\textbf{x} = \int_V
	 \frac{f(\textbf{x})}{h(\textbf{x})} h(\textbf{x}) \, d\textbf{x} 
	 = \left< \frac{f(\textbf{x})}{h(\textbf{x})} \right>_{h(\textbf{x})}
	 \label{eq.averageGeneral}
 \end{equation}

 The idea of Monte Carlo integration is to estimate the expectation value by
 generating random samples of $\textbf{x}$ from the probability density $h(\textbf{x})$. 

### Uniform Probability Density
We are free to chose the probability
distribution
$h(\textbf{x})$. The simplest case is to uniformly generate $\textbf{x}$
in the volume ($V$). In this way, $h(\textbf{x})$ becomes constant as

\begin{equation}
	h(\textbf{x}) = \frac{1}{V}
	\label{eq.uniformDist}
\end{equation}

Using this sampling density $h(\textbf{x})$, the integral becomes

\begin{equation}
	I = \int_V f(\textbf{x}) \, d\textbf{x} \approx \frac{V}{N} \sum_{i=1}^N
	f(\textbf{x}_i)
	\label{eq.averageUniform}
\end{equation}

where N is the total number of random samples and $f(\textbf{x}_i)$ is the
integrand evaluated using the $i^{th}$ sample.







````{admonition} Key Points
:class: key

- Monte Carlo methods calculate values through random sampling.
````
