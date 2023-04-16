from __future__ import annotations
from abc import ABC, abstractmethod
import os

# Creador
#Jafet Misael Diaz Chavelas

class PizzaStore(ABC):
    @abstractmethod
    def create_pizza():
        
        pass
    
    def order_pizza(self) -> None:
        product = self.create_pizza()
        product.prepare()

           
##creador concreto
class NyPizzaStore(PizzaStore):
    def prepare(self):
        dough = self.createDogh()
        return dough
        

        
#Jafet Misael Diaz Chavelas
        
class ChicagoPizzaStore(PizzaStore):
  pass

        
# Productos
class Pizzaingrdientfactory(ABC):
    toppings = []
    name = 0
    
    def CreateDough(self) -> str:
        return print(f"prepparing of the {self.name}")
     
        
    def CreateSauce(self) -> str:
        return print("Bake for 25 minutes at 350")
    def CreateChesse(self) -> str:
        return print("Cutting the pizza into diagonal alices")

    def CreateVeggies(self) -> str:
        return print("Place pizza in official PizzaStore box")
    
    def CreatePepperoni(self):
        return self.name
    
    def CreateClams(self):
        return self.name

class NYPizzaingrdientfactory(Pizzaingrdientfactory):
    def CreateDough(self) -> str:
        return ThinCrustDough()

class ChicagoPizzaingrdientfactory(Pizzaingrdientfactory):
    pass
  
#Abstract Products
class Dough(ABC):
    def CreateDough(self) -> str:
        pass

class ThinCrustDough(Dough):
    def CreateDough(self) -> str:
        return 'ThinCrustDough'
    
  
class ThickCrustDough(Dough):
    pass
  

class Sauce(ABC):
   pass

class PlumTommatoSauce(Sauce):
    pass
  
class MarianaSauce(Sauce):
    pass

class Chesse(ABC):
   pass

class MozzarellaChesse(Chesse):
    pass
  
class ReggianoChesse(Chesse):
    pass

class Clams(ABC):
    pass

class FrozzenClams(Clams):
    pass
  
class FreshClams(Clams):
    pass


        

 #Jafet Misael Diaz Chavelas
       
if __name__ == "__main__":
        PizzaStore.order_pizza(NyPizzaStore)