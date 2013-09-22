'''
Project Euler - Problem 3
http://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''
import math


def isPrime(n):
    prime = True
    if n != 1:
        i = 2
        while i < math.sqrt(n):
            if n % i == 0:
                prime = False
                break
            i += 1
    return prime


def primefactors(factors, n):
    if isPrime(n):
        factors.append(n)
        return factors
    else:
        i = 2
        while i < n:
            if n % i == 0 and isPrime(i):
                factors.append(i)
                break
            i += 1
    primefactors(factors, n/i)

factors = []
primefactors(factors, 600851475143)
print(factors)
