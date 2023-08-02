# Lennard Jones Energy of Atomic System

````{admonition} Overview
:class: overview

Questions:
- How do I use the Lennard Jones equation to calculate the energy of an atomic system?

Objectives:
- Write Python code to calculate the Lennard Jones energy.
````

```{admonition} Getting the required functions
:class: tip

To continue with this lesson, make sure you have your Lennard Jones function (`calculate_LJ`) in reduced units, and your `calculate_distance` function (written as a homework assignment.).
In your Jupyter notebook.

```

When applying the LJ potential to a set of atomic coordinates, the total potential energy of the system is equal to the sum of the LJ energy over all pairwise interactions:

$$
U \left( \textbf{r}^N \right) = \sum_{i=1}^{N} \sum_{j>i}^{N} U \left( r_{ij} \right)
$$

We can write some steps out for calculating the total Lennard Jones potential energy for a system.

1. Calculate the distance between each particle and every other particle in the system.
2. Evaluate the Lennard Jones potential for each distance
3. Sum the energies to get the total potential energy.

From this procedure, we can see that we will need a few more functions. 
We will need a function that can calculate a distance between two particles based on their coordinates. We will need to loop over particle pairs.

## Calculating the total pairwise LJ energy

Next, we will write a function for calculating the total pair potential energy of a system of particles. Using the equation above, we can write the function:

````{tab-set-code} 

```{code-block} python
def calculate_total_energy(coordinates):
    """
    Calculate the total Lennard Jones energy of a system of particles.
    
    Parameters
    ----------
    coordinates : list
        Nested list containing particle coordinates.
    
    Returns
    -------
    total_energy : float
        the total pairwise Lennard Jones energy
    """
    
    total_energy = 0
    num_atoms = len(coordinates)
    for i in range(num_atoms):
        for j in range(i+1, num_atoms):
            dist_ij = calculate_distance(coordinates[i], coordinates[j])
            total_energy += calculate_LJ(dist_ij)
    
    return total_energy
```
````

In order to test this, let's create a system where we roughly know the energy. We will want a system of more than two particles, otherwise we are just testing the `calculate_LJ` function. We will have three particles which are spaced by a distance of $2^{1/6}\sigma$. We would expect this system of particles to have an energy of roughly $-2\epsilon$.

````{tab-set-code} 

```{code-block} python
coordinates = [[0, 0, 0], [0, math.pow(2, 1/6), 0], [0, 2*math.pow(2, 1/6), 0]]

test_energy = calculate_total_energy(coordinates)

print(test_energy)
```
````


````{tab-set-code} 

```{code-block} output
-2.031005859375
```
````


This seems promising. The additional `0.031` is from the interaction of particles 1 and 3. The assert statement for this check will be a little different. We can use the function `math.isclose` to compare two numbers within a certain tolerance. If the numbers are close, `True` is returned, otherwise `False`.

We can write our assert statement to check that the two values are within 5% of one another

````{tab-set-code} 

```{code-block} python
assert math.isclose(test_energy, -2, rel_tol=0.05)
```
```` 

### Reading coordinates from NIST file

Now that we have functions for calculating the LJ energy for a system of particles, we can compare our calculated values to those reported by NIST. Use the provided `read_xyz` function below to read coordinates from the provided sample coordinate files:

````{tab-set-code} 

```{code-block} python
def read_xyz(filepath):
    """
    Reads coordinates from an xyz file.
    
    Parameters
    ----------
    filepath : str
       The path to the xyz file to be processed.
       
    Returns
    -------
    atomic_coordinates : list
        A two dimensional list containing atomic coordinates
    """
    
    with open(filepath) as f:
        box_length = float(f.readline().split()[0])
        num_atoms = float(f.readline())
        coordinates = f.readlines()
    
    atomic_coordinates = []
    
    for atom in coordinates:
        split_atoms = atom.split()
        
        float_coords = []
        
        # We split this way to get rid of the atom label.
        for coord in split_atoms[1:]:
            float_coords.append(float(coord))
            
        atomic_coordinates.append(float_coords)
        
    
    return atomic_coordinates, box_length
```
````


Use the function to read in the first sample configuration:

````{tab-set-code} 

```{code-block} python

config1_file = "../data/sample_config1.txt"

sample_coords, box_length = read_xyz(config1_file)
```
````

### Sanity Checks

1. Check that function has expected number of coordinates.
2. Check that first line, last line is as expected.

````{tab-set-code} 

```{code-block} python
# We expect this file to have 800 particles
assert len(sample_coords) == 800

# We expect the first line to be:
first_line = [-1.126362593256E-01, 1.385093082507E+00, -8.842035145736E-01]

for i in range(3):
    assert first_line[i] == sample_coords[0][i]
    
# We expect the last line to be:
last_line = [3.497455843197, 0.3754925406415, 4.393398690912]

for i in range(3):
    assert last_line[i] == sample_coords[-1][i]
```
````

### Pairwise LJ energy for NIST system

We will now compare our calculated total energy to reference values from NIST. You can see a list of reference values [on this website](https://www.nist.gov/mml/csd/chemical-informatics-group/lennard-jones-fluid-reference-calculations-cuboid-cell). We are using configuration 1.

When we try comparing our calculated energy to those reported by NIST, we will find that they are not the same. Because we've tested each of our functions as we've written them, we can be somewhat confident this isn't occurring because of errors in our code. 

Instead, it must be from different assumptions we are making about our system.

````{tab-set-code} 

```{code-block} python
total_energy = calculate_total_energy(sample_coords)
assert total_energy == -4351.5
```
````


````{tab-set-code} 

```{code-block} error
AssertionError                            Traceback (most recent call last)
<ipython-input-11-b7c5eba717e6> in <module>
----> 1 assert total_energy == -4351.5

AssertionError: 
```
````