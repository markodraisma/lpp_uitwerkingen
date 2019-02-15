def myrange(start, end, step=1):
    if start == end:
        raise Exception("Start en eind zijn gelijk")
    for i in range(start,end, step):
        yield i

try:
    for i in myrange(10,10,2):
       print(i)
except Exception:
    print("Er ging iets mis")

tientallen = [ x for x in myrange(10,101,10) ]
print(tientallen)



 

