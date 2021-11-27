simpsons = "Homer Simpson is son of Abraham Simpson and Father of Bart Simpson"
chars = simpsons.split(' ')
simpsons_set = {word for word in chars}
print(simpsons_set)


print("--------------------------------------------------------------------------------")

tags = {'Django', 'Pandas', 'Numpy'}
new_tags = {tag.lower() for tag in tags}

print(new_tags)

print("------------------------------------------------------------------------------------")

tags = {'Django', 'Pandas', 'Numpy'}
new_tags = {tag.lower() for tag in tags if tag != 'Numpy'}

print(new_tags)

print("------------------------------------------------------------------------------------")

data = {(m, n) for n in range(2) for m in range(3, 5)}
print(data)

print("------------------------------------------------------------------------------------")
data_1 = {s for s in [1, 2, 3, 4, 5, 6] if s % 2 == 0}
print(data_1)
