# Consistent and solid importing

## Abstract

TODO

## Outline

1. Creating a modular structure (10 minutes)
- Python module  
- From single file to modular structure (1000 lines limit)
- Why modular structure?
    - Developers can focus on smaller, isolated pieces of code without being overwhelmed by its size.
    - Separation of concerns.
    - Testing smaller modules individually is easier than testing a monolithic module.
    - Easier to manage version history and resolve conflicts.
    - Extremely large files can slow down editors and tools like linters or code formatters.
- Python package  
    - `__init__.py`, https://docs.python.org/3/tutorial/modules.html#packages
    - does an empty `__init__.py` makes sense?  
- `PYTHONPATH` - how does it work?
- import hierarchy -> stdlib vs your own package. `time` vs `random` example.
- running python file as a script vs as a module
    - How does it affect PYTHONPATH?
    - https://stackoverflow.com/a/2997044/6718081
- sys.modules

2. How to (not) import? (5 minutes)
- imports style and sorting
    - https://peps.python.org/pep-0008/#imports
- from module import entity
- other possibilities to import ...
- from module import * (do not use, why?)
- (this should be last one as an transition to the last part) if TYPE_CHECKING: (do not use), why?

3. Imports structures as architecture design (10 minutes)
- Python is dynamic and flexible
    - if we want a structure we need to enforce it
- Why you should care anyway?
    - https://www.piglei.com/articles/en-6-ways-to-improve-the-arch-of-you-py-project/
- circular imports (just a wrong structure)
- circular imports (caused `__init__.py`)
    - why anybody would place exports in the `__init__.py`?
    - create `interface` package and put your imports there (https://www.youtube.com/watch?v=UnKa_t-M_kM, 8:00)
- circular imports solution: layered architecture
    - Layered architecture, Kraken example (monolith with nearly 28k Python modules) https://blog.europython.eu/kraken-technologies-how-we-organize-our-very-large-pythonmonolith/
    - Import linter, https://github.com/seddonym/import-linter
    - Inversion of control, https://seddonym.me/2019/04/15/inversion-of-control/?ref=blog.europython.eu
    - https://en.wikipedia.org/wiki/Dependency_inversion_principle
- Structuring Your Project, https://docs.python-guide.org/writing/structure/

## Notes

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

Should a domain logic be concern about what DBMS is used? It most cases, no. It is a detail.

4. User interface

Can a policy components access GUI components? God forbid.

## Bibliography

<a name="clean_architecture"></a>1. https://docs.python.org/3/faq/programming.html#how-can-i-have-modules-that-mutually-import-each-other

<a name="clean_architecture"></a>1. https://softwareengineering.stackexchange.com/a/12030

<a name="clean_architecture"></a>1. https://www.reddit.com/r/ProgrammingLanguages/comments/yvkysh/languages_which_support_circular_dependency/

<a name="clean_architecture"></a>1. Robert C. Martin, "Clean Architecture: A Craftsman's Guide to Software Structure and Design"

<a name="clean_architecture"></a>1. Leonardo Giordani, "Clean Architectures in Python", https://www.youtube.com/watch?v=C7MRkqP5NRI 

<a name="modules"></a>1. docs.python.org/, "Modules", https://docs.python.org/3/tutorial/modules.html
