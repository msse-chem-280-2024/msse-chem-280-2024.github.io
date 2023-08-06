---
title: "Arrays, Pointers, Memory, and Vectors"
teaching: 120
exercises: 30
questions:
- What are pointers and references in C++
- Why/when should I use a pointer or reference?
- Pitfalls of using pointer
objectives:
- To learn about pointers
- To learn about different ways of representing lists/arrays of data
keypoints:
- Pointers are variables that point to an area of memory
- Pointers can be used to store homogeneous lists of items
---

> ## Prerequisites
> - Understanding of basic C++ syntax
> - Able to compile and run simple C++ programs
{: .prereq}

## Arrays

C++ has support for "old-fashioned", C-style arrays. In this case, the sizes
of these arrays must be known at compile time, and therefore are a constant
size. A good example of this would be a 3d point, which would be 3 double-precision
floating point numbers.

Arrays in C++, like python, are zero-indexed.

Since you know the size (at compile time), looping over all the elements of the
array can be done with a `for` loop; from the loop, you fill or access the array.

~~~
#include <iostream> // for std::cout, std::endl

int main(void)
{
    // Create an array of 10 integers
    int arr[10];

    // Fill the array
    for(int i = 0; i < 10; i++)
    {
        // Set the i-th value to 2*i
        arr[i] = 2*i;
    }

    // Print out the elements of the array (with the index)
    for(int i = 0; i < 10; i++)
    {
        std::cout << "Element " << i << ": " << arr[i] << std::endl;
    }
    
    return 0;
}
~~~
{: .language-cpp}

~~~
Element 0: 0
Element 1: 2
Element 2: 4
Element 3: 6
Element 4: 8
Element 5: 10
Element 6: 12
Element 7: 14
Element 8: 16
Element 9: 18
~~~
{: .output}


C and C++ provide additional syntax for initializing the array - just assign
the array to the values you want to store in curly braces. In this case,
the size of the array can be omitted (`int arr[] = ...`); however I generally
find it good practice to keep it as it will allow the compiler to double-check
the given size with how many elements were given in the initialization list.

~~~
#include <iostream> // for std::cout, std::endl

int main(void)
{
    int arr[10] = { 3, 5, 7, 9, 11, 13, 15, 17, 19, 21 };

    for(int i = 0; i < 10; i++)
    {
        std::cout << "Element " << i << ": " << arr[i] << std::endl;
    }
    
    return 0;
}
~~~
{: .language-cpp}

~~~
Element 0: 3
Element 1: 5
Element 2: 7
Element 3: 9
Element 4: 11
Element 5: 13
Element 6: 15
Element 7: 17
Element 8: 19
Element 9: 21
~~~
{: .output}

> ## Exercise
>
> What happens if you specify more than 10 elements in the braces? What happens if you specify fewer?
> Try compiling it and see
>
>> ## Solution
>>
>> Specifying more will result in a compiler error. Specifying too few will only initialize the elements
>> given.
> {: .solution}
{: .challenge}


> ## Overflow
> What happens when you try to write beyond the bounds of the array? That is called a
> *buffer overflow* and depending on many factors can result in a crash or random behavior.
> Attempting to read out of bounds may also result in a crash, or you may just read garbage.
{: .callout}


## Addresses

> ## A word of Warning
> Pointer mismanagement is a common source of bugs in C and often in C++.
> These bugs often lead to crashes (if you are lucky) but can also lead to silent,
> hard-to-debug issues or security vulnerabilites.
{: .callout}

In C/C++, variables you declare have a defined amount of memory and exist at
a particular location in memory. When accessing this variable, the compiler
generates (binary) code to lookup the data in that location.

We can get the location of a variable using the `&` operator. It is rarely
needed to print this information, but can be used in debugging tricky bugs.

Create a new file and try out the following code.

~~~
#include <iostream> // for std::cout, std::endl

int main(void)
{
    int j = 1234;
    std::cout << "Address of j: " << &j << std::endl;
    return 0;
}
~~~
{: .language-cpp}

When running, I get the following output. The address will likely be different
on your computer, and will change when re-running.

~~~
Address of j: 0x7ffd0046f874
~~~
{: .output}

The address of the pointer is given in hexadecimal, but its exact value is
very rarely important.


## Pointers

Now that we know how to get the address of a variable, we can then store
that address in another variable. Doing so gives us a *pointer* to the same
memory address (starting byte) as the original variable.

