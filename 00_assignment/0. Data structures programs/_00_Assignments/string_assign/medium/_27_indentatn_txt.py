# P27. REQ :  remove existing indentation from all of the lines in a given text
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

import textwrap
sample_text = ''' 
America is a beautiful country, actually its official name is United States of America. It's capital is Washington DC.
 Other famous cities in US are New York, Detroit, Chicago, New Jersey, Philadelphia, Florida, San Francisco, Houston, 
 Las Vegas, Seattle, Boston, Miami, Phoenix. The population of the country is about 333 Million with people originating
  from all over the world. Some famous landmarks and sites in worth visiting are statue of liberty in New York, casinos 
  at Las Vegas, Golden Gate bridge at San Francisco, Hollywood, Harvard University, The Capitol and the Gran Canyon. 
  One may spend a lifetime exploring places and sites in America but that won't be enough to cover all of them. Indeed,
   this country is truly blessed with variety of climates, diverse geography, rich flora and fauna and of course 
   wonderful people.
  '''
print("String :", sample_text)
text_without_Indentation = textwrap.dedent(sample_text)
print()
print("Exp. o/p :", text_without_Indentation)
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
