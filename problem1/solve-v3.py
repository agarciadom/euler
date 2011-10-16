#!/usr/bin/env python
"""This is a solver for Problem 1 in projecteuler.net.

If we list all the natural numbers below 10 that are multiples of 3 or
5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

# mcm(3,5) = 15, so we can just sum all the multiples of 3, all the
# multiples of 5, and then remove the common multiples (multiples of
# 15). I noticed this after looking at the forum.
#
# We can simply use the formula for the sum of an arithmetic
# progression here: no need for loops. However, we need to find the
# last multiple

LIMIT=1000

last_multiple = lambda base: (LIMIT - 1) / base * base
arith_sum     = lambda base: (base + last_multiple(base)) * ((LIMIT-1)/base) / 2
solution      = arith_sum(3) + arith_sum(5) - arith_sum(15)

print("The solution is: " + str(solution))
