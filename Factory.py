from __future__ import annotations
from abc import ABC, abstractmethod
import os

# Creador


class Simplepizzafactory(ABC):

    def create_pizza(self, type):
        os.system("cls")
        if type == '1':
            return ChessePizza()
        elif type == '2':
            return VeggiePizza()
        elif type == '3':
            return ClamPizza()
        elif type == '4':
            return PepperoniPizza()
        else:
            return print('Selecciona una opcion valida ')


# Productos
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


# Productos concretos
class ChessePizza(Pizza):
    def prepare(self) -> str:
        return print("{prepparing of the ChessePizza}")


class VeggiePizza(Pizza):
    def prepare(self) -> str:
        return print("{prepparing of the VeggiePizza}")


class ClamPizza(Pizza):
    def prepare(self) -> str:
        return print("{Resprepparingult of the ClamPizza}")


class PepperoniPizza(Pizza):
    def prepare(self) -> str:
        return print("{prepparing of the PepperoniPizza}")


def order_pizza(pizza: Simplepizzafactory, type) -> None:
    product = pizza.create_pizza(type)
    product.prepare()
    product.bake()
    product.cut()
    product.box()


if __name__ == "__main__":
    print("Hola que vas a Ordenar?")
    print("Selecciona 1 para ChessePizza")
    print("Selecciona 2 para VeggiePizza")
    print("Selecciona 3 para ClamPizza")
    print("Selecciona 4 para PepperoniePizza")
    type = input('opcion :')
    order_pizza(Simplepizzafactory(), type)
