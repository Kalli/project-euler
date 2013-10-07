'''
Project Euler - Problem 4
http://projecteuler.net/problem=4

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''


def reverse_number(n):
    m = 0
    while n > 0:
        m = 10 * m + n % 10
        n = n / 10
    return m


def palindrome(n):
    return n == reverse_number(n)


def problem_4():
    max_palindrome = 0
    i = 999
    while i > 0:
        j = i
        while j > 0:
            product = i * j
            if palindrome(product) and product > max_palindrome:
                max_palindrome = product
            j -= 1
        i -= 1
    return max_palindrome

print problem_4()
