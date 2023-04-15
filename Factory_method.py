from __future__ import annotations
from abc import ABC, abstractmethod
import os

# Creador


class PizzaStore(ABC):

    def create_pizza(type):
        
        pass
    
    def order_pizza(pizza: PizzaStore,type) -> None:
        product = pizza.create_pizza(type)
        product.cut()
  

        
class NyPizzaStore(PizzaStore):
    
    def create_pizza(type):
        os.system("cls")
        if type == 'ChessePizza':
            return NYStyleChessePizza()
        elif type == 'VeggiePizza':
            return NYStyleVeggiePizza()
        elif type == 'ClamPizza':
            return NYStyleClamPizza()
        elif type == 'PepperoniePizza':
            return NYStylePepperoniPizza()
        else:
            return print('Selecciona una opcion valida ')
        
class ChicagoPizzaStore(PizzaStore):
    def create_pizza(type) -> Pizza:
        os.system("cls")
        if type == 'ChessePizza':
            return ChicagoStyleChessePizza()
        elif type == 'VeggiePizza':
            return ChicagoStyleVeggiePizza()
        elif type == 'ClamPizza':
            return ChicagoStyleClamPizza()
        elif type == 'PepperoniePizza':
            return ChicagoStylePepperoniPizza()
        else:
            return print('Selecciona una opcion valida ')
        
# Productos
class Pizza(ABC):
    toppings = []
    def prepare(type) -> str:
        print(f"prepparing of the {type}")
        print("Tossing Dough")
        print("Adding Sauce")
        print("Adding Toppings")
        
    def bake() -> str:
        return print("Bake for 25 minutes at 350")
    @abstractmethod
    def cut() -> str:
        return print("Cutting the pizza into diagonal alices")

    def box() -> str:
        return print("Place pizza in official PizzaStore box")


# Productos concretos ny
class NYStyleChessePizza(Pizza):
    def __init__(self) -> None:
        namme = 'NY style Sauce and Chesse Pizza'
        dough = 'Thin Crust dough'
        sauce = 'Marinara Sauce'
  
    def cut() -> str:
        return print("Cutting the pizza into square alices")


class NYStyleVeggiePizza(Pizza):
    def prepare(self) -> str:
        return print("{prepparing of the VeggiePizza}")


class NYStyleClamPizza(Pizza):
    def prepare(self) -> str:
        return print("{prepparing  of the ClamPizza}")


class NYStylePepperoniPizza(Pizza):
    def prepare(self) -> str:
        return print("{prepparing of the PepperoniPizza}")


# Productos concretos chicago
class ChicagoStyleChessePizza(Pizza):
    def __init__(self) -> None:
        self.namme = 'Chicago style Sauce and Chesse Pizza'
        dough = 'Thin Crust dough'
        sauce = 'Marinara Sauce'
    def cut() -> str:
        return print("Cutting the pizza into square alices")

        


class ChicagoStyleVeggiePizza(Pizza):
    def prepare(self) -> str:
        return print("{prepparing of the VeggiePizza}")


class ChicagoStyleClamPizza(Pizza):
    def prepare(self) -> str:
        return print("{prepparing of the ClamPizza}")


class ChicagoStylePepperoniPizza(Pizza):
    def prepare(self) -> str:
        return print("{prepparing of the PepperoniPizza}")




        
if __name__ == "__main__":
    print("Hola que vas a Ordenar?")
    print("Selecciona 1 para ChessePizza")
    print("Selecciona 2 para VeggiePizza")
    print("Selecciona 3 para ClamPizza")
    print("Selecciona 4 para PepperoniePizza")
    type = input('opcion :')

    if type == '1':
        PizzaStore.order_pizza(NyPizzaStore,'ChessePizza')
    elif type == '2':
        PizzaStore.order_pizza(NyPizzaStore,'VeggiePizza')
    if type == '3':
        PizzaStore.order_pizza(NyPizzaStore,'ClamPizza')
    elif type == '4':
        PizzaStore.order_pizza(NyPizzaStore,'PepperoniePizza')
