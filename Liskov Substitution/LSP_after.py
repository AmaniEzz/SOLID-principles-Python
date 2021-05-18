# Solution: Inheritance tree 
"""
child classes inherited from the parent class should not break the functionality
when the child class object replaces the parent class object.

So the class must inherit from the proper parent class in such a way that when the child class
replaces the parent, it doesn't break the actual functionality provided by the parent class.
"""

from LSP_before import Engine

# Parent class
class Vehicle:
    def __init__(self, name: str, speed: float):
        self.name = name
        self.speed = speed

    def get_name(self):
        return f"The vehicle name {self.name}"

    def get_speed(self):
        return f"The vehicle speed {self.speed} mph"
 

# Subclass for vehicles with engines
class VehicleWithEngine(Vehicle):
    def __init__(self, name, speed, engine: Engine):
        super().__init__(name, speed)
        self.engine = engine

    def start_engine(self):
        print(f"Strating {self.name}'s engine...")
        return self.engine.on()
        
class Car(VehicleWithEngine):
    def start_engine(self):
        return super().start_engine()

class Bus(VehicleWithEngine):
    def start_engine(self):
        return super().start_engine()

class MotorCar(VehicleWithEngine):
    def start_engine(self):
        return super().start_engine()


# Subclass for vehicles without engine
class VehicleWithoutEngine(Vehicle):
    def start_moving(self):
        # Complex logic for starting an engine-less vehicles ....
        return f"Start an engine-less vehicle: {self.name}"

class ElectricCar(VehicleWithoutEngine):
    def start_moving(self):
        return super().start_moving()


if __name__ == "__main__":
    car_engine = Engine()
    bmw = Car("BMW", 62.00, car_engine)
    print(bmw.start_engine())

    tesla = ElectricCar("Tesla", 60.0)
    print(tesla.start_moving())
