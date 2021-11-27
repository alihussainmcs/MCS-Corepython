# CRUD ----- Update
data = open('my_text.txt', 'a')
data.write('I do coding in python ! ')
data.close()

data = open('my_text.txt')
print(data.readlines())

