# 1
str1 = 'abc'
str2 = 'defg'

c = ''
for i in range(len(str1)):
    c += str1[i] + str2[i]

print(c)




# 2
str1 = 'abc'
str2 = 'defg'
def solve(s, t):
   i = j = 0
   result = ""
   while i < len(s) and j < len(t):
      result += s[i] + t[j]
      i+=1
      j+=1
   while i < len(s):
      result += s[i]
      i += 1
   while j < len(t):
      result += t[j]
      j += 1
   return result

print(solve(str1, str2))
