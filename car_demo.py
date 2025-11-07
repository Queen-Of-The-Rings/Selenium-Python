class Car:
    # Class variable - shared by all cars
    wheels = 4

    def __init__(self, brand, color):
        """
        
        :param brand:
        :param color:
        """
        # Instance variables - unique to each car
        self.brand = brand
        self.color = color

    def display_info(self):
        """
                :return:
        """
        return f"{self.color} {self.brand} with {self.wheels} wheels"

# Creating instances
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

print(car1.display_info())  # Output: Red Toyota with 4 wheels
print(car2.display_info())  # Output: Blue Honda with 4 wheels

# Changing class variable affects all instances
Car.wheels = 6
print(car1.display_info())