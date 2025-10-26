# Consistent importing

## Elevator pitch (up to 300 characters)

Discover how Python imports work and how they can affect a project architecture. Explore importing strategies and enforce consistency with CI.

## Description (Markdown)

# Abstract

Have you ever wondered what happens behind the scenes when you use import in Python? In this talk, we will demystify Python's import system and explore best practices for managing imports. Moreover, we will discuss how your importing strategy impacts project architecture, influencing modularity and maintainability. For developers working on large Python projects, consistent importing is crucial. It helps maintain codebases by reducing complexity and avoiding technical debt. Finally, we will learn how to integrate tools like Import Linter and Ruff into your CI pipeline to ensure adherence to your chosen strategy and avoid common pitfalls.

Whether you are a beginner or an experienced Python developer, this talk will help you streamline imports. You will learn practical strategies and tools to enforce consistency, making your projects easier to scale and manage.

# Schedule

## I. Why am I talking about this? (~5 minutes)

1. Interesting import approach in a legacy codebase
2. Consistency reduces decision fatigue

## II. How importing in Python works? (~10 minutes)

1. Python interpreter
2. Python module
3. Python package
4. sys.path
5. Package vs namespace

## III. What is the best importing strategy? (~5 minutes)

1. (PEP) Place imports at the top of a file
2. Lazy imports of heavy modules
3. Do not use "if TYPE_CHECKING" to avoid ImportError
4. (PEP) Imports should be grouped
5. Import one definition per line
6. (PEP) Absolute imports
7. Use only well-known abbreviations
8. Avoid using Namespace Packages
9. (PEP) Avoid using wildcard imports
10. Import directly from module where a definition is defined

## IV. How internal dependencies impact a codebase architecture? (~5 minutes)

1. Why to care about clean modular structure?
2. Acyclic dependencies principle (ADP)
3. Python circular imports. A bug or a feature?
4. Circular dependencies between packages

## V. How can we enforce the selected strategy in CI? (~5 minutes)

1. Ruff
2. Import Linter


## Notes (Markdown)

I am currently working on Python project with around 100k lines of code. There were different strategies applied all around the repository when it comes to importing. I decided to understand deeply how importing works in Python and what is the best strategy for it.

After deep debugging, research and hours trial and error I feel understand a topic good enough to share the knowledge. Having in mind my shallow understanding before the research I would love to make other Python developers experience a similar boost of knowledge in this topic.

The presentation is not just a copy of existing speeches. It includes considerations about importing strategy impact on architecture and tips for CI setup to assure consistency.

Moreover, I recently started contributing to the import-linter package to use the knowledge by improving open-source tools (PR: https://github.com/seddonym/import-linter/pull/250). Since I am actively working in the field both open-source and my private work, I am aware of new developments in the field. This will positively impact the quality of the final presentation.

## Tags

Python, Imports, Architecture, Consistency, CI, Ruff, import-linter

## Bio

Senior Full Stack Developer, currently working at Ørsted, with over 6 years of professional experience in software development. Interested in science, digital and energy transformation, sports and music.

## Recording

I already gave the talk on PyCon Greece 2025 conference. Link to the recording: https://youtu.be/ApUEmy62mPQ?t=4735
