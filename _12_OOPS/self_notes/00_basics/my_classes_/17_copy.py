class Copy:
    def __init__(self, c_name, c_type, c_price):
        self.c_name = c_name
        self.c_type = c_type
        self.c_price = c_price

    def cop(self):
        print("Copy Details : ", self.c_name, self.c_type, self.c_price)


copy1 = Copy("Long Rough", "Non-blank", 45)
copy1.cop()
