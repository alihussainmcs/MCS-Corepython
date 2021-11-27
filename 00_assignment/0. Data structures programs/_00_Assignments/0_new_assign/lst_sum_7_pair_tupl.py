from itertools import combinations


def closest_pair_sum(lst_, value_):
    return list(t for t in combinations(lst_, r=2) if sum(t) == value_)


lst = [1, 2, 5, 6, 9, 10, 3, 4]
value = 7
print(closest_pair_sum(lst, value))
dumpy = [(1, 6), (2, 5), (3, 4)]
d = []
for i in dumpy:
    d.append(sum(i))


print(d)
