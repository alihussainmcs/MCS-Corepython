"""def __new__(cls,*args,**kwargs):
        print(cls)
        print("*args =",*args)
        print("**kwargs =",**kwargs)
  """


# http://agiliq.com/blog/2012/06/__new__-python/
# http://spyhce.com/blog/understanding-new-and-init

class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, l1):
        Shape.__init__(self)
        self.length = l1

    def area(self):
        return self.length * self.length


aSquare = Square(3)
print(aSquare.area())
