'''
Problem 7
28 December 2001
http://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
import math

def isPrime(n):
  prime=True
  if n==1: prime = False
  if n==2: prime = True
  if n%2==0: prime = False
  else:
    i=2
    while i < math.sqrt(n)+1:
      if n%i==0:
        prime=False
        break
      i+=1  
  return prime
  
def getNthPrime(n):
  i=0
  j=0
  while i<n:
    if j>2:j+=2
    else: j+=1 
    if isPrime(j):
      i+=1 
  return j

print(getNthPrime(10001))
