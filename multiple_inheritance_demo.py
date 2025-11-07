

class Flyable:
    def fly(self):
        return "I can fly!"

class Swimmable:
    def swim(self):
        return "I can swim!"

class Duck(Swimmable, Flyable):
    def quack(self):
        return "Quack quack!"

# Duck inherits from both Flyable and Swimmable
duck = Duck()
print(duck.fly())     # Output: I can fly!
print(duck.swim())    # Output: I can swim!
print(duck.quack())   # Output: Quack quack!

# Check Method Resolution Order
print(Duck.__mro__)