'''
Project Euler - Problem 5
http://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lowest_common_multiple(a, b):
    return a * b / greatest_common_divisor(a, b)

print reduce(lowest_common_multiple, range(1, 21))
