# P56. REQ :  find the 2nd most repeated word in a given string
"""
1. CRUD       -->  Retrieval
2. STATE      -->  String
3. BEHAVIOR   -->   str    |     =    |   for, if/else
"""

# 0. Mathematics
"""

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# 2. Algorithm
print("--------2 Algorithm              ----------")

# 3 Using Functions
print("--------3 Using Functions        ----------")


def word_count(str_a):
    counts = dict()
    words = str_a.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    counts_x = sorted(counts.items(), key=lambda kv: kv[1])
    # print(counts_x)
    return counts_x[-2]


str_s = '''Both of these issues are fixed by postponing the evaluation of annotations. Instead of compiling code which
        executes expressions in annotations at their definition time, the compiler stores the annotation in a string
        form equivalent to the AST of the expression in question. If needed, annotations can be resolved at runtime 
        using typing.get_type_hints(). In the common case where this is not required, the annotations are cheaper to
        store (since short strings are interned by the interpreter) and make startup time faster.'''

print("String str_s is :", str_s)
print('2nd most word count is :', word_count(str_s))

str_1 = "ab ca bc ab ca ab"
print("String str_1 is :", str_1)

print('2nd most word count is :', word_count(str_1))

# 4 OOPS
print("--------4 Object Oriented        ----------")

# 5 Exception handling
print("--------5 Exception handling     ----------")

# 6 File Handling
print("--------6 File Handling          ----------")

# 7 Database interaction MVC
print("--------7 Database interaction   ----------")

# 8 UI Interaction
print("--------8 UI Interaction         ----------")
