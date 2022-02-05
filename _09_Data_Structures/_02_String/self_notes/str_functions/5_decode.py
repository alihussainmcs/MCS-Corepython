"""
The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.

Syntax

string.encode(encoding=encoding, errors=errors)

Parameter Values

Parameter	Description

encoding	Optional. A String specifying the encoding to use. Default is UTF-8

errors	Optional. A String specifying the error method. Legal values are:

'backslashreplace'	- uses a backslash instead of the character that could not be encoded

'ignore'	- ignores the characters that cannot be encoded

'namereplace'	- replaces the character with a text explaining the character

'strict'	- Default, raises an error on failure

'replace'	- replaces the character with a question mark

'xmlcharrefreplace'	- replaces the character with an xml character

"""

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
