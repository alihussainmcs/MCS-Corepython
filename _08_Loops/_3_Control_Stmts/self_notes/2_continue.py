print("...............Continue.......................")

"""
REQ:  # Numbers between 1 to 1000 which are divisble by 5.
      # If value is also divisible by 10 don't display it.

Approach : 
            1. Print number between 1 to 1000
            2. Print number divisible by 5 between 1 to 1000
            3. If value divisible by 10 also ignore it
      
"""
print("Number between 1 to 1000 which is divisible by 5 and not divisible by 10 are :")
for i in range(1, 1001):
    if i % 5 == 0:

        if i % 10 == 0:
            continue
        print(i)
print("..........Loop End............")


