#	||-------------------------------------------------------||
#	||------------------- Day 5: Loops ----------------------||
#	||-------------------------------------------------------||

# Objective
# In this challenge, we're going to use loops to help us do
# some simple math. Check out the Tutorial tab to learn more.

# Task
# Given an integer, n, print its 10 first multiples. Each
# multiple n x i(where 1 ≤ i ≤ 10) should be printed on a new
# line in the form: n x i = result.

# Input Format
# A single integer, n.

# Constraints
# 2 ≤ n ≤20

# Output Format
# Print 10 lines of output; each line i (where 1 ≤ i ≤ 10)
# contains the result of n x i in the form: n x i = result.


# --------------------------------------------------------------

if __name__ == '__main__':
    n = int(input())
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')
