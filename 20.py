#	||-------------------------------------------------------||
#	||------------------ Day 20: Sorting --------------------||
#	||-------------------------------------------------------||

# Objective
# Today, we're discussing a simple sorting algorithm called
# Bubble Sort. Check out the Tutorial tab for learning materials
# and an instructional video!

# Task
# Given an array, a, of size n distinct elements, sort the array
# in ascending order using the Bubble Sort algorithm above. Once
# sorted, print the following 3 lines:

# 1. Array is sorted in numSwaps swaps.
#	 where numSwaps is the number of swaps that took place.
# 2. First Element: firstElement
#	 where first Element is the first element in the sorted array.
# 3. Last Element: lastElement
#	 where lasElement is the last element in the sorted array.

# Hint: To complete this challenge, you will need to add a
# variable that keeps a running tally of all swaps that occur
# during execution. 

# Input Format
# The first line contains an integer, n, denoting the number of
# elements in array a.
# The second line contains n space-separated integers describing
# the respective values of a0, a1, a2, ... , an-1.

# Constraints
# 2 ≤ n ≤ 600
# 1 ≤ ai ≤ 2 x 10^6, where 0 ≤ i ≤ n.

# Output Format
# Print the following three lines of output:

# 1. Array is sorted in numSwaps swaps.
#	 where numSwaps is the number of swaps that took place.
# 2. First Element: firstElement
#	 where first Element is the first element in the sorted array.
# 3. Last Element: lastElement
#	 where lasElement is the last element in the sorted array.


# ---------------------------------------------------------------


import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

counter = 0

for i in range(len(a)):
    for j in range(i,len(a)):
        if(a[i] > a[j]):
            counter += 1
            aux = a[i]
            a[i] = a[j]
            a[j] = aux

print(f'Array is sorted in {counter} swaps.')
print(f'First Element: {a[0]}')
print(f'Last Element: {a[n-1]}')