"""
A double-ended queue, or deque, supports adding and removing elements from either end. The more commonly used stacks and
queues are degenerate forms of deque, where the inputs and outputs are restricted to a single end.

Example"""
import collections

DoubleEnded = collections.deque(["Mon", "Tue", "Wed"])
DoubleEnded.append("Thu")

print("Appended at right - ")
print(DoubleEnded)

"""
Output-->

Appended at right - 
deque(['Mon', 'Tue', 'Wed', 'Thu'])
"""
DoubleEnded.appendleft("Sun")
print("Appended at right at left is - ")
print(DoubleEnded)

"""
Output-->

Appended at right at left is - 
deque(['Sun', 'Mon', 'Tue', 'Wed', 'Thu'])

"""
DoubleEnded.pop()
print("Deleting from right - ")
print(DoubleEnded)

"""
Output-->

Deleting from right - 
deque(['Sun', 'Mon', 'Tue', 'Wed'])

"""

DoubleEnded.popleft()
print("Deleting from left - ")
print(DoubleEnded)
"""
Output-->

Deleting from left - 
deque(['Mon', 'Tue', 'Wed'])
"""
