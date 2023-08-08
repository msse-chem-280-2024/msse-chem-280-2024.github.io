# Class Warm Up

Today, for the class warm-up, we will be learning about and applying the [Programming Design Recipe](https://course.ccs.neu.edu/cs5010sp15/recipe.html). 
This is a formalized strategy and design process for writing a function. 
There is a more detailed specification, but we present a condensed version here.

Some text is taken directly and adapted from the reference.

As you read through the design recipe, apply it to the following problems for both Python and C++:

1. Calculation of number density given a number of molecules an a box length (assume cubic box).
2. Calculation of the solute's contribution to final volume in a dilution. Given a starting concentration $C_{1}$ and volume of solution $V_{1}$, and knowing the final concentration $C_2$ after adding solvent, calculate the volume $V_2$ that represents the solute's contribution to the final solution. The relationship between these quantities is represented by the equation:
$ C_1 \times V_1 = C_2 \times V_2 $

As you work through the Design Recipe steps, record your answers in the [class Google Doc](https://docs.google.com/document/d/1Bs5K45Y9uPrfE1XoGYgawg4_oA9DGKwAGTD_-KCbe0Y/edit?usp=sharing) 


## Summary of Recipe Steps

1. Data Design
2. Function Specification
3. Function Implementation
4. Testing
5. Program Review

## Step 1 - Data Design

All programs must process and compute with facts from the real world. We call these facts information. For example,

- One program may process road and location information to compute driving directions.
- Another may process player input information to compute the current state of a game.
- Another may process information about files on a disk to create a user interface.

To do this processing, however, programs must first encode information from the real world as data representations in the computer. The Data Design step determines these data representations.

**This is the most critical step of the design recipe. It dictates all subsequent steps.**
Deciding "how" to represent information on a computer can sometimes be very difficult and takes practice!
Over time, you will develop an intuition for this.
Sometimes data representations of real-world information as data will seem abstract.
Data design can involve creating representations that may not directly resemble the real-world objects or concepts being modeled.

### Step 1.1 - Data Definitions

To create a data representation for a piece of information, we write *data definitions*.

A *data definition* is a written statement that defines a piece of data. 
In simpler terms, it helps us describe what the data should look like and how it is structured. 

#### Why Data Design Matters

Data design is essential because it lays the foundation for writing functions. 
By defining data clearly, we can better understand what inputs our functions need and what outputs they should produce. 
This understanding is crucial for writing effective and reliable programs.

#### Examples of Data Definitions

Let's consider a few examples of data definitions:

1. **3D Coordinate in Python**:
   - A coordinate is a *list* with format [x, y, z].
   - An x value is a floating-point number.
   - A y value is a floating-point number.
   - A z value is a floating-point number.

2. **A Rectangle**:
   - A rectangle is represented by a *length* and *width*.
   - A width is a floating point number (Python) or a double (C++).
   - A height is a floating point number or a double (C++).

3. **Person's Information**:
   - A person's information is a *dictionary* with keys: "name", "age", "email".
   - The name is a *string*.
   - The age is an integer.
   - The email is a *string*.

Now that we understand the importance of data design and how to create data definitions, we are ready to move on to the next steps in the Programming Design Recipe.

## Step 2 - Function Specification

You will next define the function specification.
This involves deciding the function inputs and signature and writing
function documentation.

In Python a function signature looks like

````{tab-set-code}
```{code-block} python

def function_name(arguments):
    ...
```
````

In C++, a function signature looks like

````{tab-set-code} 

```{code-block} c++
return_type function_name(arguments) {
    ...
}
```
````

### Step 2.1 - Defining Function Inputs

Before writing a function, you need to determine what inputs the function requires to perform its task. 
These inputs are known as function parameters or arguments. 
Think about the data that the function will need to process and how it should be organized.

### Step 2.2 - Writing Function Documentation

Once you have identified the function's inputs and purpose, it is essential to write clear documentation for the function. 
Good documentation explains the function's purpose, its inputs, expected behavior, and the data it returns. 
Documentation is crucial for both your understanding of the function's design and for other programmers who may use your code.

#### Example Function Specification and Documentation

Let's consider an example of a function in C++ that calculates the area of a rectangle:

````{tab-set-code}
```{code-block} python
def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters
    ----------
    length : float 
        The length of the rectangle.
    width : float
        The width of the rectangle.

    Returns
    ---------
    area : float
        The area of the rectangle.
    """
```
````

## Step 3 - Function Implementation

Once you have designed the data and specified your function, the next step is to implement it. 
Function implementation is where you turn the design and specification into actual code that accomplishes the task you set out to perform.

### Step 3.1 - Break the Problem Down

A good practice before writing any code is to break the problem down into smaller tasks or components. 
Think about the sequence of operations that need to be performed and jot them down. 
This will give you a clearer path and can simplify the coding process.

### Step 3.2 - Write the Code

Now that you have a road map, start coding. 
Use the function signature and documentation you wrote in the previous step as a guide. 
Make sure to adhere to the data definitions and respect the expected inputs and outputs.

### Step 3.3 - Add Comments

While coding, it's good practice to add comments explaining complex or non-intuitive parts of your code. This can be beneficial for your future self or other programmers who might work on the code later.

#### Example Function Implementation

Continuing with our rectangle area calculation example:

````{tab-set-code}
```{code-block} python
def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters
    ----------
    length : float 
        The length of the rectangle.
    width : float
        The width of the rectangle.

    Returns
    ---------
    area : float
        The area of the rectangle.
    """
    area = length * width

    return area

```
````

In this example, we've taken the function specification and added the necessary code to compute the rectangle's area. 

With the function now implemented, the next step would be to test it thoroughly to ensure it works as expected.

## Step 4 - Testing (aka "Sanity Checks")

After implementing your function, it's crucial to test it to ensure it behaves as expected. 
Testing can identify errors or discrepancies in your code, allowing you to correct them before using the function in larger programs or deploying it in real-world scenarios.

### Step 4.1 - Write Test Cases

Before running any tests, identify and write down several test cases. These should include:

- **Normal Cases**: These are typical inputs that the function will handle most of the time.
- **Edge Cases**: Inputs that test the boundaries or limits of your function.
- **Error Cases**: Inputs that the function should reject or handle gracefully.

### Step 4.2 - Use Assertions or Print Statements

In languages that support them, assertions can be used to automatically verify if a function's output is as expected.
 Otherwise, you can use print statements to display outputs for manual verification.

### Step 4.3 - Run the Tests

Execute each test case and compare the function's output to your expected result. 
Take note of any discrepancies.

### Step 4.4 - Review and Refine

If a test case fails, analyze why it failed. 
Is there a bug in the function? 
Did you overlook a specific scenario? 
Review the function and refine it as necessary, then retest until all test cases pass.

#### Example Testing for Rectangle Area Function

Using the `calculate_rectangle_area` function from our previous sections:

1. **Normal Case**: 
    - Input: `calculate_rectangle_area(5.0, 10.0)`
    - Expected Output: `50.0`

2. **Edge Case**: 
    - Input: `calculate_rectangle_area(0.0, 10.0)`
    - Expected Output: `0.0`

3. **Error Case**: 
    - While our function doesn't have explicit error handling, think about scenarios that could be problematic, 
    such as negative lengths or widths.

````{tab-set-code}
```{code-block} python
# Tests
result = calculate_rectangle_area(5.0, 10.0)
assert result == 50.0, f"Test 1 Failed: Expected 50.0 but got {result}"

result = calculate_rectangle_area(0.0, 10.0)
assert result == 0.0, f"Test 2 Failed: Expected 0.0 but got {result}"
```
````

It's important to understand that no matter how thorough your tests are, there's always the possibility of undiscovered issues.
Regular testing and refinement are essential to maintaining reliable code.

## Step 5 - Program Review

The final step of the Programming Design Recipe is reviewing your code. 
This process involves revisiting the entire codebase, from data definitions to function implementations, and checking for any discrepancies, possible improvements, or overlooked details. 
Code review is a crucial practice in the professional world, and developing this habit early will benefit you in the long run.

### Step 5.1 - Review for Consistency

Ensure that your data definitions, function specifications, and implementations align with one another. 
Any deviation might lead to unexpected behaviors.

### Step 5.2 - Check for Code Quality

Review the code to ensure it's readable, maintainable, and follows good coding practices. 
Check variable names, function names, and comments to ensure clarity.

### Step 5.3 - Refactor if Necessary

As you review, you might identify parts of the code that could be improved. 
Refactoring involves restructuring existing code without changing its external behavior. 
It's a way to improve the code's design, readability, or reduce complexity.

### Step 5.4 - Peer Review

If possible, have a classmate or colleague review your code. 
They might provide a fresh perspective, notice things you've missed, or offer suggestions for improvement. 
This is a common practice in the software industry and is known to improve code quality significantly.

#### Example Program Review for Rectangle Area Function

1. **Review Data Definitions**: Ensure the function uses the defined data types and adheres to their structure. 
For the rectangle function, we used `float` for both length and width as defined.

2. **Review Function Specification**: Re-read the documentation and ensure it aligns with the function's behavior. 
In our case, the function should take two floating-point numbers and return the computed area.

3. **Check for Quality**: The function is simple and straightforward, but always ensure there's no redundant code, variables have meaningful names, and comments are clear.

4. **Refactor**: While our example function is already concise, always be on the lookout for repetitive patterns or overly complex segments that can be simplified.

5. **Peer Review**: Share the function with a classmate. 
Did they understand its purpose immediately? 
Did they notice any potential issues or have suggestions for improvement?


