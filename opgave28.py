#! /usr/bin/env python

for i in range(128):
    regel = "{0:5d} {0:#5x} {0:5o}".format(i)
    print(regel, end="")
    if i > 31:
        print(" {:5c}".format(i))
    else:
        print()
