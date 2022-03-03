def isValid(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
            # print(stack)
        elif s == ')':
            try:
                stack.pop()
            except:
                return False

    if len(stack) == 0:
        return True
    else:
        return False


sequence1 = "()"
print(f'Is {sequence1}      valid ? : {isValid(sequence1)}')

sequence1 = ")(()))"
print(f'Is {sequence1}      valid ? : {isValid(sequence1)}')

sequence1 = "("
print(f'Is {sequence1}      valid ? : {isValid(sequence1)}')

sequence1 = "(())((()())())"
print(f'Is {sequence1}      valid ? : {isValid(sequence1)}')

sequence1 = ")test"
print(f'Is {sequence1}      valid ? : {isValid(sequence1)}')

sequence1 = "hi())("
print(f'Is {sequence1}      valid ? : {isValid(sequence1)}')

sequence1 = "(hello))"
print(f'Is {sequence1}      valid ? : {isValid(sequence1)}')

sequence1 = "hello"
print(f'Is {sequence1}      valid ? : {isValid(sequence1)}')

sequence1 = "(hello(0))"

print(f'Is {sequence1}      valid ? : {isValid(sequence1)}')
