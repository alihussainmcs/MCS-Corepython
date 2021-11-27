class Book:
    def __init__(self, b_name, b_auth, b_lang):
        self.b_name = b_name
        self.b_auth = b_auth
        self.b_lang = b_lang

    def book_1(self):
        print("Book Details :", self.b_name, self.b_auth, self.b_lang)


book_0 = Book("Python for Data Science", "Ali ", "English")
book_0.book_1()
