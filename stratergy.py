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
    
    def swim(self):
        return print('I cant float!')

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
    type = 0
    while(salir):
        print('MENU')
        print('select the option')
        print('Press 1 - Select Duck')
        print('Press 2 - start')
        print('Press 3 - Change Fly')
        print('Press 4 - Change Quack')
        print('Press 5 - Exit Program')
        op = input()
        os.system('cls')

        if op =='1':
            print('Ducks!')
            print('select the option')
            print('Select 1 for MallarDuck ')
            print('Select 2 for RedHeadDuck ')
            print('Select 3 for RubberDuck ')
            print('Select 4 for DecoyDuck ')
            type = input('option : ')
            os.system('cls')

            if type == '1':
                mallar = MallardDuck()
            elif type == '2':
                mallar = RedHeadDuck()
            elif type == '3':
                mallar = RubberDuck()
            elif type == '4':
                mallar = DecoyDuck()
           
        elif op =='2':
                if type != 0:
                    mallar.perfomfly()
                    mallar.perfomQuack()
                    mallar.swim()
                else:
                    print('First selecte Duck!!')
          
        elif op =='3':
            if type != 0:
                    print('CHANGE')
                    print('select the option')
                    print('Press 1 - FlyRocketPowered ')
                    print('Press 2 - FlyWithWing')
                    print('Press 3 - FlyNoWay')
                    cf = input('option:')
                    os.system('cls')

                    if cf == '1':
                        mallar.setflybehaivor(FlyRocketPowered())
                    elif cf == '2':
                        mallar.setflybehaivor(FlyWithWing())
                    elif cf == '3':
                        mallar.setflybehaivor(FlyNoWay())
                    else :
                        print('Select Valid Option')
            else:
                    print('First selecte Duck')

        elif op =='4':
            if type != 0:
                    print('CHANGE')
                    print('select the option')
                    print('Press 1 - Quack ')
                    print('Press 2 - Squeak')
                    print('Press 3 - MuteQuack')
                    cq = input('option:')
                    os.system('cls')

                    if cq =='1':
                        mallar.setQuackbehaivor(Quack())
                    elif cq =='2':
                        mallar.setQuackbehaivor(Squeak())
                    elif cq =='3':
                        mallar.setQuackbehaivor(MuteQuack())
                    else :
                        print('Select Valid Option')

            else:
                    print('First selecte Duck')
        elif op =='5':
            salir = False
        else:
            print('Select Valid Option')
