"""
zipping-file contents compressed and size will reduced

Python zip() method takes iterable or containers and returns a single iterator object, having mapped values
from all the containers.

It is used to map the similar index of multiple containers so that they can be used just using a single entity.

Parameters : Python iterables or containers ( list, string etc )
Return Value : Returns a single iterator object, having mapped values from all the
containers.
"""
# Python code to demonstrate the application of
# zip()

# initializing list of players.
Data_value= [887.3, 843.9, 925.1, 880, 905.1, 874.3, 890.5, 917.7, 895.9, 945.9]


# initializing their scores
Period = [2007.01, 2007.02, 2007.03, 2007.05, 2007.06, 2007.12, 2008.01, 2008.02, 2008.05, 2008.06]

# printing players and scores.
for dv, pr in zip(Data_value, Period):
    print("Player :  %s     Score : %s" % (dv, pr))

print("------------------------------   unzipping the data: ---------------------------------------")

# initializing lists
name = ["Green lantern", "Hulk", "Iron Man", "Ant Man", 'Thor']
roll_no = [101, 102, 103, 104, 105]
marks = [40, 50, 60, 70, 90]

# using zip() to map values
mapped = zip(name, roll_no, marks)

# converting values to print as list
mapped = list(mapped)

# printing resultant values
print("The zipped result is : ", end="")
print(mapped)

print("----------------------------------   unzipping values ----------------------------------------")
# unzipping values
nam_z, roll_noz, marks_z = zip(*mapped)

print("The unzipped result: \n", end="")

# printing initial lists
print("The name list is : ", end="")
print(nam_z)

print("The roll_no list is : ", end="")
print(roll_noz)

print("The marks list is : ", end="")
print(marks_z)
