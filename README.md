# What is OOP, and its goal?

The goal of OOP is tied to goals of correct functional software system; A correct software implementation must be such that it is;

1. **Robustness**: ability to handle unexpected inputs that are not explicitly defined in the application.

2. **Adaptability**: This is the ability of a software program to be capable of evolving in response to changing conditions, **with little efforts**.

3. **Reusability**: this is the ability of a software program to easily fit as component of different systems in different applications.

### OOP is an attempt to facilitate the goals of software programs listed above; It achieves this under three general principles.

#### **Modularity**: 
Dividing a software systems into interacting components that represents a seperate functional unit. That is, each component performs a well defined function, and when fitted with other components, forms a unifying whole of the entire software system.

> This is achieved with **modules** in Python

With a software system separated into interacting components, it easier to test each component seperately, it is easy to evolve the component, and a given component can easily be fitted into another application easily.

#### **Abstraction**: 

This involves breaking down a software system into its most fundamental parts, which in turns gives a **model** of the software system; explaining the function, the components and how they interact.

An abstract data type is an example an abstraction of a data structure

---
---
---|||
### Abstract Data Types (ADT)

This is a mathematical model of a data structure that specifies;

- the **type** of **data** stored
- the **operations** supported on the data structure
- the **types** of **parameters** of the operation; i.e. what do is need to perform the operation

Hence, the **ADT specifies** ***what*** each operation does, and **NOT how** the operations are performed. And the **collective set of behaviours (operations)** supported by an ADT is referred to as its **public interface**.

How does a user of a public interface knows which types to pass to it? 

When a given method can be passed on the object; hence behaviour of an object in python is a stand-in for the type of that object

### Abstract Base Class (ABC):

This is Python mechanism for supporting abstract data types. An ABC cannot be instantiated, rather it defines a common set of methods that all implementation of the abstraction must have.

Since Python has no compile-time type checking, it relies on whether a given method can be called on an object. If the said method can be called on the object then we say it behaves like the type expected; in fact we say it is the type expected - this is known as **duck typing**

---
This is similar to the **trait** system in Rust, where

- the Trait itself acts like an abstract base class, providing a set of functions (methods), and

- any type implementing that trait (acts like; classes inheriting the abstract base class) must implement those methods

---
---

### **Encapsulation**: 

This involve hiding the internal details (i.e. implementation details )of a public interface from a user.


---
---
---|||
## Design Patterns

This describe a solution to a typical software design problem. A pattern provides general template for a solution that can be applied in many different situations.

It consist of:

- a **name**: identifies the pattern

- a **context**: scenarios *where* the pattern can be applied

- a **template**: describes *how* the pattern is applied

- a **result**: which describes and analyzes what the pattern produces

### Two Categories of Design Patters;

- **Algorithm Design Patterns**

	- Recursion
	- Amortization
	- Divide-and-Conquer
	- Prune-and-Search, (aka, decrease-and-conquer)
	- Brute Force
	- Dynamic Programming
	- The Greedy Method

- **Software Engineering Design Patterns**

	- Iterator
	- Adapter
	- Position
	- Composition
	- Template
	- Locator
	- Factory Method

---
---
---||||

## Classes

A class in python is the primary means of abstraction in OOP, such that;

- instance of a class represents a piece of data
- member functions (or methods) represents the behaviours supported on/by the object

A class also serves as a **blueprint** for its instances (i.e. how concrete objects can be created), such that **state information** for each instances is represented in the form of **attributes**; a.k.a - **fields or instance variables or data members**.

---
---
---|||

### Operator Overloading

This a process where a class implements special unique method from Python built-in classes  by **overiding** their method definition.


---
---
---|||

### Iterators

The mechanism for iteration is provided by the special **__next__** method, that returns the next element of a collection, if any, OR raises a StopIteration exception to indicate that there are no further elements.

By default, implementing the special methods below, guarantees an automatic iterator implementation for the object, hence the **__next__** method need not be implemented once the two special methods are implemented on the class;

- **__len__**
- **__getitem__**

> By convention, an iterator must return itself in the special **__iter__** method

---
---
---|||

## Inheritance

Python's inheritance provides an hierarchical structure between classes; where one class **inherits** properties from the other on an **is a kind of** basis;

e.g.
If A, and B are two classes, and A inherits the properties of B, then A **is a kind** of B. Infact, we go on to say that A *is* B, because of duck-typing. Remember, behaviour acts as types in Python, so anywhere we can put A, so can we put B

In general, since **A** inherits from **B**, we say **A is a *subclass (or child class)* of B** AND **B is a *super-class (or parent ( or base ) class)* of A**  

> **In general, inheritance allows us to organize common functions at the super-class level, and only overide/extend these functions (behaviours) at the subclass(es) level**

- When it overides: it specialise the base class functionality

- When it extends: it adds new functionality to the base class' by providing new methods
---

At the file level, modularity is provided by python modules, at the class level, the mechanism for modularity and hierarchical organization is through inheritance. 

---
---

---|||

### Template Method Pattern

This is realized when the an abstract base class provides **concrete behaviours** that rely upon calls to other **abstract behaviours**. So that, when a subclass of the ABC provides definitions for the missing abstract behaviours, the inherited concrete behaviours are well defined.

This is similar to Rust's trait system, where one can define multiple functions in a trait definition such that;

- concrete implementations are provide for some ==> **concrete behaviour** of the ABC
- the others are required to be implemented by the user of the trait ==> **absract behaviour**

When the user implements this so called **abstract behaviours**, they immediately inherits the **concrete behaviours**

---
---
---|||

### Namespaces and Object Orientation

Namespace refers to all identifiers defined within a particular scope.

Nesting a class within another class allows grouping functionalities into different scopes or namespaces



---|||
## Algorithm Analysis


**Data Structure** is a systematic way of organizing and accessing data.

> How can I design a data structure that can **organize, and access data efficiently**?

**Algorithm** is a step-by-step procedure for performing some task in a **finite amount of time**

> How can I design an **efficient** algorithm, that can perform a given task in an the **shortest time possible** way?

The above questions are answered by means of the **analysis of the data structure and algorithm**.

---|||

The analysis of algorithm or data structure operation makes it possible to characterize how relatively **efficient** :

- an algorithm performs a given task, or

-  one can perform an operation on a given data structure. 

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

---
---|||




---|||
## Reference Material

Data Structures and Algorithms in Python - Michael T. Goodrich, Roberto Tamassia, Michael H. Goldwasser