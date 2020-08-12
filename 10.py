#	||-------------------------------------------------------||
#	||--------------- Day 10: Binary Numbers ----------------||
#	||-------------------------------------------------------||

# Objective
# Today, we're working with binary numbers. Check out the Tutorial
# tab for learning materials and an instructional video!

# Task
# Given a base-10 integer, n, convert it to binary(base-2). Then
# find and print the base-10 integer denoting the maximum number
# of consecutive 1's in n's binary representation.

# Input Format
# A single integer, n.

# Constraints
# 1 ≤ n ≤ 1000000

# Output Format
# Print a single base-10 integer denoting the maximum number of
# consecutive 1's in the binary representation of n.


# ---------------------------------------------------------------


import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    counter = 0
    max_counter = 0

    while True:
        if(n == 1):
            counter += 1
            break

        if(n == 2):
            break

        if(n % 2 == 0):
            if(counter > max_counter):
                max_counter = counter
            counter = 0

        counter += (n % 2)

        n = n//2

    print(max(counter, max_counter))
