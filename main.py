
import unittest

def Add(a,b):
    return a+b


def Subtract(a,b):
    return a-b

def Multiply(a,b):
        return a*b


def Divide(a,b):
    if (b==0):
        print("Nie dziel przez zero!")
        return "Blad!"
    return a/b





def Calculator(a,b,action):

    if(action == '+'):

        return Add(a,b)
    elif (action == '-'):

        return Subtract(a, b)
    elif (action == '*'):

        return Multiply(a, b)
    elif (action == '/'):

        return Divide(a, b)
    else:
        print("Bledne argumenty")
        return -1

print(10/5+2)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
