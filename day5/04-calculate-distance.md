# Rewriting the Distance Function

````{admonition} Overview
:class: overview

Questions:
- How can I rewrite functions to take advantage of NumPy element-wise operation and broadcasting?

Objectives:
- Rewrite calculate distance function for numpy arrays
````


Consider the following `calculate_distance` function which is written for Python lists using functions in the Python Standard Library:

````{tab-set-code} 

```{code-block} python
def calculate_distance(coord1, coord2, box_length=None):
    """
    Calculate the distance between two 3D coordinates.
    Parameters
    ----------
    coord1, coord2: list
        The atomic coordinates
    box_length : float
        The box length. If given, the minimum image convention will be used to calculate the distance.

    Returns
    -------
    distance: float
        The distance between the two points.
    """
    distance = 0
    for i in range(3):
        dim_dist = (coord1[i] - coord2[i])
        if box_length:
            dim_dist = dim_dist - box_length * round(dim_dist / box_length)
        dim_dist = dim_dist**2
        distance += dim_dist
    distance = math.sqrt(distance)
    return distance
```
````


Now that we have learned a bit about NumPy arrays, you can imagine that we could rewrite this function to take advantage of broadcasting and element-wise operations to avoid this `for` loop. Let's take some time to rewrite this. Let's work outside of the function before we write our new numpy function.

First, define some numpy arrays:

````{tab-set-code} 

```{code-block} python
point1 = np.array([0, 0, 0])
point2 = np.array([0, 8, 0])
```
````


Notice that we can calculate the distance with our function:

````{tab-set-code} 

```{code-block} python
calculate_distance(point1, point2)
```
````


Let's consider calculating the distance between these two points using numpy operations. First, we can get the distance between in each point in each dimension by subtracting the two numpy arrays:

````{tab-set-code} 

```{code-block} python
dimensional_distance = point1 - point2
print(dimensional_distance)
```
````


If we aren't considering periodic boundaries, the next thing we would need to do would be to square each element of this array. We can use the element wise capabilities of NumPy instead of doing this with a for loop:

````{tab-set-code} 

```{code-block} python
dd2 = dimensional_distance ** 2
```
````


Next, we sum all of these numbers together and take the square root. 
````{tab-set-code} 

```{code-block} python
dd2_sum = dd2.sum()
distance = math.sqrt(dd2_sum)
print(distance)
```
````


````{tab-set-code} 

```{code-block} output
8.0
```
````


Let's put this into a function:

````{tab-set-code} 

```{code-block} python
def calculate_distance_np(coord1, coord2, box_length=None):
    """
    Calculate the distance between two 3D coordinates.
    Parameters
    ----------
    coord1, coord2: np.ndarray
        The atomic coordinates

    Returns
    -------
    distance: float
        The distance between the two points.
    """
    coord_dist = coord1 - coord2

    coord_dist = coord_dist ** 2

    coord_dist_sum = coord_dist.sum()

    distance = math.sqrt(coord_dist_sum)

    return distance
```
````


Next, let's add the minimum image convention to our calculation. For the minimum image convention, we will need to make an adjustment if necessary before squaring `coord_dist`. We might just try altering the line from our original function:

````{tab-set-code} 

```{code-block} python
if box_length:
    coord_dist = coord_dist - box_length * round(coord_dist / box_length)
```
````


However, if we attempt to execute this function with a box length, we will get an error.

````{tab-set-code} 

```{code-block} python
calculate_distance_np(point1, point2, 10)
```
````


````{tab-set-code} 

```{code-block} python
TypeError: type numpy.ndarray doesn't define __round__ method
```
````


This is because `round` which is part of the Python Standard Library will not work on the multidimensional NumPy array. We will have to switch it out for the function `np.round` which will perform element-wise rounding.

````{tab-set-code} 

```{code-block} python
def calculate_distance_np(coord1, coord2, box_length=None):
    """
    Calculate the distance between two 3D coordinates.
    Parameters
    ----------
    coord1, coord2: np.ndarray
        The atomic coordinates

    Returns
    -------
    distance: float
        The distance between the two points.
    """
    coord_dist = coord1 - coord2

    if box_length:
        coord_dist = coord_dist - box_length * np.round(coord_dist / box_length)

    coord_dist = coord_dist ** 2

    coord_dist_sum = coord_dist.sum()

    distance = math.sqrt(coord_dist_sum)

    return distance
```
````


Rewriting our function this way isn't very advantageous for the case where each array represents only one coordinate. However, remember that with NumPy arrays, we could calculate the distance between sets of particles or between one particle and a set of particles at once. Let's consider the case where we have two sets of coordinates and we want to know the distance between each one:

````{tab-set-code} 

```{code-block} python
coord_set1 = np.array([[0, 0, 0], [0,1,0]])
coord_set2 = np.array([[0,8,0], [0, 1.5, 0]])
```
````


If you work with these variables outside of your function, you will see that we need to modify our `calculate_distance_np` function to use the `axis=1` argument for `sum`. Then, we need to change `math.sqrt` to the `numpy` version so it will work on arrays:

````{tab-set-code} 

```{code-block} python
def calculate_distance_np(coord1, coord2, box_length=None):
    """
    Calculate the distance between two 3D coordinates.
    Parameters
    ----------
    coord1, coord2: np.ndarray
        The atomic coordinates

    Returns
    -------
    distance: float
        The distance between the two points.
    """
    coord_dist = coord1 - coord2

    if box_length:
        coord_dist = coord_dist - box_length * np.round(coord_dist / box_length)

    coord_dist = coord_dist ** 2

    coord_dist_sum = coord_dist.sum(axis=1)

    distance = np.sqrt(coord_dist_sum)

    return distance
```
````


Try our function with our two sets of points:

````{tab-set-code} 

```{code-block} python
calculate_distance_np(coord_set1, coord_set2)
```
````


````{tab-set-code} 

```{code-block} python
array([8. , 0.5])
```
````


We should also make sure this will work when box length is specified:

````{tab-set-code} 

```{code-block} python
calculate_distance_np(coord_set1, coord_set2, 10)
```
````


````{tab-set-code} 

```{code-block} python
array([2 , 0.5])
```
````


Excellent! And before deciding we are done, we should test our other test case (you can see out pytest would be useful here!)

````{tab-set-code} 

```{code-block} python
calculate_distance(point1, point2)
```
````


````{tab-set-code} 

```{code-block} python
AxisError: axis 1 is out of bounds for array of dimension 1
```
````


Now our function is not working for the case where our numpy arrays only have one dimension. When you check the shape of our first points, you will see there is only one value. We will want to reshape these to force them to be of size (1, 3) instead of (3,).

````{tab-set-code} 

```{code-block} python
def calculate_distance_np(coord1, coord2, box_length=None):
    """
    Calculate the distance between two 3D coordinates.
    Parameters
    ----------
    coord1, coord2: np.ndarray
        The atomic coordinates
    box_length : float
        The box length to be used for minimum image distance.

    Returns
    -------
    distance: float
        The distance between the two points.
    """
    coord_dist = coord1 - coord2

    if box_length:
        coord_dist = coord_dist - box_length * np.round(coord_dist / box_length)

    if coord_dist.ndim < 2:
        coord_dist = coord_dist.reshape(1, -1)

    coord_dist = coord_dist ** 2

    coord_dist_sum = coord_dist.sum(axis=1)

    distance = np.sqrt(coord_dist_sum)

    return distance
```
````


Now we have a `calculate_distance` function which will work on a set of particles, rather than just one particle.























````{admonition} Key Points
:class: key


````
