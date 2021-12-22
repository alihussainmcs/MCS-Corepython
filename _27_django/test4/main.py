# #myproject
#     # app1
#     #app2
#
# #models.py
# #setting.py
# #main.py
# #myproject --> project name
#     #myproject --> module of the project
# #pycharm
#     #folder view
#     #terminal
#     #code eitor
#
#
#
# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
#
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/





class A:


    def _init_(self,user_size):
        self.size=user_size

    def parenthesis_append(self, result,open=0, close=0):
        if (close == self.size):
            #  When get the result of parentheses in given size
            print(result)
            return

        if (open < self.size):
            #  Add open parentheses
            self.parenthesis_append(result + "(",
                                 open + 1, close)

        if (open > close):
            #  Add close parentheses
            self.parenthesis_append(result + ")",
                                 open, close + 1)

user_size=int(input("Enter the range :"))
a=A(user_size)
a.parenthesis_append("")