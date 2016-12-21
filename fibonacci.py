#!/usr/bin/python

###
def fibo():
  a = 0
  b = 1
  while b>0:
    yield a
    b = a+b
    a = b-a
###

def number(n):
    fibo_gen = fibo()
    for counter in range(0,(n-1)):
        next(fibo_gen)
    return next(fibo_gen)
