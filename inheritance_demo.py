class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

    def sleep(self):
        return f"{self.name} is sleeping"


# Child class inheriting from Animal
class Cat(Animal):
    # Overriding parent method
    def speak(self):
        return "Meow!"


# Another child class
class Dog(Animal):
    def speak(self):
        return "Woof!"


# Using inheritance
cat = Cat("Whiskers")
dog = Dog("Buddy")

print(cat.speak())  # Output: Meow!
print(dog.speak())  # Output: Woof!

print(cat.sleep())