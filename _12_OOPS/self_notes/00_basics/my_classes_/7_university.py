class Univercity:
    # State
    def __init__(self,u_name, u_id, u_add):
        self.u_name = u_name
        self.u_id = u_id
        self.u_add = u_add

    # Behaviour
    def clg(self):
        print("Univercity Details : ", self.u_name, self.u_id, self.u_add)


clg1 = Univercity("RGPV", 4620, "MP")
clg1.clg()
