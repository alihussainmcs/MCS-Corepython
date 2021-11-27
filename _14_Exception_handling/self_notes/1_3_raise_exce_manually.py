try:
    amt = 1000
    if amt < 5000:
        raise NameError("Snuff. Funds")  # Raise exception manually
except NameError as name:
    print("AN EXCEPTION OCCURRED ::", name)

'''
In Java, below line is object creation

Java   : NameError name = NameError("Snuff. Funds")

Python : name = NameError("Snuff. Funds")  # Rem. all scenarios
         NameError name = NameError("Snuff. Funds")   #Exception handling
'''


class BookNotAvailable(Exception):
    def __init__(self, book_Id):
        self.bookId = book_Id


def findBook(book_Id):
    print("finding book")
    raise BookNotAvailable(book_Id)


try:

    findBook(12345)

except BookNotAvailable as e:
    print("Book with id : {}  is not available".format(e.bookId))


print("---------------------------------------------------------------------")


class SomethingIsWrong(BaseException):

    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return self.reason


try:
    print('one')
    raise SomethingIsWrong('xyz')

except SomethingIsWrong as somethingWrong:
    print(f'Exception caught: {str(somethingWrong)}')
