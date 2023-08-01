# The Lennard Jones Equation

````{admonition} Overview
:class: overview

Questions:
- How can Monte Carlo be applied to a thermodynamic problem?
- How do we model the interaction of nonbonded atoms?

Objectives:
- Understand the Lennard Jones potential.
- Understand periodic boundary conditions.
````

This module is based on work by former MolSSI Software Scientist Eliseo Marin-Rimoldi and Prof. John D. Chodera.

## Lesson Slides

{download}`Lennard Jones Slides <../_files/intro-lennard-jones.pdf>`


## Motivation - Using Monte Carlo on molecular systems

We are going to use Monte Carlo simulation to solve a chemical problem. MC simulation is used in a lot of different fields, and one of those is molecular simulation. MC methods for molecules can be quite advanced these days, but for this bootcamp, we will be using MC to simulate noble gases.

In statistical mechanics, we are interested in computing averages of thermodynamic properties as a function of atom positions an momenta. A thermodynamic average depending only on configurational properties can be computed by evaluating a multivariate integral.

$$ 
\left<Q\right> = \int_V Q\left(\textbf{r}^N\right)
	\rho\left(\textbf{r}^N\right) d\textbf{r}^N
	\label{eq.statMechAverage} 
$$ 

where $Q\left(\textbf{r}^N\right)$ is the thermodynamic quantity of interest that depends on only on the configuration, $\rho\left(\textbf{r}^N\right)$ is the probability density, and $V$ defines the volume of configuration space over which $\rho$ has support.

This integral is very hard to compute, even for small atomic systems. For instance, a monoatomic system of 10 atoms leads to a 30 dimensional integral. 

We learned in the previous lesson about using Monte Carlo to evaluate integrals. We can apply this same approach to solve this integral. There are a few extra things we have to consider, however, because of the high dimensionality of the problem. We'll worry more about exactly how to implement this MC integration tomorrow. Today's lesson will focus on the model we are going to use for our thermodynamic quantity (in our case the system potential energy). 

## Modeling the system

When modeling atomic and molecular systems, the energy of nonbonded interactions are often approximated using the **Lennard Jones Potential**.

$$ 
U(r) = 4 \epsilon \left[\left(\frac{\sigma}{r}\right)^{12} -\left(\frac{\sigma}{r}\right)^{6} \right] 
$$

This is a pairwise potential which is a function of distance between two atoms. It has two parameters, $\sigma$ and $\epsilon$, which represent the size of the particle, and the depth of the potential well (you can think of this as how strongly the particles are attracted to one another), respectively.

This potential is commonly used in molecular simulation to model nonbonded interactions, not just for those of noble gases. For more complicated systems, you will have additional energy terms in addition to the LJ potential, but for our system of noble gases, the is the only contribution to the potential energy. 

The first thing we will do is write a function which evaluates the LJ energy based on an input of distance.

Commonly used parameters for simulating Argon are $\sigma = 3.4 \unicode{xC5} $ and $\epsilon/k_B = 120~K$

### Dealing with units
Throughout this project, we will be working with **reduced units**. As stated above, common values are $\sigma = 3.4 \unicode{xC5}$ and $\epsilon/k_B = 120~K$. When converted to SI units, these quickly become inconvenient to work with. Often, in simulation, we will use something called *reduced units* in order to make calculations more convenient. This approach essentially scales quantities by characteristic values to get them closer to unity.

For example, when working with Argon, the distances we compute will be in units of $$\sigma$$ instead of angstrom. 

Quantity    | Expression
------------|------------
Length      | $L^*=L / \sigma$
Density     | $\rho^* = N \sigma^3 / V$
Energy      | $U^* = U / \epsilon$
Pressure    | $P^* = P \sigma^3 / \epsilon$
Volume      | $V^* = V / \sigma^3 $
Temperature | $T^* = k_{B} T / \epsilon $
Time        | $t^* = t \sqrt{\frac{\epsilon}{ m \sigma^2}}$

Conveniently for us, Lennard Jones fluids have the surprisingly pleasant property of possessing universal behavior when expressed in terms of reduced units as (you can verify this for yourself by substituting $\sigma$ and $\epsilon$ for their reduced unit expressions):

$$ 	
U^*\left(r_{ij} \right) = 4 \left[\left(\frac{1}{r^*_{ij}}\right)^{12} -\left(\frac{1}{r^*_{ij}}\right)^{6} \right] 
$$

Since we know that we will need this as a function for our MC calculation, we will write a function for it to use later.

Recall that in Python, we define a function using the syntax:

````{tab-set-code} 

```{code-block} python
def function_name(function_arguments):
    ** FUNCTION HERE **
    return return_value
```
````

For our `calculate_LJ` function, we will need to raise $$\frac{1}{r_ij}$$ to the 12th and 6th power. We will use the `pow` function in the python `math` module for this.

````{tab-set-code} 

```{code-block} python
def calculate_LJ(r_ij):
    r6_term = math.pow(1/r_ij, 6)
    r12_term = math.pow(r6_term, 2)
    
    pairwise_energy = 4 * (r12_term - r6_term)
    
    return pairwise_energy
```
````

### Sanity checks

It is always a good idea to test the expected behavior of your function, or do some "sanity checks". We'll think about a few qualities of the LJ potential to check if our function is reasonable.

From the equation for the LJ potential, we can see a few qualities that should be true if our function is implemented correctly - 

