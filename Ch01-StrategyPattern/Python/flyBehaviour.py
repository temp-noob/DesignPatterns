from abc import ABC, abstractmethod, ABCMeta

class FlyBehaviour(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'fly') and
                callable(subclass.fly))
    
    @abstractmethod
    def fly(self):
        ...

class FlyWithWings(FlyBehaviour):
    def fly(self):
        print("I'm flying")

class FlyNoWay(FlyBehaviour):
    def fly(self):
        print("I can't fly")
