# Creating a Python Module

````{admonition} Overview
:class: overview

Questions:
- What is a Python module?

Objectives:
- Put Python code into a module (.py file)
- Import functions from our module.
````

## Moving Code into a module

For the next section, we will move our code from the Jupyter notebook to a module.  
We will be able to import functions from that module into the Jupyter notebook to more cleanly run our simulations. 

Create a file called `monte_carlo_yourname.py` in `day5` folder.

Gather all of your functions from your Jupyter notebook and paste them into the python module you created. 
In a Python module, most import statements are typically at the top of the module, followed by function definitions. 
When you are done, your file might look something like the following (this code is missing the random and cubic lattice configuration generators):

````{tab-set-code} 

```{code-block} python
import math
import random

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

def calculate_tail_correction(num_particles, box_length, cutoff):
    """
    Calculate the long range tail correction
    """

    const1 = (8 * math.pi * num_particles**2) / (3 * box_length**3)
    const2 = (1 / 3) * (1 / cutoff) ** 9 - (1 / cutoff) ** 3

    return const1 * const2

def accept_or_reject(delta_e, beta):
    """
    Accept or reject a move based on the Metropolis criterion.

    Parameters
    ----------
    delta_e : float
        The change in energy resulting from a particle movement.
    beta : float
        The inverse of the system temperature.

    Returns
    -------
    accept : bool
        Whether to accept the move.
    """

    if delta_e <= 0:
        accept = True
    else:
        random_number = random.random()
        p_acc = math.exp(-beta*delta_e)

        if random_number < p_acc:
            accept = True
        else:
            accept = False

    return accept

def calculate_pair_energy(coordinates, i_particle, box_length, cutoff):
    """
    Calculate the interaction energy of a particle with its environment (all other particles in the system).
    
    Parameters
    ----------
    coordinates : list
        The coordinates for all particles in the system.
    
    i_particle : int
        The particle number for which to calculate the energy.
    
    cutoff : float
        The simulation cutoff. Beyond this distance, interaction energies are not calculated.
    
    Returns
    -------
    e_total : float
        The pairwise interaction energy of the i_th particle with all other particles.
    """
    
    e_total = 0
    i_position = coordinates[i_particle]
    num_atoms = len(coordinates)
    
    for j_particle in range(num_atoms):
        if i_particle != j_particle:
            j_position = coordinates[j_particle]
            rij = calculate_distance(i_position, j_position, box_length)
    
            if rij < cutoff:
                e_pair = calculate_LJ(rij)
                e_total += e_pair
    
    return e_total
        
```
````

Put your simulation loop in a second cell:

````{tab-set-code} 

```{code-block} python

# Simulation Parameters
reduced_temperature = 0.9
num_moves = 1
max_displacement = 0.1
cutoff = 3.0
freq = 1000

# Calculated quantities
beta = 1 / reduced_temperature

# Define initial coordinates
coordinates, box_length = read_xyz("../data/sample_config1.txt")
num_particles = len(coordinates)

# Set up energy
delta_energy = 0

total_energy = calculate_total_energy(coordinates, box_length, cutoff)
total_energy += calculate_tail_correction(num_particles, box_length, cutoff)

print(f"The starting energy is {total_energy}.")

# Monte Carlo Simulation Loop

for move in range(num_moves):
    # 1. Randomly pick one of N particles.
    random_particle = random.randrange(num_particles)
    
    # 2. Calculate the interaction energy of the selected particle with the system, and store this value.
    current_energy = calculate_pair_energy(coordinates, random_particle, box_length, cutoff)
    
    # 3. Generate a random x, y, z displacement within max_displacement.
    x_rand = random.uniform(-max_displacement, max_displacement)
    y_rand = random.uniform(-max_displacement, max_displacement)
    z_rand = random.uniform(-max_displacement, max_displacement)
    
    # 4. Modify the coordinate of the selected particle by the generated displacements.
    coordinates[random_particle][0] += x_rand
    coordinates[random_particle][1] += y_rand
    coordinates[random_particle][2] += z_rand
    
    # 5. Calculate the interaction energy of the moved particle with the system, and store this value.
    proposed_energy = calculate_pair_energy(coordinates, random_particle, box_length, cutoff)
    energy_difference = proposed_energy - current_energy
    
    # 6. Based on the energy difference, decide to accept or reject the movement.
    accept = accept_or_reject(energy_difference, beta)
    
    # 7. If we accept, move the particle.
    if accept:
        total_energy += energy_difference
    else:
        coordinates[random_particle][0] -= x_rand
        coordinates[random_particle][1] -= y_rand
        coordinates[random_particle][2] -= z_rand

    if move % freq == 0:
        print(move, total_energy/num_particles)

```
````


Note that we have moved all the imports to the top and also changed the location of our file path. 
If you have moved everything without problems, you should be able to run the simulation by typing the following command from your `day5` folder.

````{tab-set-code} 

```{code-block} shell
$ python monte_carlo_yourname.py
```
````

This seems great! 
But, we want to make our simulation code importable from another file like a Jupyter notebook. 
Let's make our simulation run into a function. 
For this function, we want to consider what are input simulation parameters. 
In other words, if we want to run several simulations, what would we change? We will want to make these our function arguments. 
We will also modify our function to return a list of generated coordinates, so we can analyze them later.

````{tab-set-code} 

