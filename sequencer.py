#!/usr/bin/python

output_list = []
####
def sequencer(number_list, out_count=0):
    for count in range(0, len(number_list)):
        x = number_list.pop(count)
        output_list.append(x)
        if(len(number_list) > 0):
            sequencer(number_list, out_count-1)
        else:
            print output_list

        number_list.insert(count, x)
        output_list.pop()
####
