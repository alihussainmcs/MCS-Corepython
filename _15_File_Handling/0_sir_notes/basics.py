''''
File handling is an important part of any web application.
Python has several functions for creating, reading, updating, and deleting files.

The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the fil e exists

In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)

syntax:
To open a file for reading it is enough to specify the name of the file:
f = open("demofile.txt")
f = open("demofile.txt", "rt")
Because "r" for read, and "t" for text are the default values, you do not need to specify them.
'''

f = open("con.txt")
print("file opened successfully")


# To Read a file

f = open("context.txt", "r")
print(f.read())

# To Read a line
print("____Read single line___")
f = open("context.txt", "r")
print("1", f.readline())
print("2", f.readline())


print("__Read first characters__")
f = open("context.txt", 'r')
print(f.readline(3))

 # Write to an Existing File
# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

f = open("context.txt", "a")
f.write("Now the file has more content!")
f.close()

print("open and read the file after the appending:")
f = open("context.txt", "r")
print(f.read())


print("overwrite the content:")

f = open("context.txt", "w")
f.write("I have overwrite the content!")
f.close()

print("after overwriting")
f = open("context.txt", "r")
print(f.read())
