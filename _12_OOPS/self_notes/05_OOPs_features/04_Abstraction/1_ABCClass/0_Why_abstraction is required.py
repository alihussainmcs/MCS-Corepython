"""
Abstraction : Hiding the implementation details


                              Animal

                 Cat    Dog              Tiger Lion

Super class : Common/Generic behavior
Sub class   : Specific behavior wrt sub class


# SC 1 :When few methods are same for all sub classes,
        few are unique for each sub class #1
#1 .Below is the perfect example_1 of using inheritance
                           Animal
                              eating()
                  Cat      Dog     Tiger      Lion
                    c1()    d1()     t1()       l1()

#2. Methods ==> Only in Super class : **This is wrong approach**
    Animal,Employee : Unnecessarily other behavior also will come to our sub class

                           Animal
                              eating() c1()    d1()     t1()       l1()
                  Cat      Dog     Tiger      Lion

#3. Methods ==> ****  This is wrong approach ****
Only in Sub classes : Code duplication.
For example_1 one method is common for all classes,then code duplication will happen

                  Cat        Dog         Tiger      Lion
                    c1()       d1()       t1()        l1()
                    eating()   eating()   eating()    eating()




# SC 2 :When all the methods are same for all sub classes
                           Animal
                                eating()
                                running()
                                sleeping()
                  Cat      Dog     Tiger      Lion

# SC 3 :When combination of common,different implementation required

                           Animal
                                eating()    #body
                                running()   #body
                                sleeping()  #dont give body  (required in unique way)

                  Cat          Dog       Tiger      Lion
                  sleeping() sleeping() sleeping() sleeping()   # Method overriding

So solution here is : make sleeping() method as "abstract method" not concrete method


"""


class Animal:
    def __init__(self):
        pass

    def eating(self):  # eating() is required for all sub classes,but they required in unique way
        pass


class Cat(Animal):

    def eating(self):
        print("Cat Eating")


class Tiger(Animal):

    def eating(self):  # method overriding
        print("Tiger Eating")


animal = Animal()
animal.eating()

cat = Cat()
cat.eating()

tig = Tiger()
tig.eating()

print("-----------------------")


class Bank:
    def bank_info(self):
        print("Welcome to bank")

    def interest(self):
        # "Abstract Method"
        pass


# Sub class/ child class of abstract class
class SBI(Bank):
    def interest(self):
        print("In sbi bank 5 rupees interest")


s = SBI()
s.bank_info()
s.interest()
