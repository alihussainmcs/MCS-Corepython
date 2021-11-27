# CRUD ----- Delete

# Creating a file for delete

data = open('file_for_delete.txt', 'w')
data.write("This file is for deleting purpose !")
data.close()


import os
print("---------------------------------------  if file exist  ------------------------------------------")

if os.path.exists('file_for_delete.txt'):
    os.remove('file_for_delete.txt')
    print("File deleted !")
else:
    print("file does not exist ! ")

print("---------------------------------------  if file not exist  ------------------------------------------")
if os.path.exists('file_for_delete_1.txt'):
    os.remove('file_for_delete.txt')
    print("File deleted !")
else:
    print("file is not exist ! ")
