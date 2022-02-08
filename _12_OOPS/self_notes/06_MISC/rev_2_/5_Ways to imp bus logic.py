"""
OOPs : Object Oriented Programming
Why oops : To overcome drawback of direct state initialization(STATE + BEHAVIOR)

    obj.method().method1().method().method()
type declaration : int x = 10
                       x = 10

CRUD DATATYPE   STATE + BEHAVIOR

list1  = [1,2,3]
1. Builtin functions     : print("Length of list : ",len(list1))
2. DecisionMaking,Loops  : list1 = [1,2,3]  Beh : for loop            # we will never implement
3. Functions             : list1 = [1,2,3]  Beh : function : for loop
                            # STATE   # BEHAVIOR
4. OOPs                  : class : STATE + BEHAVIOR
"""

# REQUIREMENT : Find length of the given list
# 1. CRUD       2. Datatype   3. State Behavior
# 1. Retrieval
# 2. list(input) int
# 3. State (Data)  Behavior (Functionality implementation)

# Approach 0 : Using Builtin functions
list1 = [1, 2, 3, 4, 5]
print("---------Approach 0 : Using Builtin functions----------")
print("Length of list :", len(list1))

# Approach 1 : Normal code
print("---------Approach 1 : Normal code----------")
# STATE
list1 = [1, 2, 3, 4, 5]  # customer provided input
le1 = 0  # To work on requirement
# BEHAVIOR
for each in list1:
    le1 += 1
print("Length of list :", le1)

# Disadvantage : Code reusability is missing


print("---------Approach 2 : Using functions----------")

# Approach 2 : Using functions
# STATE
list1 = [1, 2, 3, 4, 5]


# BEHAVIOR
def find_length(in_list):
    le = 0
    for _ in in_list:
        le += 1
    # print("Length of list : ", le)
    return le


# find_length(list1) # 2.1
val = find_length(list1)  # 2.2
print("Length of list :", val)
print("Length of list :", find_length(list1))  # 2.3

# Using Functions
list1 = [1, 2, 3, 4, 5]


def find_length(in_list):
    count = 0
    for _ in in_list:
        count += 1
    print("Length of list : ", count)


# Disadvantage : No security for State. To avoid this,use class structure

print(".............................................")


class SequenceLength:
    def __init__(self):
        pass

    # BEHAVIOR
    @staticmethod
    def find_length(ab):
        count = 0
        for _ in ab:
            count += 1
        print("Length of list : ", count)


s = SequenceLength()
s.find_length([1, 2, 3, 4])
