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
        os.system('clear')
        product.prepare()
        product.cut()
        product.bake()
        product.box()
        
           
##creador concreto
class NyPizzaStore(PizzaStore):
     def create_pizza():
        print("NEW YORK STORE")
        print("Hola que vas a Ordenar?")
        print("Selecciona ChessePizza")
        print("Selecciona VeggiePizza")
        print("Selecciona ClamPizza")
        print("Selecciona PepperoniePizza")
        type = input('opcion :')
        
        if type == 'ChessePizza':
            Pizza.getname( NYStyleChessePizza,'New York Style chesse Pizza')
            return NYStyleChessePizza()
        elif type == 'VeggiePizza':
            Pizza.getname( NYStyleVeggiePizza,'New York Style Veggie Pizza')
            return NYStyleVeggiePizza()
        elif type == 'ClamPizza':
            Pizza.getname( NYStyleClamPizza,'New York Style Clam Pizza')
            return NYStyleClamPizza()
        elif type == 'PepperoniePizza':
            Pizza.getname( NYStylePepperoniPizza,'New York Style Pepperoni  Pizza')
            return NYStylePepperoniPizza()
        else:
            return print('Selecciona una opcion valida ')

        

        
#Jafet Misael Diaz Chavelas
        
class ChicagoPizzaStore(PizzaStore):
       def create_pizza() -> Pizza:
        print("CHICAGO STORE")
        print("Hola que vas a Ordenar?")
        print("Selecciona ChessePizza")
        print("Selecciona VeggiePizza")
        print("Selecciona ClamPizza")
        print("Selecciona PepperoniePizza")
        type = input('opcion :')
        if type == 'ChessePizza':
            Pizza.getname( ChicagoStyleChessePizza,'Chicago Style Chesse  Pizza')
            return ChicagoStyleChessePizza()
        elif type == 'VeggiePizza':
            Pizza.getname( ChicagoStyleVeggiePizza,'Chicago Style Veggie  Pizza')
            return ChicagoStyleVeggiePizza()
        elif type == 'ClamPizza':
            Pizza.getname( ChicagoStyleClamPizza,'Chicago Style Clam  Pizza')
            return ChicagoStyleClamPizza()
        elif type == 'PepperoniePizza':
            Pizza.getname( ChicagoStylePepperoniPizza,'Chicago Style Pepperoni  Pizza')
            return ChicagoStylePepperoniPizza()
        else:
            return print('Selecciona una opcion valida ')

# Productos creador
class Pizza(ABC):
    @abstractmethod
    def prepare(self) -> str:
        pass
        
    def bake(self) -> str:
        return print("Bake for 25 minutes at 350")
    def cut(self) -> str:
        return print("Cutting the pizza into diagonal alices")

    def box(self) -> str:
        return print("Place pizza in official PizzaStore box")
    
    def getname(self,name) -> str:
        self.name = name
        return name
    
# Productos concretos ny
class NYStyleChessePizza(Pizza):
    def prepare(self) -> None:
        print(f'preparing {self.name}')
        self.dough = NYPizzaingrdientfactory.CreateDough()
        self.sauce = NYPizzaingrdientfactory.CreateSauce()
        self.chesse = NYPizzaingrdientfactory.CreateChesse()
  
    def cut(self) -> str:
        return print("Cutting the pizza into square alices")

#Jafet Misael Diaz Chavelas

class NYStyleVeggiePizza(Pizza):
       def prepare(self) -> None:
        print(f'preparing {self.name}')
        self.dough = NYPizzaingrdientfactory.CreateDough()
        self.sauce = NYPizzaingrdientfactory.CreateSauce()
        self.chesse = NYPizzaingrdientfactory.CreateChesse()
        self.Veggies= NYPizzaingrdientfactory.CreateVeggies()
  

class NYStyleClamPizza(Pizza):
    def prepare(self) -> None:
        print(f'preparing {self.name}')
        self.dough = NYPizzaingrdientfactory.CreateDough()
        self.sauce = NYPizzaingrdientfactory.CreateSauce()
        self.chesse = NYPizzaingrdientfactory.CreateChesse()
        self.clam = NYPizzaingrdientfactory.CreateClams()
  


class NYStylePepperoniPizza(Pizza):
    def prepare(self) -> None:
        print(f'preparing {self.name}')
        self.chesse = NYPizzaingrdientfactory.CreateChesse()
        self.pepperoni = NYPizzaingrdientfactory.CreatePepperoni()


# Productos concretos chicago
class ChicagoStyleChessePizza(Pizza):
    def prepare(self) -> None:
        print(f'preparing {self.name}')
        self.dough = ChicagoPizzaingrdientfactory.CreateDough()
        self.sauce = ChicagoPizzaingrdientfactory.CreateSauce()
        self.chesse = ChicagoPizzaingrdientfactory.CreateChesse()
        
    def cut(self) -> str:
        return print("Cutting the pizza into square alices")

        


