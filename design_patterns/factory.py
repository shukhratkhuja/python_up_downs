"""
Consider a scenario where you have a company that produces cars, 
and you want to create a factory that produces different types of cars 
based on the customer's requirements. 
You can implement this scenario using the factory pattern as follows:
"""

class Car:
    def __init__(self, name):
        self._name = name

    def drive(self):
        print(f"Driving a {self._name}")

class SportsCar(Car):
    def drive(self):
        print(f"Driving a sporty {self._name}")

class FamilyCar(Car):
    def drive(self):
        print(f"Driving a family-friendly {self._name}")

class CarFactory:
    def create_car(self, car_type):
        if car_type == "sports":
            return SportsCar("sports car")
        elif car_type == "family":
            return FamilyCar("family car")
        else:
            return Car("car")

factory = CarFactory()
car = factory.create_car("sports")
car.drive()

# Output: Driving a sporty sports car


"""
In this example, the CarFactory class acts as a factory for creating different types of cars. 
The create_car method takes a car_type parameter, 
and returns the appropriate type of car based on the value of car_type. 
The client code can then call create_car to get an instance of the desired car, 
without having to know the exact type of car that it will get.
"""