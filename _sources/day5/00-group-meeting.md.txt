# Class Warm Up

To start class, take the Warm Up Quiz under Day 5 on bCourses.

After taking the quiz, please take the mid-course survey available on BCourses under the Day 5 module.

## Activity: Debugging 

For this next session, you will spend some time debugging as a group.

When you are writing Python code, you will encounter two types of errors - (1) Exceptions (errors that cause program to halt) (2) Code errors - logical mistakes or typos that cause your code to be incorrect.

### Debugging Exceptions

Consider the following code example:

```python
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

data = [10, 20, 30, 40, 50]
print("Average of data:", calculate_average(data))

empty_data = []
print("Average of empty_data:", calculate_average(empty_data))
```

Running this in a Jupyter notebook will result in a message similar to the following:

```error
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
File ~/my_code.py:11
      8 print("Average of data:", calculate_average(data))
     10 empty_data = []
---> 11 print("Average of empty_data:", calculate_average(empty_data))

File ~/my_code.py:4, in calculate_average(numbers)
      2 total = sum(numbers)
      3 count = len(numbers)
----> 4 average = total / count
      5 return average

ZeroDivisionError: division by zero
```

### How to Read a Python Error Message

When your Python code encounters an error, Python generates an error message (often called a "traceback") that can help you figure out what went wrong. 

When reading a Python error message, you should start at the bottom of the message to determine what the problem is and the line of code. In the example above, the first line we should look at is

```error
ZeroDivisionError: division by zero
```

This tells us that a division by zero was attempted in our code. We now have to figure out where and why.

Going up from this first line, we see what is called the "traceback". The traceback is the sequence of commands taht led to this error. 

Let's break down the traceback from the error message:

```error
File ~/my_code.py:11
      8 print("Average of data:", calculate_average(data))
     10 empty_data = []
---> 11 print("Average of empty_data:", calculate_average(empty_data))
```

This part of the traceback tells you:

* File: The error occurred in the file named my_code.py.
* Line Number: The error occurred at line 11 in the file.
* Code Context: The specific line of code that caused the error was print("Average of empty_data:", calculate_average(empty_data)).
The arrow (`--->`) points to the exact line that caused the problem. This line is where the calculate_average(empty_data) function was called.

Now, let's look at the next part of the traceback:

```
File ~/my_code.py:4, in calculate_average(numbers)
      2 total = sum(numbers)
      3 count = len(numbers)
----> 4 average = total / count
      5 return average
```

This part tells us that the error happened inside the calculate_average function on line 4, where the code tried to execute `average = total / count`. Since count was 0 (because the list empty_data was empty), this resulted in a `ZeroDivisionError`.

To fix this error, you have a few options. 
You might choose to check if a list is empty before calling the `calculate_average` function, or you might modify your function to handle the case of the list length being zero.

Practice debugging with the following code example.
Write about your debugging process in the class [Google Presentation](https://docs.google.com/presentation/d/13b2208ItU8VLqdxMI1ovSCl0Ll3aIYy6CdWZUZi5LxA/edit?usp=sharing). How would you fix this problem?

```python
def find_max(numbers):
    max_number = numbers[0]
    for i in range(1, len(numbers) + 1):
        if numbers[i] > max_number:
            max_number = numbers[i]
    return max_number

numbers = [3, 5, 7, 2, 8]
print(find_max(numbers))
```

