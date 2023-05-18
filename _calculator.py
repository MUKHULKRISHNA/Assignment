"""Create a class"""


class Operation:
    """Create a class"""

    def addition(self):
        """create a function"""
        first = int(input('First Value: '))
        second = int(input('Second Value: '))
        plus = first + second
        print(plus)
        print('-----------------------------------')

    def subraction(self):
        '''create a function'''
        first = int(input('First Value: '))
        second = int(input('Second Value: '))
        difference = first - second
        print(difference)
        print('-----------------------------------')

    def multiplication(self):
        '''create a function'''
        first = int(input('First Value: '))
        second = int(input('Second Value: '))
        multiple = first * second
        print(multiple)
        print('-----------------------------------')

    def division(self):
        '''create a function'''
        first = int(input('First Value: '))
        second = int(input('Second Value: '))
        try:
            divide = first / second
        except ZeroDivisionError as err:
            print('Error:', err)
        else:
            print(divide)
        print('-----------------------------------')


def option(user_input):
    """Use conditional statement"""
    if user_input == 1:
        access.addition()
    elif user_input == 2:
        access.subraction()
    elif user_input == 3:
        access.multiplication()
    elif user_input == 4:
        access.division()
    else:
        print('Enter Valid Option')
        print('-----------------------------------')


class Choice(Operation):
    """create a function"""


A = True
while A:
    print('''
    1. Addition
    2. Subraction
    3. Multiplication
    4. Division
    5. Exit''')

    user_input_1 = int(input('\nEnter the option: '))
    access = Operation()
    key = Choice()
    if user_input_1 == 5:
        print('THANK YOU FOR USING CALCULATOR')
        exit()
    option(user_input_1)
