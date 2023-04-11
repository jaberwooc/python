from __future__ import annotations
from abc import ABC, abstractmethod


class Simplepizzafactory(ABC):

    def create_pizza(self):
      return VeggiePizza()
    
    def some_operation(self) -> str:
        
        product = self.create_pizza()

        result = f"Creator: The same creator's code has just worked with {product.prepare()}"

        return result


class ConcreteCreator2(Simplepizzafactory):
    def create_pizza(self) -> Pizza:
        return VeggiePizza()
    
    
class Pizza(ABC):
    @abstractmethod
    def prepare(self) -> str:
        pass



class ChessePizza(Pizza):
    def prepare(self) -> str:
        return "{Result of the ChessePizza}"


class VeggiePizza(Pizza):
    def prepare(self) -> str:
        return "{Result of the VeggiePizza}"

class ClamPizza(Pizza):
    def prepare(self) -> str:
        return "{Result of the ClamPizza}"


class PepperoniPizza(Pizza):
    def prepare(self) -> str:
        return "{Result of the PepperoniPizza}"

def order_pizza(pizza: Simplepizzafactory) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
        f"{ pizza.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    order_pizza(ConcreteCreator2())
