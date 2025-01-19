# Consistent importing

**Session type**: Talk  
**Track**: Testing, Quality Assurance, Security  
**Duration**: 00:30

## Abstract (max 2100 characters)

Have you ever wondered what happens behind the scenes when you use import in Python? In this talk, we will demystify Python's import system, explore best practices for managing imports, and discuss how your importing strategy impacts project architecture.

The session will begin with an introduction to Python's modular structure: what modules and packages are, how sys.path influences imports, and what truly happens during the import process. We will also cover the importance of naming conventions and the difference between executing scripts and modules.

Next, we'll dive into various importing strategies and their implications. From absolute versus relative imports to lazy imports, wildcard imports, and typing-specific imports, we’ll clarify how to choose the right approach for maintainable and readable code.

The session will then explore how your importing structure affects the overall architecture of your project. We’ll address challenges like circular dependencies, separation of concerns, and the role of a layered architecture in maintaining flexibility and scalability.

Finally, we'll look at tools and techniques to enforce consistent importing practices. Learn how to integrate tools like Import Linter and Ruff into your CI pipeline to ensure adherence to your chosen strategy and avoid common pitfalls.

Whether you’re a beginner or an experienced Python developer, this talk will provide actionable insights to help you streamline imports. For developers working on large Python projects, consistent importing is crucial. It helps maintain codebases by reducing complexity and avoiding technical debt. Imports directly impact project architecture, influencing modularity and maintainability. In this talk, you’ll learn practical strategies and tools to enforce consistency, making your projects easier to scale and manage.

## Outline (max 1000 characters)

I. How does importing in Python actually works? (10 minutes)

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

After reading some articles and watching videos (there were actually a few already on the importing topic on different Python conferences) I now understand a topic on a level when I can share the knowledge. For sure, I am not an expert, yet. But having in mind my lack of understanding before the research I would love to ensure that other Python developers experience a similar boost of knowledge in this topic.

The presentation is not just a copy of previous speeches. It includes considerations about importing strategy impact on architecture and tips for CI setup to assure consistency.

Moreover, I recently started contributing to the import-linter package to put my knowledge into practice (PR: https://github.com/seddonym/import-linter/pull/250). I believe that in the coming months, I will continue to apply this knowledge, and my practical experience on the topic will improve. This will positively impact the quality of the final presentation.

## Abstract as a short post (max 150 characters)

Discover how Python imports work and how they can affect project architecture. Explore importing strategies and enforce consistency with CI.
