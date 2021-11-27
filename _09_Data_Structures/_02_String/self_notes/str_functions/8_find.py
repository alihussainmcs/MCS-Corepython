
# find(str, beg=0 end=len(string))
mg = 'hi hello hi hello hi hi '

Str = "this is string example....wow!!!"

print("String Str is : ", Str)

print(" find(str, beg=0 end=len(string))")

print(""" Determine if str occurs in string or in a substring of string if starting index beg 
      and ending index end are given returns index if found and -1 otherwise. """)

print(" Using find function ", mg.find('hi', 0, len(mg)))

print(" Using find function ", mg.find('hello', 0, len(mg)))

print(" Using find function ", mg.find('py', 0, len(mg)))
