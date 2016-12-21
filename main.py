#!/usr/bin/python

import diamond
import sequencer
import balance
import fibonacci
import twist
import adjacent
from stack_queue import *

def stack_queue_menu():
    print "Stack and Queue"

    while True:
        print "Choices:"
        print "1    Display stack"
        print "2    Push to stack"
        print "3    Pop from stack"
        print "4    Display queue"
        print "5    Enqueue"
        print "6    Dequeue"
        print "0    Exit Stack and Queue"
        choice = raw_input("Enter choice:")

        if choice == '1':
            print stack
        elif choice == '2':
            pushee = raw_input("Enter thing to push:")
            stack_push(pushee)
        elif choice == '3':
            stack_pop()
        elif choice == '4':
            print queue
        elif choice == '5':
            pushee = raw_input("Enter thing to push:")
            queue_push(pushee)
        elif choice == '6':
            queue_pop()
        else:
            break


print "Main file for PythonProblems"

while True:
    print "Choices:"
    print "1    Diamond"
    print "2    Possible Sequences"
    print "3    Removing adjacent similar characters"
    print "4    Calculate Interest from Balance and Rate"
    print "5    Fibonacci Number"
    print "6    Stacks and Queues"
    print "7    Guess the jumbled word"
    print "0   Exit"
    choice = raw_input("Enter choice:")

    if choice == '1':
        print "Diamond:"
        diamond_input = raw_input("Enter Size:")
        diamond.diamond(diamond_input)
    elif choice == '2':
        print "Possible Sequences:"
        sequencer_input = raw_input("Enter sequence")
        sequencer.sequencer(sequencer_input)
    elif choice == '3':
        print "Remove adjacent similar Characters"
        adjacent_input = raw_input("Enter list of strings:")
        print (adjacent.cleaner(adjacent_input))
    elif choice == '4':
        print "Balance growth"
        balance_start = int(raw_input("Enter Starting Balance:"))
        balance_rate = float(raw_input("Enter interest rate:"))
        balance_year = int(raw_input("Enter number of years:"))
        print balance.bal_growth(balance_start,balance_rate,balance_year)
    elif choice == '5':
        print "Fibonacci Number"
        fibonacci_input = int(raw_input("Enter N of fibonacci nubmer:"))
        print fibonacci.number(fibonacci_input)
    elif choice == '6':
        stack_queue_menu()
    elif choice == '7':
        print "Guess the Jumbled word"
        twist.twist()
    elif choice == '0':
        break
    else:
        print "Invalid choice"
        continue
