class AgeError(Exception):
    """Exceptions raised for errors in input
       Attributes:
         Expression : Input expression in which error occured.
         Message    : Explanation of error
    """
    '''
    def __init__(self,expression,message):
        self.expression=expression
        self.message=message
    '''

    def __init__(self, message):
        self.message = message


'''
try:
    age = int(input("Enter your age"))
    if(age >= 18): #Raise exception
        print("---You are eligible to vote-------")
    else:
        raise Exception("Not eligible") # manually raising exception as per our use case
    print("-----Voting process completed------")
except Exception as ageex:   # Exception ageex = Exception("Not eligible")    # 5L Can <== 5L Water
    print(ageex)



try:
    age = int(input("Enter your age"))
    if(age >= 18): #Raise exception
        print("---You are eligible to vote-------")
    else:
        raise AgeError("Not eligible") # manually raising exception as per our use case
    print("-----Voting process completed------")
except AgeError as ageex:   # AgeError ageex = AgeError("Not eligible")    # 2L Can <== 2L Water
    print(ageex)

'''

try:
    age = int(input("Enter your age"))
    if age < 18:
        raise AgeError("**Not eligible**")  # manually raising exception as per our use case
    print("---You are eligible to vote-------")
    print("-----Voting process completed------")
except Exception as ageex:  # Exception ageex = AgeError("Not eligible")    # 5L Can <== 2L Water
    print("Exception :", ageex)
except AgeError as aer:
    print("AgeError :", aer)

'''
Correct approach
----------------
except AgeError as aer:
    print("AgeError :", aer)
except Exception as ageex: 
    print("Exception :", ageex)

'''

print("------------------------------------------------------------------------------")

import hug

from project import exceptions


@hug.exception((exceptions.CustomExceptionTypeOne, exceptions.CustomExceptionTypeTwo))
def handle_custom_exceptions(exception):
    # handles the passed in custom exception, able to return a different response here:
    return {'error': 'No error here!'}


@hug.exception(Exception)
def handle_exception(exception):
    return {'error': "Python broke again! Don't blame us!"}


print("-------------------------------------------")


class GitHubApiException(Exception):

    def __init__(self, status_code):
        if status_code == 403:
            message = "Rate limit reached. Please wait a minute and try again."
        else:
            message = f"HTTP Status Code was: {status_code}."

        super().__init__(message)