To do so, we must define the type of the new variable to be a pointer
type. This is denoted with a *star* (`*`) that comes after the pointed-to type.

~~~
#include <iostream> // for std::cout, std::endl

int main(void)
{
    int j = 1234;
    std::cout << "Address of j: " << &j << std::endl;
    std::cout << "Value of j: " << j << std::endl;

    int * pj = &j; // pj points to address of j
    std::cout << "Value of pj: " << pj << std::endl;
    return 0;
}
~~~
{: .language-cpp}

~~~
Address of j: 0x7fff9eebe4ec
Value of j: 1234
Value of pj: 0x7fff9eebe4ec
~~~
{: .output}

You will notice that the value of the pointer `pj` is the address that
we assigned to it.  So how can we retrieve the actual value stored in the
pointed-to memory? By again using *star* (in this case, called the *pointer
dereferencing operator*)

~~~
#include <iostream> // for std::cout, std::endl

int main(void)
{
    int j = 1234;
    std::cout << "Address of j: " << &j << std::endl;
    std::cout << "Value of j: " << j << std::endl;

    int * pj = &j; // pi points to address of j
    std::cout << "Value of pj: " << pj << std::endl;
    std::cout << "Value of *pj: " << *pj << std::endl;
    return 0;
}
~~~
{: .language-cpp}

~~~
Address of j: 0x7ffd8e66f70c 
Value of j: 1234
Value of pj: 0x7ffd8e66f70c
Value of *pj: 1234
~~~
{: .output}

So now we've shown that we can access the same memory location, but can we change the value?

> ## Exercise
>
> Change the main function to modify the value of j through pointer pj.
>
>> ## Solution
>>
>> We can assign data directly to `*pj`
>>
>>~~~
>>#include <iostream> // for std::cout, std::endl
>>
>>int main(void)
>>{
>>    int j = 1234;
>>    std::cout << "Value of j: " << j << std::endl;
>>
>>    int * pj = &j; // pj points to address of j
>>    std::cout << "Value of *pj: " << *pj << std::endl;
>>
>>    // Change j via pj
>>    *pj = 5678;
>>
>>    std::cout << "Value changed!" << std::endl;
>>    std::cout << "New Value of j: " << j << std::endl;
>>    std::cout << "New Value of *pj: " << *pj << std::endl;
>>    
>>    return 0;
>>}
>>~~~
>>{: .language-cpp}
>>
>>
>>~~~
>>Value of j: 1234
>>Value of *pj: 1234
>>Value changed!
>>New Value of j: 5678
>>New Value of *pj: 5678
>>~~~
>>{: .output}
> {: .solution}
{: .challenge}


> ## Exercise
>
> What is the size of a pointer (that is, how many bytes)?
> Does it change with the type that is being pointed to?
> What does that mean about the amount of memory that you can
> access from your program?
>
>> ## Solution
>>
>> Pointers are almost always 8 bytes (64-bits) nowadays, so they can access ~2^64 bytes of memory,
>> since a pointer points to a byte of memory. Before, with 32-bit machines, you could only access
>> ~2^32 = 4 GB of memory.
> {: .solution}
{: .challenge}

### Null Pointers

All pointers can be set to a special value - `nullptr`. In pre-c++11
(and C), `NULL` can also be used. This means that the pointer points to
nothing. Attempting to dereference a null pointer should result in a runtime
error. It is often used as a signal that the pointer was not set to anything.

If you are not setting a pointer to point to existing data, or to memory
allocated via `new` (see below), it is good practice to set it to `nullptr`
instead. If you don't, the pointer might point to a random area of memory.


> ## Manual addressing of pointers
> Can you manually set the address of a pointer via something like `int * j = 0x13579bdf;`? Yes.
> However, in scientific computing, this would be extremely rarely done, if ever.
> It does have its uses with embedded platforms, microcontrollers, etc. You will likely
> never need to do this in your entire scientific career.
{: .callout}


## Dynamic memory allocation

Think about the array examples. We must know how many elements exist at
compile time. But what if we don't?

For example, lets say we want to read in the coordinates of a molecule. How
big should that array be? One solution is to make a very large array and
then only use part of it. This not only results in inefficient use of memory,
but also can cause many headaches down the road when people try to run using
larger molecules.

The solution is to use *dynamic memory allocation*. In C++, this is done with
the `new` keyword, which returns (you guessed it) a pointer! This points to
the newly-allocated memory that is the number of elements you requested.

