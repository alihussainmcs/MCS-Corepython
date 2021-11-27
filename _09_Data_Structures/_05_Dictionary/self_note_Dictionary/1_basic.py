order_details_1 = [12123321, 2133213, 12323, 'TLEE234e3', 43243, '560036']
e_data = [1001, 'Ali Hussain', 99000, 'Male', 'Bangalore', '560068', ['111', 'area', ]]
# address
print("Employee data : ", e_data)

e_data = {'eid': 1001,
          'name': 'Ali Hussain',
          'sal': 99000,
          'gender': 'Male',
          'loc': 'Bangalore',
          'pin': [5, 6, 0, 0, 6, 8],
          'address': {'hno': '111', 'area': 'Bommanhalli'}
          }
print("..................................................")
print("House no :", e_data['address']['hno'])
print("Area :", e_data['address']['area'])
print("Pin no   :", e_data['pin'])
print("Pin no  ['pin'][3] :", e_data['pin'][3])

order_details = {'order_no': 123213,
                 'ref_no': 3432,
                 'cust_name': 'Ali Hussain',
                 'del_loc': 'Bangalore',
                 'total_bill': 5430.56,
                 'discount': 239,
                 'disc_percnt': 50,
                 'pin_code': '560068',
                 'no_of_items': 11,
                 }

e_ids = {1, 2, 3, 4, 5, 6}
print("Order details : ", order_details)
print("Location : ", order_details['del_loc'])
print("Order No : ", order_details['order_no'])
# print("Order No : ", order_details[100])


'''
Dictionary : 
    - Mutable data structure
    - Un-ordered
    - Key value pair i.e, item 
    Key properties:
        - Keys must be UNIQUE
        - Keys must be IMMUTABLE
        - Values can be anything

'''
# 1. Keys must be IMMUTABLE and values can be anything
dict1 = {100: 10,
         200: {1: 1, 2: 2},
         102.3: 29,
         True: 'Ali Hussain',
         'Message': [1, 2, 3, 4, 5],
         (1, 2, 3): (1, 2, 3),
         # [1,2,3] : {1:1,2:2},  # TypeError: unhashable type: 'list'
         # {1:1,2:2} : "Hello"   # TypeError: unhashable type: 'dict'
         # {1,2,3} : "Hello"     # TypeError: unhashable type: 'set'
         }

print("Keys immutable : ", dict1)
# Dict keys should not be List, Dictionary, Set

# 2. Keys must be unique
x = 10

dict1 = {101: 100,
         201: 200,
         102: 100
         }
print("Keys must be unique :", dict1.keys())

print("Values can be duplicate :", dict1.values())
