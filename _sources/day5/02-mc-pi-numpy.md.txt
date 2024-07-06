# Using NumPy Arrays to Calculate pi

````{admonition} Overview
:class: overview

Questions:
- What are the differences between numpy arrays and lists?

Objectives:
- Be able to name the differences between Python lists and numpy arrays.
- Understand the idea of broadcasting.
````

## Rewriting our calculation of pi using NumPy

We will now return to our calculation of $\pi$. Instead of using the Python Standard Library functions, we will examine how this calculation could have been made much simpler using the NumPy library.

Recall our former code for calculating $\pi$
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

pi = 4 * (num_inside) / n_samples
```
````


To start using numpy, we will first import it.

````{tab-set-code} 

```{code-block} python
import numpy as np
```
````


We set the same number of samples:

````{tab-set-code} 

```{code-block} python
n_samples = 100
```
````


Next, we generate 100 random points. In our previous code, we did this using the `random.random` function in a `for` loop.

NumPy also has a `random.random` function. You can try it out:

````{tab-set-code} 

```{code-block} python
np.random.random()
```
````


````{tab-set-code} 

```{code-block} output
0.627385792598836
```
````


When no argument is given to `np.random.random` it behaves exactly as we are used to `random.random`. It gives us one random number. However, you can also give the function a size to generate an array of random numbers. 

For us, we would like a random array that is size `n_samples, 2`. 

````{tab-set-code} 

```{code-block} python
random_numbers = np.random.random((n_samples, 2))
```
````


If you check this variable, you will see it is an array with 100 rows and 2 columns.

The next thing we need to do is to square and sum the x and y values. We can square all the values at once because of element-wise operations:

````{tab-set-code} 

```{code-block} python
r_squared = random_numbers ** 2
```
````


Next, we want to sum all of the rows of r_squared. We will want to use the numpy function `sum` which we learned about in the last module.

Executing 

````{tab-set-code} 

```{code-block} python
np.sum(r_squared)
```
````


will give us the value of the sum of all the elements. We want a sum of the rows, so we will want to use the `axis` arugment.

To figure out the axis we want, check the shape of `r_squared`

````{tab-set-code} 

```{code-block} python
r_squared.shape
```
````


````{tab-set-code} 

```{code-block} output
(100, 2)
```
````


If we want the sum of the rows, we should use `axis=1 `. We expect that this sum should have 100 values, so check this after your calculation:

````{tab-set-code} 

```{code-block} python
vals = np.sum(r_squared, axis=1)
vals.shape
```
````


````{tab-set-code} 

```{code-block} output
(100, )
```
````


Next, we can easily count the number of points inside the circle using logical comparison with the numpy array.

````{tab-set-code} 

```{code-block} python
points_inside = vals < 1
num_inside = np.sum(points_inside)
```
````


Finally, we estimate $\pi$

````{tab-set-code} 

```{code-block} python
pi = 4 * num_inside / n_samples
```
````



Final code:
````{tab-set-code} 

```{code-block} python
import math
import numpy as np

# Start by using 100 samples.
n_samples = 100

random_numbers = np.random.random(size=(n_samples,2))

vals = np.sum(random_numbers**2, axis=1)
vals = np.sqrt(vals)
num_inside = np.sum(vals < 1)

pi = 4 * num_inside / n_samples
```
````


## Comparing Performace : NumPy vs Python Standard Library

Let's try timing how long it takes to calculate $$\pi$$ with 10 million samples for each method:

````{tab-set-code} 

```{code-block} python
import time
import random

start = time.time()
# Start by using 100 samples.
n_samples = 1000000

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
4 * num_inside / n_samples

end = time.time()

elapsed_time = end - start
print(elapsed_time)
```
````


````{tab-set-code} 

```{code-block} output
0.6184561252593994
```
````


Do the same thing with the method which uses NumPy:

````{tab-set-code} 

```{code-block} python
import time

start = time.time()
n_samples = 10000000

random_numbers = np.random.random(size=(n_samples,2))

vals = np.sum(random_numbers**2, axis=1)
num_inside = np.sum(vals < 1)
pi = 4 * num_inside / n_samples

end = time.time()

elapsed_time = end - start
print(elapsed_time)
```
````


````{tab-set-code} 

```{code-block} output
0.059281349182128906
```
````


We can see that our NumPy version is about 10 times faster than the one written in pure Python. This is a huge advantage to using NumPy - it can make your Python code much faster.

In our case, we were only waiting 5 seconds for our first calculation, so the pure Python version may not bother us that much. However, there are some cases (such as our MC simulation) which become very slow using pure Python for large systems.

For your homework, your task (it's a bonus), is to rewrite your MC simulation to use NumPy and to test the speed up.

See the description on the next page for more information!
````{admonition} Key Points
:class: key

- NumPy arrays which are the same size use element-wise operations when added or subtracted.
- NumPy uses something called *broadcasting* for arrays which are not the same size to allow arrays to be added or multiplied.
- NumPy has extensive documentation online - you should check this out if you need to do a computation.
````
