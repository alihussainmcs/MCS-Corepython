from _04_Operators import self_ops

print("From arithmetic : ", self_ops.x)
print("From arithmetic : ", self_ops.emp_id)
print("From arithmetic : ", self_ops.e_name)

print("From arithmetic : ", self_ops.get_data())
print("From arithmetic : ", self_ops.xyz())

from _04_Operators.self_ops import x, emp_id, e_name, get_data, xyz

print("From arithmetic : ", x)
print("From arithmetic : ", emp_id)
print("From arithmetic : ", e_name)
print("From arithmetic : ", get_data())
print("From arithmetic : ", xyz())

'''
# Find even or odd
num = 145
if num % 2 == 0:
    print("Even number",num)
else:
    print("Odd number",num)
'''
def get_result(input_no):
    self_ops.find_even_odd(input_no)

if __name__ == '__main__':
    num = int(input("Enter number : "))
    self_ops.find_even_odd(num)
    # get_result(num)