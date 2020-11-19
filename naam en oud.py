#!/usr/bin/env python
"""
Info about our project comes here
"""


__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"


def main():
    NAME = input("How may whe call you sir? ")

    AGE = input("And what is your age? ")

    print("Good day", NAME, "you are", AGE, "years old")

if __name__ == '__main__':  # code to execute if called from command-line
    main()
