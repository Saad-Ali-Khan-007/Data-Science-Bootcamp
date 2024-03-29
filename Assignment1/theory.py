# Define a function in Python and explain its purpose:

# A function in Python is a block of reusable code that performs a specific task. It is defined using the def keyword followed by the function name and parentheses containing optional parameters. The purpose of a function is to encapsulate a set of actions or computations into a single unit that can be easily invoked (called) from different parts of the program.
# Example:


def greet(name):
    print(f"Hello, {name}!")


# Discuss the importance of using functions in Python programming:

# Functions promote code reusability, making programs easier to maintain and understand.
# They allow breaking down complex tasks into smaller, manageable parts, enhancing code organization.
# Functions facilitate abstraction, enabling developers to focus on high-level logic without worrying about implementation details.
# They promote modular programming, encouraging the separation of concerns and enhancing code readability and scalability.
# Differentiate between defining a function and calling a function in Python:

# Defining a function involves writing the function's code block, specifying its name, parameters, and optional return value using the def keyword.
# Calling a function involves invoking the function by using its name followed by parentheses containing any required arguments or parameters. The function's code block is executed when it is called.
# Example:


# Define a function
def add(a, b):
    return a + b


# Call the function
result = add(3, 5)
# Parameters vs Arguments:

# Parameters are placeholders defined in the function's definition that receive values when the function is called.
# Arguments are the actual values passed to a function when it is called, which are assigned to the parameters defined in the function's signature.
# Example:


def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")


greet("Alice")  # 'Alice' is an argument
# What role does the return statement play in a Python function?

# The return statement in a Python function is used to exit the function and return a value (or multiple values) to the caller. It terminates the function's execution and optionally provides a result that can be utilized by the calling code.
# Example:


def square(x):
    return x**2


result = square(4)  # 'result' will be assigned 16
# Explain the concept of function reusability and its significance:

# Function reusability refers to the ability to use a function multiple times in a program or across different programs without modifying its code. Once a function is defined, it can be called from anywhere in the program, promoting code reuse and minimizing redundancy.
# Significance:
# Saves development time by avoiding redundant code.
# Enhances code readability and maintainability.
# Promotes modular programming and facilitates code organization.
# Describe how you can pass multiple parameters to a Python function:

# Multiple parameters can be passed to a Python function by separating them with commas within the parentheses of the function's definition.
# When calling the function, corresponding arguments are provided in the same order as the parameters in the function's definition.
# Example:


def add(a, b, c):
    return a + b + c


result = add(1, 2, 3)  # 'result' will be assigned 6
