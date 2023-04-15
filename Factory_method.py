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
        product.cut()
        product.bake()
        product.box()
        
  
        
  

##creador concreto
class NyPizzaStore(PizzaStore):
    
    def create_pizza():
        print("Hola que vas a Ordenar?")
        print("Selecciona ChessePizza")
        print("Selecciona VeggiePizza")
        print("Selecciona ClamPizza")
        print("Selecciona PepperoniePizza")
        type = input('opcion :')
        
        if type == 'ChessePizza':
            x = menutops()
            return NYStyleChessePizza(x)
        elif type == 'VeggiePizza':
            x = menutops()
            return NYStyleVeggiePizza(x)
        elif type == 'ClamPizza':
            x = menutops()
            return NYStyleClamPizza(x)
        elif type == 'PepperoniePizza':
            x = menutops()
            return NYStylePepperoniPizza(x)
        else:
            return print('Selecciona una opcion valida ')
        
#Jafet Misael Diaz Chavelas
        
class ChicagoPizzaStore(PizzaStore):
    def create_pizza() -> Pizza:
        print("Hola que vas a Ordenar?")
        print("Selecciona ChessePizza")
        print("Selecciona VeggiePizza")
        print("Selecciona ClamPizza")
        print("Selecciona PepperoniePizza")
        type = input('opcion :')
        if type == 'ChessePizza':
            x = menutops()
            return ChicagoStyleChessePizza(x)
        elif type == 'VeggiePizza':
            x = menutops()
            return ChicagoStyleVeggiePizza(x)
        elif type == 'ClamPizza':
            x = menutops()
            return ChicagoStyleClamPizza(x)
        elif type == 'PepperoniePizza':
            x = menutops() 
            return ChicagoStylePepperoniPizza(x)
        else:
            return print('Selecciona una opcion valida ')
        
# Productos
class Pizza(ABC):
    toppings = []
    name = 0
    
    def prepare(self) -> str:
        print(f"prepparing of the {self.name}")
        print("Tossing Dough")
        print("Adding Sauce")
        print(f"Adding Toppings {self.toppings[0]}")
        
    def bake(self) -> str:
        return print("Bake for 25 minutes at 350")
    def cut(self) -> str:
        return print("Cutting the pizza into diagonal alices")

    def box(self) -> str:
        return print("Place pizza in official PizzaStore box")
    
    def getname(self):
        return self.name


# Productos concretos ny
class NYStyleChessePizza(Pizza):
    def __init__(self,t) -> None:
        self.name = 'NY style Sauce and Chesse Pizza'
        self.dough = 'Thin Crust dough'
        self.sauce = 'Marinara Sauce'
        self.toppings.append(t)
  
    def cut(self) -> str:
        return print("Cutting the pizza into square alices")

#Jafet Misael Diaz Chavelas

class NYStyleVeggiePizza(Pizza):
   def __init__(self,t) -> None:
        self.name = 'NY style Sauce and Veggie Pizza'
        self.dough = 'Thin Crust dough'
        self.sauce = 'Marinara Sauce'
        self.toppings.append(t)


class NYStyleClamPizza(Pizza):
  def __init__(self,t) -> None:
        self.name = 'NY style Sauce and Clam Pizza'
        self.dough = 'Thin Crust dough'
        self.sauce = 'Marinara Sauce'
        self.toppings.append(t)


class NYStylePepperoniPizza(Pizza):
    def __init__(self,t) -> None:
        self.name = 'NY style Sauce and Pepperoni Pizza'
        self.dough = 'Thin Crust dough'
        self.sauce = 'Marinara Sauce'
        self.toppings.append(t)


# Productos concretos chicago
class ChicagoStyleChessePizza(Pizza):
    def __init__(self,t) -> None:
        self.name = 'Chicago style Sauce and Chesse Pizza'
        self.dough = 'Extra Thick Crust dough'
        self.sauce = 'Flum Tomato Sauce'
        self.toppings.append(t)

    def cut(self) -> str:
        return print("Cutting the pizza into square alices")

        


class ChicagoStyleVeggiePizza(Pizza):
  def __init__(self,t) -> None:
        self.name = 'Chicago style Sauce and Veggie Pizza'
        self.dough = 'Extra Thick Crust dough'
        self.sauce = 'Flum Tomato Sauce'
        self.toppings.append(t)



class ChicagoStyleClamPizza(Pizza):
    def __init__(self,t) -> None:
        self.name = 'Chicago style Sauce and Clam Pizza'
        self.dough = 'Extra Thick Crust dough'
        self.sauce = 'Flum Tomato Sauce'
        self.toppings.append(t)


#Jafet Misael Diaz Chavelas

class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self,t) -> None:
        self.namme = 'Chicago style Sauce and Pepperoni Pizza'
        self.dough = 'Extra Thick Crust dough'
        self.sauce = 'Flum Tomato Sauce'
        self.toppings.append(t)



def menutops():
        os.system("clear")
        print('adding toppings?')
        print('select Grated Regiano Chesse')
        print('select Shered Mozzarella Chesse')
        x=input('option:')
        return x
        

 #Jafet Misael Diaz Chavelas
       
if __name__ == "__main__":
        PizzaStore.order_pizza(NyPizzaStore)
        PizzaStore.order_pizza(ChicagoPizzaStore)
