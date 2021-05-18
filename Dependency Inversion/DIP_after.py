from abc import ABC, abstractmethod


# define a common interface any food should have and implement
class Food(ABC):
    @abstractmethod
    def bake(self):
        pass
        
    @abstractmethod
    def eat(self):
        pass

class Bread(Food):
    def bake(self):
        print("Bread was baked")
    def eat(self):
        print("Bread was eaten")

class Pastry(Food):
    def bake(self):
        print("Pastry was baked")
    def eat(self):
        print("Pastry was eaten")

class Production:
    def __init__(self, food: Food): # food now is any concrete implementation of abstract class Food
        self.food = food            # this is also dependnecy injection, as it is a parameter not hardcoded

    def produce(self):
        self.food.bake()           

    def consume(self):
        self.food.eat()        