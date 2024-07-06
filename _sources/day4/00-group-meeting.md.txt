# Class Warm Up

## Explain xkcd
In your groups, take 5 minutes come up with an explanatin of this [xkcd](https://xkcd.com/) webcomic.

```{image} ../fig/git.png
:align: center
```

If you'd like, you can read the explaination on [Explain xkcd](https://explainxkcd.com/wiki/index.php/1597:_Git).

## Class Prep 

Make sure all pull requests from Day 3 are merged and you've pulled the changes to your main branch!

Create a Jupyter notebook for today's lecture in your Day 4 folder, named with your first and last name.
Create a markdown cell with a title.
Then, make a code cell with your group's tail correction function (make the function name be `calculate_tail_correction`). 
Also add the following code:

````{tab-set-code}

```{code-block} python

import math

def calculate_LJ(r_ij):
    r6_term = math.pow(1/r_ij, 6)
    r12_term = math.pow(r6_term, 2)
    pairwise_energy = 4 * (r12_term - r6_term)
    return pairwise_energy


def calculate_distance(coord1, coord2, box_length=None):
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

    distance = 0
    for i in range(3):
        dim_dist = coord1[i] - coord2[i]

        if box_length:
            dim_dist = dim_dist - box_length * round(dim_dist / box_length)

        dim_dist = dim_dist**2
        distance += dim_dist

    distance = math.sqrt(distance)
    return distance
    
def calculate_total_energy(coordinates, box_length, cutoff):
    """
    Calculate the total Lennard Jones energy of a system of particles.

    Parameters
    ----------
    coordinates : list
        Nested list containing particle coordinates.

    Returns
    -------
    total_energy : float
        The total pairwise Lennard Jones energy of the system of particles.
    """

    total_energy = 0

    num_atoms = len(coordinates)

    for i in range(num_atoms):
        for j in range(i + 1, num_atoms):

            dist_ij = calculate_distance(
                coordinates[i], coordinates[j], box_length=box_length
            )

            if dist_ij < cutoff:
                interaction_energy = calculate_LJ(dist_ij)
                total_energy += interaction_energy

    return total_energy

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

# Replace this with your group's function
def calculate_tail_correction(arguments):
    ...

```
````

In the class [Google Doc](https://docs.google.com/document/d/1Bs5K45Y9uPrfE1XoGYgawg4_oA9DGKwAGTD_-KCbe0Y/edit?usp=sharing) write an explanation of changes to our `calculate_distance` function and our `calculate_total_energy` function under the section "Code Difference Explanation" at the end of the document. 
Add a header with your group name over your explanation.

If you need a `calculate_tail_correction` function, use this one:

````{tab-set-code}

```{code-block} python
def calculate_tail_correction(num_particles, box_length, cutoff):
    """
    Calculate the long range tail correction
    """

    const1 = (8 * math.pi * num_particles**2) / (3 * box_length**3)
    const2 = (1 / 3) * (1 / cutoff) ** 9 - (1 / cutoff) ** 3

    return const1 * const2
```
````