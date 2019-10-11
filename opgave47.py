def myrange(start, end, step=1):
    huidig = start
    if start < end and step > 0:
        while huidig < end:
            yield huidig
            huidig += step
    elif start > end and step < 0:
        while huidig > end:
            yield huidig
            huidig += step
    else:
        return;


tientallen = [ x for x in myrange(100,-1,-10) ]
print(tientallen)



 

