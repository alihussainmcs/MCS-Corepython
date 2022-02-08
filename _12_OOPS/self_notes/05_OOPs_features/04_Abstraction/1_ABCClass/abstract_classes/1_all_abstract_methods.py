from abc import ABC, abstractmethod

'''
Access modifiers:  private public default protected
_ __



4. ABSTRACTION :
===================
Hiding the implementation details i.e, method body

Class, Abstract Class, Interface


Inheritance: Super class Sub class
           : When all sub classes has common features ==> Define Methods Super class with body
		   : When all sub classes has unique implementation ==> 
		               - Make class as Abstract class(super class)
		               - Define abstract methods* in super class
		               
Abstraction : 0 to 100%
0%   -- In super abstract class,all are concrete methods      define - class
50%  -- 10 methods - 5 abstract methods + 5 concrete methods  define - abstract class
100% -- In super abstract class, all are abstract methods     define - interface

Employee emp = new SoftwareEmployee()
animal R = new Human()
R.move()

'''


class Animal(ABC):  # Animal is Abstract Class
    @abstractmethod
    def move(self):
        pass


class Human(Animal):
    # overriding abstract method
    def move(self):
        print("I can walk and run")


class Snake(Animal):
    # overriding abstract method
    def move(self):
        print("I can crawl")


class Dog(Animal):
    # overriding abstract method
    def move(self):
        print("I can bark")


class Lion(Animal):
    # overriding abstract method
    def move(self):
        print("I can roar")


R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()
