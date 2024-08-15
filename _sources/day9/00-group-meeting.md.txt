# Class Warm Up

Today, we will examine different ways Python and C++ behave related to passing function arguments.

To start, consider the two code snippets. 
For each one, predict what you think the output will be before you run it.
After you have made a prediction, run each one to check your answers.

As you work through this discussion, record answers for your group in the [class Google Presentation](https://docs.google.com/presentation/d/13b2208ItU8VLqdxMI1ovSCl0Ll3aIYy6CdWZUZi5LxA/edit?usp=sharing)

````{tab-set-code} 

```{code-block} python
def append_element(lst):
    lst.append(42)
    print(f"Inside function: {lst}")

my_list = [1, 2, 3]
print(f"Before function call: {my_list}")
append_element(my_list)
print(f"After function call: {my_list}")

```
````


````{tab-set-code} 

```{code-block} cpp
#include <iostream>
#include <vector>

void append_element(std::vector<int> vec) {
    vec.push_back(42);
    std::cout << "Inside function: ";
    for (int i : vec) std::cout << i << " ";
    std::cout << std::endl;
}

int main() {
    std::vector<int> my_vector = {1, 2, 3};
    std::cout << "Before function call: ";
    for (int i : my_vector) std::cout << i << " ";
    std::cout << std::endl;

    append_element(my_vector);

    std::cout << "After function call: ";
    for (int i : my_vector) std::cout << i << " ";
    std::cout << std::endl;

    return 0;
}
```
````

Do either function behave differently than you expect? 
In your group discuss why particular behaviors might be observed.
How could you make the C++ function match the behavior of the Python function?
As an exercise, create a new C++ function to match the Python function behavior.

Now consider the behavior of this code snippet using NumPy and Python lists.

````{tab-set-code} 

```{code-block} python
# Create a Python list
original_list = [1, 2, 3, 4, 5]
print(f"Original list before modification: {original_list}")

# Slice the list
sliced_list = original_list[1:4]
print(f"Sliced list before modification: {sliced_list}")

# Modify the sliced list
sliced_list[0] = 99
print(f"Sliced list after modification: {sliced_list}")

# Check the original list to see if it was modified
print(f"Original list after modification: {original_list}")

```
````

````{tab-set-code} 

```{code-block} python
import numpy as np

# Create a NumPy array
original_array = np.array([1, 2, 3, 4, 5])
print(f"Original array before modification: {original_array}")

# Slice the array
sliced_array = original_array[1:4]
print(f"Sliced array before modification: {sliced_array}")

# Modify the sliced array
sliced_array[0] = 99
print(f"Sliced array after modification: {sliced_array}")

# Check the original array to see if it was modified
print(f"Original array after modification: {original_array}")

```
````

What might be some consequences of your observed behavior?



