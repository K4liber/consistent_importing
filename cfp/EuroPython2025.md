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

1. Python module
- using Python interpreter with raw code
- keeping code in files
2. Why modular structure?
- reusability
- readability
- separation of concerns
- maintainability
- testing
3. Python package
4. Importance of package/module naming
5. sys.path
6. Execute a script vs execute a module
7. What actually happens when we do import?

II. How to import in a consistent way? (5 minutes)

0. Consistency advantages
- no need to think about the same thing twice
- creating space for automation
1. Imports on separate lines
- reduction of version control conflicts
2. Imports at the top of the file
- clear dependencies
3. Lazy imports of heavy modules
- improve startup time
4. Absolute imports
- avoiding ambiguity
- (exception) relative imports in an encapsulated package
5. From module import entity
- avoiding namespace pollution
6. Package vs namespace
- understanding the difference
7. import module (as ...)
- pandas/numpy as an example
8. Wildcard imports
- avoiding namespace pollution
- avoiding ambiguity
9. Import from package
- avoiding ambiguity
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

IV. How we can enforce the selected strategy in CI? (5 minutes)
1. Import Linter
2. Ruff setup

## Why am I qualified to speak about this topic?

I am currently working on Python project with around 100k lines of code. There were different strategies applied all around the repository when it comes to importing. I decided to understand deeply how importing works in Python and what is the best strategy for it.

After deep debugging, research (there were already a few presentations on the importing topic on different Python conferences), and hours trial and error I feel understand a topic good enough to share the knowledge. For sure, I am not an expert, yet. Having in mind my shallow understanding before the research I would love to make other Python developers experience a similar boost of knowledge in this topic.

The presentation is not just a copy of previous speeches. It includes considerations about importing strategy impact on architecture and tips for CI setup to assure consistency.

Moreover, I recently started contributing to the import-linter package to use the knowledge by improving open-source tools (PR: https://github.com/seddonym/import-linter/pull/250). Since I am actively working in the field both open-source and my private work, I am aware of new developments in the field. This will positively impact the quality of the final presentation.

## Abstract as a short post (max 150 characters)

Discover how Python imports work and how they can affect project architecture. Explore importing strategies and enforce consistency with CI.
