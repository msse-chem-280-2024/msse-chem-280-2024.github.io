# Total Energy Comparison

````{admonition} Overview
:class: overview

Questions:
- Does my total energy agree with the values reported from NIST?

Objectives:
- Apply a cut-off and periodic boundaries to the energy calculation and compare it to values reported by NIST.
````

```{admonition} Prerequisites

Make sure you have the functions from the previous page in a Jupyter notebook.

```

Now that we have accounted for periodic boundaries and a cut-off, we can compare our results to those from NIST.

````{tab-set-code} 

```{code-block} python
nist_3cut = -4.3515E+03
nist_4cut = -4.4675E+03

config1_file = "../data/sample_config1.txt"

coords, box_length = read_xyz(config1_file)
calc_3cut = calculate_total_energy(coords, box_length, 3)
calc_4cut = calculate_total_energy(coords, box_length, 4)

print(f"Cut off 3: {calc_3cut}")
print(f"Cut off 4: {calc_4cut}")
```

````

:::{admonition} Formatted Strings   
:class: tip


The code block above uses a special syntax in the print statment called a formatted string.
In Python, formatted strings, denoted by an f prefix, allow us to embed expressions and variables directly into a string. 
By using curly braces {} to wrap the expressions, the values of those expressions are evaluated and inserted into the string when it is printed.

Here is another example of a formatted string:

```python
class_name = "Chem 280"
my_string = f"Hello from {class_name}!"

print(my_string)    # prints "Hello from Chem 280!"
```
:::


Now that we have our calculated values, we can compare our results to those computed by NIST.


````{tab-set-code} 

```{code-block} python
assert math.isclose(calc_3cut, nist_3cut, rel_tol=0.02)
assert math.isclose(calc_4cut, nist_4cut, rel_tol=0.02)
```

````

