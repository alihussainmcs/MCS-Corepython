"""
Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid.
The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

"""

"""
class Solution:
    @staticmethod
    def isValid(sequence):
        '''
       Function to check if sequence contains valid parenthesis
       :param sequence: Sequence of brackets
       :return: True is sequence is valid else False
       '''
        # Replace the proper pairs until sequence becomes empty or no pairs are present
        while True:
            if '(' and ')' in sequence:
                sequence = sequence.replace('()', '')
            elif '{' and '}' in sequence:
                sequence = sequence.replace('{}', '')
            elif '[' and ']' in sequence:
                sequence = sequence.replace('[]', '')
            else:
                return not sequence


sequence1 = "()"
print(f'Is {sequence1}      valid ? : {Solution().isValid(sequence1)}')

sequence1 = ")(()))"
print(f'Is {sequence1}      valid ? : {Solution().isValid(sequence1)}')

sequence1 = "("
print(f'Is {sequence1}      valid ? : {Solution().isValid(sequence1)}')

sequence1 = "(())((()())())"
print(f'Is {sequence1}      valid ? : {Solution().isValid(sequence1)}')

sequence1 = '{[()]}'
print(f'Is {sequence1}      valid ? : {Solution().isValid(sequence1)}')

sequence1 = '{[()]}{]{}}'
print(f'Is {sequence1}      valid ? : {Solution().isValid(sequence1)}')

sequence1 = ")test"
print(f'Is {sequence1}      valid ? : {Solution().isValid(sequence1)}')

sequence1 = "hi())("
print(f'Is {sequence1}      valid ? : {Solution().isValid(sequence1)}')

sequence1 = "(hello))"
print(f'Is {sequence1}      valid ? : {Solution().isValid(sequence1)}')

sequence1 = "hello"
print(f'Is {sequence1}      valid ? : {Solution().isValid(sequence1)}')

sequence1 = "(hello(0))"
print(f'Is {sequence1}      valid ? : {Solution().isValid(sequence1)}')
"""

"""
Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid.
The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

"""


class Solution:
    @staticmethod
    def isValid(sequence):
        """
       Function to check if sequence contains valid parenthesis
       :param sequence: Sequence of brackets
       :return: True is sequence is valid else False
       """
        for i in sequence:
            if i.isalnum():
                sequence = sequence.replace(i, '')
        # Replace the proper pairs until sequence becomes empty or no pairs are present
        while True:
            if '()' in sequence:
                sequence = sequence.replace('()', '')
            elif '{}' in sequence:
                sequence = sequence.replace('{}', '')
            elif '[]' in sequence:
                sequence = sequence.replace('[]', '')
            else:
                return not sequence


sequence1 = "()"
print(f'Is {sequence1}      valid ? : {Solution().isValid(sequence1)}')

sequence1 = ")(()))"
print(f'Is {sequence1}      valid ? : {Solution().isValid(sequence1)}')

sequence1 = "("
print(f'Is {sequence1}      valid ? : {Solution().isValid(sequence1)}')

sequence1 = "(())((()())())"
print(f'Is {sequence1}      valid ? : {Solution().isValid(sequence1)}')

sequence1 = ")test"
print(f'Is {sequence1}      valid ? : {Solution().isValid(sequence1)}')

sequence1 = "hi())("
print(f'Is {sequence1}      valid ? : {Solution().isValid(sequence1)}')

sequence1 = "(hello))"
print(f'Is {sequence1}      valid ? : {Solution().isValid(sequence1)}')

sequence1 = "hello"
print(f'Is {sequence1}      valid ? : {Solution().isValid(sequence1)}')

sequence1 = "(hello(0))"
print(f'Is {sequence1}      valid ? : {Solution().isValid(sequence1)}')
