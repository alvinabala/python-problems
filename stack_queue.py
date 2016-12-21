#!/usr/bin/python

from functools import partial


stack = []
queue = []

def push (data, list):
    list.append(data)

stack_push = partial(push, list = stack)

queue_push = partial(push, list = queue)

def pop (position, list):
    list.pop(position)

stack_pop_base = partial(pop, list = stack)
stack_pop = partial(stack_pop_base, position = (len(stack)-1))

queue_pop_base = partial (pop, list = queue)
queue_pop = partial(queue_pop_base, position = 0)