class ChicagoStyleVeggiePizza(Pizza):
    def prepare(self) -> None:
        self.name = 'NY style Sauce and Clam Pizza'
        print(f'preparing {self.name}')
        self.dough = ChicagoPizzaingrdientfactory.CreateDough()
        self.sauce = ChicagoPizzaingrdientfactory.CreateSauce()
        self.chesse = ChicagoPizzaingrdientfactory.CreateChesse()
        self.Veggies= ChicagoPizzaingrdientfactory.CreateVeggies()
  


class ChicagoStyleClamPizza(Pizza):
       def prepare(self) -> None:
        self.name = 'Chicago style Sauce and Clam Pizza'
        print(f'preparing {self.name}')
        self.dough = ChicagoPizzaingrdientfactory.CreateDough()
        self.sauce = ChicagoPizzaingrdientfactory.CreateSauce()
        self.chesse = ChicagoPizzaingrdientfactory.CreateChesse()
        self.clam = ChicagoPizzaingrdientfactory.CreateClams()

#Jafet Misael Diaz Chavelas

class ChicagoStylePepperoniPizza(Pizza):
   def prepare(self) -> None:
        self.name = 'NY style Pepperoni Pizza'
        print(f'preparing {self.name}')
        self.chesse = ChicagoPizzaingrdientfactory.CreateChesse()
        self.pepperoni = ChicagoPizzaingrdientfactory.CreatePepperoni()

        

# Productos
class Pizzaingrdientfactory(ABC):
    @abstractmethod
    def CreateDough() -> Dough:
        pass     
    
    @abstractmethod
    def CreateSauce() -> Sauce:
        pass
    
    @abstractmethod
    def CreateChesse() -> Chesse:
        pass

    @abstractmethod
    def CreateVeggies() -> Veggie:
        pass
        
    @abstractmethod
    def CreatePepperoni()-> Pepperoni:
        pass
    
    @abstractmethod
    def CreateClams()-> Clams:
        pass

class NYPizzaingrdientfactory(Pizzaingrdientfactory):
    def CreateDough() -> Dough:
        return ThinCrustDough()
     
    def CreateSauce() -> Sauce:
        return MarianaSauce()
    
    def CreateChesse() -> Chesse:
        return ReggianoChesse()

    def CreateVeggies() -> Veggie:
        Veggies = {BlackOlives() , Spinach(),Eggplant()}
        return Veggies
        
    def CreatePepperoni()-> Pepperoni:
        return SlicedPepperoni()
    
    def CreateClams()-> Clams:
        return FreshClams()


class ChicagoPizzaingrdientfactory(Pizzaingrdientfactory):
    def CreateDough() -> Dough:
        return ThickCrustDough()
     
    def CreateSauce() -> Sauce:
        return PlumTommatoSauce()
    
    def CreateChesse() -> Chesse:
        return MozzarellaChesse()
    
    def CreateVeggies() -> Veggie:
        Veggies = {BlackOlives() , Spinach(),Eggplant()}
        return Veggies
        
    def CreatePepperoni()-> Pepperoni:
        return SlicedPepperoni()
    
    def CreateClams()-> Clams:
        return FrozzenClams()
  
#Abstract Products
class Dough(ABC):
    def CreateDough() -> str:
        pass

class ThinCrustDough(Dough):
    def __init__(self) -> None:
        return print('ThinCrustDough')
    
  
class ThickCrustDough(Dough):
       def __init__(self) -> None:
        return print('ThickCrustDough')
  

class Sauce(ABC):
   pass

class PlumTommatoSauce(Sauce):
    def __init__(self) -> None:
        return print('PlumTommatoSauce')

  
class MarianaSauce(Sauce):
      def __init__(self) -> None:
        return print('MarianaSauce')

class Chesse(ABC):
   pass

class MozzarellaChesse(Chesse):
     def __init__(self) -> None:
        return print('MozzarellaChesse')
  
class ReggianoChesse(Chesse):
    def __init__(self) -> None:
        return print('ReggianoChesse')

class Clams(ABC):
    pass

class FrozzenClams(Clams):
    def __init__(self) -> None:
        return print('FrozzenClams')
  
class FreshClams(Clams):
    def __init__(self) -> None:
        return print('FreshClams')

class Veggie(ABC):
    pass


class BlackOlives(Veggie):
    def __init__(self) -> None:
        return print('BlackOlives')
  
class Spinach(Veggie):
    def __init__(self) -> None:
        return print('Spinach')

class Eggplant(Veggie):
    def __init__(self) -> None:
        return print('Eggplant')

class Pepperoni(ABC):
    pass

class SlicedPepperoni(Pepperoni):
    def __init__(self) -> None:
        return print('SlicedPepperoni')

 #Jafet Misael Diaz Chavelas
       
if __name__ == "__main__":
        PizzaStore.order_pizza(NyPizzaStore)
        print(f"\n")
        PizzaStore.order_pizza(ChicagoPizzaStore)

