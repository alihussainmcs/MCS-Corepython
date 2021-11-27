"""
Class variable     : Will be initialized when class is loaded by interpreter
                    and memory allocation will be done at the loading itself
Instance variable : When we create an object for class,these will get initialized
"""


class MathDojo(object):
    def __init__(self):
        self.sum = 0

    def add(self, *pars):
        for par in pars:
            if type(par) == int or type(par) == float:
                self.sum += par
            elif type(par) == list or type(par) == tuple:
                for item in par:
                    self.sum += item
        return self

    def subtract(self, *pars):
        for par in pars:
            if type(par) == int or type(par) == float:
                self.sum -= par
            elif type(par) == list or type(par) == tuple:
                for item in par:
                    self.sum -= item
        return self


md = MathDojo()
print(md.add([1], (3, 4)).add((3, 5, 7, 8), [2, 4.3, 1.25]).subtract(2, [2, 3], [1.1, 2.3]).sum)

print("............................................................")


class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print("Current health: " + str(self.health))
        return self


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name, 150)

    def pet(self):
        self.health += 5
        return self


class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name, 170)

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        super(Dragon, self).display_health()
        print("I am a dragon!")
        return self


generic = Animal("Jenny", 100)
generic.walk().walk().walk().run().run().display_health()

fido = Dog("Fido")
fido.walk().walk().walk().run().run().pet().display_health()

draco = Dragon("Draco")
draco.fly().fly().fly().display_health()

