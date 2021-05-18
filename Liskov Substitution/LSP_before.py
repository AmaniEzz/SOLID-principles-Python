"""
The Liskov Substitution Principle states that subclasses should be substitutable for their base classes.
If S is a subtype of T, then objects of type T may be replaced with objects of type S,
without altering the correctness of the program.
"""

# Violation of LCP

class Engine:
    def on(self):
        # Complex logic for starting vehicle's engine ....
        return "engine is on"

class Vehicle():
    def __init__(self, name: str, speed: float):
        self.name = name
        self.speed = speed
        self.engine = Engine

    def start_engine(self, engine):
        pass

class Car(Vehicle):
    def start_engine(self, engine):
        print(f"Strating {self.name}'s engine...")
        return engine.on()

class ElectricCar(Vehicle):
    def start_engine(self):
        # throwing an exeption by the child class for a not supported method.
        return AssertionError("electric cars has no engine")


"""
In ElectricCar class violates the LSP. Cause the Vehicle class has an engine method. 
Electric cars has no engine (they work by battery pack). So we could not start any engine.
So we was forced to write exception handler, or maybe reture "0" or "None", which is not the best practice!
Beacause code throws a run time error or exception or also might not work as expected
and that leads to program failure or incorrect results.
"""

if __name__ == "__main__":

    car_engine = Engine()
    bmw = Car("BMW", 260.00)
    print(bmw.start_engine(car_engine))
    tesla = ElectricCar("Tesla", 60.0)
    print(tesla.start_engine())