'''
Problem 6
14 December 2001
http://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is:
1^2+2^2+3^2+ ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def sumsquares(n):
  return reduce(lambda a,b:a+b,range(1,n+1))**2

def squaresum(n):
  return reduce(lambda a,b:a+b,map(lambda a:a**2,range(1,n+1)))

print(sumsquares(100)-squaresum(100))
