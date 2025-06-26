# python_functions_guide.py

# ========================================
# 1. What Is a Function?
# ========================================
# A function is a reusable block of code that performs a specific task.

# ========================================
# 2. Defining a Function
# ========================================
def greet():
    print("Hello, world!")

# ========================================
# 3. Calling a Function
# ========================================
greet()  # Output: Hello, world!


# ========================================
# 4. Parameters and Arguments
# ========================================
def greet_with_name(name):
    print("Hello, " + name + "!")

greet_with_name("Alice")  # Output: Hello, Alice!
greet_with_name("Bob")    # Output: Hello, Bob!


# ========================================
# 5. Return Values
# ========================================
def add(a, b):
    return a + b

result = add(3, 5)
print("3 + 5 =", result)  # Output: 8


# ========================================
# 6. Default Parameters
# ========================================
def greet_default(name="stranger"):
    print("Hello, " + name + "!")

greet_default()         # Output: Hello, stranger!
greet_default("Daisy")  # Output: Hello, Daisy!


# ========================================
# 7. Multiple Return Values
# ========================================
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

lowest, highest, total = get_stats([1, 5, 9])
print("Lowest:", lowest)   # Output: 1
print("Highest:", highest) # Output: 9
print("Total:", total)     # Output: 15


# ========================================
# 8. Docstrings
# ========================================
def greet_doc(name):
    """Prints a greeting to the user."""
    print("Hello, " + name + "!")

# Access the docstring:
print(greet_doc.__doc__)  # Output: Prints a greeting to the user.


# ========================================
# 9. Why Use Functions?
# ========================================
# - Organize code into reusable chunks
# - Avoid repeating yourself (DRY principle)
# - Make programs easier to read, test, and debug


# ========================================
# 10. Example: Putting It All Together
# ========================================
def describe_pet(animal, name="Unknown"):
    """Display information about a pet."""
    print(f"I have a {animal}.")
    print(f"My {animal}'s name is {name}.")

describe_pet("dog", "Buddy")
describe_pet("cat")

# ========================================
# END OF FILE
# ========================================
