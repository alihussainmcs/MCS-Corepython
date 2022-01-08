# A robot moves in a plane starting from the original point (0,0). 
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
# The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps. 
# Please write a program to compute the distance from current position after a sequence of movement and original point. 
# If the distance is a float, then just print the nearest integer.

# Input :
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2

# Output :
# 2

from math import sqrt

directions = []
for i in range(4):
    directions.append(input().split(' ')[1])

# Assuming the input is supplied in the above sequence of UP, DOWN, LEFT, RIGHT
vertical_point = int(directions[0]) - int(directions[2])
horizontal_point = int(directions[1]) - int(directions[3])

print(round(sqrt(vertical_point ** 2 - horizontal_point ** 2)))
