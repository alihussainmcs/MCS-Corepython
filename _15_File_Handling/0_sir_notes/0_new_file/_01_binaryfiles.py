# working with Binary Files
'''
Binary Files handles data in form of bytes.
It can be used to read images, audio, video files. such as bytes, megabytes, gigabytes
To open a Binary file for reading purpose use 'rb' b(binary) is attached to r(read) represents it is a binary file.
similarly to write a binary file use 'wb' represents w-write, b-bytes
To read bytes from binary file  use read()
To write bytes into binary file use write()

'''
# copy an image into new file

f1 = open('pic.jpg', 'rb')
f2 = open('new.jpg', 'wb')

# read bytes from f1 and write the bytes to f2
bytes = f1.read()
f2.write(bytes)
print("copy data to new.jpg  successfully")
f1.close()
f2.close()
