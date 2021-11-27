class City:
    def __init__(self, c_name, c_pin, c_state):
        self.c_name = c_name
        self.c_pin = c_pin
        self.c_state = c_state

    def city(self):
        print("City Details ", self.c_name, self.c_pin, self.c_state)


city1 = City("Bangalore", "KA-06", "Karnataka")
city1.city()
