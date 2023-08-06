---
title: "Documentation"
teaching: 30
exercises: 5
questions:
- TODO
objectives:
- TODO
keypoints:
- TODO
---

> ## Prerequisites
> - TODO
{: .prereq}

## Doxygen-style Documentation

In Python, documentation is almost always generated using Sphinx. C++
in general uses a program called [Doxygen](https://www.doxygen.nl/index.html).
While the syntax is different than in Python, conceptually it is similar.

In typical C/C++ fashion, there are multiple ways to add documentation. We will
be showing you one way, however note that there can be different, equivalent
syntaxes.


### Where to place documentation

As shown in a previous section, C++ projects typically span multiple source
and header files. So where should the documentation go - at the function definition
in a source file or the declaration in the header file? There are pros and cons to each

Adding to the header file
  * **Pro**: Other developers usually only care about the interface shown header files
  * **Pro**: Header files are distributed with the binaries
  * **Con**: Changing documentation requires lots of recompilation
  * **Con**: Not all functions exist in header files

Adding to the source file
  * **Pro**: Closest to the actual code, so developers of the package can keep changes in behavior in sync with documentation more easily
  * **Pro**: Only requires recompilation of that source file if documentation changes
  * **Pro**: Sometimes functions have no entry in header files (internal functions)
  * **Con**: Not distributed with binary packages
  * **Con**: Developers may have to hunt for the documentation in the code. Header files tend to be all in one place.

Either way you choose, the main thing is to be consistent. For our purposes, we will be adding documentation in header files.

## What to document

What kind of things should we include in the documentation? As a general idea, you should rely on past experience
and think about what you usually want to see in documentation in packages you use.

Some common things to document:

  * A short description
  * A longer description
  * Descriptions of arguments (see below for how this is easier in C++)
  * Description of the return type
  * Exceptions and error conditions
  * Edge cases
    * What are some common errors
  * Implementation details relevant to the caller
    * Scaling?
    * Threading?

What to add, and more importantly what *not* to add, requires experience
and intuition. However, like code, you can always change it later.

Keep in mind, though, that as a general rule, having zero documentation is
better than having incorrect and/or outdated documentation. So always try
to keep your documentation up-to-date.


## Basic syntax

The basic syntax for Doxygen is as follows

1. Documentation goes before the function definition or declaration
2. There is a special comment character
3. Parameters and return descriptions are specfied with \param
4. Doxygen extracts types for you (no need to specify them like in Python)

Below is an example of our `convert_temperature` function, now fully documented.

~~~
// temperature.hpp

#include <vector>

/*! \brief Converts a vector of temperatures from Celsius to Fahrenheit
 *
 * Given a vector of temperatures in Celsius, convertes each element of the vector
 * to Fahrenheit.
 *
 * \param [in] temperatures Temperatures (in Celsius) to convert
 * \return All elements of \p temperatures converted to Fahrenheit
 */
std::vector<double> convert_temperature(const std::vector<double> & temperatures);
~~~
{: .language-cpp}

Let's go over this in more detail.

Unlike Python, the comment goes before the function, not inside the function. It
is started with `/*!`, which signals to Doxygen that the comment is documentation.
Not that the `!` is the main difference, and without it `/*` is just interpreted
as a regular C-style comment.

The `\brief` command gives the brief description. After the newline, everything is part of
the *detailed* description.

Parameters are denoted by `\param`. After that is a tag for how that parameter
is used - `[in]` means input, `[out]` means output, and `[inout]` means both.
These are similar to the Fortran tags for parameters. Things passed in by
copy or constant reference are `[in]`, and thing passed in by non-constant reference
are usually `[inout]`. Unlike Python, you don't have to specify the type in the
documentation - that information is already there in the code!

Parameters can be referenced within the documentation by `\p`.

The documentation comment is closed by `*/` like a normal C-style comment.
