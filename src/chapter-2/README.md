# What is OOP, and its goal?

The goal of OOP is tied to goals of correct functional software system; A correct software implementation must be such that it is;

1. **Robust**: ability to handle unexpected inputs that are not explicitly defined in the application.

2. **Adaptable**: This is the ability of a software program to be capable of evolving in response to changing conditions, **with little efforts**.

3. **Reusable**: this is the ability of a software program to easily fit as component of different systems in different applications.

## OOP is an attempt to facilitate the goals of software programs listed above; It achieves this under three general principles

### **Modularity**

Dividing a software systems into interacting components that represents a seperate functional unit. That is, each component performs a well defined function, and when fitted with other components, forms a unifying whole of the entire software system.

> This is achieved with **modules** in Python

With a software system separated into interacting components, it easier to test each component seperately, it is easy to evolve the component, and a given component can easily be fitted into another application easily.

### **Encapsulation**

This involve hiding the internal details (i.e. implementation details )of a public interface from a user.

### **Abstraction**

This involves breaking down a software system into its most fundamental parts, which in turns gives a **model** of the software system; explaining the function, the components and how they interact.

An abstract data type is an example an abstraction of a data structure

---
---
---|||

## Abstract Data Types (ADT)

This is a mathematical model of a data structure that specifies;

- the **type** of **data** stored
- the **operations** supported on the data structure
- the **types** of **parameters** of the operation; i.e. what is needed to perform the operation

Hence, the **ADT specifies** ***what*** each operation does, and **NOT how** the operations are performed. And the **collective set of behaviours (operations)** supported by an ADT is referred to as its **public interface**.

How does a user of a public interface knows which types to pass to it?

When a given method can be invoked on the object; hence behaviour of an object in python is a stand-in for the type of that object

### Abstract Base Class (ABC)

This is Python mechanism for supporting abstract data types. An ABC cannot be instantiated, rather it defines a common set of methods that all implementation of the abstraction must have.

Since Python has no compile-time type checking, it relies on whether a given method can be invoked on an object. If the said method can be invoked on the object, then we say it **behaves like the type expected**; in fact we say it is the type expected - this is known as **duck typing**.

---
This is similar to the **trait** system in Rust, where

- the ***Trait*** itself acts like an **abstract base class**, providing a set of functions (methods), and

- any type implementing that trait (acts like; classes inheriting the abstract base class) must implement those methods

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

### Two Categories of Design Patters

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

The mechanism for iteration is provided by the special ****next**** method, that returns the next element of a collection, if any, OR raises a StopIteration exception to indicate that there are no further elements.

By default, implementing the special methods below, guarantees an automatic iterator implementation for the object, hence the ****next**** method need not be implemented once the two special methods are implemented on the class;

- ****len****
- ****getitem****

> By convention, an iterator must return itself in the special ****iter**** method

---
---
---|||

## Inheritance

Python's inheritance provides an hierarchical structure between classes; where one class **inherits** properties from the other on an **is a kind of** basis;

e.g.
If A and B are two classes, and A inherits the properties of B, then A **is a kind** of B. Infact, we go on to say that A *is* B, because of duck-typing. Remember, behaviour acts as types in Python, so anywhere we can put A, so can we put B

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