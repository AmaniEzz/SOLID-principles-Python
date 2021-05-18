"""
The Dependency Inversion principle states that our classes should depend upon 
interfaces or abstract classes instead of concrete classes and functions.
"""

class Bread():
    def bake(self):
        print("Bread was baked")
    def eat(self):
        print("Bread was eaten")

class Production:
    def __init__(self, bread: Bread): 
        self.bread = bread  # Dependnecy on concrete implementation is violating DIP

    def produce(self):
        self.bread.bake() 

    def consume(self):
        self.bread.eat() 