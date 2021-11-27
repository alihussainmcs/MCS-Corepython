# 2. Extend()---> method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list

print("*****Extend*****")

print("extend()--->method adds the specified list elements to the end of the current list")


list1 = [1, 2, 3, 4]

print("Normal list 1:", list1)

list2 = [9, 8, 10, 11]

print("Normal list 2:", list2)

list2.extend(list1)

print("List after extending:", list2)

# Add Elements of Tuple and Set to List

languages1 = ["Tamil", "English"]

languages2 = {"Hindi", "Malayalam"}

languages3 = ("French", "Telugu")

languages1.extend(languages2)  # adding set to the list
languages1.extend(languages3)  # adding tuple to the list

print("Updated Languages List:", languages1)




