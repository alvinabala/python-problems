#!/usr/bin/python

def bal(start, rate):
    while True:
            yield round(start, 2)
            start = start + rate*start

def bal_growth(start, rate, years):
    bal_gen = bal(start, rate)
    for counter in range(0,(years-1)):
        x = next(bal_gen)
    return x
