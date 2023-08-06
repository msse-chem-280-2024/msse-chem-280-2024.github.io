---
title: "Testing"
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

## The Catch2 package

The Catch2 package [https://github.com/catchorg/Catch2]() is a testing framework
for C++. It provides the ability to call and test functions in a similar manner
to Pytest.

One main benefit of Catch2 is that it is "header only", meaning that you only
have to install or copy header files for use in your project, and do not
have to build a Catch2 library and link against it.

### Obtaining Catch2

The easiest way to get Catch2 is to download its single header file and place
it with the rest of your files.

Download the single file using your favorite method (browser, wget, curl, etc):

[`https://raw.githubusercontent.com/catchorg/Catch2/v2.13.9/single_include/catch2/catch.hpp`](https://raw.githubusercontent.com/catchorg/Catch2/v2.13.9/single_include/catch2/catch.hpp`)


## Writing simple tests

To write tests with Catch2, we will be creating a new source file, `test.cpp`.
This file will be compiled by itself, and **not with your already-exiting main file**.

This file will contain `#define CATCH_CONFIG_MAIN` at the top, which will automatically
create a `main` function in this source file.

~~~
#define CATCH_CONFIG_MAIN
#include "catch.hpp"
#include "temperature.hpp"

double convert_temperature(double t)
{
    return t*1.8+32.0;
}

TEST_CASE("Temperature functions", "[temperature]")
{
    REQUIRE(convert_temperature(-40.0) == -40.0);
}


~~~
{: .language-cpp}


Now we will compile our new source file and the `temperature.cpp` file together.

~~~
g++ test.cpp temperature.cpp -o test_temperature
~~~
{: .language-bash}

The `test_temperature` executable now has lots of command line arguments related
to testing. Try running `./test_temperature -h` and see!

To run your tests, just run `./test_temperature`.

~~~
===============================================================================
All tests passed (1 assertion in 1 test case)
~~~
{: .output}

