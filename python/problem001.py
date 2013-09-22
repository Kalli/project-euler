'''
Project Euler - Problem 1
http://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000
'''


def problem1(div1, div2, high):
    sum = 0
    for i in range(0, high):
        if i % div1 == 0 or i % div2 == 0:
            sum = sum + i
    return sum

print problem1(3, 5, 1000)
