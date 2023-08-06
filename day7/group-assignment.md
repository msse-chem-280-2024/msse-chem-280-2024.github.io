# Group Homework Assignment - Day 7 & 8

Your group assignment for today (and tomorrow) is to rewrite your
Python `mcsim` package into C++.

Begin by looking through your mcsim code and determining common data structures
that you are using (ie, a list of coordinates).  Think about what C++ data
types you would use for those.

First, identify which functions are standalone - that is, they do not call
other functions that you would have to write. Focus on rewriting these
functions first. Which functions are these?

Test the functions by calling them from `main` with values for which you
know the result -- we will cover testing in C++ later.

After you have the simple functions, find the next functions you can rewrite,
which should be functions that only call the already-written functions. This
is the basic workflow of refactoring and rewriting code.

## Random number generation

The random number generator given in the third individual homework can
also be used here.

````{tab-set-code}

```{code-block} c++
#include <random> // for random numbers
#include <chrono> // for generating the seed

// A Global! Probably shouldn't be used in real code
std::default_random_engine re;

/*! Generate a random double within a given range */
double random_double(double lower_bound, double upper_bound)
{
   std::uniform_real_distribution<double> dist(lower_bound, upper_bound);
   return dist(re);
}

/*! Generate a random integer within a given range
    The generated integer will be on the range [a,b)
*/
double random_integer(int lower_bound, int upper_bound)
{           
   //dist will return [a,b] but we want [a,b)
   std::uniform_int_distribution<int> dist(lower_bound, upper_bound-1);
   return dist(re);
}  

int main(void)
{
    // Initialize random number generation based on time
    re.seed(std::chrono::system_clock::now().time_since_epoch().count());

    /*
      Other code here
    */
}
```
````

## Default Arguments

Function arguments can also have default values, just like in python. The syntax
is the same. However, keep in mind that the default argument must be of the same
type as the variable, and C++ does not have a `None` type. What would be a
good default `box_length`?


## Reading XYZ files

Below is the function for reading XYZ files in C++. Notice the `typedefs`
and the example of how to use it in `main`.

````{tab-set-code}

```{code-block} c++
// Include these at the top of your file
#include <fstream> // for reading/writing files
#include <array>   // for std::array
#include <vector>  // for std::vector
#include <utility> // for std::pair

// Make some types more convenient
typedef std::array<double, 3> AtomCoord;
typedef std::vector<AtomCoord> Coordinates;

std::pair<Coordinates, double> read_xyz(std::string file_path)
{
    // Opens up a file stream for input
    std::ifstream infile(file_path);

    // Check that it was successfully opened
    if(!infile.is_open())
    {   
        throw std::runtime_error("File path in read_xyz does not exist!");
    }
    
    double dummy; // Data that is thrown away (box length, atom indices)
    double box_length;
    int num_atoms;
    
    // Grab box_length from first number, throw the rest away
    infile >> box_length >> dummy >> dummy;
    
    // now the number of atoms
    infile >> num_atoms;
    
    // Uncomment to help troubleshoot
    //std::cout << "Box length: " << box_length << " natoms: " << num_atoms << std::endl;
    
    // Stores the atomic coordinates
    // Remember, this is a vector of arrays
    Coordinates coords;
    
    for(int i = 0; i < num_atoms; i++)
    {   
        AtomCoord coord;
        
        // Throws away the atom index
        infile >> dummy >> coord[0] >> coord[1] >> coord[2];
        
        // Add to the vector
        coords.push_back(coord);
    }

    // Makes an appropriate pair object
    return std::make_pair(coords, box_length);
}


int main(void)
{
    /* other code here */
    std::pair<Coordinates, double> xyz_info = read_xyz("../lj_sample_configurations/lj_sample_config_periodic1.txt");

    Coordinates coords = xyz_info.first;
    double box_length = xyz_info.second;

    // can now use box_length and coords

    /* other code here */
}
```
````
