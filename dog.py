class Dog:
    # Constructor method - called when object is created
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

    # Method (function inside class)
    def bark(self):
        """
                Returns:

        """
        return f"{self.name} says Woof!"

    def get_info(self):
        return f"{self.name} is {self.age} years old"


# Creating objects (instances)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.bark())
print(dog2.bark())

print(dog1.get_info())
print(dog2.get_info())