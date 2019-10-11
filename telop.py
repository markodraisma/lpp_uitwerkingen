def telop(a=0, b=0, *rest):
    som = a + b
    for getal in rest:
        som += getal
    return som

if __name__ == '__main__':
    import sys
    getallen = sys.argv[1:]
    getallen2 = []
    for getal in getallen:
        getallen2.append(float(getal))
    print(telop(*getallen2))

#   of in één keer:
#   print(telop(*map(float,sys.argv[1:])))
        

