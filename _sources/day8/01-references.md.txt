
# References

While pointers are inherited from the C language, C++ introduces a new but
similar concept - a *reference*.  References are similar to pointers
with a few key differences

1. References must be set to reference an existing object
1. References cannot be NULL/nullptr
1. Once set, references cannot be *re-seated* (made to reference something else)
1. The star operator is not required to dereference a reference

References are created by using `&` with the type. For example,

````{tab-set-code} 

```{code-block} cpp
std::string my_string = "Hello world!"; // Regular string
std::string & ref_string = my_string; // Reference to my_string
```
````


However, given the differences listed above

````{tab-set-code} 

```{code-block} cpp
std::string & empty_ref; // not valid - must reference something

std::string my_string = "Hello world!"; // Regular string
std::string & ref_string = my_string; // Ok, reference to my_string

std::string my_string_2 = "Hello again, world!"; // Regular string
ref_string = my_string_2; // Cannot re-seat reference. Will copy instead.
```
````



If we go back to our original pointer example, we can see that taking the address
of the reference results in the same address as the pointed-to object.
And, like pointers, the original object can be modified via the reference.

````{tab-set-code} 

```{code-block} cpp
#include <iostream> // for std::cout, std::endl

int main(void)
{
    int j = 1234;
    std::cout << "Value of j: " << j << std::endl;

    int & rj = j; // rj references j
    std::cout << "Value of rj: " << rj << std::endl;

    std::cout << "Address of j: " << &rj << std::endl;
    std::cout << "Address of rj: " << &rj << std::endl;

    // Change j via rj
    rj = 5678;

    std::cout << "Value changed!" << std::endl;
    std::cout << "New Value of j: " << j << std::endl;
    std::cout << "New Value of rj: " << rj << std::endl;

    return 0;
}
```
````


````{tab-set-code} 

```{code-block} output
Value of j: 1234
Value of rj: 1234
Address of j: 0x7fff8727380c
Address of rj: 0x7fff8727380c
Value changed!
New Value of j: 5678
New Value of rj: 5678
```
````


It is not common to use references by themselves, but they are very common
when passing arguments to functions (which we will see in the next lesson).
````{admonition} Key Points
:class: key

- Pointers are variables that point to an area of memory
- Pointers can be used to store homogeneous lists of items
````


## The `const` Keyword

In C/C++, it is possible to mark a variable as constant, such that after
setting, the value cannot be changed. Marking a variable as constant can also
enable some performance improvements, although these are typically very small.
However, they are primarily used to signify intent to other programmers,
and can prevent some mistakes.

To create a constant variable, the keyword `const` is placed before the type.

````{tab-set-code} 

```{code-block} cpp
const double pi = 3.1415; // Constant double
const std::string my_string = "Hello world!"; // Constant string
my_string = "Another string"; // Error - my_string is const!
```
````


Because the constant variable cannot be changed, it must be set at the same
time it is declared. Otherwise, you would never be able to set the value!

````{tab-set-code} 

```{code-block} cpp
const int i = 123; // Declare and set
const int j; // j can never be changed after this, so this is invalid.
```
````


Constant variables can be very useful in some cases. For example, for storing
physical constants or common strings. As we will see, they are most often
used for declaring objects passed to functions as `const`.

Constant references work in a simiar way. Data cannot be changed through a
constant reference.

A constant reference can refer to a constant or non-constant variable.
However, a non-const reference can only refer to a non-constant variable.
Otherwise, we would be able to change constant data just my making a reference
to it.

``````{admonition} Exercise
:class: exercise

What happens when you try to make a non-const reference to const data?

`````{tab-set-code} 

````{code-block} cpp
int main(void)
{
    const double d = 1.123;
    double & d2 = d;
    return 0;
}
````
`````


````{admonition} Solution
:class: dropdown solution
A compiler error, of course!

```{code-block} output
test.cpp: In function ‘int main()’:
test.cpp:4:19: error: binding reference of type ‘double&’ to ‘const double’ discards qualifiers
    4 |     double & d2 = d;
      |    
```
In C++, the `const` keyword is called a *qualifiers*. The compiler is telling
you that making the reference discards the `const` qualifier. `volitile` is another qualifier, however
it is very rarely used in scientific computing.
````
``````
