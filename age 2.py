#!/usr/bin/env python
"""
Info about our project comes here
"""


__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"


def main():
    YEAR = 2020                                                                   

    x = 100

    NAME = input("What is your name good sir ")

    AGE = input("What age are you? ")

    print(NAME,", you are a 100 years old in this year: " + str(int(YEAR) - int(AGE) + int(x)))

    HOW_MUCH = int(input("How many times do you want to print this? "))

    for i in range(HOW_MUCH):
        print(NAME,", you are a 100 years old in this year: " + str(int(YEAR) - int(AGE) + int(x)))



if __name__ == '__main__':  # code to execute if called from command-line
    main()
