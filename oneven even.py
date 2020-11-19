#!/usr/bin/env python
"""
Info about our project comes here
"""


__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"


def main():


    num = int(input("Enter a number: "))
    if (num % 2) == 0:
        print("{0} is Even".format(num))
    else:
        print("{0} is Odd".format(num))


if __name__ == '__main__':  # code to execute if called from command-line
    main()
