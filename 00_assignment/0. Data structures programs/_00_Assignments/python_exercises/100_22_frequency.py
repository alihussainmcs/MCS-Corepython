# Write a program to compute the frequency of the words from the input. 
# The output should output after sorting the key alphanumerically. 

# Input  : New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3
# Output :
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

sentence = input().split(' ')
sentence_counter = {sentence[i]: sentence.count(sentence[i]) for i in range(len(sentence))}
for key, value in sorted(sentence_counter.items()):
	print(key, value)
