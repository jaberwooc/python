from  __future__ import annotations
from abc import ABC,abstractmethod
import os
##stratergy class
class Duck(ABC):
    fliybehaivor=0
    quackbehaivor=0
    @abstractmethod
    def display(self):
        pass

    def perfomQuack(self):
        return self.quackbehaivor.quack()
    
    def perfomfly(self):
        return self.fliybehaivor.fly()
    
    def setQuackbehaivor(self,qb:QuackBehaivor):
        self.quackbehaivor = qb
    
    def setflybehaivor(self,fb:FlyBehaivor):
        self.fliybehaivor = fb
    
    def swim(self):
        return print('All ducks float, even decoy s!')
##concret class
class MallardDuck(Duck):
    def __init__(self) -> None:
        self.fliybehaivor = FlyWithWing()
        self.quackbehaivor = Quack()

    def display(self):
        return print('Im model Duck MallarDuck')
        

class RedHeadDuck(Duck):
    def __init__(self) -> None:
        self.fliybehaivor = FlyRocketPowered()
        self.quackbehaivor = Quack()
    def display(self):
        return print('Im model Duck RedHeadDuck')
        

class RubberDuck(Duck):
    def __init__(self) -> None:
        self.fliybehaivor = FlyNoWay()
        self.quackbehaivor = Squeak()
    def display(self):
        return print('Im model Duck RubberDuck')

class DecoyDuck(Duck):
    def __init__(self) -> None:
        self.fliybehaivor = FlyNoWay()
        self.quackbehaivor = MuteQuack()
    def display(self):
        return print('Im model Duck DecoyDuck')

class FlyBehaivor(ABC):
    @abstractmethod
    def fly(self):
        pass

class FlyWithWing(FlyBehaivor):
    def fly(self):
        return print('Im Flying!!')

class FlyRocketPowered(FlyBehaivor):
    def fly(self):
        return print('Im Flying with a rocket!!')
    
class FlyNoWay(FlyBehaivor):
    def fly(self):
        return print('I cant Fly!!')

class QuackBehaivor(ABC):
    def quack(self):
        pass

class Quack(QuackBehaivor):
    def quack(self):
        return print('Quack!!')


class Squeak(Quack):
    def quack(self):
        return print('Squeak!!')


class MuteQuack(Quack):
    def quack(self):
        return print('<<silence>>')



if __name__ == "__main__" :
    salir = True
    while(salir):
        os.system('cls')
        print('Ducks!')
        print('select the option')
        print('Select 1 for MallarDuck ')
        print('Select 2 for RedHeadDuck ')
        print('Select 3 for RubberDuck ')
        print('Select 4 for DecoyDuck ')
        type = input('option : ')
        if type == '1':
            mallar = MallardDuck()
            mallar.perfomfly()
            mallar.setflybehaivor(FlyRocketPowered())
            mallar.perfomfly()
            mallar.perfomQuack()
        if type == '2':
            mallar = MallardDuck()
            mallar.perfomfly()
            mallar.setflybehaivor(FlyRocketPowered())
            mallar.perfomfly()
            mallar.perfomQuack()
        if type == '3':
            mallar = MallardDuck()
            mallar.perfomfly()
            mallar.setflybehaivor(FlyRocketPowered())
            mallar.perfomfly()
            mallar.perfomQuack()
        if type == '4':
            mallar = MallardDuck()
            mallar.perfomfly()
            mallar.setflybehaivor(FlyRocketPowered())
            mallar.perfomfly()
            mallar.perfomQuack()