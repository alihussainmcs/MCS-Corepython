# fromkeys()------method creates a new dictionary from the given sequence of elements with a value provided by the user

print("*****Fromkeys*****")
print("fromkeys()--->Returns a dictionary with the specified keys and value")


'''
With Specifying the Value:
--------------------------
'''
x = ('1', '2', '3')
values = "numbers"

a = dict.fromkeys(x, values)
print(a)

'''
Without Specifying the Value:
-----------------------------
'''
x = ('1', '2', '3')
b = dict.fromkeys(x)  # without specifying the value none will be stored for every key
print(b)