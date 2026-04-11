class Car:
    total_cars = 0  # Class variable to keep track of total cars created
    def __init__(self,brand,model):
        # self.brand = brand
        self.__brand = brand  # Private attribute
        self.__model = model
        Car.total_cars += 1  # Increment the total cars count when an instance of Car is created

    def get_brand(self):
        return self.__brand

    def display_info(self):
        # return f"Car Brand: {self.brand}, Model: {self.model}"  
        return f"Car Brand: {self.__brand}, Model: {self.__model}"  # Accessing private attribute within the class
    
    def fuel_type (self):
        return "Petrol or Diesel"
    @staticmethod
    def general_description():
        return "Cars are a common mode of transportation used worldwide."
    @property
    def model(self):
        return self.__model
    
# car1 = Car("Toyota", "Corolla")
# print(car1.brand)  # Output: Toyota
# print(car1.model)  # Output: Corolla\

# my_car = Car("Honda", "Civic")
# my_car.model = "Accord"  # Modifying the model attribute of my_car instance
# print(my_car.brand)  # Output: Honda

# print(my_car.display_info()) # Output: Car Brand: Honda, Model: Civic

#inheritence
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def display_battery_info(self):
        return f"Battery Capacity: {self.battery_capacity} kWh"
    
    def fuel_type(self):
        return "Electricity"
    
my_tesla = ElectricCar("Tesla", "Model S", 100)
# print(my_tesla.display_info())  # Output: Car Brand: Tesla, Model: Model S
# print(my_tesla.display_battery_info())  # Output: Battery Capacity: 100

# print(isinstance(my_tesla,Car))
# print(isinstance(my_tesla,ElectricCar))



#Encapsulation
# print(my_car.get_brand())  # Output: Honda
# print(my_car.model)
# print(my_car.display_info())  # Output: Car Brand: Honda, Model: Civic

#Polymorphism
# print(my_car.fuel_type())  # Output: Petrol or Diesel
# print(my_tesla.fuel_type())  # Output: Electricity

# print(f"Total cars created: {Car.total_cars}")  # Output: Total cars created: 3

# print(my_car.general_description())  # Output: Cars are a common mode of transportation used worldwide. but it is static method so it can be called using the class name as well
# print(Car.general_description())  # Output: Cars are a common mode of transportation used


# multiple Inheritence
class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElecticVechile(Battery,Engine,Car):
    pass

my_new_tesla = ElecticVechile("Tesla","Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())



