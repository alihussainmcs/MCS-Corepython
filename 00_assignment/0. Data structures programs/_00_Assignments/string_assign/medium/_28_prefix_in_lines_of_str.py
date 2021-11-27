# P28. REQ :  to add a prefix text to all of the lines in a string
"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  str  |     =    |
"""

# 0. Mathematics
"""

"""


# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

str_1 = """ Hey i am a Wichita.Now days i am doing training in AI and Machine learning.I am doing training 
from Github. If you want to join then you are welcome."""
import textwrap
sample_text = """ Hey i am a Ali.Now days i am doing training in AI and Machine learning.I am doing training 
from Github. If you want to join then you are welcome."""
text_without_Indentation = textwrap.dedent(sample_text)
wrapped = textwrap.fill(text_without_Indentation, width=50)

# wrapped += '\n\nSecond paragraph after a blank line.'
final_result = textwrap.indent(wrapped, '> ')
print()
print(final_result)
print()

# 2. Algorithm
print("--------2 Algorithm              ----------")

# 3 Using Functions
print("--------3 Using Functions        ----------")

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
