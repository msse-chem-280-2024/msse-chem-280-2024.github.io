# Python Warm Up & Returning to the LJ Equation

To start class today, we will spend about 20 minutes reviewing Python concepts, and another half hour working with the Lennard Jones equation.


## Python Review

Pick a chapter from the e-book [Think Python](https://greenteapress.com/thinkpython/html/index.html). 
To pick your chapter, read the topics and one you think you don't understand. 
To complete the activity, go into the break out room for the chapter you pick.
Read the chapter for 15 minutes. As you read, take note of at least four new or interesting points. 
If you have any questions, or if anything is unclear, make a note of that also.
During the last 5 minutes of the Python Review, each group should share their observations on the [class Google Doc](https://docs.google.com/document/d/1Bs5K45Y9uPrfE1XoGYgawg4_oA9DGKwAGTD_-KCbe0Y/edit?usp=sharing)]. (You must be logged into your UC Berkeley account to view the Google Doc.)

## Calculation of Lennard Jones Energy for System of Particles

Take 20 minutes to work alone, then 10 minutes to discuss your answers as a group on the following questions.

When applying the LJ potential to a set of atomic coordinates, the total potential energy of the system is equal to the sum of the LJ energy over all pairwise interactions:

$$
U \left( \textbf{r}^N \right) = \sum_{i=1}^{N} \sum_{j>i}^{N} U \left( r_{ij} \right)
$$

Consider the system of three particles represented by the picture below.  

```{image} ../fig/three-particles.png
:align: center
```

Complete the following tasks:

1. Based on what we discussed yesterday, make an estimate of what you would expect the total system energy to be. For this, think about our expected energy between two particles at the equilibrium distance.
2. Calculate the total system energy **by hand**, using a pen/paper and a calculator (you can use a calculator on a computer). If you finish early, see if you can translate your calculation into a Python code.