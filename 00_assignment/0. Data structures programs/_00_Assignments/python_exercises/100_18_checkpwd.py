# A website requires the users to input username and password to register. 
# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria
# Passwords that match the criteria are to be printed, each separated by a comma.

# Input  : ABd1234@1,a F1#,2w3E*,2We3345
# Output : ABd1234@1

valid_password = []
password = input().split(',')
for pwd in password:
    if len(pwd) < 6 or len(pwd) > 12:
        continue
    count_l = count_u = count_n = count_s = 0
    for p in pwd:
        if p in 'abcdefghijklmnopqrstuvwxyz':
            count_l += 1
        if p in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            count_u += 1
        if p in '0123456789':
            count_n += 1
        if p in '$#@':
            count_s += 1
    if count_s != 0 and count_u != 0 and count_n != 0 and count_l != 0:
        valid_password.append(pwd)
print(",".join(valid_password))
