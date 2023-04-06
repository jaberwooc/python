from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

# Diaz Chavelas Jafet Misael 

class Subject(ABC):

    @abstractmethod
    def registerObserver(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def removeObserver(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notifyObserver(self) -> None:
        pass

# Diaz Chavelas Jafet Misael 

class DispleyElement(ABC):
    @abstractmethod
    def display(self):
        pass

# Diaz Chavelas Jafet Misael 

class whaterdata(Subject):
    temperatura: int =None
    humidity: int =None
    pressure: int =None  
    _observers: List[Observer] = []
 

    def registerObserver(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def removeObserver(self, observer: Observer) -> None:
        self._observers.remove(observer)



    def notifyObserver(self) -> None:


        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def measuremetsChanged(self,temperatura,humidity,pressure) -> None:

        print("\nSubject: I'm doing something important.")
        self.temperatura = temperatura
        self.humidity = humidity
        self.pressure = pressure

        self.notifyObserver()

# Diaz Chavelas Jafet Misael 

class Observer(ABC):



    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass

# Diaz Chavelas Jafet Misael 

class CurrenConditionsDisplay(Observer): 
    def update(self, subject: Subject):
        T= subject.temperatura
        RH= subject.humidity
        a = 16.923 + 1.85212 * 10**-1 * T + 5.37941 * RH - 1.00254 * 10**-1 *T * RH + 9.41695 * 10**-3 * T**2 + 7.28898 * 10**-3 * RH**2 + 3.45372 *10**-4 * T**2 * RH - 8.14971 * 10**-4 * T * RH**2 + 1.02102 * 10**-5 * T**2 *RH**2 - 3.8646 * 10**-5 * T**3 + 2.91583 * 10**-5 * RH**3 + 1.42721 * 10**-6* T**3 * RH + 1.97483 * 10**-7 * T * RH**3 - 2.18429 * 10**-8 * T**3 * RH**2+ 8.43296 * 10**-10 * T**2 * RH**3 - 4.81975 * 10**-11 * T**3 * RH**3
        print(f"Current cdonditions {subject.temperatura}  F degrees and {subject.humidity} % humidity")
        print(f"Heat Index is {a}")


# Diaz Chavelas Jafet Misael 

if __name__ == "__main__":
  
    subject = whaterdata()
    observer_a = CurrenConditionsDisplay()
    subject.registerObserver(observer_a)
    subject.measuremetsChanged(80,65,30.4)
    subject.measuremetsChanged(82,70,29.2)
    subject.measuremetsChanged(78,90,29.2)
    subject.removeObserver(observer_a)
