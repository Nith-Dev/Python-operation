# --- 1. Built-in Function Example ---
print("Built-in function: print()")
print(len("Python"))
print(type(42))

# --- 2. User-defined Function ---
def greet(name):
    return f"Hello, {name}!"

print("User-defined function:", greet("Alice"))

# --- 3. Lambda Function ---
square = lambda x: x * x
print("Lambda function result:", square(6))

# --- 4. Recursive Function ---
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Recursive function (factorial of 5):", factorial(5))

# --- 5. Nested Function ---
def outer():
    def inner():
        return "Inner function result"
    return inner()

print("Nested function:", outer())

# --- 6. Higher-order Function ---
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet_with(func):
    return func("Hello")

print("Higher-order function (shout):", greet_with(shout))
print("Higher-order function (whisper):", greet_with(whisper))

# --- 7. Generator Function ---
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

print("Generator function output:")
for number in count_up_to(3):
    print(number)

# --- 8. Coroutine (Async Function) ---
import asyncio

async def say_hello():
    print("Async function: Hello")
    await asyncio.sleep(1)
    print("Async function: World")

print("Running async function...")
asyncio.run(say_hello())

# --- 9. Example: Shopping Cart with Common Function Types ---
products = [
    ("Laptop", 1200, 0.10),
    ("Smartphone", 800, 0.05),
    ("Headphones", 150, 0.20),
]

def apply_discount(price, discount_rate):
    return price * (1 - discount_rate)

final_prices = list(map(lambda p: apply_discount(p[1], p[2]), products))
total = sum(final_prices)

for i, product in enumerate(products):
    print(f"{product[0]}: Original ${product[1]}, After Discount: ${final_prices[i]:.2f}")

print(f"\n\U0001F9FE Total amount due: ${total:.2f}")
