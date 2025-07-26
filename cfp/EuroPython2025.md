# Consistent importing

**Session type**: Talk  
**Track**: Testing, Quality Assurance, Security  
**Duration**: 00:30

## Abstract (max 2100 characters)

Have you ever wondered what happens behind the scenes when you use import in Python? In this talk, we will demystify Python's import system and explore best practices for managing imports. Moreover, we will discuss how your importing strategy impacts project architecture, influencing modularity and maintainability. For developers working on large Python projects, consistent importing is crucial. It helps maintain codebases by reducing complexity and avoiding technical debt. 

The session will begin with an introduction to Python's modular structure: what modules and packages are, how sys.path influences imports, and what happens during the import process. We will also cover the importance of naming conventions and the difference between executing scripts and modules. Some of the things explained in this part may surprise you.

Next, we'll dive into various importing strategies and their implications. From absolute versus relative imports to lazy imports, wildcard imports, and typing-specific imports, we’ll clarify how to choose the right approach for maintainable and readable code.

The session will then explore how your importing structure affects the overall architecture of your project. We’ll address challenges like circular dependencies, separation of concerns, and the role of a layered architecture in maintaining flexibility and scalability.

Finally, we'll look at tools and techniques to enforce consistent importing practices. Learn how to integrate tools like Import Linter and Ruff into your CI pipeline to ensure adherence to your chosen strategy and avoid common pitfalls.

Whether you are a beginner or an experienced Python developer, this talk will help you streamline imports. You will learn practical strategies and tools to enforce consistency, making your projects easier to scale and manage.

## Outline (max 1000 characters)

0. Why this topic?
- Interesting import approach in a legacy codebase
- Why do successful people wear the same outfits every day?

I. How importing in Python works? (10 minutes)

1. Python interpreter
2. Python module
- using Python interpreter with raw code
- keeping code in files
3. Python package
4. Why modular structure?
- reusability
- readability
- separation of concerns
- maintainability
- testing
5. Importance of package/module naming
- utils as a root package name
6. sys.path
7. Execute a script vs execute a module
8. Package vs namespace
9. What actually happens when we do import?

II. How to import in a consistent way? (5 minutes)

1. Import one definition per line
- reduction of version control conflicts
2. Imports at the top of the file
- clear and evident set of dependencies
3. Lazy imports of heavy modules
- improve startup time
4. Absolute imports
- avoiding ambiguity (we can be sure what we import)
- IDEs are handling absolute imports better
- (exception) relative imports in an encapsulated package
- recommendation: use absolute imports by default
5. from module import definition
- the most clear and evident way to import specific definition
- recommendation: use from module import definition by default
6. import module (as ...)
- pandas/numpy as an example
7. Package vs namespace
- create package as default, namespace only when needed
8. Wildcard imports
- avoiding namespace pollution
- avoiding ambiguity
9. from package import definition (from __init__.py)
- (exception) an encapsulated package
10. Typing, if TYPE_CHECKING
- avoiding circular dependencies

III. How internal dependencies impact a codebase architecture? (5 minutes)

1. Python vs other languages
- Python's flexibility in importing
- "... (most likely due to a circular import)" as a feature
2. SOLID, DRY, KISS, ... ADP principles
- Robert C. Martin's "clean code" principles
- effort vs benefit of applying principles (presented on XY chart)
- automating architecture checks reducing the effort (presented on XY chart)
3. Acyclic dependencies principle (ADP)
- following ADP to improve architecture
- avoiding italian pasta code
- thinking about hierarchy of dependencies while importing
- using import statements to extract dependency graph

IV. How we can enforce the selected importing strategy in CI? (5 minutes)
1. Ruff
2. Import Linter

## Why am I qualified to speak about this topic?

I am currently working on Python project with around 100k lines of code. There were different strategies applied all around the repository when it comes to importing. I decided to understand deeply how importing works in Python and what is the best strategy for it.

After deep debugging, research (there were already a few presentations on the importing topic on different Python conferences), and hours trial and error I feel understand a topic good enough to share the knowledge. For sure, I am not an expert, yet. Having in mind my shallow understanding before the research I would love to make other Python developers experience a similar boost of knowledge in this topic.

The presentation is not just a copy of previous speeches. It includes considerations about importing strategy impact on architecture and tips for CI setup to assure consistency.

Moreover, I recently started contributing to the import-linter package to use the knowledge by improving open-source tools (PR: https://github.com/seddonym/import-linter/pull/250). Since I am actively working in the field both open-source and my private work, I am aware of new developments in the field. This will positively impact the quality of the final presentation.

## Abstract as a short post (max 150 characters)

Discover how Python imports work and how they can affect project architecture. Explore importing strategies and enforce consistency with CI.
