class Table:
    def __init__(self, t_name, t_size, t_clr):
        self.t_name = t_name
        self.t_size = t_size
        self.t_clr = t_clr

    def tab(self):
        print("Table Details : ", self.t_name, self.t_size, self.t_clr)
        
table1 = Table("Foldable Table ", 50, "Black")
table1.tab()
