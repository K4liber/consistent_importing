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

I. How does importing in Python works? (10 minutes)

1. Python module
2. Why modular structure?
3. Python package
4. sys.path
5. Importance of package/module naming
6. Execute a script vs execute a module
7. What actually happens when we do import?

II. What is the best importing strategy? (5 minutes)

0. Typing
1. Imports on separate lines
2. Imports at the top of the file
3. Lazy import of heavy modules
4. Absolute imports
5. From module import entity
6. Package vs namespace
7. import module
8. Wildcard imports
9. Import from package 
10. if TYPE_CHECKING

III. How does modularization and packaging strategy impact a Python project architecture? (5 minutes)

1. Python as dynamic and flexible language
2. Circular modules dependencies
3. Circular package dependencies
4. Separation of concerns
5. Layered architecture

IV. How can we enforce the selected strategy in CI? (5 minutes)
1. Import Linter
2. Ruff setup

## Why am I qualified to speak about this topic?

I am currently working on Python project with around 100k lines of code. There were different strategies applied all around the repository when it comes to importing. I decided to understand deeply how importing works in Python and what is the best strategy for it.

After deep debugging, research (there were already a few presentations on the importing topic on different Python conferences), and hours trial and error I feel understand a topic good enough to share the knowledge. For sure, I am not an expert, yet. Having in mind my shallow understanding before the research I would love to make other Python developers experience a similar boost of knowledge in this topic.

The presentation is not just a copy of previous speeches. It includes considerations about importing strategy impact on architecture and tips for CI setup to assure consistency.

Moreover, I recently started contributing to the import-linter package to use the knowledge by improving open-source tools (PR: https://github.com/seddonym/import-linter/pull/250). Since I am actively working in the field both open-source and my private work, I am aware of new developments in the field. This will positively impact the quality of the final presentation.

## Abstract as a short post (max 150 characters)

Discover how Python imports work and how they can affect project architecture. Explore importing strategies and enforce consistency with CI.
