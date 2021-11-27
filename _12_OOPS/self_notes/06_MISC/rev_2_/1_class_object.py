"""
# Store Vehicle details and display its details

CRUD    Datatype                State              Behavior
-----------------------------------------------------------------------
CR      int str float           name mileage capacity      display_fare_details()
"""
# 3 With Functions
print("--------------With Functions-------------------")

# STATE
name_1 = "School Volvo"
mileage_1 = 12
capacity_1 = 50

# BEHAVIOR


def display_bus_details(name, mileage, capacity):
    print("Bus Details : ", name, mileage, capacity)


display_bus_details(name_1, mileage_1, capacity_1)

print("....................with oops ............................")


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def display_bus_details(self):
        print("Bus Details : ", self.name, self.mileage, self.capacity)


s = Vehicle("School Volvo", 12, 50)
s.display_bus_details()
