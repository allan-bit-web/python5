# Base Class: Animal
class Animal:
    def move(self):
        pass  # This will be overridden by subclasses

# Subclass: Dog (Inherits from Animal)
class Dog(Animal):
    def move(self):
        print("Running 🐕")

# Subclass: Bird (Inherits from Animal)
class Bird(Animal):
    def move(self):
        print("Flying 🦅")

# Base Class: Vehicle
class Vehicle:
    def move(self):
        pass  # This will be overridden by subclasses

# Subclass: Car (Inherits from Vehicle)
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass: Plane (Inherits from Vehicle)
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Create objects of each class
dog = Dog()
bird = Bird()
car = Car()
plane = Plane()

# Call the move() method on each object
print("Animal Movements:")
dog.move()  # Output: Running 🐕
bird.move()  # Output: Flying 🦅

print("\nVehicle Movements:")
car.move()  # Output: Driving 🚗
plane.move()  # Output: Flying ✈️
