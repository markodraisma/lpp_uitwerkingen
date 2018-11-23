geld = 1788 
# geld = int(geld)


g500 = geld//500
geld = geld%500
g200 = geld//200
geld = geld%200
g100 = geld//100
geld = geld%100
g50 = geld //50
geld = geld%50
g20 = geld//20
geld = geld%20
g10 = geld//10
geld = geld%10
g5 = geld//5
geld = geld%5
print("briefjes van 500:", g500)
print("briefjes van 200:", g200)
print("briefjes van 100:", g100)
print("briefjes van 50:", g50)
print("briefjes van 20:", g20)
print("briefjes van 10:", g10)
print("briefjes van 5:", g5)
print("rest in euro's", geld)

