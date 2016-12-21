#!/usr/bin/python

def diamond (n):
    for top_count in range (1,n + 1):
        print " " * (n + 1 - top_count), "1 " * (top_count)
    for bottom_count in range(n-1, 0, -1):
        print " " * (n+1 - bottom_count), "1 " * (bottom_count)
