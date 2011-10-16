#!/usr/bin/env python
"""This is a solver for Problem 1 in projecteuler.net.

If we list all the natural numbers below 10 that are multiples of 3 or
5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

from itertools import takewhile

def multiples(n):
    """Generator which produces the infinite sequence of all multiples
    of n."""
    current = n
    while True:
        yield current
        current += n

def merge(s1, s2):
    """Generator which merges two monotonically increasing sequences
    of numbers into a single monotonically increasing sequence, while
    avoiding duplicates."""
    current1 = s1.next()
    current2 = s2.next()
    while True:
        if current1 < current2:
            yield current1
            current1 = s1.next()
        elif current2 < current1:
            yield current2
            current2 = s2.next()
        else:
            yield current1
            current1 = s1.next()
            current2 = s2.next()

less_than_1000       = lambda x: x < 1000
multiples_of_3_and_5 = merge(multiples(3), multiples(5))
selected_multiples   = takewhile(less_than_1000, multiples_of_3_and_5)
solution             = sum(selected_multiples)

print("The solution is: " + str(solution))
