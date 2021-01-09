from abc import ABC, abstractmethod, ABCMeta

class QuackBehaviour(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'quack') and
                callable(subclass.quack))
    
    @abstractmethod
    def quack(self):
        ...

class Quack(QuackBehaviour):
    def quack(self):
        print("Quack")

class MuteQuack(QuackBehaviour):
    def quack(self):
        print("<<Silence>>")

class Squeak(QuackBehaviour):
    def quack(self):
        print("Squeak")
