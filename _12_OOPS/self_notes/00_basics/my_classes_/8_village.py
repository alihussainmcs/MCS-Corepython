class Village:
    def __init__(self,v_name, v_pin, v_dist):
        self.v_name = v_name
        self.v_pin = v_pin
        self.v_dist = v_dist

    def vilag(self):
        print("Village details :", self.v_name, self.v_pin, self.v_dist)


vil1 = Village("Line Bazar", 841438, "Gopalganj")
vil1.vilag()
