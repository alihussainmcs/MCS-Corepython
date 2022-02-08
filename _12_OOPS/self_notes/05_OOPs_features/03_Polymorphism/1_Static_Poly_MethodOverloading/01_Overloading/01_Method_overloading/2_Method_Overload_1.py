class FeedbackForm:

    def __init__(self):
        pass

    @staticmethod
    def feedback(rating=10, comments=None):  # method overloading (function overloading)
        print("Feedback is :", rating, ", ", comments)


# Method overloading
feed = FeedbackForm()
feed.feedback()  # Default args
feed.feedback(4)  # Default args
feed.feedback(9, 'Good')  # Positional args
feed.feedback(comments='Very Bad')  # keyword args
feed.feedback(comments='Very Bad', rating=1)  # keyword args

'''
In java/.net
def feedback(self):
    pass

def feedback(self, rating):
    pass

def feedback(self, rating, comments):
    pass

def feedback(self,comments):
    pass
'''


# Function overloading
def sum(a=10, b=20, c=30):
    print("Sum is ", a + b + c)


# Overloading - Depends on how many arguments we are passing
sum()
sum(15)
sum(15, 25)
sum(15, 25, 35)
sum(b=200, a=100)
sum(b=200, c=300)
sum(a=100, c=300)
sum(b=200, a=100, c=300)


class Biryani:
    def __init__(self):
        print("Pass ..............")

    @staticmethod
    def variety(price=200, taste='Good'):
        print("Biryani price ", price, 'and taste is ', taste)


b1 = Biryani()

b1.variety()

b1.variety(300, 'very good')

b1.variety(100, 'Not bad')

b1.variety(80, 'Bad')

b1.variety(70, 'Very Bad')

print("......................................................")


# Program to illustrate method overloading
class Press:
    @staticmethod
    def hello(name=None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')


# Create an instance
obj = Press()

# Call the method
obj.hello()

# Call the method with a parameter
obj.hello('Ali')

print("..........................................................")


class MethodOverloading:
    @staticmethod
    def greeting(name=None):
        if name is not None:
            print('Welcome ' + name)
        else:
            print('Welcome')


# Create an object referencing by variable ob


ob = MethodOverloading()
# call the method greeting without parameter
ob.greeting()
# call the method with parameter
ob.greeting('Alien  !!!')

print(".........................................................")


class MethodOverride1:
    def display(self):
        print("method invoked from base class")


class MethodOverride2(MethodOverride1):
    def display(self):
        print("method invoked from derived class")
        super().display()


ob = MethodOverride2()
ob.display()
