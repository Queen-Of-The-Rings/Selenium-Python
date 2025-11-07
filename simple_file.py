
def simple_file_operations():
    # Writing to a file
    print("Writing to file...")
    with open('my_diary.txt', 'w') as file:
        file.write("Dear Diary,\n")
        file.write("Today I learned Python file handling!\n")
        file.write("It's really useful.\n")

    # Reading from a file
    print("\nReading from file:")
    with open('my_diary.txt', 'r') as file:
        content = file.read()
        print(content)

    # Appending to a file
    print("Appending to file...")
    with open('my_diary.txt', 'a') as file:
        file.write("I can't wait to learn more!\n")

    # Reading line by line
    print("\nReading line by line:")
    with open('my_diary.txt', 'r') as file:
        for line_number, line in enumerate(file, 1):
            print(f"Line {line_number}: {line.strip()}")


# Run file operations
simple_file_operations()