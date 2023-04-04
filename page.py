from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def registerObserver(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def removeObserver(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notifyObserver(self) -> None:
        """
        Notify all observers about an event.
        """
        pass

class DispleyElement(ABC):
    @abstractmethod
    def display(self):
        pass

class whaterdata(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    temperatura: int =None
    humidity: int =None
    pressure: int =None  
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """

    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def registerObserver(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def removeObserver(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notifyObserver(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def measuremetsChanged(self,temperatura,humidity,pressure) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

        print("\nSubject: I'm doing something important.")
        self.temperatura = 10
        self.humidity = 10
        self.pressure = 10

        self.notifyObserver()


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass


"""
Concrete Observers react to the updates issued by the Subject they had been
attached to.
"""

class CurrenConditionsDisplay(Observer): 
    def update(self, subject: Subject):
        print(f"Current cdonditions {subject.temperatura}  F degrees and")



if __name__ == "__main__":
    # The client code.

    subject = whaterdata()

    observer_a = CurrenConditionsDisplay()
    subject.registerObserver(observer_a)

 

    subject.measuremetsChanged(10,10,10)
    subject.removeObserver(observer_a)
