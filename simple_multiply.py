"""
Simple Multiply Program

A minimal Python module demonstrating basic multiplication function
with proper documentation for Sphinx.
"""


def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers and return the product.

    This function takes two numbers as input and returns their multiplication result.
    It supports both integers and floating-point numbers.

    Args:
        a (float): The first number to multiply
        b (float): The second number to multiply

    Returns:
        float: The product of a and b

    Raises:
        TypeError: If either argument is not a number

    Example:
        >>> multiply(2, 3)
        6.0
        >>> multiply(2.5, 4)
        10.0
        >>> multiply(0, 5)
        0.0

    Note:
        This function handles both integer and float inputs seamlessly.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")

    return a * b


def main():
    """
    Demonstrate the multiply function with example usage.
    """
    # Example usage
    result1 = multiply(5, 3)
    result2 = multiply(2.5, 4)

    print("Simple Multiply Program Demo")
    print("=" * 30)
    print(f"multiply(5, 3) = {result1}")
    print(f"multiply(2.5, 4) = {result2}")
    print(f"multiply(0, 10) = {multiply(0, 10)}")


if __name__ == "__main__":
    main()