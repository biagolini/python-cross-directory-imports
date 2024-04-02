# Python Module Import Example

This repository is a demonstration of how to organize and import modules across different folders in a Python project. The structure and code within aim to provide clear examples for handling relative and absolute import paths, facilitating a deeper understanding of Python's module system.

## Project Structure

The project is organized into two main directories: `lib` and `use_cases`. Here's a brief overview of their roles:

- `lib`: Contains reusable code modules, including `shared_functions.py` which has simple mathematical functions, and `math_operations_runner.py` that demonstrates the use of these functions.
- `use_cases`: Contains specific use case implementations that leverage the `lib` directory's modules. It is further divided into subdirectories (e.g., `01_example`, `02_example`), each representing a different scenario or configuration set.

### File and Folder Structure

The project layout is as follows:

```
repo/
│
├── lib/
│   ├── __init__.py
│   ├── shared_functions.py
│   └── math_operations_runner.py
│
└── use_cases/
    ├── 01_example/
    │   ├── __init__.py
    │   ├── config.py
    │   └── main.py
    │
    └── 02_example/
        ├── __init__.py
        ├── config.py
        └── main.py
```

### File and Folder Descriptions

- `lib/`: A directory that contains reusable code.
  - `__init__.py`: Makes 'lib' a Python package.
  - `shared_functions.py`: Defines functions for addition and multiplication.
  - `math_operations_runner.py`: Demonstrates the usage of functions defined in `shared_functions.py`.
- `use_cases/`: Contains specific use case implementations that leverage the `lib` directory's modules.
  - `01_example/`: An example use case directory.
    - `__init__.py`: Makes '01_example' recognizable as a Python module.
    - `config.py`: Configuration variables for the first example.
    - `main.py`: Utilizes `shared_functions.py` with `01_example`'s configuration.
  - `02_example/`: Another example use case directory.
    - `__init__.py`: Makes '02_example' recognizable as a Python module.
    - `config.py`: Configuration variables for the second example.
    - `main.py`: Utilizes `shared_functions.py` with `02_example`'s configuration.

## Importing Modules Across Folders

One of the challenges addressed in this project is importing modules from a different directory which is not a subdirectory of the directory where the Python script is run. This is commonly encountered in projects structured to separate core logic from its applications or use cases.

The approach taken involves modifying the `sys.path` list, which Python uses to search for module files. By appending the path to the `lib` directory to `sys.path`, Python can locate and import the modules contained therein, regardless of the current script's location.

## Running the Project

To effectively run the example use cases and observe the Python module import system in action, it's important to start from the root directory of the project. If you've just cloned or downloaded the project, ensure you're in the directory where this README.md file is located. You can use the terminal (or command prompt) to navigate to the project root.

Once you're in the root directory of the project, you can run the example use cases using the following commands in your terminal:

- For the first example, which demonstrates the use case in `01_example`, enter:

```
python3 ./use_cases/01_example/main.py
```

- For the second example, which is located in `02_example`, use:

```
python3 ./use_cases/02_example/main.py
```

These commands execute the `main.py` script in each example directory. They demonstrate how the project's structure supports importing modules from the `lib` directory into scripts located in the `use_cases` directories, regardless of the current script's location in the project hierarchy.

## Conclusion

This project illustrates a method to structure a Python project and import modules across different directories, addressing a common but sometimes confusing aspect of Python development. It is hoped that this repository will serve as a helpful reference for those looking to understand and apply similar patterns in their own projects.

Feel free to explore the code, experiment with the structure, and adapt the principles to your own needs.
