# **ALGORITHM ANALYSIS**

**Data Structure** is a systematic way of organizing and accessing data.

> How can I design a data structure that can **organize, and access data efficiently**?

**Algorithm** is a step-by-step procedure for performing some task in a **finite amount of time**

> How can I design an **efficient** algorithm, that can perform a given task in an the **shortest time possible** way?

The above questions are answered by means of the **analysis of the data structure and algorithm**.

---|||

The analysis of algorithm or data structure operation makes it possible to characterize how relatively **efficient** :

- an algorithm performs a given task, or

- one can perform an operation on a given data structure.

---|||

### Measuring Efficiency Of an Algorithm OR a Data Structure Operation

The two resources of concern in the execution of an algorithm, the organization and access of data in a data structure are;

- **space (memory)** => organize data using less memory

- **CPU time** ==> executing the algorithm, and accessing data in the data structure in a relatively **short time**

> Sometimes, trade-offs may occur where we sacrifice *time* for less space or vice-versa.

Since one would expect that the larger the **input size** of the problem, the more **CPU time**, and space one would use to perform the task.

> Hence, the efficiency of the algorithm would be measured as a function of the input size, independent on the hardware environment (memory, processor, clock rate, disk...) or software environment (OS, programming language...)

---
---|||

### Experimental VS Theoretical Analysis of Algorithms and Data Structures

In experimental analysis, one is concerned with measuring **the time it takes to execute an algorithm or perform a data structure operation (access data), and the space used in the organization of data in a data structure**. But in this approach;

1. the implementation of **the** algorithm and **designing or choosing** a data structure to analyze it, must be performed in order to carry out the experimental analysis.

    - Since significant amount of time is spent in designing an algorithm and choosing a data structure, then it would be a waste of the programmers effort if the algorithm doesn't measure up to expectation. Hence, having a **high-level** analysis of the algorithm without implementing it, will save a lot of time.

2. It is possible for the running time of two algorithms to differ due to several factors

    - Different hardware environment will measure different running time. An hardware environment with a faster processor will have a shorter time compared with one with a slower processor, all other factors being constant.

    - On the same hardware, the context of the CPU (i.e. what the CPU was doing before executing the algorithm), before executing the algorithm will determine the running time of the algorithm. Switching execution context between threads or processes.

    - OS scheduling of tasks will also affect, since our program must wait for the OS to schedule it for execution before running

    - A compiled programming language will execute the algorithm faster than an interpreted programming language.

3. The experiments can only be carried out on a **limited set of test inputs**, thereby neglecting the running times of the inputs not included in the test set.

All of this challenges are easily overcome in theoretical (high-level) analysis of an algorithm, which measures efficiency of an algorithm or data structure as a function of input size, independently of the hardware and software environments.

---

### Theoretical Or High-Level Analysis of Algorithm or Data Structure

**Primitive Operations**

A primitive operation is one that corresponds to a low-level instruction with a constant execution time. This includes:

- Assigning a variable to an object
- Determining the object associated with an identiﬁer
- Performing an arithmetic operation (for example, adding two numbers)
- Comparing two numbers
- Accessing a single element of a Python list by index
- Calling a function (excluding operations executed within the function)
- Returning from a function.

In high-level analysis, one is interested in **counting how many primitive operations are executed**, and use this as a measure of the **running time of the algorithm**.

> I should try and see the number of low-level (assembly) instruction it takes to carry out each of these **primitive operations** on different processors.

**Measuring Efficiency as a Function of Input Size**

It is noted that in this high-level analysis, our running time, will depend on the number of primitive operations, then a measure of efficiency of an algorithm will then be to **determine the number of primitive operations performed by the algorithm as a function of the input size**

Average-Case Analysis: measuring the efficiency of an algorithm by averaging over all possible inputs of the same size. This requires that we have a probability distribution on the sets of input.

Worst-Case Analysis: uses the worst-case input to analyze the efficiency of an algorithm.

### Categories of Function Depending On The Input-Size

NOTE:

NPO: Number of Primitive Operations

Assume the base of a logarithm is 2

1. Constant Function **f(n) = constant**: this characterize the NPO to run the algorithm on the input-size **n** to be a constant number, **independent of the size of the input n**.

2. Logarithmic Function **f(n) = log(n)**: here the NPO to run the algorithm on the input-size n, depends the **number of times we divide the input size by 2 until we get to 1 or a number less than 1** - the logarithm. E.g.

- if the input size is 256, then the NPO is 8 since log(256) == 8.
- if the input-size is 99, then the NPO is 7 since log(99) ~ 7

3. Linear Function **f(n) = n**: here the NPO to run the algorithm on the input-size n, is proportional on the input-size. E.g
  
- if the input size is 256, then the NP0 is **k*n**, where k is the proportionality constant.

4. N-LOG-N Function **f(n) = n * log(n)**: here, the NPO to run the algorithm on the input-size n, depends on two factors:

- the input size itself,
- how many times the input-size divided by 2, will equal 1 or a number less than 1.

 Since these two factors are independent, then the total NPO is therefore product

5. Polynomial Functions **f(n) = k_0 + k_1 * n + k_2 * n^2 + k_3 * n^3 + ...**, where k_i is a constant term.

- > A good data structure operations should ideally run in times proportional to constant OR logarithm function.

- >An efficient algorithm should run in linear or n-log-n time

---
---|||

### Asymptotic Analysis

This is a measure of the **growth rate** of the running time of an algorithm as a function of the input size **n**, neglecting constant factors.

Hence we measure the running time of a algorithm by the NPO executed up to a constant factor, as the input-size increases.