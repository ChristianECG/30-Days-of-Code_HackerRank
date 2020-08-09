#	||-------------------------------------------------------||
#	||------------------- Day 7: Arrays ---------------------||
#	||-------------------------------------------------------||

# Objective
# Today, we're learning about the Array data structure. Check
# out the Tutorial tab for learning materials and an instructional
# video!

# Task
# Given an array, A, of N integers, print A's elements in reverse
# order as a single line of space-separated numbers.

# Input Format
# The first line contains an integer, N (the size of our array).
# The second line contains space-separated integers describing
# array A's elements.

# Constraints
# 1 ≤ N ≤ 1000
# 1 ≤ Ai ≤ 10000, where Ai is the ith integer in the array.

# Output Format
# Print the elements of array Ain reverse order as a single line
# of space-separated numbers.


# ---------------------------------------------------------------


import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    txt = ""

    for i in range(n):
        txt += str(arr[n-i-1])
        txt += " "

    print(txt)
