#!/usr/bin/env python
geld = 1788 
# geld = int(geld)


g500 = geld//500
geld %= 500
g200 = geld//200
geld %= 200
g100 = geld//100
geld %= 100
g50 = geld //50
geld %=50
g20 = geld//20
geld %=20
g10 = geld//10
geld %=10
g5 = geld//5
geld %= 5
print(g500, "briefjes van 500")
print(g200, "briefjes van 200")
print("briefjes van 100:", g100)
print("briefjes van 50:", g50)
print("briefjes van 20:", g20)
print("briefjes van 10:", g10)
print("briefjes van 5:", g5)
print("rest in euro's", geld)

