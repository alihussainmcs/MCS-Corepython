from abc import ABC, abstractmethod


class Animal(ABC):  # Animal is Abstract Class
    @abstractmethod
    def move(self):
        pass


class Snake(Animal):
    # overriding abstract method
    def move(self):
        print("I can crawl")


class Lion(Animal):
    # overriding abstract method
    def move(self):
        print("I can roar")


K = Snake()

K.move()

K = Lion()

K.move()
