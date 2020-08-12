#	||-------------------------------------------------------||
#	||----------------- Day 2: Operators --------------------||
#	||-------------------------------------------------------||

# Objective
# In this challenge, you'll work with arithmetic operators.
# Check out the Tutorial tab for learning materials and an
# instructional video!

# Task
# Given the meal price (base cost of a meal), tip percent
# (the percentage of the meal price being added as tip),
# and tax percent (the percentage of the meal price being
# added as tax) for a meal, find and print the meal's total
# cost.

# Note: Be sure to use precise values for your calculations,
# or you may end up with an incorrectly rounded result!

# Input Format

# There are 3 lines of numeric input:
# 	* The first line has a double, mealCost(the cost of the
# 	  meal before tax and tip).
#	* The second line has an integer, tipPercent(the percentage
# 	  of mealCost being added as tip).
# 	* The third line has an integer, taxPercent(the percentage
# 	  of mealCost being added as tax).

# Output Format

# Print the total meal cost, where totalCost is the rounded
# integer result of the entire bill(mealCost with added tax
# and tip).

# -------------------------------------------------------------


import math
import os
import random
import re
import sys

# Complete the solve function below.


def solve(meal_cost, tip_percent, tax_percent):
    total_percent = (tip_percent + tax_percent) / 100
    print(round(meal_cost * (1 + total_percent)))


if __name__ == '__main__':
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
