# Module variable
PI = 3.14

# Function to add two numbers
def add(a, b):
    """Return the sum of a and b"""
    return a + b


# Function to multiply two numbers
def multiply(a, b):
    """Return the product of a and b"""
    return a * b


# Function to check if number is even
def is_even(number):
    """Return True if number is even"""
    return number % 2 == 0


# This code runs only when the module is executed directly
if __name__ == "__main__":
    print("Testing simple_math module:")
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"multiply(4, 5) = {multiply(4, 5)}")
    print(f"is_even(10) = {is_even(10)}")
    print(f"PI = {PI}")
