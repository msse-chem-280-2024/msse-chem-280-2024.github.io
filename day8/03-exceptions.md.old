---
title: "Exceptions"
teaching: 45
exercises: 10
questions:
- "How do we handle major errors in C++?"
- "How do exceptions differ from python?"
objectives:
- "Learn about throwing and catching exception in C++"
keypoints:
- "Exceptions stop execution and go back up the call stack until they are caught"
- "Exceptions are the main way to handle major errors in C++"
---

> ## Prerequisites
> - Knowledge of basic C++ functions
{: .prereq}

## Exception overview

Like python, C++ handles errors using exceptions. 


## Throwing exceptions

If we take our simple temperature conversion example, lets throw an exception
if the temperature is below absolute zero and therefore unphysical.

First, we need to include the `stdexcept` component of the standard library.
This will allow us to use the `runtime_error` exception.

~~~
#include <iostream>
#include <stdexcept>

const double absolute_zero = -459.67; // in Fahrenheit

double convert_F_to_C(double temperature)
{
    if(temperature < absolute_zero)
    {
        throw std::runtime_error("Temperature must be above absolute zero!");
    }

    return (temperature - 32.0)*(5.0/9.0);
}

int main(void)
{
    double temperature = -999.0;

    temperature = convert_F_to_C(temperature);

    std::cout << "Temperature is " << temperature << std::endl;
    
    return 0;
}
~~~
{: .language-cpp}

~~~
terminate called after throwing an instance of 'std::runtime_error'
  what():  Temperature must be above absolute zero!
Aborted (core dumped)
~~~
{: .output}

When run, this code will terminate with an exception, signifying that
something went wrong and the program could not continue.


## Catching exceptions

Exceptions can also be *caught* and appropriate handling of the error can happen.
Often this means that the error is logged appropriately, and the program may then continue
if the error was not serious.

If an exception is not caught, the result is program termination, as in the above example.

Exceptions in the standard library (like `runtime_error`) have a `.what()` function that returns
a string describing the error. In `runtime_error`, this is the string passed to it when it is thrown.

Lets catch the exception, and write some better output to the terminal

~~~
#include <iostream>
#include <stdexcept>

const double absolute_zero = -459.67; // in Fahrenheit

double convert_F_to_C(double temperature)
{
    if(temperature < absolute_zero)
    {   
        throw std::runtime_error("Temperature must be above absolute zero!");
    }   

    return (temperature - 32.0)*(5.0/9.0);
}

int main(void)
{
    double temperature = -999.0;

    try {
        temperature = convert_F_to_C(-999.0);
    }
    catch(std::exception & ex)
    {
        std::cout << "Caught an exception! Could not convert temperature = " << temperature << std::endl;
        std::cout << "Exception: " << ex.what() << std::endl;
        return 1
    }

    std::cout << "Temperature is " << temperature << std::endl;
        
    return 0;
}
~~~
{: .language-cpp}

~~~
Caught an exception! Could not convert temperature = -999
Exception: Temperature must be above absolute zero!
Temperature is -999
~~~
{: .output}

Now, the error printed to the terminal is a bit better for the end user.

When we catch an exception, we give it the type of exception to
catch. Typically, all exceptions (including exceptions in the standard library)
derive from `std::exception`, so catching `std::exception` will catch all
exceptions. You can narrow this if needed to only catch specific exceptions,
or use `(...)` to catch absolutely everything.

Typically, exceptions are caught by reference to avoid copying. You can also
catch by `const` reference if you would like.

Also note that we `return 1` inside the exception handler. This is a
signal to the operating system or parent process that this process exited
abnormally. That is, `return 0` from `main` signifies a successful run of
the process, while returning non-zero signifies an error.