1. This function should equal zero at r = 1.
1. A minimum occurs at $r = 2^{1/6}\sigma.$ In our case, we are using reduced units and $\sigma$ is equal to one. This minimum will have a value equal to $-\epsilon$, in our case -1. 

We'll check these two test statements using something called an `assert` statement in Python. In an `assert` statement, you assert that something is `True`. If the statement following the word `assert` is `True`, nothing happens. However, if the statement is `False`, you will get an assertion error.

````{tab-set-code} 

```{code-block} python
assert 1 == 1
```
````


results in no visible output. But,

````{tab-set-code} 

```{code-block} python
assert 2 == 1
```
````


results in an `AssertionError`.

````{tab-set-code} 

```{code-block} error
AssertionError                            Traceback (most recent call last)
<ipython-input-26-39a8159f4693> in <module>
----> 1 assert 2 == 1

AssertionError:
```
````


Let's translate our two criteria into `asserts` to check our function:

````{tab-set-code} 

```{code-block} python
assert calculate_LJ(1) == 0
assert calculate_LJ(math.pow(2, (1/6))) == -1
```
````


### Python Style - Docstrings

Part of this class is cultivating good coding habits. A "best practice" when writing your code is to make sure that your code is adequately documented. This could be through code comments, but a very good way to document your code is to use something called `docstrings` in Python. In this course, we may not always write `docstrings` right away, but you should always write them.

A `docstring`, or `documentation string` is a string which follows the function definition and describes a function's inputs and behavior. If you write `docstrings`, you will have a much easier time returning to your code, sharing it with others, and creating online documentation. For Python, there is a tool called `Sphinx` which can parse your code for `docstrings` and build web documentation for you (we will not discuss this in this course).

We will write `Numpy` style `docstrings`. Consider our `calculate_LJ` function with a docstring:

````{tab-set-code} 

```{code-block} python
def calculate_LJ(r_ij):
    """
    The LJ interaction energy between two particles.

    Computes the pairwise Lennard Jones interaction energy based on the separation distance in reduced units.

    Parameters
    ----------
    r_ij : float
        The distance between the particles in reduced units.
    
    Returns
    -------
    pairwise_energy : float
        The pairwise Lennard Jones interaction energy in reduced units.

    Examples
    --------
    >>> calculate_LJ(1)
    0

    """
    r6_term = math.pow(1/r_ij, 6)
    r12_term = math.pow(r6_term, 2)
    
    pairwise_energy = 4 * (r12_term - r6_term)
    
    return pairwise_energy
```
````


We've now added a multi-line comment to the beginning of our function. Docstrings **are the first statement after a function or module definition** and are opened and closed with three quotes.

The `docstring` should explain what the function or module does (and not how it is done).

### Sections of a Docstring
There are many ways you could format this docstring (different styles/conventions). We recommend using [numpy style docstrings], and this is what the example above and `calculate_LJ` function are written in.

Each docstring has a number of sections which are separated by headings. Headings should be underlined with hyphens (`-----`). There are many options for sections, we will only cover the most relevant here. If you would like to see a full list, check out the documentation for [numpy style docstrings].

#### 1. Short summary
A one-line summary that does not use the variable name or the function name. In our `calculate_LJ` function, this corresponds to the following.

````{tab-set-code} 

```{code-block} python
"""
The LJ interaction energy between two particles.
"""
```
````


#### 2. Extended summary
A few sentences giving a detailed description of the function or module. This section should be used to clarify *functionality*, not to discuss implementation.

````{tab-set-code} 

```{code-block} python
"""
Computes the pairwise Lennard Jones interaction energy based on the separation distance in reduced units.
"""
```
````


#### 3. Parameters
This section contains a description of the function arguments - keywords and expected types.

The parameters for our `calculate_LJ` function is shown below:

````{tab-set-code} 

```{code-block} python
"""
    Parameters
    ----------
    r_ij : float
        The distance between the particles in reduced units.
"""
```
````

Here, you can see that the parameter section begins with the section title ("Parameters"), followed by a line of hypens ("----"). On the next line, we have the argument name (r_ij), then a colon followed by the input type of the argument. This line says that the argument should be of type `float`. The next line gives a more detailed description of the variable. When the there is more than one input parameter,they should be written on new line.

#### 4. Returns
This section is very similar to the `Parameters` section above. In contrast to the `Parameters` section, each returned value does not have to be named, but the type of the return value is required.

For our `calculate_LJ` function, our `Returns` section looks like the following.

````{tab-set-code} 

```{code-block} python
"""
Returns
    -------
    pairwise_energy : float
        The pairwise Lennard Jones interaction energy in reduced units.
"""
```
````


#### 5. Examples
This is an optional section to show examples of functionality. This section is meant to illustrate usage. Though this section is optional, its use is strongly encouraged.

Consider the example we have in our docstring

````{tab-set-code} 

```{code-block} python
"""
Examples
--------
>>> calculate_LJ(1)
    0
"""
```
````


It is important that your Examples in docstrings be working Python.

We have one line of code for our example. In examples, lines of code begin with `>>>`. On the last line, you give the output (with no `>>>` in front.)

[numpy style docstrings]: https://numpydoc.readthedocs.io/en/latest/format.html#sections


````{admonition} Key Points
:class: key

- Thermodynamic properties of a system can be thought of as a very high dimensional integral.
- We can use MC methods for this, but the calculation is more complicated due to the high dimensionality of the problem.
- We model pairwise atomic interactions using the Lennard Jones potential.
````
