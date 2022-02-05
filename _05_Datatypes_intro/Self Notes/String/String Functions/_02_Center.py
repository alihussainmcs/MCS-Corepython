# 2. Returns a string which is padded with the specified character

print("------------- 2. center() -----------------")
print("******************")
print("center() : Returns a centered string padded with specified character")
print("******************")

str1 = "Good language"
print("Normal String:", str1)
print("string after center method:  ", str1.center(20))

# center() method will center align the string, using a specified character (space is default) as the fill character.

print("-------------center(length, character)-------------")

# Length---> Length of the returned string
# character---> The character to fill the missing space on each side. Default is " "

str2 = "Programming"
print("Normal String:", str2)
print("With padding Character:", str2.center(25, "*"))  # '*' acts as a padding character
