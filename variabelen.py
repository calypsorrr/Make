#!/usr/bin/env python
"""
Info about our project comes here
"""


__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"


def main():
    x = input("Enter the first number: ")
    y = input("Enter the second number: ")
    z = input("Enter the thirth number: ")

    if x >= y and x >= z:
        print(x)
    elif y >= x and y >= z:
        print(y)
    else:
        print(z)

if __name__ == '__main__':  # code to execute if called from command-line
    main()
