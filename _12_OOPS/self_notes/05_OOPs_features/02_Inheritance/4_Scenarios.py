"""
  Super class       Sub class
  ================================
class SuperA:      class SubB:
  m1()              0                : Sub class will inherit method from super class
  m1()              m1()             : Sub class overridden inherited method
  m1() m2()         0                : Sub class inherits 2 super class methods
  m1() m2()         m3() m4()        : Sub class inherits 2 super class methods,its own 2 methods
  m1() m2()         m1()* m3() m4()  : Sub class inherits 2 super class methods,its own 2 methods
                                        overridden method m1()
                                        inherited method m2()
                                        own specific methods m3() m4()

"""


class Parent:
    def __init__(self):
        self.parent_attribute = 'I am a parent'

    def parent_method(self):
        print('Back in my day...')


# Create a child class that inherits from Parent
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.child_attribute = 'I am a child'


# Create instance of child
child = Child()

# Show attributes and methods of child class

print(child.child_attribute)

print(child.parent_attribute)

child.parent_method()


child1 = Child()

# Show attributes and methods of child class

print(child1.child_attribute)

print(child1.parent_attribute)

child1.parent_method()

