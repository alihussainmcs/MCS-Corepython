from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass


class Tesla(Car):
    def mileage(self):
        print("The mileage is 30 km/h")


class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25 km/h ")


class Duster(Car):
    def mileage(self):
        print("The mileage is 24 km/h ")


class Renault(Car):
    def mileage(self):
        print("The mileage is 27 km/h ")


t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()

d = Duster()
d.mileage()

'''
# Perfect example_1 for Abstract class

Abstraction - Hiding implementation details
            - 0 to 100%   - combination of concrete and abstract methods
            - 0%          - all concrete methods
            -100%         - all abstract methods
'''
