#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Module docstring goes here
'''

for i in range(1000):
    i_p = 2**i

    print('2^%s: ' %  i)
    i_s = str(i_p)
    for j in range(10):
        print('%s:%s | ' % (j, i_s.count(str(j))), end='')
    print()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 showbreak=… ruler
# vim: foldmethod=indent foldcolumn=4 wrap linebreak spelllang=en nospell
