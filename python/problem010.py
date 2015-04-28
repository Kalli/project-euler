'''
Project Euler - Problem 10
http://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''


def prime_sieve_sum(n):
    l = [0, 0] + range(2, n+1)
    for i in l:
        if i != 0:
            p = 2*i
            while p < n:
                l[p] = 0
                p += i
    return sum(l)

print prime_sieve_sum(2000000)
