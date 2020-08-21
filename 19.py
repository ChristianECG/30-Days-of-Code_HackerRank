#	||-------------------------------------------------------||
#	||----------------- Day 19: Interfaces ------------------||
#	||-------------------------------------------------------||

# Objective
# Today, we're learning about Interfaces. Check out the Tutorial
# tab for learning materials and an instructional video!

# Task
# The AdvancedArithmetic interface and the method declaration for
# the abstract divisorSum(n) method are provided for you in the
# editor below.

# Complete the implementation of Calculator class, which implements
# the AdvancedArithmetic interface. The implementation for the
# divisorSum(n) method must return the sum of all divisors of n.

# Input Format
# A single line containing an integer, n.

# Constraints
# 1 ≤ n ≤ 1000

# Output Format
# You are not responsible for printing anything to stdout. The
# locked template code in the editor below will call your code
# and print the necessary output.


# ---------------------------------------------------------------


class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        ans = 0
        for i in range(n):
            if(n%(i+1)==0):
                ans+=(i+1)
        return ans

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)