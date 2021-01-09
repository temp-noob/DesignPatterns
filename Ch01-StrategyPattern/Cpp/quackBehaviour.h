#ifndef INCLUDE_QUACKBEHAVIOUR
#define INCLUDE_QUACKBEHAVIOUR

#include <iostream>

class QuackBehaviour
{
public:
    virtual void quack() = 0;
};

class Quack : public QuackBehaviour
{
public:
    void quack() override
    {
        std::cout << "Quack\n";
    }
};

class MuteQuack : public QuackBehaviour
{
public:
    void quack() override
    {
        std::cout << "<<Silence>>\n";
    }
};

#endif
