# Effective Software Testing - Python version

This repository contains the code examples in python of the [Effective Software Testing: A Developer's Guide](https://www.manning.com/books/effective-software-testing) book, by [Maurício Aniche](https://www.mauricioaniche.com/).

Each folder contains the code examples of their respective chapter:

    Chapter 1: Effective and systematic software testing
    Chapter 2: Specification-based testing
    Chapter 3: Structural testing and code coverage
    Chapter 4: Design by Contracts
    Chapter 5: Property-based testing
    Chapter 6: Test doubles and mocks
    Chapter 7: Designing for testability
    Chapter 8: Test-Driven Development
    Chapter 9: Larger tests
    Chapter 10: Test code quality

Please go to the [original repository](https://github.com/effective-software-testing/code) to checkout the Java version.

Each folder is an independent [hatch](https://hatch.pypa.io/latest/) project. You should be able to import the project directly in your favorite IDE (e.g. PyCharm, Spyder). You can also run all the tests via hatch test.

I used a [java-to-python-converter](https://www.codeconvert.ai/java-to-python-converter) to speed up the conversion from Java to Python, but made it more Pythonic by hand to keep the linters happy.

To run code coverage in chapter 3, TODO

To run the web tests of chapter 9, TODO

Maybe you found a test I missed or a better way to implement the code. You are most welcome to submit your PRs!


# License and reuse
You are free to reuse and modify the code provided in this repository, for personal or business purposes, as long as the book is always explicitly mentioned as reference. For example, if you are providing training or workshops, you are required to have a dedicated slide with the picture of the book in each of the slide decks that make use of examples from here.
