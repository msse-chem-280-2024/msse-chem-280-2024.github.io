---
title: "Namespaces"
teaching: 20
exercises: 5
questions:
- "How can we group functions together under a single collection?"
- "How can I prevent collisions with functions having the same name in other libraries?"
objectives:
- "Learn about grouping functions and objects with namespaces"
keypoints:
- "Namespaces allow programmers to group all their functions under a single name"
---

> ## Prerequisites
> - Knowledge of basic C++ functions
{: .prereq}

## Namespace overview

If you are working on a large package, you will often have a large number of
functions and other code that could logically be grouped together. This may
be a top-level group (for your whole package) or even smaller groups within
your package.

Just like in python, where you group your code into modules, you can group
your code into C++ *namespaces*.

There is one important difference between C++ and Python in this respect,
however -- in python, your module names reflect the filename and directory
of those modules. In C++, there is no restriction, and the namespace is
often split over many files and directories.

## Creating namespaces

You can create a namespace with the `namespace` keyword. The following code creates
a namespace `my_package` and adds a simple function to it. The function is then
accessed using the *scope resolution operator* (`::`).

~~~
#include <iostream>

namespace my_package {

    void print_string(std::string s)
    {
        std::cout << "String: " << s << std::endl;
    }

} // close namespace my_package


int main(void)
{
    my_package::print_string("Hello, world!");

    return 0;
}
~~~
{: .language-cpp}


Namespaces can be nested as well, and can contain global variables.

~~~
#include <iostream>

namespace my_package {

    const double pi = 3.1415;

    namespace printing {

        void print_string(std::string s)
        {
            std::cout << "String: " << s << std::endl;
        }

    } // close namespace functions
} // close namespace my_package

int main(void)
{
    my_package::printing::print_string("Hello, world!");
    std::cout << "Pi: " << my_package::pi << std::endl;

    return 0;
}
~~~
{: .language-cpp}

In general, namespaces are a good idea, particularly if you are writing a library that
will be used by other people. This makes it clear where each function is coming from,
as well as prevents collisions with functions that may have the same name.

## Importing all names from a namespace

It can be tedious to have to always prefix functions with the namespace, especially if you are using
many of them all the time. You can tell the compiler to always search a particular namespace
for a function with the `using` keyword. This keyword can be used at the file level or even
at the function level.

One common one is to always use `std` without needing to prefix with `std::`.

~~~
#include <iostream>

// Search std for functions/objects 
using namespace std; 

namespace my_package {

    const double pi = 3.1415;

    namespace printing {

        void print_string(string s)
        {
            cout << "String: " << s << endl;
        }

    } // close namespace functions
} // close namespace my_package

int main(void)
{
    using namespace my_package;

    // Still need to use the inner namespace
    printing::print_string("Hello, world!");
    cout << "Pi: " << my_package::pi << ::endl;

    return 0;
}
~~~
{: .language-cpp}

Importing things this way is analogous to using `from package import *` in python.

> ## Importing everything from a namespace
>
> Do you think it is a good idea to import everything from a namespace? When should it be done?
> Is it cleaner to do it, or does it make code more confusing?
{: .discussion}
