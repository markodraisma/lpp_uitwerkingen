#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Module docstring goes here
'''

import time
import sys

if len(sys.argv) == 2:
    interval = int(sys.argv[1])
else:
    raise Exception('Deze commando vereist precies 1 argument')

need_to_wait = 60 - time.localtime().tm_sec
print ('Sleeping for %ss, until it is a whole minute' % need_to_wait)
time.sleep(need_to_wait)

while True:
    print(time.strftime('%Y/%mm/%d  %H:%M:%S  Bingggg', time.localtime()))
    time.sleep(interval)



# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 showbreak=… ruler
# vim: foldmethod=indent foldcolumn=4 wrap linebreak spelllang=en nospell
