# File: Collatz_conjecture.py
# Description: Implementing Collatz conjecture by recursive function
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Implementing Collatz conjecture by recursive function // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Collatz_conjecture (date of access: XX.XX.XXXX)



# Collatz conjecture
# Creating a recursive function for calculating sequence of numbers,
# described by Collatz conjecture
# As input is natural number n > 0


# Recursive function for calculating Collatz' sequence of numbers
def Collatz(number):
    print(number, end=' ')  # Printing the number
    # Checking if the current calculated number is still more then 1
    if number > 1:
        # Checking if the current number is even
        if number % 2 == 0:
            # Calling the recursive function and printing the integer division of current number
            return Collatz(number // 2)
        else:
            # Calling the recursive function and printing processed number
            return Collatz(number * 3 + 1)


# Input beginning number for calculating Collatz sequence
n = int(input())

# Implementing the recursive function
Collatz(n)
