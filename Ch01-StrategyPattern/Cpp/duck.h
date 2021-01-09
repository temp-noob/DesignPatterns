#include <iostream>
#include <flyBehaviour.h>
#include <quackBehaviour.h>

class Duck
{
public:
    Duck() = default;
    virtual void display() = 0;
    void performFly()
    {
        flyBehaviour->fly();
    }
    void performQuack()
    {
        quackBehaviour->quack();
    }
    void swim()
    {
        std::cout << "All ducks float, even decoys\n";
    }

    void setFlyBehaviour(FlyBehaviour *fb)
    {
        flyBehaviour = fb;
    }

    void setQuackBehaviour(QuackBehaviour *qb)
    {
        quackBehaviour = qb;
    }

private:
    FlyBehaviour *flyBehaviour;
    QuackBehaviour *quackBehaviour;
};

class MallardDuck : public Duck
{
public:
    MallardDuck()
    {
        setFlyBehaviour(new FlyWithWings());
        setQuackBehaviour(new Quack());
    }
    void display() override
    {
        std::cout << "I'm a Mallard Duck\n";
    }
};
