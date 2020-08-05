#	||-------------------------------------------------------||
#	||------- Day 3: Intro to Conditional Statements --------||
#	||-------------------------------------------------------||

# Objective
# In this challenge, we're getting started with conditional
# statements. Check out the Tutorial tab for learning materials
# and an instructional video!

# Task
# Given an integer, n, perform the following conditional actions:

# - If n is odd, print Weird
# - If n is even and in the inclusive range of 2 to 5, print
# 	Not Weird
# - If n is even and in the inclusive range of 6 to 20, print Weird
# - If n is even and greater than 20, print Not Weird

# Complete the stub code provided in your editor to print whether
# or not n is weird.

# Input Format
# A single line containing a positive integer, n.

# Constraints
# 1 ≤ n ≤ 100

# Output Format
# Print Weird if the number is weird; otherwise, print Not Weird.


# -----------------------------------------------------------------


import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    if(N % 2 != 0):
        print('Weird')
    elif (N >= 2 and N <= 5):
        print('Not Weird')
    elif (N >= 6 and N <= 20):
        print('Weird')
    else:
        print('Not Weird')
