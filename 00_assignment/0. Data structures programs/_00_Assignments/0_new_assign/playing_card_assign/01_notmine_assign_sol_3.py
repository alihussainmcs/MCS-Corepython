"""
create a deck of cards assign values to them
shuffle the cards without builtin functions ,add two players distribute cards between them add the values of
cards each player is having who have the more value print he is the winner

"""

import time

list1 = [i for i in range(1, 14)]
list2 = [i for i in range(1, 14)]
list3 = [i for i in range(1, 14)]
list4 = [i for i in range(1, 14)]


def rand_val(y):
    random = int(time.time() ** 2)
    random //= 2
    random %= y
    return random


def sum_list(la):
    sum = 0
    for i in la:
        sum += i
    return sum


list5 = list1 + list2 + list3 + list4
print(list5)
list6 = []
while len(list5) > 0:
    a = rand_val(len(list5))
    list6.append(list5[a])
    del list5[a]
print(list6)
player_1 = []
player_2 = []
run = 0
while run < 26:
    a = rand_val(len(list6))
    player_1.append(list6[a])
    del list6[a]
    b = rand_val(len(list6))
    player_2.append(list6[b])
    del list6[b]
    run += 1

sum_player1 = sum_list(player_1)
sum_player2 = sum_list(player_2)

if sum_player1 > sum_player2:
    print(f"Player 1 is the Winner with point {sum_player1}")
else:
    print(f"Player 2 is the Winner with point {sum_player2}")
