#!/usr/bin/env python
"""
Info about our project comes here
"""


__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"


def main():
    INPUT_LIST = input("Enter a list elements separated by space ")

    USER_LIST = INPUT_LIST.split()

    print("user list is ", USER_LIST)

    print("The First and last element of you list is")

    print(USER_LIST[0], USER_LIST[-1])


if __name__ == '__main__':  # code to execute if called from command-line
    main()
