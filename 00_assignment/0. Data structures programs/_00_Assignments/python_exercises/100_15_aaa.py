# Write a program that computes the value of a+aa+aaa+aaaa 
# with a given digit as the value of a.
# Input  : 9
# Output : 11106

a = input()
print(int(a) + int(a+a) + int(a+a+a) + int(a+a+a+a))
