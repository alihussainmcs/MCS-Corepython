

#my_file = open("C:/Users/0_sir_notes/Desktop/python_data.txt", 'r')

my_file = open("test.txt", 'r')
print("content type :", type(my_file))
print("File content :", my_file)
print("----------------------")


# Read data from file
for each_line in my_file:
    print(each_line)
    if 'Python' in each_line.split():
        print("YES, Python Word exists in this line")
    else:
        print("No keyword called Python in this line")
    print("-------------------------------")
'''        
# Read data from file
for each_line in my_file:
    words = each_line.split()
    print(words)
'''
my_file.close()
print("End of program")

