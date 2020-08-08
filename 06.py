#	||-------------------------------------------------------||
#	||---------------- Day 6: Let's Review ------------------||
#	||-------------------------------------------------------||

# Objective
# Today we're expanding our knowledge of Strings and combining
# it with what we've already learned about loops. Check out the
# Tutorial tab for learning materials and an instructional video!

# Task
# Given a string, S, of length N that is indexed from 0 to N - 1,
# print its even-indexed and odd-indexed characters as 2
# space-separated strings on a single line(see the Sample below
# for more detail).

# Note: 0 is considered to be an even index.

# Input Format
# The first line contains an integer, T (the number of test cases).
# Each line i of the T subsequent lines contain a String, S.

# Constraints
# 1 ≤ T ≤ 10
# 2 ≤ length of S ≤ 10000

# Output Format
# For each String Sj (where 0 ≤ j ≤ T-1), print Sj's even-indexed
# characters, followed by a space, followed by Sj's odd-indexed
# characters.


# ----------------------------------------------------------------


if __name__ == '__main__':
    array_text = []
    test_cases = int(input())

    for _ in range(test_cases):
        array_text.append(input())

    for text in array_text:
        even_text = ''
        other_text = ''

        for i in range(len(text)):
            if(i % 2 == 0):
                even_text += text[i]
            else:
                other_text += text[i]

        print(even_text, other_text)
