from abc import ABC, abstractmethod, ABCMeta
from flyBehaviour import *
from quackBehaviour import *

class Duck(ABC):

    def __init__(self):
        self.flyBehaviour: FlyBehaviour = None
        self.quackBehaviour: QuackBehaviour = None

    @abstractmethod
    def display(self, *args):
        ...
    
    def swim(self):
        print('All ducks float, even decoys')

    def performFly(self):
        self.flyBehaviour.fly()
    
    def performQuack(self):
        self.quackBehaviour.quack()

    def setFlyBehaviour(self, flyBehaviour):
        self.flyBehaviour = flyBehaviour

    def setQuackBehaviour(self, quackBehaviour):
        self.quackBehaviour = quackBehaviour
    

class MallardDuck(Duck):

    def __init__(self):
        super().__init__()
        self.flyBehaviour = FlyWithWings()
        self.quackBehaviour = Quack()

    def display(self):
        print("I'm a Mallard Duck")

md = MallardDuck()
md.performFly()
md.performQuack()
md.setFlyBehaviour(FlyNoWay())
md.setQuackBehaviour(Squeak())
md.performFly()
md.performQuack()