If you allocate memory with `new`, you must also *deallocate* it with
`delete`. Doing this tells the operating system that you are done using it
and allows it to be used by other programs.

If you fail to deallocate/free the memory, you will have a memory leak. When
your program ends, the operating system will still be able to free any memory
that you did not. However, if your program is long-lived (ie, a very long
simulation), memory usage can steadily increase and maybe even trigger an OOM
(out-of-memory) error in the operating system, which will kill your process
(best-case scenario) or kill someone elses (worst-case).

~~~
#include <iostream> // for std::cout, std::endl

int main(void)
{
    // Would come from somewhere like a function argument
    int n_doubles = 16;

    // Store the result of new in a pointer
    // Note that the type of the pointer and the type
    // passed to 'new' must match
    double * data = new double[n_doubles];

    // Loop over it like before
    for(int i = 0; i < n_doubles; i++)
    {
        data[i] = 3.1415 * i;
    }
    
    for(int i = 0; i < n_doubles; i++)
    {
        std::cout << "Element " << i << ": " << data[i] << std::endl;
    }

    // When done, free it
    delete [] data; 
    
    return 0;
}
~~~
{: .language-cpp}

Note the `[]` given to the delete operator. That tells delete to expect to be deleting
an array. You can allocate single objects (ie, `double * data = new double;`) in which
case you do not need the `[]`. This is less common in scientific computing, but still
occassionally needed.


## A better way - std::vector

Dynamic-sized, resizable arrays of data are commonly needed. Python has a
`list` which fits this idea, for example. If you need a dynamically-sized
array of data that behaves like a `list` in Python, then you can use
`std::vector` in C++. A `std::vector` is an array that can be added to and
resized just like a `list`, while the memory management shown above is all
handled automatically. In general, I recommend using `std::vector` rather
than pointers and `new`, as it is much easier to deal with and comes with
nice features, while the overhead in almost all cases is negligible.

The big difference between C++ `vector` and Python `list` is that a C++
`vector` is *homogeneous* - that is, it can only hold data of a single
specified type. For example, you cannot add a string to a `vector`
of integers. That example is possible in python, where `list`s are
*heterogeneous*.

Another difference is that C++ does not support the slicing syntax that Python has (with `:`).

To use `std::vector`, we must add `#include <vector>` at the top of our file.

To declare a `std::vector`, we need to put the type in angled
brackets. For example, a `std::vector` of `double` would be declared as
`std::vector<double>`.

Then, functions can be used to modify the vector, similar to lists in python

| `std::vector` function | Python `list` function | Description                                          |
| ---------------------- | ---------------------- | ---------------------------------------------------- |
| `[]` operator          | (none)                 | Access an element at an index (no bounds check)      |
| `.at()`                | `[]` operator          | Access an element at an index (with bounds checking) |
| `.push_back(x)`        | `.append(x)`           | Add an element to the end                            |
| `.pop_back()`          | `.pop()`               | Remove & Return the last element                     |
| `.size()`              | `len(list)`            | Get the number of elements in the list/vector        |

Consider the examples in the previous section. We can rewrite that to use a
`std::vector` with the following change

~~~
#include <iostream> // for std::cout, std::endl
#include <vector>   // for std::vector


int main(void)
{
    int memsize = 16;

    // A dynamic array of double
    std::vector<double> data;

    for(int i = 0; i < memsize; i++)
    {
        data.push_back(3.1415 * i);
    }

    for(int i = 0; i < data.size(); i++)
    {
        std::cout << "Element " << i << ": " << data[i] << std::endl;
    }

    // Memory is deleted automatically! No need to delete/deallocate
    
    return 0;
}
~~~
{: .language-cpp}

`std::vector` also supports construction with a list of objects like the C-style array
does (`std::vector<double> data = { 1.0, 2.0, 3.0 };`)


## Safely accessing elements of a vector

An `std::vector` has an `.at()` function which takes an index. This is interchangeable with
using square brackets `[]`, except the `.at()` function will cause a runtime error if the index
is beyond the bounds of the vector.

~~~
#include <iostream> // for std::cout, std::endl
#include <vector>   // for std::vector


int main(void)
{
    int memsize = 16;

    // A dynamic array of double
    std::vector<double> data;

    for(int i = 0; i < memsize; i++)
    {
        data.push_back(3.1415 * i);
    }

    std::cout << "Element 100: " << data.at(100) << std::endl;

    return 0;
}
~~~
{: .language-cpp}


