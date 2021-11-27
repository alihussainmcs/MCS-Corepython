"""
winzip software is used to compress files and hence reduce size of files and format of size will be changed

1010 1010                           0
1111 0010    -----> zipping----->  1
0101 1110    <-----unzipping <---- 10
1111 0001                          11

While zipping a file content, a zipping algorithm is used in such away that the algorithm finds out  which bit
pattern is most often repeated that should be  in first position,

in python module Zipfile contains zipfile class that helps us to zip  or unzip with an attribute  ZIP_DEFLATED

f = ZipFile('test.Zip', 'w', ZIP_DEFLATED
f - Zipclass clas object

f.write('file1.txt')
f.write('file2.txt')

"""


# create zip file

from zipfile import *

f = ZipFile('my_first.zip', 'w', ZIP_DEFLATED)

f.write('first.py')
f.write('second.py')

print("zipfile is created")
f.close()

print("--------- To unzip zipfile ----------       ")

from zipfile import *
x = ZipFile('my_first.zip', 'r')
x.extractall()
