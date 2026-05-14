def greeting(name):
    return f"Hello, {name}! Welcome to the calculator."

VERSION = "1.0.0"

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y