---
title: "Common data types"
teaching: 30
exercises: 15
start: true
questions:
- "What are the common, built-in data types in C++pointers and references in C++"
- "When should I use each data type?"
objectives:
- "Learn about the built-in data types in C++, and what they are used for"
keypoints:
- "C++ has several integral data types, with different sizes and use cases"
- "C++ also has several different floating point types"
---

> ## Prerequisites
> - Understanding of basic C++ syntax
> - Able to compile and run simple C++ programs
{: .prereq}

## `sizeof` operator

C/C++ has an operator `sizeof` that can apply to a data type or variable.
This returns the size of the object in **bytes**. You can use this
to see how much memory a particular variable or data type holds.

~~~
#include <iostream>

int main(void)
{
    double number = 1.234;
    std::cout << "int: " << sizeof(int) << std::endl;
    std::cout << "double: " << sizeof(number) << std::endl;
    return 0;
}

~~~
{: .language-cpp}

~~~
int: 4
double: 8
~~~
{: .output}

The output is technically dependent on your operating system and architecture, although 4-byte `int` is
very common, and 8-byte (64-bit) `double` is farily universal.

> ## Exercise
>
> What is the size of a `bool`?
>
>> ## Solution
>>
>> A `bool` is usually 1 bytes (8 bits), even though it only really needs 1 bit. This is because
>> A byte is generally the smallest quantity a program works with.
> {: .solution}
{: .challenge}

## Integral data types

C++ has several integer data types

| C++ Type   | Typical size (bytes) | Typical range                               |
| ---------- | -------------------- | ------------------------------------------- |
| char       | 1                    | [-128, 127]                                 | 
| short      | 2                    | [-32768, 32767]                             |
| int        | 4                    | [-2147483648, 2147483647]                   |
| long       | 8                    | [-9223372036854775808, 9223372036854775807] |
| long long  | 8                    | [-9223372036854775808, 9223372036854775807] |

These types can hold both positive and negative values. We can modify this behavior, though,
with the `unsigned` keyword. This increases the range on the positive side, at the expense
of not being able to hold negative values.

| C++ Type            | Typical size (bytes) | Typical range               |
| ------------------- | -------------------- | --------------------------- |
| unsigned char       | 1                    | [0, 255]                    | 
| unsigned short      | 2                    | [0, 65536]                  |
| unsigned int        | 4                    | [0, 4294967295]             |
| unsigned long       | 8                    | [0, 18446744073709551615]   |
| unsigned long long  | 8                    | [0, 18446744073709551615]   |

`unsigned char` is often used to represent a raw byte.

In general, signed data types are preferred over unsigned, and `int` is typically
used as the "general purpose" integer number, with the others being used in
specialized cases.


> ## Exercise
>
> What happens if you assign a negative value to an `unsigned int`?
>
>> ## Solution
>>
>> The value of the `unsigned int` becomes a large positive number.
>> The negative number *wraps around* to become positive.
> {: .solution}
{: .challenge}


## Floating point data types

C++ has a couple of floating-point (decimal) types as well.

| C++ Type     | Typical size (bytes) | Digits of Precision  | Typical range                 |
| ------------ | -------------------- | -------------------- | ----------------------------- |
| float        | 4                    | 6-9                  | [1.17549e-38, 3.40282e+38]    |
| double       | 8                    | 15-17                | [2.22507e-308, 1.79769e+308]  |
| long double  | 16                   | 33-36 (see below)    | [3.3621e-4932, 1.18973e+4932] |

There are no `unsigned` floating point types.

`long double` may or may not really have 16-bytes (128-bits) of precision, and is rarely used.
CPUs generally understand 32-bit floats and 64-bit doubles much better, and these are very
efficient.


## Variable initialization

It is generally good practice to initialize variables to a set value. In general,
the value of a variable is not set by the compiler, and may be any value that
happens to be in the memory that that variable has.

> ## Exercise
>
> Print an uninitialized double. What is the value? Does that value change
> each time that program runs?
>
>> ## Solution
>>
>> ~~~
>>#include <iostream>
>>
>>int main(void)
>>{
>>    double d;
>>    std::cout << d << std::endl;
>>    return 0;
>>}
>>~~~
>>{: .language-cpp}
>>
>> The value printed is random, and changes each time you run the program.
> {: .solution}
{: .challenge}


## Compiler warnings

Compilers have settings to warn you of dangerous behavior like the use of
unitialized variables. We can enable these warnings with the GCC and Clang
compilers with `-Wall`.

> ## Exercise
>
> Compile the code from the previous exercise (with the unitialized variable)
> using `-Wall`. What does the compiler output?
{: .challenge}

It is generally good practice to compile with `-Wall` (or other flags,
depending on the compiler) such that common mistakes (but not necessarily
errors) are caught by the compiler.
