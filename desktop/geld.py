#!/usr/bin/env python3

class Geld(object):
    """een Geld klasse
    """
    def __init__(this, euro, cent):
        this.euro=euro
        this.cent=cent

    def __str__(this):
        return "%d,%02d" % (this.euro, this.cent) 
    
    def __add__(this, other):
        e = this.euro + other.euro
        c = this.cent + other.cent
        e += (c//100)
        c = c%100
        return Geld(e,c)

    def __mul__(this, count):
        e = this.euro * count
        c = this.cent * count
        e += (c//100)
        c = c%100
        return Geld(e,c)

    def __rmul__(this, count):
        return this.__mul__(count)

    def __truediv__(this, count):
        e = this.euro / count
        c = this.cent / count
        c += (e%1)*100
        e = e//1
        e += (c//100)
        c = c%100
        return Geld(e,c)



g1=Geld(2,17)
print(g1)

g2=Geld(2, 88)
print(g2)
#
g3=g1+g2
print(g3)
#
g3=g1*7
print(g3)
#
g3=7*g1
print(g3)
#
g4=g3/3
print(g4)

