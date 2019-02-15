#! /usr/bin/env python

for i in range(50):
    regel = "{0:5d} {0:#5x} {0:#5o}".format(i)
    print(regel, end="")
    if i > 31:
        print(" {:5c}".format(i))
    else:
        print()
print()

for i in range(50):
    regel = "%5d 0x%-5x 0o%-5o" % (i,i,i)
    print(regel, end="")
    if i > 31:
        print(" %c" % i)
    else:
        print()
