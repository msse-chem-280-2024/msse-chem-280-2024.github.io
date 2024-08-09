# Group Homework Assignment - Day 5

## Rewriting $\pi$ calculation

For your group work today, you should rewrite the Monte Carlo calculation of $\pi$ (from Day 2 lecture) to use NumPy.
You should be able to eliminate the use of loops entirely with this rewrite.
Note that you can use [NumPy array creation routines](https://numpy.org/doc/stable/user/basics.creation.html) to quickly create arrays.
For example, you might find it useful to use `np.random.random_sample(n_samples)` to quickly create an array with `n_samples` random numbers ([documentation](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random_sample.html).

After your rewrite, use the Python `time` module (see Day 4 task 2) to compare performance for `n_samples=100` and `n_samples=10000000` for the two versions of your code.


## Molecular Monte Carlo using NumPy

For your final project, you will need to write a version of your molecular Monte Carlo simulation that uses NumPy.

Today, take time to to discuss with your teammates what changes you can make to your code to take advantage of the features of NumPy arrays. If you have extra time, start working on your NumPy implementation with your group.
Remember that you will have to write a NumPy version of your code, so it might be a good idea to start while you have time.

## Turning in your Pull Request
For today, turn in a pull request that contains your Monte Carlo $\pi$ calculation using Numpy and a markdown explanation of code changes you discussed for the NumPy version of your molecular Monte Carlo simulation. Like usual, name your file with `lastname_firstname`. You also need to review a group member's pull request. Check that they have the completed task and explanation. 