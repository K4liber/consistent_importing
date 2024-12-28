# Consistent importing

## Abstract

TODO

## Outline

1. Why do we care? (1 minute)
- Consistency: not repeating same questions in CRs
- Can imports structure impact project architecture?

2. Creating a modular structure (10 minutes)
- Python module  
    - Any python file (`.py`) is a module

"If you quit from the Python interpreter and enter it again, the definitions you have made (functions and variables) are lost. Therefore, if you want to write a somewhat longer program, you are better off using a text editor to prepare the input for the interpreter and running it with that file as input instead. This is known as creating a script.

To support this, Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter. Such a file is called a module. A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Definitions from a module can be imported into other modules or into the main module.
"

- From single file to modular structure (1000 lines limit)

- Why modular structure?
    - Developers can focus on smaller, isolated pieces of code without being overwhelmed by its size.
    - Separation of concerns.
    - Testing smaller modules individually is easier than testing a monolithic module.
    - Easier to manage version history and resolve conflicts.
    - Extremely large files can slow down editors and tools like linters or code formatters.

- Python package  
    - just a directory with python modules
    - `__init__.py` is executed on the package import, https://docs.python.org/3/tutorial/modules.html#packages

- `PYTHONPATH` - how does it work?

- It is import how you name the package/module because of import hierarchy
    - stdlib vs your own package
    - `time` vs `random` example.

- running python file as a script vs as a module
    - How does it affect PYTHONPATH?
    - https://stackoverflow.com/a/2997044/6718081
    - running python package as module (`__main__.py` module)

- what happens when we import?
    - execution of a module
    - creating a module object and assigning the object to global variable
    - all entities defined in a module became module's attributes
    - module cached in sys.modules

3. How to (not) import? (5 minutes)
- imports style and sorting
    - https://peps.python.org/pep-0008/#imports

- module lvl imports
    - https://docs.astral.sh/ruff/rules/banned-module-level-imports/

- relative imports
    - `-` not recommened in pep
    - ...

- from module import entity
    - `-` import always executes the entire file
    - `+` cannot create a way around circular import
    - `+` the most clear and explicit way to import

- from module import * (not recommended, why?)
    - `+` imports only "public" objects (ignore ones starting from `_`)
    - `+` execute the whole module (as any other import) and loads everything in the namespace
    - `+` using `__all__` to specify what is imported under the asterisk `*`
    - `-` masking attributes in a namespace -> uncertain state of the namespace. Could lead to potential bugs

- exporting using `__init__.py`
    - `+` shorter imports
    - `-` executing all the modules
    - `-` not explicite stated where the module comes from (the actual definition away from declaration)
    - `-` both IDEs and developers can be confused

- (this should be last one as an transition to the last part) if TYPE_CHECKING: (do not use), why?

4. Imports structure impact on project architecture (5 minutes)
- Python is dynamic and flexible
    - if we want a structure we need to enforce it

- Why you should care anyway?
    - https://www.piglei.com/articles/en-6-ways-to-improve-the-arch-of-you-py-project/

- circular imports most of the time indicate a wrong structure

- circular imports (sub-package init circles, caused `__init__.py`)
    - why anybody would place exports in the `__init__.py`?
    - create `interface` package and put your imports there (https://www.youtube.com/watch?v=UnKa_t-M_kM, 5:30)
- circular imports most common example (network/graph)

![alt text](images/clean_architecture.png)
[Clean Architecture](#clean_architecture)

Lets say that we have 2 modules A and B. If we ever face need for a bidirectional dependency we should ask ourselves the following questions:

- can A exist without B?
- is A anyhow useful without B?

Can a node exists without an edge? Yes. An edge is not a node concern.

- use typing everywhere to disclose hidden circular imports

- circular imports solution: layered architecture
    - Layered architecture, Kraken example (monolith with nearly 28k Python modules) https://blog.europython.eu/kraken-technologies-how-we-organize-our-very-large-pythonmonolith/
    - Import linter, https://github.com/seddonym/import-linter
    - Inversion of control, https://seddonym.me/2019/04/15/inversion-of-control/?ref=blog.europython.eu
    - https://en.wikipedia.org/wiki/Dependency_inversion_principle

- structuring Your Project, https://docs.python-guide.org/writing/structure/

- separation of concerns

"In computer science, separation of concerns (sometimes abbreviated as SoC) is a design principle for separating a computer program into distinct sections. Each section addresses a separate concern, a set of INFORMATION that affects the code of a computer program."

- layering based on abstraction level (database case)
    - should a domain logic be concern about what DBMS is used? It most cases, no. It is a detail.

- user interface
    - can a policy components access GUI components? God forbid.

5. Consisted imports enforced by CI (5 minutes)
- lintering
    - https://docs.astral.sh/ruff/rules/
    - https://github.com/seddonym/import-linter

- formatting
    - sorting

6. Margin + Questions (4 minutes) 


## Bibliography

<a name="circular_imports"></a>1. Circular imports, https://docs.python.org/3/faq/programming.html#how-can-i-have-modules-that-mutually-import-each-other

<a name="circular_references"></a>2. What is wrong with circular references, https://softwareengineering.stackexchange.com/a/12030

<a name="languages_with_circular_references"></a>3. Languages which support circular dependency imports, https://www.reddit.com/r/ProgrammingLanguages/comments/yvkysh/languages_which_support_circular_dependency/

<a name="clean_architecture"></a>4. Robert C. Martin, "Clean Architecture: A Craftsman's Guide to Software Structure and Design"

<a name="clean_architecture_in_python"></a>5. Leonardo Giordani, "Clean Architectures in Python", https://www.youtube.com/watch?v=C7MRkqP5NRI 

<a name="modules"></a>6. docs.python.org/, "Modules", https://docs.python.org/3/tutorial/modules.html
