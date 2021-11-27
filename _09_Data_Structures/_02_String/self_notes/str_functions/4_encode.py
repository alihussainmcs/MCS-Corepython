# 4. decode() : Decodes the string using the codec registered for encoding.
str1 = 'hello world'
str2 = str1.encode('UTF-8', 'strict')
print("------------- 4. decode() -----------------")
print('decode() : Decodes the string using the codec registered for encoding..')

print("Encoded string        :", str2)
print("Decoded string        :", str2.decode('UTF-8', 'strict'))

str1 = 'hello'
str2 = str1.encode()
print("Normal  : ", str1)
print("Encoded : ", str2)
print("Decoded : ", str2.decode())

txt = "My name is Ståle"

x = txt.encode()

print(x)
print("........................................................")
txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