~~~
terminate called after throwing an instance of 'std::out_of_range'
  what():  vector::_M_range_check: __n (which is 100) >= this->size() (which is 16)
Aborted (core dumped)
~~~
{: .output}


## std::array

The C++ standard library also has a replacement for C-style, fixed-sized arrays (like `int arr[5]`).
It is called `std::array` and takes both the type and constant size between the angled brackets
(as opposed to just specifying the type in `std::vector`).

This is useful, for example, for 3d points (x,y,z for a molecule).

~~~
#include <iostream> // for std::cout, std::endl
#include <vector>   // for std::vector


int main(void)
{
    int memsize = 16;

    // A dynamic array of double
    std::vector<double> data;

    for(int i = 0; i < memsize; i++)
    {
        data.push_back(3.1415 * i);
    }

    for(int i = 0; i < data.size(); i++)
    {
        std::cout << "Element " << i << ": " << data[i] << std::endl;
    }

    // Memory is deleted automatically! No need to delete/deallocate
    
    return 0;
}
~~~
{: .language-cpp}

What are the benefits of using `std::array` over C-style arrays? `std::array`
contains functions like `.at`, which will do bounds checking. But perhaps the
most important aspect is that copying `std::array` (for example, when passing to
functions) is much more clearer than C-style arrays, which can be very tricky.

~~~
int main(void)
{
    int c_arr1[5] = {1, 2, 3, 4, 5}; 
    int c_arr2[5] = {6, 7, 8, 9,10};

    // ERROR!
    c_arr2 = c_arr1;
}
~~~
{: .language-cpp}


~~~
#include <iostream>
#include <array>


int main(void)
{
    std::array<int, 5> c_arr1 = {1, 2, 3, 4, 5};
    std::array<int, 5> c_arr2 = {6, 7, 8, 9, 10};

    // OK with C++ Standard library
    c_arr2 = c_arr1;

    for(int i = 0; i < 5; i++)
    {
        std::cout << "c_arr1[" << i << "] = " << c_arr1[i] << std::endl;
        std::cout << "c_arr2[" << i << "] = " << c_arr2[i] << std::endl;
    }

    return 0;
}
~~~
{: .language-cpp}

In general, `std::array` should be preferred over C-style arrays.

> ## Exercise
>
> How would you specify an `std::vector` of 3D points?
>
>> ## Solution
>>
>> `std::vector<std::array<double, 3>>`
> {: .solution}
{: .challenge}


## Typedefs

The solution for the previous exercise shows that types can become cumbersome
in C++. Fortunately, C++ defines a way to make types a little more manageable
by allowing the programmer to give them a more descriptive name. This
is done by the `typedef` keyword.

~~~
typedef std::array<double, 3> AtomCoord;
typedef std::vector<AtomCoord> Coordinates;
~~~
{: .language-cpp}

The types `AtomCoord` and `Coordinates` can now be used.

~~~
AtomCoord coord1 = {1.0, 2.0, 3.0};
Coordinates coords;
coords.push_back(coord1);
~~~
{: .language-cpp}


## References

While pointers are inherited from the C language, C++ introduces a new but
similar concept - a *reference*.  References are similar to pointers
with a few key differences

1. References must be set to reference an existing object
1. References cannot be NULL/nullptr
1. Once set, references cannot be *re-seated* (made to reference something else)
1. The star operator is not required to dereference a reference

References are created by using `&` with the type. For example,

~~~
std::string my_string = "Hello world!"; // Regular string
std::string & ref_string = my_string; // Reference to my_string
~~~
{: .language-cpp}

However, given the differences listed above

~~~
std::string & empty_ref; // not valid - must reference something

std::string my_string = "Hello world!"; // Regular string
std::string & ref_string = my_string; // Ok, reference to my_string

std::string my_string_2 = "Hello again, world!"; // Regular string
ref_string = my_string_2; // Cannot re-seat reference. Will copy instead.
~~~
{: .language-cpp}


If we go back to our original pointer example, we can see that taking the address
of the reference results in the same address as the pointed-to object.
And, like pointers, the original object can be modified via the reference.

~~~
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
~~~
{: .language-cpp}

~~~
Value of j: 1234
Value of rj: 1234
Address of j: 0x7fff8727380c
Address of rj: 0x7fff8727380c
Value changed!
New Value of j: 5678
New Value of rj: 5678
~~~
{: .output}

It is not common to use references by themselves, but they are very common
when passing arguments to functions (which we will see in the next lesson).
