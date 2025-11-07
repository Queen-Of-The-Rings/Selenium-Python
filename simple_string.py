def simple_string_formatting():
    name = "Alice"
    age = 25
    score = 95.5

    # 1. f-strings (Easiest and most readable)
    message1 = f"My name is {name} and I am {age} years old."
    print("f-string example:")
    print(message1)

    # 2. format() method
    message2 = "My name is {} and I am {} years old.".format(name, age)
    print("\nformat() method example:")
    print(message2)

    # 3. % formatting (Old style)
    message3 = "My name is %s and I am %d years old." % (name, age)
    print("\n% formatting example:")
    print(message3)

    # Number formatting with f-strings
    print("\nNumber formatting:")
    print(f"Score: {score}")  # Default
    print(f"Score: {score:.1f}")  # 1 decimal place
    print(f"Score: {score:.0f}")  # No decimal places

    # Calculations inside f-strings
    print(f"\nNext year I will be {age + 1} years old")

    # String methods in f-strings
    print(f"My name in uppercase: {name.upper()}")

simple_string_formatting()
