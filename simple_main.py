
def simple_module_demo():
    # Import the entire module
    import simple_math as math

    # Use module functions
    result1 = math.add(10, 5)
    result2 = math.multiply(3, 7)

    print("Using simple_math module:")
    print(f"10 + 5 = {result1}")
    print(f"3 * 7 = {result2}")
    print(f"Is 8 even? {math.is_even(8)}")
    print(f"PI value: {math.PI}")

    # Import specific functions only
    from simple_math import add, is_even

    # Now we can use them directly
    print(f"\nDirect import: 20 + 15 = {add(20, 15)}")
    print(f"Is 7 even? {is_even(7)}")


# Run the module demo
simple_module_demo()