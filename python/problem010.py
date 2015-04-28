'''
Project Euler - Problem 10
http://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import math


def is_prime(n):
    prime = n != 1
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            prime = False
            break
        i += 1
    return prime


def prime_sum(n):
    s, i = 0, 0
    while i < n:
        if is_prime(i):
            s += i
        i += 1
    print s
    return s

print prime_sum(2000000)
