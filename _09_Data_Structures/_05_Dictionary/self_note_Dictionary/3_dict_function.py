
# len()
e_data = {'eid': 101,
          'name': 'Ali Hussain',
          'sal': 40000,
          'mobile': '9988776655',
          'office': 'Bangalore'
          }

print("Length of dict : ", len(e_data))

# type()
print("Length of dict : ", type(e_data))

# str()
di_str = str(e_data)
print("Dict in string format :", type(di_str), di_str)

# dict()
# di2 = dict({})


# Builtin functions:
print("................Builtin functions.........................")
# 1. keys() :To retrieve all keys from dictionary
print("-----------1,. KEYS----------")
d_keys = e_data.keys()
print("E Data keys : ", d_keys, type(d_keys))
d_keys = list(e_data.keys())
print("E Data keys : ", d_keys, type(d_keys))

print("-----Dictionary keys ------")
for key in e_data.keys():   # list(e_data.keys())
    print(key)

print("-----------2. values()----------")
# values() : To retrieve all values from dictionary
d_vals = e_data.values()
print("E Data values :", d_vals, type(d_vals))
d_vals = list(d_vals)
print("E Data values :", d_vals, type(d_vals))

print("-----Dictionary values ------")
for val in e_data.values():  # list(e_data.values())
    print(val)


print("-----------3. items() ----------")
# 3. items() : To retrieve all items from dictionary
items = e_data.items()
print("E DATA Items : ", items, type(items))
items = list(items)
print("E DATA Items : ", items, type(items))


n1, n2 = (1, 2)  # tuple unpacking
print("Values : ", n1, n2)

print("Iterating through dict items")
for item in e_data.items():
    print(item)

print("-------------------")

for key, val in e_data.items():
    print(key, " --- ", val)


# 4. update()
print("-----------4. update() ----------")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)

dict1 = {1: 1, 2: 2}
dict2 = {3: 3, 4: 4}
dict1.update(dict2)
print("Dictionary Update  : ", dict1, dict2)

print("-----------5. clear() ----------")
di = {1: 1, 2: 2, 3: 3, 4: 4}
print("Before clear : ", di)
di.clear()
print("After clear : ", di)

print("-----------6. fromkeys() ----------")

di = {1: 1, 2: 2}
di = di.fromkeys([10, 20, 30, 40], "Hello")
print("Dictionary from keys : ", di)

print("-----------7. copy() ----------")
di1 = {1: 1, 2: 2}
di2 = di1.copy()
print("-----Before modification-----------")
print("Dict1 copy : ", di1)
print("Dict2 copy : ", di2)
print("-----After modification-----------")
di2['name'] = 'Ali'
print("Dict1 copy : ", di1)
print("Dict2 copy : ", di2)

print("-----------8 . has_key() ----------")

dict1 = {1: 1, 2: 2, 'Hello': 'Ali'}
'''
print("Has key : ", dict1.has_key('Hello'))
print("Has key : ", dict1.has_key(1))
print("Has key : ", dict1.has_key(10))
'''
'''
pop() popitem() setdefault()
'''

print("-----------8 . get() ----------")
# ecommerce:
xyz = {'orderno': 12123232,
       'ref_no': 324324,
       'items_qty': 4,
       'price': 324324,
       'del_addr': []}

# singup loginpage username password

print("Employee data : ", e_data)
print("Employee name : ", e_data['name'])
print("Employee mobile  : ", e_data['mobile'])
# print("Employee name : ",e_data['company'])  # ERROR
print("Employee company : ", e_data.get('company'))  # to avoid exception
print("Employee company : ", e_data.get('company', 'ORACLE'))  # to set default value if key doesnot exists


print("Employee name : ", e_data.get('name'))
print("Employee name : ", e_data.get('mobile'))
print("Employee name : ", e_data.get('mobile', '----------'))
print("Employee name : ", e_data.get('company'))
print("Employee name : ", e_data.get('company', 'ORACLE'))

'''Aadhar card info '''

aadhar_deatils = {'a_no': 54893423210011,
                  'name': 'Ali Hussain',
                  'email': 'ali15436@gmail.com',
                  'mobile': '8899776655',
                  'location': 'Bangalore'
                  }


aadhar_deatils = {'a_no': 54893423210011,
                  'name': 'Ali Hjussain',
                  'location': 'Bangalore'
                  }

'''
Database:
-----------------------------------------------------------------------------
SNo A_NO       NAME         MOBILE       EMAIL                    LOCATION 
-----------------------------------------------------------------------------
11   3243243   0_sir_notes       7406900500    nettemmadhu@gmail.com    Bangalore
11   3243243   0_sir_notes       null          null                     Bangalore
------------------------------------------------------------------------------
'''