```{code-block} python
def run_simulation(coordinates, box_length, cutoff, reduced_temperature, num_moves, max_displacement, freq=1000):
    # Calculated quantities
    beta = 1 / reduced_temperature

    num_particles = len(coordinates)
    
    # Set up energy
    delta_energy = 0
    
    total_energy = calculate_total_energy(coordinates, box_length, cutoff)
    total_energy += calculate_tail_correction(num_particles, box_length, cutoff)
    
    print(f"The starting energy is {total_energy}.")
    
    # Monte Carlo Simulation Loop
    
    for move in range(num_moves):
        # 1. Randomly pick one of N particles.
        random_particle = random.randrange(num_particles)
        
        # 2. Calculate the interaction energy of the selected particle with the system, and store this value.
        current_energy = calculate_pair_energy(coordinates, random_particle, box_length, cutoff)
        
        # 3. Generate a random x, y, z displacement within max_displacement.
        x_rand = random.uniform(-max_displacement, max_displacement)
        y_rand = random.uniform(-max_displacement, max_displacement)
        z_rand = random.uniform(-max_displacement, max_displacement)
        
        # 4. Modify the coordinate of the selected particle by the generated displacements.
        coordinates[random_particle][0] += x_rand
        coordinates[random_particle][1] += y_rand
        coordinates[random_particle][2] += z_rand
        
        # 5. Calculate the interaction energy of the moved particle with the system, and store this value.
        proposed_energy = calculate_pair_energy(coordinates, random_particle, box_length, cutoff)
        energy_difference = proposed_energy - current_energy
        
        # 6. Based on the energy difference, decide to accept or reject the movement.
        accept = accept_or_reject(energy_difference, beta)
        
        # 7. If we accept, move the particle.
        if accept:
            total_energy += energy_difference
        else:
            coordinates[random_particle][0] -= x_rand
            coordinates[random_particle][1] -= y_rand
            coordinates[random_particle][2] -= z_rand
    
        if move % freq == 0:
            print(move, total_energy/num_particles)
```
````

For a Monte Carlo simulation, we want to keep track of the coordinates so we can analyze them.
We can add some additional statements to our functions under `if move % freq` to keep the coordinates
at specified snapshots, then we can return them at the end of the simulation.

```{code-block} python
def run_simulation(coordinates, box_length, cutoff, reduced_temperature, num_moves, max_displacement, freq=1000):
    # Calculated quantities
    beta = 1 / reduced_temperature

    num_particles = len(coordinates)
    
    # Set up energy
    delta_energy = 0
    
    total_energy = calculate_total_energy(coordinates, box_length, cutoff)
    total_energy += calculate_tail_correction(num_particles, box_length, cutoff)

    # Create a list for coordinates
    all_coordinates = []
    
    print(f"The starting energy is {total_energy}.")
    
    # Monte Carlo Simulation Loop
    
    for move in range(num_moves):
        # 1. Randomly pick one of N particles.
        random_particle = random.randrange(num_particles)
        
        # 2. Calculate the interaction energy of the selected particle with the system, and store this value.
        current_energy = calculate_pair_energy(coordinates, random_particle, box_length, cutoff)
        
        # 3. Generate a random x, y, z displacement within max_displacement.
        x_rand = random.uniform(-max_displacement, max_displacement)
        y_rand = random.uniform(-max_displacement, max_displacement)
        z_rand = random.uniform(-max_displacement, max_displacement)
        
        # 4. Modify the coordinate of the selected particle by the generated displacements.
        coordinates[random_particle][0] += x_rand
        coordinates[random_particle][1] += y_rand
        coordinates[random_particle][2] += z_rand
        
        # 5. Calculate the interaction energy of the moved particle with the system, and store this value.
        proposed_energy = calculate_pair_energy(coordinates, random_particle, box_length, cutoff)
        energy_difference = proposed_energy - current_energy
        
        # 6. Based on the energy difference, decide to accept or reject the movement.
        accept = accept_or_reject(energy_difference, beta)
        
        # 7. If we accept, move the particle.
        if accept:
            total_energy += energy_difference
        else:
            coordinates[random_particle][0] -= x_rand
            coordinates[random_particle][1] -= y_rand
            coordinates[random_particle][2] -= z_rand
    
        if move % freq == 0:
            print(move, total_energy/num_particles)
            all_coordinates.append(coordinates)

    return all_coordinates

```
````

Now we can try this out in another Python module Jupyter notebook. 

Create a Python module called `run_sim.py` - make sure that you replace yourname with your name!
The any time "monte_carlo_yourname" is used in the cell below, it should match the name of the module you created above.

````{tab-set-code} 

```{code-block} python
import monte_carlo_yourname

# Set simulation parameters
reduced_temperature = 0.9
num_steps = 50000
max_displacement = 0.1 
cutoff = 3
freq = 1000

# Read initial coordinates
coordinates, box_length = monte_carlo_yourname.read_xyz("../data/sample_config1.txt")

monte_carlo_yourname.run_simulation(coordinates, box_length, reduced_temperature, cutoff, num_steps, max_displacement)
```
````

You can now run your simulation from the command line (terminal) by typing:

````{tab-set-code}

```{code-block} shell
python run_sim.py
```

````

You can also now import your module into a Jupyter notebook.

````{admonition} Key Points
:class: key

- When working on a large project, you should organize your code into modules.
````
