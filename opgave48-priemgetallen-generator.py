#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Module docstring goes here
'''

import sys

def prime_gen(max):
    for max_nr in range(1, max, 2):
        # only considering odd numbers
        for pot_prime in range(2, max_nr//2):
            # nested loop 
            if max_nr % pot_prime == 0:
                break
        else:
            yield max_nr

for i in prime_gen(int(sys.argv[1])):
    print(i, end=' ')

print()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 showbreak=… ruler
# vim: foldmethod=indent foldcolumn=4 wrap linebreak spelllang=en nospell

