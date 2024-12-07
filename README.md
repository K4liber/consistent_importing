# Circular import error as a friend of a clean architecture

## Concepts

### Python module

"If you quit from the Python interpreter and enter it again, the definitions you have made (functions and variables) are lost. Therefore, if you want to write a somewhat longer program, you are better off using a text editor to prepare the input for the interpreter and running it with that file as input instead. This is known as creating a script.

To support this, Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter. Such a file is called a module. A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Definitions from a module can be imported into other modules or into the main module.
"

### Separation of concerns

"In computer science, separation of concerns (sometimes abbreviated as SoC) is a design principle for separating a computer program into distinct sections. Each section addresses a separate concern, a set of INFORMATION that affects the code of a computer program."


### Layering based on abstraction level

![alt text](images/clean_architecture.png)
[Clean Architecture](#clean_architecture)

Lets say that we have 2 modules A and B. If we ever face need for a bidirectional dependency we should ask ourselves the following questions:

- can A exist without B?
- is A anyhow useful without B?

## Examples

1. Network

Can a node exists without an edge? Yes. An edge is not a node concern. 

2. [an another simple example]

3. Layering based on abstraction level (database case)

Can the raw data exist (and be useful) without the software? Yes! If you like to do calculations on paper.

Can a software exist without the data? No.

Should a domain logic be concern about what DBMS is used? It most cases, no.

4. User interface

Can a simulation engine software access GUI elements? God forbid.

## Bibliography

<a name="clean_architecture"></a>1. https://docs.python.org/3/faq/programming.html#how-can-i-have-modules-that-mutually-import-each-other

<a name="clean_architecture"></a>1. https://softwareengineering.stackexchange.com/a/12030

<a name="clean_architecture"></a>1. https://www.reddit.com/r/ProgrammingLanguages/comments/yvkysh/languages_which_support_circular_dependency/

<a name="clean_architecture"></a>1. Robert C. Martin, "Clean Architecture: A Craftsman's Guide to Software Structure and Design"

<a name="clean_architecture"></a>1. Leonardo Giordani, "Clean Architectures in Python", https://www.youtube.com/watch?v=C7MRkqP5NRI 

<a name="modules"></a>1. docs.python.org/, "Modules", https://docs.python.org/3/tutorial/modules.html
