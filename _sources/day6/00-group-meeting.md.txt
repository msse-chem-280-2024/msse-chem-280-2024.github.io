# Class Warm Up

To start class today, you will analyze the number of times functions are called within your Monte Carlo simulation code. 
Your goal is to identify the most computational intensive functions to target for optimization when rewriting your MC code using NumPy.
In programming, optimizing the performance of your code is very important, especially in areas that are executed frequently. 
By focusing on the functions that are called the most, you can target those sections of the code that have the greatest impact on overall performance. 

Consider each of the functions in your code.
Without executing any code, calculate the number of times each function is called in a simulation with 10 steps, 100 steps, and 1000 steps.
Create a table on the class [Google Presentation](https://docs.google.com/presentation/d/13b2208ItU8VLqdxMI1ovSCl0Ll3aIYy6CdWZUZi5LxA/edit?usp=sharing) that contains the function name and the number of times it is called for each simulation length.

After you have calculated the number of times each function is called, insert a counter for your two most frequently called functions to check your answer.

Based on your results, which functions should you target to most effectively optimize your code? Why?

You might also try commenting out these functions or replacing them with a simpler version to get a sense of how much time they are taking up in your code.
Does this match your expectations based on the number of times they are called?