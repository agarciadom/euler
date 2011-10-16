#!/usr/bin/env python
"""This is a solver for Problem 1 in projecteuler.net.

If we list all the natural numbers below 10 that are multiples of 3 or
5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

# mcm(3,5) = 15, so we can just sum all the multiples of 3, all the
# multiples of 5, and then remove the common multiples (multiples of
# 15). I noticed this after looking at the forum.
LIMIT=1000

print sum(range(3,LIMIT,3)) + sum(range(5,LIMIT,5)) - sum(range(15,LIMIT,15))
