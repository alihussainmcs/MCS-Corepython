# working with Binary Files
"""
Binary Files handles data in form of bytes.
It can be used to read images, audio, video files. such as bytes, megabytes, gigabytes
To open a Binary file for reading purpose use 'rb' b(binary) is attached to r(read) represents it is a binary file.
similarly to write a binary file use 'wb' represents w-write, b-bytes
To read bytes from binary file  use read()
To write bytes into binary file use write()

"""
f = open('ang4.jpg', 'rb')
b = open('ang5.jpg', 'rb')

f1 = open('ang6.jpg', 'wb')
# read bytes from f1 and write the bytes to f2
bytes_1 = f.read()
f1.write(bytes_1)
print("copy data to ang4.jpg  successfully")
f1.close()
f.close()
b.close()
